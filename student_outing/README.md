# 🛡️ Student Outing Monitoring Web App

A simple full-stack web application to monitor student outings and check-ins. Built with **Flask + SQLite**, using **Vanilla JS** on the frontend and optionally hosted on **AWS EC2** with infrastructure managed via **Terraform**.

---

## 🚀 Features

- 🧍 Student can register "Outing" using Student ID
- ✅ On return, student can "Check In"
- 🕒 Admin can view students who haven't returned within 24 hours
- 🔐 Admin login authentication (session-based)
- 📜 Students can view their personal outing logs
- ⏳ Optional: Auto-check pending via cron or Lambda

---

## 🛠️ Technologies Used

| Layer        | Technology                   |
|--------------|-------------------------------|
| Frontend     | HTML, CSS, Vanilla JavaScript |
| Backend      | Python (Flask)                |
| Database     | SQLite (embedded, simple)     |
| Infra-as-Code| Terraform                     |
| Hosting      | AWS EC2 (Flask backend)       |
| (Optional)   | AWS S3 (for static files)     |
| Scheduler    | Python cron or AWS Lambda     |

---

## 📁 Project Structure

```plaintext
student-outing-monitoring/
│
├── backend/
│   ├── app.py              # Flask backend routes
│   ├── database.py         # All DB functions (register, check-in, logs, etc.)
│   ├── outing.db           # SQLite database (auto-created)
│   ├── templates/
│   │   └── index.html      # Main frontend file (served by Flask)
│   └── static/
│       ├── style.css       # Styles
│       └── script.js       # JS logic (validation, fetch, etc.)
│
├── terraform/
│   ├── main.tf             # Terraform config for EC2 deployment
│   └── variables.tf        # AWS key variables
│
└── README.md               

1.Clone & Setup Environment
git clone https://github.com/your-username/student-outing-monitoring.git
cd student-outing-monitoring/backend

# Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate

# Install Flask
pip install flask

2. Run the Application
python app.py
