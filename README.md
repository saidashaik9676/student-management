# 🎓 Student Management System

A web-based **Student Management System** developed using Python and FastAPI to manage student records efficiently. The application allows users to add, view, update, and delete student details through a simple and user-friendly web interface.

## 🚀 Project Overview

The Student Management System provides a centralized platform for managing student information. It uses FastAPI for backend development, SQLite for database management, and Jinja2 templates for rendering dynamic HTML pages.

This project demonstrates practical implementation of CRUD operations, database connectivity, form handling, data validation, and dynamic web page rendering.

## ✨ Features

- **Add Students:** Register new students with their personal and academic details.
- **View Students:** Display student records on the home page.
- **Student Details:** View individual student information.
- **Update Students:** Edit existing student records.
- **Delete Students:** Remove student records from the database.
- **Form Handling:** Collect student information using HTML forms.
- **Data Validation:** Validate student details using Pydantic.
- **Database Integration:** Store and manage student records using SQLite.
- **Dynamic Templates:** Render web pages using Jinja2.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | Web framework |
| SQLite | Database management |
| Jinja2 | HTML templating |
| Pydantic | Data validation |
| HTML | Web page structure |
| CSS | Web page styling |

## 📂 Project Structure

```text
Student-Management-System/
│
├── main.py
├── student.db
│
├── templates/
│   ├── home.html
│   ├── add-std.html
│   ├── single-std.html
│   └── edit.html
│
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Student-Management-System.git
```

### 2. Navigate to the Project Folder

```bash
cd Student-Management-System
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
.venv\Scripts\activate
```

### 5. Install Required Dependencies

```bash
pip install fastapi uvicorn jinja2 python-multipart
```

### 6. Run the Application

```bash
uvicorn main:app --reload
```

### 7. Open in Browser

```text
http://127.0.0.1:8000
```

## 🗄️ Database Details

The application uses SQLite to store student information.

**Table Name:** `students`

| Column | Description |
|---|---|
| id | Unique student ID |
| name | Student name |
| age | Student age |
| gender | Student gender |
| marks | Student marks |
| course | Enrolled course |
| image | Student image reference |
| status | Student status |

The database table is automatically created when the application starts.

## 🔄 CRUD Operations

The application implements the four fundamental database operations:

- **Create:** Add new student records.
- **Read:** Retrieve and display student information.
- **Update:** Modify existing student details.
- **Delete:** Remove student records.

## 📸 Application Screenshots

Screenshots of the application interface will be added here.

<!-- Add your screenshots here -->

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Building web applications using FastAPI.
- Implementing CRUD operations.
- Connecting Python applications with SQLite.
- Handling HTML form submissions.
- Validating user input using Pydantic.
- Working with Jinja2 templates.
- Managing application routes and HTTP requests.

## 🔮 Future Enhancements

- Implement student search functionality.
- Add student authentication and authorization.
- Improve form validation and error handling.
- Add pagination for student records.
- Enhance the dashboard and user interface.

## 👨‍💻 Author

**Gopi Dintakurti**

Python Full Stack Developer (Fresher)

GitHub: https://github.com/gopi.dintkurti

---

⭐ If you find this project useful, feel free to explore the repository and share your feedback.

**Thank you for visiting my project!**
