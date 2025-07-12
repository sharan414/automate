# 🚗 AutoMate – Smart Vehicle Maintenance Tracker

AutoMate is a full-stack web application built using **Flask**, **MySQL**, and **Tailwind CSS**. It helps vehicle owners easily track and manage their vehicles and maintenance records with a clean, modern UI and user authentication.

---

## 🌟 Features

- 🔐 **User Authentication** (Register & Login)
- 🧾 **Add & Manage Vehicles**
- 🛠️ **Track Maintenance Records**
- 📅 **Filter & View Maintenance by Date**
- 🧑‍💻 **Role-based Access Control**
- 🎨 **Modern UI using Tailwind CSS**

---

## 📸 Screenshots

### 🔐 Login Page  
![Login](screenshots/login.png)

### 📝 Register Page  
![Register](screenshots/register.png)

### 📊 Dashboard – Your Vehicles  
![Dashboard](screenshots/dashboard.png)

### 🛠️ Maintenance Record Management  
![Maintenance](screenshots/maintenance.png)
---

## 🚀 Tech Stack

| Layer      | Technology                  |
|------------|-----------------------------|
| Frontend   | HTML5, Tailwind CSS         |
| Backend    | Flask (Python)              |
| Database   | MySQL + SQLAlchemy ORM      |
| Auth       | Flask-Login + Flask-WTF     |
| Deployment | `localhost` (dev), Render (prod) |

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/sharan414/automate.git
cd automate
2. Create Virtual Environment & Install Dependencies
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
3. Configure Database
Make sure MySQL is running locally.

Create a database named automate:

sql
Copy
Edit
CREATE DATABASE automate;
Update your database credentials inside app/__init__.py if needed:

python
Copy
Edit
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Mysql1234@localhost/automate'
4. Run the App
bash
Copy
Edit
python run.py
Go to 👉 http://127.0.0.1:5000

📁 Folder Structure
arduino
Copy
Edit
automate/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── forms.py
│   ├── routes.py
│   ├── templates/
│   │   ├── login.html, register.html, dashboard.html ...
│   └── static/
│       └── images/
│           ├── automate dashbord.png
│           ├── automate login.png
│           ├── automate register.png
│           └── automate Maintenance.png
├── run.py
└── requirements.txt
💡 Future Improvements
Email verification

Password reset flow

Notifications for upcoming maintenance

Admin panel for user management

🧑‍💻 Author
Built by Sharan – GitHub

