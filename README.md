# 🚀 AI-Based Autonomous Navigation System

An interactive AI simulation that demonstrates **autonomous navigation using the A* path planning algorithm** with a modern **Streamlit web interface**.

The system allows users to dynamically create obstacles and visualize how an intelligent agent finds the optimal path from start to goal in real time with animation.

---

## 📌 Project Overview

This project simulates how autonomous systems (like self-driving cars and warehouse robots) navigate in an environment while avoiding obstacles.

It combines:
- Artificial Intelligence (Path Planning)
- A* Algorithm
- Grid-based simulation
- Interactive Web UI (Streamlit)
- Real-time visualization

---

## 🎯 Problem Statement

Autonomous systems must:
- Find the shortest path
- Avoid obstacles dynamically
- Adapt to changing environments

This project solves these challenges using a grid-based AI simulation.

---

## 🌍 Real-World Applications

- 🚗 Self-driving cars
- 🤖 Warehouse robots (Amazon)
- 🚁 Drone navigation
- 📦 Delivery robots
- 🏭 Industrial automation

---

## ⚙️ Tech Stack

- Python 🐍
- NumPy
- Matplotlib
- Streamlit
- A* Pathfinding Algorithm

---

## 🧠 Algorithm Used

### 🔹 A* (A-Star)
A* finds the optimal path using:
- g(n): cost from start
- h(n): estimated cost to goal

It ensures **efficient and optimal navigation**.

---

## 🏗️ System Architecture
User Input (Clickable Grid) ↓ Environment (Grid Matrix) ↓ Obstacle Placement ↓ A* Algorithm ↓ Optimal Path ↓ Animated Navigation

---

## 📁 Project Structure
AI-Autonomous-Navigation-System/ │
├── algorithms/ │
└── astar.py │
├── src/ │
├── app.py │
└── main.py │
├── outputs/ │
  └── screenshots/ │   
      ├── grid.png │     
      ├── obstacles.png │    
      └── navigation.png │ 
├── README.md 
└── requirements.txt

---

## 🚀 Installation

```bash
git clone https://github.com/your-username/AI-Autonomous-Navigation-System.git
cd AI-Autonomous-Navigation-System
Bash
python -m venv venv
venv\Scripts\activate
Bash
pip install -r requirements.txt
▶️ Run the Project
Bash
streamlit run src/app.py
🎮 How It Works
Set grid size
Click cells to add/remove obstacles
Click Run Navigation
AI computes optimal path
Agent moves from start → goal
📊 Outputs
The system demonstrates:
✔ Grid environment creation
✔ Dynamic obstacle placement
✔ Optimal path generation
✔ Real-time animated navigation
📸 Screenshots
🟢 Grid Interface
�
⬛ Obstacles Added
�
🔵 Navigation Output (Path + Agent)
�
📈 Future Improvements
Add BFS & Dijkstra algorithms
Add speed control
Multi-agent simulation
Integrate OpenCV
Upgrade to CARLA simulator
🧠 Learning Outcomes
A* path planning
Autonomous navigation logic
Simulation design
Streamlit UI development
Real-time visualization
