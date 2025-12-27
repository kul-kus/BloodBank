# 🩸 Blood Bank Management System

A **Blood Bank Management System** built using **Python, Flask, and MySQL** as a school/college project.  
This project demonstrates **role-based authentication**, **session handling**, and **database-driven dashboards**.

---

## 📌 Features

### 👤 User

-  Login & Logout
-  View blood stock (read-only)

### 🧑‍💼 Agent

-  Login & Logout
-  View blood stock
-  Access agent dashboard

### 👑 Admin

-  Login & Logout
-  Create users (user / agent / admin)
-  Add or subtract blood stock
-  View and manage stock
-  Admin dashboard

---

## 🛠 Tech Stack

| Layer      | Technology    |
| ---------- | ------------- |
| Backend    | Python 3      |
| Framework  | Flask         |
| Database   | MySQL         |
| DB Driver  | PyMySQL       |
| Frontend   | HTML, CSS     |
| Env Config | python-dotenv |
| Session    | Flask Cookies |

---

## 📁 Project Structure

```
BloodBank/
│
├── app/
│   ├── main.py
│   │
|   |── Database/
│   │   ├── connect.py
│   │   ├── creation_tables.py
│   │
│   ├── Logic/
│   │   └── common.py
│   │
│   ├── templates/
│   │   ├── login.html
│   │   ├── user_home.html
│   │   ├── admin_dashboard.html
│   │   └── agent_dashboard.html
│   │
│   └── static/
│       └── home.css
│       └── style.css
├── .env
├── requirements.txt
└── README.md
```

---

## 🐍 Python Requirement

-  Python 3.8 or higher

Check version:

```bash
python3 --version
```

---

## 📦 Install Dependencies

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Packages

```bash
pip install flask pymysql python-dotenv
```

---

## 🔐 Environment Configuration (.env)

Create `.env` file:

```env
FLASK_SECRET_KEY=your_secret_key_here
DB_HOST=localhost
DB_PORT=3306
DB_NAME=blood_bank
DB_USER=root
DB_PASSWORD=password
```

---

## ▶️ Run the Application

```bash
python3 app/main.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 🚫 Security Notes

-  Do not commit `.env`
-  Password hashing recommended

---

## 🎯 Learning Outcomes

-  Flask routing
-  MySQL integration
-  Sessions & cookies
-  Role-based access

---

## 🎯 Future Enahncement

-  Create, Update, Delete, View Operations for users
-  Create, Update, Delete, View Operations for Blood Stock
