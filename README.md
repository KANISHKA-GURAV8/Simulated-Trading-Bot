# Trading Bot Demo (Simulated)

## 📌 Project Overview

This project is a **simulated trading bot system** built as part of an **internship assignment**.
It demonstrates how a real trading platform works **without using real money or real APIs**.

The system allows users to place **BUY/SELL market and limit orders** through:

* A **web interface (UI)** built with HTML, CSS, JavaScript, and Bootstrap
* A **Flask backend** that handles validation, order processing, and logging

This project follows the same concept as a **demo booking system (like IRCTC demo booking)** — logic is real, execution is simulated.

---

## 🛠️ Tech Stack

### Backend

* **Python**
* **Flask** (Web framework)
* Modular architecture (`orders`, `client`, `validators`)
* Logging using Python `logging` module

### Frontend

* **HTML5**
* **CSS3**
* **JavaScript**
* **Bootstrap 5** (via CDN)
* **Font Awesome** (icons)
* **Google Fonts (Inter)**

### CDN Links Used

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
```

---

## 📂 Project Structure

```
trading-bot/
│
├── app.py                  # Flask application entry point
├── bot/
│   ├── client.py           # Mock Binance client (simulated API)
│   ├── orders.py           # Order handling logic
│   ├── validators.py       # Input validation
│   └── logging_config.py   # Logging configuration
│
├── templates/
│   └── index.html          # Frontend UI (HTML)
│
├── static/
|               # (Optional) CSS / JS files
│
├── logs/
│   └── trading_bot.log     # Application logs
│
└── README.md
```

---

## 🚀 Features

* Place **Market Orders** (executed immediately)
* Place **Limit Orders** (created but pending)
* Input validation (quantity, order type, price checks)
* Clear error messages for invalid inputs
* Simulated order execution (no real trading)
* Logging of all actions and errors
* Clean and responsive UI

---

## 🧠 How the System Works

1. User submits order details from the web UI
2. Flask receives the request
3. Input is validated (BUY/SELL, quantity, price rules)
4. Order is processed using a **mock trading client**
5. Result is displayed on the UI
6. All actions are logged in a log file

---

## ▶️ How to Run the Project

### 1️⃣ Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 2️⃣ Install dependencies

```bash
pip install flask
```

### 3️⃣ Run the Flask app

```bash
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

