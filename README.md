🚀 Employee Management System – REST API
A secure, scalable, and cloud-deployed Employee Management REST API built using Django & Django REST Framework. This system allows organizations to manage employee records with full CRUD operations,
JWT authentication, pagination, and role-based access.

🔗 Live API:https://employee-management-qa6y.onrender.com
🔗 GitHub Repository:https://github.com/varshasuresh3/employee_management.git

📌 Features
JWT Authentication (Login & Token-based access)
Create, Read, Update & Delete Employees
Email uniqueness validation
Pagination for large data
Filter by department and role
Secure API access
Deployed on Render (Cloud)

🛠 Tech Stack
Layer
Technology
Backend
Python, Django
API
Django REST Framework
Authentication
JWT (SimpleJWT)
Database
SQLite
Deployment
Render
API Testing
Postman
Version Control
Git & GitHub

🔐 Authentication (JWT)
Generate Token
POST /api/token/

Request Body
            Json
{
  "username": "admins",
  "password": "admin123"
}
Response:
    Json
{
  "access": "<JWT_ACCESS_TOKEN>",
  "refresh": "<JWT_REFRESH_TOKEN>"
}


Use the access token in all secured API calls.
In Postman:
          Authorization → Bearer Token → <your access token>

          
📂 API Endpoints
Method        Endpoint               Description
POST          /api/token/            Get JWT token
POST          /api/employees/        Create new employee
GET           /api/employees/        Get all employees
GET           /api/employees/{id}/   Get employee by ID
PUT           /api/employees/{id}/   Update employee
DELETE        /api/employees/{id}/   Delete employee


📌 Create Employee: POST /api/employees/
Json
        {
  "name": "Asha",
  "email": "asha@gmail.com",
  "department": "HR",
  "role": "Manager"
}
       
       Success Response: 201 Created
       
📌 List Employees (Pagination)

GET /api/employees/?page=1
             Filter:/api/employees/?department=HR
             /api/employees/?role=Manager

             
📌 Update Employee

PUT /api/employees/1/
Json
{
  "name": "Sree",
  "email": "sree@company.com",
  "department": "IT",
  "role": "Technician"
}

📌 Delete Employee

DELETE /api/employees/1/
Response: 204 No Content

⚠ Error Handling
Scenario             Status
Duplicate email      400 Bad Request
Unauthorized         401 Unauthorized
Not found            404 Not Found
Success create       201 Created
Success delete       204 No Content


☁ Deployment
The project is deployed on Render Cloud Platform and accessible through a public live API link.

🧑‍💻 Author
Varsha Suresh
Python | Django | REST APIs | Cloud Deployment

⭐ Conclusion
This project demonstrates real-world backend development including:
Secure authentication
RESTful API design
Cloud deployment
API testing
Professional documentation
