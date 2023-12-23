
### BD Project README

This repository contains a FastAPI project with SQLAlchemy for interacting with a PostgreSQL database. The project implements CRUD (Create, Read, Update, Delete) operations for three entities: Student, Study, and Faculty. Additionally, it provides endpoints for executing various types of queries and aggregations.

### Prerequisites
- Python 3.7 or later
- PostgreSQL installed and running

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/bd_project.git
   cd bd_project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the PostgreSQL database:
   - Open `db_creation.py` and modify the database connection parameters (user, password, host, port).
   - Run the script to create the database:
     ```bash
     python db_creation.py
     ```

4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

The FastAPI server should now be running at `http://127.0.0.1:8000`. You can access the API documentation at `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc`.

### Usage
- Use the provided API endpoints to perform CRUD operations on Students, Studies, and Faculties.
- Execute various types of queries, such as filtering, joining, updating with complex conditions, and aggregations.

### Example API Endpoints
- Add a student:
  `POST /add_student`

- Get all students:
  `GET /get_all_students`

- Update a student:
  `PUT /update_student/{student_id}`

- Delete a student:
  `DELETE /delete_student/{student_id}`

- Get average GPA by entry year:
  `GET /average_gpa_by_entry_year`

- Add a study:
  `POST /add_study`

- Get faculty by ID:
  `GET /get_faculty/{faculty_id}`

- Update faculty:
  `PUT /update_faculty/{faculty_id}`

- Delete faculty:
  `DELETE /delete_faculty/{faculty_id}`
