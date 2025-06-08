# 🛒 E-commerce Chatbot Project

This is a full-stack E-commerce Chatbot web application that provides product information and basic customer interaction features. It includes user authentication (login/register) and real-time product query response. Built with a combination of modern web technologies including **React**, **Node.js**, **Flask**, **PostgreSQL**, and styled using **HTML** and **CSS**.

---

## 🔧 Tech Stack

- **Frontend:**
  - React.js
  - HTML5, CSS3
- **Backend:**
  - Node.js
  - Flask (Python)
- **Database:**
  - PostgreSQL
- **Others:**
  - RESTful APIs
  - JWT Authentication
  - Express.js (Node backend)

---

## 🚀 Features

- 🧾 **User Authentication**  
  Secure login and registration pages:
  - Login: `http://localhost:3000/login`
  - Register: `http://localhost:3000/register`

- 🤖 **Interactive Chatbot**  
  - The chatbot provides information about products in real-time.
  - ChatBox interface built using React.

- 📦 **Product Query System**  
  Ask about product details and receive accurate information instantly.

---

## 📂 Folder Structure

root/
├── client/ # React frontend
│ └── src/
│ └── components/ # Chatbox, Login, Register etc.
├── server/ # Node backend
├── flask-api/ # Python Flask chatbot API
└── database/ # PostgreSQL schema and scripts


---

## 🛠️ Local Setup

### Prerequisites:
- Node.js & npm
- Python & pip
- PostgreSQL

### Steps to Run:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/ecommerce-chatbot.git
   cd ecommerce-chatbot


2. **Install Frontend Dependencies0**:

bash
Copy
Edit
cd client
npm install
npm start
Open on:

http://localhost:3000

On your network: http://192.168.154.124:3000

3. **Install Backend (Node.js) Dependencies:**

bash
Copy
Edit
cd ../server
npm install
npm run start

4. **Run Flask API:**

bash
Copy
Edit
cd ../flask-api
pip install -r requirements.txt
python app.py

5. **Set up PostgreSQL Database:**

Create the database using the schema in /database/schema.sql.

📌 Important URLs

| Page        | URL                                                              |
| ----------- | ---------------------------------------------------------------- |
| Homepage    | [http://localhost:3000](http://localhost:3000)                   |
| Login       | [http://localhost:3000/login](http://localhost:3000/login)       |
| Register    | [http://localhost:3000/register](http://localhost:3000/register) |
| Network URL | [http://192.168.154.124:3000](http://192.168.154.124:3000)       |



🙌 **Contribution**
If you'd like to contribute, feel free to fork the repo and submit a pull request. For major changes, please open an issue first to discuss what you'd like to change.