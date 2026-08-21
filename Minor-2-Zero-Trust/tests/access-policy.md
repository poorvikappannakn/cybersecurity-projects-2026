# Zero Trust Access Policy

## Identity Requirement

All protected enterprise resources require a valid Keycloak access token.

Unauthenticated requests are denied.

## Role-Based Access

### Employee Role

The employee role can access:

- `/api/employee`

The employee role cannot access:

- `/api/admin`

### Admin Role

The admin role can access:

- `/api/employee`
- `/api/admin`

## Expected Security Behavior

| Identity | Employee API | Admin API |
|---|---:|---:|
| No token | 401 DENY | 401 DENY |
| Alice (employee) | 200 ALLOW | 403 DENY |
| Bob (admin) | 200 ALLOW | 200 ALLOW |

## Zero Trust Principles Demonstrated

1. Authentication is required for protected resources.
2. Authorization is evaluated based on the user's role.
3. Access is denied by default when authentication or authorization requirements are not satisfied.
4. Administrative resources require elevated privileges.
5. Access decisions are made per request rather than trusting the user solely because they can reach the API.