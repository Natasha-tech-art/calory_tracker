#  Calorie Counter Website

A web-based calorie tracking application built with **Django** that helps users monitor and manage their daily calorie intake. The project follows Django’s **Model-View-Template (MVT)** architecture and is deployed using **Render**.

---

#  Features

- Add daily meals and calorie values
- Track total calorie intake
- Edit and delete food entries
- Clean and responsive user interface
- Django MVT architecture implementation
- Database management using Django ORM
- Deployment with Render

---

#  Technologies Used

- Python
- Django
- HTML5
- TAILWIND
- SQLite3
- Postgresql

---


# Installation Guide

## 1️ Clone the Repository

```bash
git clone https://github.com/your-username/calorie-counter.git
cd calorie-counter
```

---

## 2️ Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️ Apply Database Migrations

```bash
python manage.py migrate
```

---

## 5️ Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```bash
http://127.0.0.1:8000/
```

---


#  Deployment on Render

This application is deployed using **Render**.

## Render Deployment Steps

### 1. Push Project to GitHub

```bash
git add .
git commit -m "Initial deployment"
git push origin main
```

### 2. Create a Render Web Service

- Log in to Render
- Click **New Web Service**
- Connect your GitHub repository

### 3. Add Build Command

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

### 4. Add Start Command

```bash
gunicorn calorie_counter.wsgi:application
```

### 5. Deploy the Project

Render will automatically build and deploy the application.

---

#  Environment Variables

Create a `.env` file in the project root directory:

```env
DEBUG=False
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=your-app-name.onrender.com
```

---

#  Requirements

Example dependencies inside `requirements.txt`:

```txt
Django
gunicorn
python-dotenv
dj-database-urls
```

---


#  Future Improvements

- User authentication system
- Nutrition API integration
- Weekly and monthly reports
- Graphs and analytics dashboard
- Mobile app version

---

#  Author

Developed by **Natasha Bolyn**

---



