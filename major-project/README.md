# Security Awareness & Phishing Simulation Platform

A cybersecurity-focused web application for conducting controlled security-awareness and phishing simulations, recording participant interactions, assessing risk, and maintaining an audit trail of administrative actions.

## Project Overview

This project provides a prototype platform for organizations or educational institutions to conduct controlled phishing-awareness exercises.

The platform allows an administrator to:

- Create and manage security-awareness campaigns
- Add participants to campaigns
- Run controlled phishing-style simulations
- Record email-open and link-click interactions
- Calculate participant risk scores
- View campaign analytics and participant risk levels
- Maintain audit logs for administrative actions
- Enforce authentication and role-based access control

The simulation is designed for security awareness and does not collect real user credentials.

---

## Key Features

### Authentication

- User registration
- User login
- JWT-based authentication
- Password hashing using Argon2
- Protected API endpoints
- Invalid/expired token rejection

### Role-Based Access Control

The application currently supports role-based authorization using:

- `admin`
- `student`

Administrative endpoints require the appropriate role.

Examples:

- Admin → administrative operations allowed
- Student → admin-only operations return `403 Forbidden`

### Campaign Management

Administrators can:

- Create campaigns
- View campaigns
- View individual campaigns
- Change campaign status

Supported campaign states:

```text
draft
active
completed