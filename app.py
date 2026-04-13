import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
import os

# Fix imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from algorithms.astar import astar

st.set_page_config(layout="wide")

st.title("🚀 AI-Based Autonomous Navigation System")

# Sidebar
st.sidebar.header("⚙️ Configuration")

ROWS = st.sidebar.number_input("Rows", 5, 25, 12)
COLS = st.sidebar.number_input("Columns", 5, 25, 12)

# Initialize grid
if "grid" not in st.session_state:
    st.session_state.grid = np.zeros((ROWS, COLS))

# Resize grid if changed
if st.session_state.grid.shape != (ROWS, COLS):
    st.session_state.grid = np.zeros((ROWS, COLS))

grid = st.session_state.grid

# Reset
if st.sidebar.button("🔄 Reset Grid"):
    st.session_state.grid = np.zeros((ROWS, COLS))
    grid = st.session_state.grid

start = (0, 0)
goal = (ROWS - 1, COLS - 1)

grid[start[0], start[1]] = 0
grid[goal[0], goal[1]] = 0

st.subheader("🖱️ Click cells to add/remove obstacles")

# Grid UI
for i in range(ROWS):
    cols = st.columns(COLS)
    for j in range(COLS):

        if (i, j) == start:
            label = "🟨"
        elif (i, j) == goal:
            label = "🟥"
        elif grid[i, j] == 1:
            label = "⬛"
        else:
            label = "⬜"

        if cols[j].button(label, key=f"{i}-{j}"):
            if (i, j) != start and (i, j) != goal:
                grid[i, j] = 1 - grid[i, j]

# Centered animation area
col1, col2, col3 = st.columns([1,2,1])
placeholder = col2.empty()

# Run animation
if st.sidebar.button("▶ Run Navigation"):

    path = astar(grid.tolist(), start, goal)

    if not path:
        st.error("❌ No Path Found")
    else:
        for step in path:

            # 🔥 FIXED SIZE (NOT BIG ANYMORE)
            fig, ax = plt.subplots(figsize=(4, 4))

            ax.imshow(grid, cmap='gray_r')

            # Clean square grid
            ax.set_xticks(np.arange(-0.5, COLS, 1), minor=True)
            ax.set_yticks(np.arange(-0.5, ROWS, 1), minor=True)
            ax.grid(which='minor', color='black', linestyle='-', linewidth=1)

            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_aspect('equal')  # 🔥 important

            # Path
            path_x = [p[1] for p in path]
            path_y = [p[0] for p in path]
            ax.plot(path_x, path_y, color='blue', linewidth=2)

            # Start, goal, agent
            ax.scatter(start[1], start[0], color='yellow', s=100)
            ax.scatter(goal[1], goal[0], color='red', s=100)
            ax.scatter(step[1], step[0], color='green', s=100)

            placeholder.pyplot(fig)

            time.sleep(0.15)

        st.success("✅ Goal Reached Successfully!")