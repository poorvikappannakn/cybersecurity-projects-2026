# Minor Project 2 - Zero Trust Architecture for Enterprise Security

## Project Overview

This project implements a controlled **Zero Trust enterprise security environment** based on the principle:

> **Never trust, always verify.**

The project demonstrates identity verification, authentication, authorization, role-based access control, secure API access, security logging, container security, credential protection, and automated security testing.

The implementation uses **Docker** to create the application environment and **Keycloak** as the Identity and Access Management (IAM) platform.

---

## Official Project Requirements

According to the official project allocation, the project requires:

1. Understand Zero Trust principles.
2. Define authentication models such as Multi-Factor Authentication (MFA) and Role-Based Access Control (RBAC).
3. Design a Zero Trust framework with:
   - Identity verification
   - Micro-segmentation
   - Encryption
4. Simulate an enterprise security environment using virtualization tools such as VMware or Docker.
5. Implement access-control policies using Identity & Access Management (IAM) systems.
6. Test security effectiveness by simulating insider and external threats.
7. Document results and suggest improvements.

---

# Project Architecture

The implemented environment consists of two primary services:

```text
                         +----------------------+
                         |        User          |
                         |  Alice / Admin User  |
                         +----------+-----------+
                                    |
                                    | Authentication
                                    v
                         +----------------------+
                         |      Keycloak        |
                         |        IAM           |
                         |                      |
                         | - Identity           |
                         | - MFA                |
                         | - Roles              |
                         | - JWT Tokens         |
                         +----------+-----------+
                                    |
                              Bearer JWT
                                    |
                                    v
                         +----------------------+
                         |   Enterprise API     |
                         |      FastAPI         |
                         |                      |
                         | - JWT validation     |
                         | - RBAC               |
                         | - Audit logging      |
                         | - Security headers   |
                         +----------------------+