from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
import jwt
import httpx

app = FastAPI(
    title="Zero Trust Enterprise API",
    description="Protected enterprise resources for the Minor Project 2 Zero Trust lab.",
    version="2.0.0",
)

KEYCLOAK_ISSUER = "http://localhost:8080/realms/Enterprise-Zero-Trust"

KEYCLOAK_JWKS_URL = (
    "http://host.docker.internal:8080/"
    "realms/Enterprise-Zero-Trust/"
    "protocol/openid-connect/certs"
)

security = OAuth2AuthorizationCodeBearer(
    authorizationUrl=(
        "http://localhost:8080/realms/Enterprise-Zero-Trust/"
        "protocol/openid-connect/auth"
    ),
    tokenUrl=(
        "http://localhost:8080/realms/Enterprise-Zero-Trust/"
        "protocol/openid-connect/token"
    ),
)


def verify_token(token: str = Depends(security)):
    try:
        jwks_response = httpx.get(KEYCLOAK_JWKS_URL)
        jwks_response.raise_for_status()
        jwks = jwks_response.json()

        header = jwt.get_unverified_header(token)
        key_id = header.get("kid")

        key = next(
            (
                key
                for key in jwks["keys"]
                if key.get("kid") == key_id
            ),
            None,
        )

        if key is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unable to find signing key.",
            )

        public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)

        payload = jwt.decode(
            token,
            public_key,
            algorithms=["RS256"],
            issuer=KEYCLOAK_ISSUER,
            options={"verify_aud": False},
        )

        return payload

    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired access token.",
        )

    except httpx.HTTPError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Unable to reach Keycloak.",
        )


def require_roles(*allowed_roles):
    def role_checker(token: dict = Depends(verify_token)):
        realm_access = token.get("realm_access", {})
        user_roles = realm_access.get("roles", [])

        if not any(role in user_roles for role in allowed_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions.",
            )

        return token

    return role_checker


@app.get("/")
def root():
    return {
        "service": "Zero Trust Enterprise API",
        "status": "running",
    }


@app.get("/api/public")
def public_resource():
    return {
        "resource": "public",
        "message": "This is a public enterprise resource.",
    }


@app.get("/api/employee")
def employee_resource(
    token: dict = Depends(require_roles("employee", "admin")),
):
    return {
        "resource": "employee",
        "message": "This is an employee-level enterprise resource.",
    }


@app.get("/api/admin")
def admin_resource(
    token: dict = Depends(require_roles("admin")),
):
    return {
        "resource": "admin",
        "message": "This is an administrator-level enterprise resource.",
    }