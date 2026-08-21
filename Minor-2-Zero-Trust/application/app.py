from fastapi import FastAPI

app = FastAPI(
    title="Zero Trust Enterprise API",
    description="Protected enterprise resources for the Minor Project 2 Zero Trust lab.",
    version="1.0.0",
)


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
def employee_resource():
    return {
        "resource": "employee",
        "message": "This is an employee-level enterprise resource.",
    }


@app.get("/api/admin")
def admin_resource():
    return {
        "resource": "admin",
        "message": "This is an administrator-level enterprise resource.",
    }