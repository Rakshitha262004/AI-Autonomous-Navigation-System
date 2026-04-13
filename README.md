# 🚀 AI-Based Autonomous Navigation System

An interactive AI simulation that demonstrates **autonomous navigation using A* path planning algorithm** with a modern **web-based Streamlit interface**.

The system allows users to create obstacles dynamically and visualize how an intelligent agent finds the optimal path from start to goal in real time.

---

## 📌 Project Overview

This project simulates how autonomous systems (like self-driving cars and delivery robots) navigate in an environment while avoiding obstacles.

It combines:
- Artificial Intelligence (Path Planning)
- Graph-based algorithms (A*)
- Interactive Web UI (Streamlit)
- Real-time visualization

---

## 🎯 Problem Statement

Autonomous systems must:
- Find the shortest path from source to destination
- Avoid obstacles dynamically
- Adapt to environment changes in real-time

This project solves these challenges using a grid-based simulation.

---

## 🌍 Real-World Applications

- 🚗 Self-driving cars (Tesla, Waymo)
- 🤖 Warehouse robots (Amazon robotics)
- 🚁 Drone navigation systems
- 📦 Delivery robots
- 🏭 Industrial automation systems

---

## ⚙️ Tech Stack

- Python 🐍
- NumPy
- Matplotlib
- Streamlit (Frontend UI)
- A* Path Planning Algorithm

---

## 🧠 Algorithm Used

### 🔹 A* (A-Star) Algorithm
A* is a pathfinding algorithm that finds the shortest path using:
- Cost from start (g)
- Heuristic estimate to goal (h)

It ensures **optimal and efficient navigation**.

---

## 🏗️ System Architecture
User Interaction (Clickable Grid)
↓
Grid Environment Creation
↓
Obstacle Placement
↓
A* Path Planning Algorithm
↓
Optimal Path Generation
↓
Real-time Visualization (Streamlit UI)


---

## 📁 Folder Structure


AI-Autonomous-Navigation-System/
│
├── algorithms/
│ └── astar.py
│
├── simulation/
│ ├── agent.py
│ └── environment.py
│
├── src/
│ ├── app.py # Streamlit Web App
│ └── main.py # Pygame Simulation (optional)
│
├── outputs/
│ └── screenshots/
│ ├── grid.png
│ ├── obstacles.png
│ └── navigation.png
│
├── README.md
└── requirements.txt


---

## 🚀 Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/AI-Autonomous-Navigation-System.git
cd AI-Autonomous-Navigation-System
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ How to Run
🔹 Run Streamlit Web App (Recommended)
streamlit run src/app.py
🔹 Run Pygame Simulation (Optional)
python -m src.main