# 📚 Student Management System

A Django-based web application for managing student records, including adding, editing, and deleting students with proper success/error messages.

# 📌 Features

* ✅ Add new students with details (Name, Roll, Department, Address, Phone, Email)
* ✅ Edit student details
* ✅ Delete student records
* ✅ Bootstrap-based responsive UI
* ✅ Success and error messages using Django’s messages framework

# 🛠️ Tech Stack
* Frontend: HTML, CSS, Bootstrap
* Backend: Django, Python
* Database: SQLite (default) / PostgreSQL (optional)
* Version Control: Git & GitHub

# 🚀 Installation & Setup

### 🔹 Step 1: Clone the Repository
```bash 
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system
```
# 🔹 Step 2: Create a Virtual Environment (Optional)

```bash 
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

## 🔹 Step 3: Install Dependencies

    pip install -r requirements.txt

## 🔹 Step 4: Apply Migrations

    python manage.py makemigrations
    python manage.py migrate

## 🔹 Step 5: Create a Superuser

    python manage.py createsuperuser

### 👉 Enter username, email, and password when prompted.

## 🔹 Step 6: Run the Server

    python manage.py runserver

#### Now, visit http://127.0.0.1:8000/ in your browser. 🎉

# 📂 Project Structure
```bash
student-management-system/
│── std_app/                  # Main Django app
│   ├── migrations/           # Database migrations
│   ├── templates/std_app/     # HTML Templates
│   │   ├── base.html         # Base template with Navbar/Footer
│   │   ├── index.html        # Home page (List of students)
│   │   ├── add_std.html      # Add Student form
│   │   ├── update.html       # Edit Student form
│   │   ├── about.html        # About page
│   │   ├── services.html     # Services page
│   ├── models.py             # Database Models
│   ├── views.py              # Application Logic
│   ├── urls.py               # URL Routing
│   ├── admin.py              # Admin Panel Configuration
│── static/                   # Static Files (CSS, JS, Images)
│── db.sqlite3                 # SQLite Database (Default)
│── manage.py                  # Django Management Script
│── requirements.txt           # Python dependencies
│── README.md                  # Project Documentation
```
🖥️ Screenshots

# 🏠 Home Page

<img src="screenshots/homepage.png" alt="Home Page" width="600">


# 📝 Add Student

<img src="screenshots/add_student.png" alt="Add Student" width="600">


# ✏️ Edit Student

<img src="screenshots/edit_student.png" alt="Edit Student" width="600">


# 📜 License

* This project is open-source and available under the MIT License.

# 💡 Future Enhancements

* 🔹 Student Profile Upload – Allow students to upload profile images.
* 🔹 Search & Filter – Add search functionality for better record management.
* 🔹 Pagination – Improve UI for large datasets.
* 🔹 Export Data – Generate reports in CSV or PDF format.

# 🙌 Contributing

👨‍💻 Contributions are welcome! Feel free to fork this repo, create a new branch, and submit a pull request.

## 📬 Contact
- **Developer:** Abdullah Nazmus-Sakib
- **GitHub:** [AbdullahRFA](https://github.com/AbdullahRFA)
- **Portfolio:** [abdullah-nazmus-sakib-rfa.netlify.app](https://abdullah-nazmus-sakib-rfa.netlify.app/)
- **Email:** [shakibrybmn@gmail.com)](mailto:shakibrybmn@gmail.com)

### Developed with ❤️ using Django.