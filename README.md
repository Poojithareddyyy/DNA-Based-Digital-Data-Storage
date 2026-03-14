# DNA-Based Digital Data Storage System

A full-stack web application that demonstrates how digital data can be encoded into DNA sequences and decoded back into its original form. This project explores the concept of **DNA as a long-term digital data storage medium**, combining bioinformatics principles with modern web technologies.

The system provides a user-friendly interface where users can upload files, encode them into DNA-like sequences, and decode them back into their original digital format.

---

# Live Demo

Frontend (Vercel)
dna-based-digital-data-storage.vercel.app

Backend API (Render)
https://dna-based-digital-data-storage.onrender.com

API Documentation
https://dna-based-digital-data-storage.onrender.com/docs

---

# Tech Stack

## Frontend

* React.js
* Vite
* JavaScript
* HTML5
* CSS3

## Backend

* FastAPI
* Python
* Uvicorn

## Libraries

* NumPy
* Pandas
* Pillow
* Cryptography
* Matplotlib

---

# Project Architecture

User
↓
React Frontend (Vercel)
↓ API Requests
FastAPI Backend (Render)
↓
DNA Encoding & Decoding Algorithm
↓
File Reconstruction

---

# Features

* Upload digital files
* Convert digital data into DNA sequences
* Decode DNA sequences back into original files
* Interactive web interface
* Fast API-based backend processing
* Secure and efficient data encoding logic

---

# How It Works

1. User uploads a digital file.
2. The backend converts binary data into a DNA sequence.
3. The DNA sequence is displayed to the user.
4. The user can decode the DNA sequence.
5. The original file is reconstructed.

---

# Project Structure

DNA-Based-Digital-Data-Storage

backend/
Contains the FastAPI backend responsible for encoding and decoding DNA sequences.

frontend/
Contains the React.js user interface built using Vite.

render.yaml
Configuration file for deploying backend on Render.

---

# Installation (Run Locally)

## Clone the Repository

git clone https://github.com/Poojithareddyyy/DNA-Based-Digital-Data-Storage.git

cd DNA-Based-Digital-Data-Storage

---

# Run Backend

Navigate to backend folder

cd backend

Install dependencies

pip install -r requirements.txt

Start FastAPI server

python -m uvicorn app:app --port 8000 --reload

Backend will run on

http://localhost:8000

API Docs

http://localhost:8000/docs

---

# Run Frontend

Open another terminal

cd frontend

Install dependencies

npm install

Start development server

npm run dev

Frontend will run on

http://localhost:3000

---

# Deployment

## Backend Deployment

The backend is deployed using **Render**.

Build Command

pip install -r requirements.txt

Start Command

uvicorn app:app --host 0.0.0.0 --port 10000

---

## Frontend Deployment

The frontend is deployed using **Vercel**.

Framework

Vite

Build Command

npm run build

Output Directory

dist

---

# Future Improvements

* Error correction algorithms for DNA storage
* Support for larger file sizes
* Cloud storage integration
* Improved visualization of DNA sequences
* User authentication system

---

# Use Cases

* Long-term archival storage
* Bioinformatics research
* Experimental digital storage methods
* Educational demonstration of DNA computing

---

# Author

Poojitha Reddy
Information Technology Student
Mallareddy University

GitHub
https://github.com/Poojithareddyyy

---

# License

This project is licensed under the MIT License.
