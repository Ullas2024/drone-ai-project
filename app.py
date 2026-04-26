import streamlit as st
import time
import folium
from streamlit_folium import st_folium
import pandas as pd
import numpy as np

# ===== PAGE CONFIG =====
st.set_page_config(page_title="Drone AI System", layout="wide")

st.title("🚁 Autonomous Drone AI Control Center")
st.caption("AI-Based Real-Time Drone Monitoring System")

st.markdown("---")

# ===== SIDEBAR =====
st.sidebar.header("⚙️ Drone Controls")

mode = st.sidebar.selectbox(
    "Mode",
    ["Standby", "Surveillance", "Search & Rescue", "Fire Detection"]
)

altitude = st.sidebar.slider("Altitude (m)", 10, 500, 120)
speed = st.sidebar.slider("Speed (km/h)", 10, 120, 40)

battery = st.sidebar.slider("Battery (%)", 0, 100, 85)
st.sidebar.progress(battery)

takeoff = st.sidebar.button("🚀 Takeoff")
land = st.sidebar.button("🛬 Land")

# ===== STATUS =====
col1, col2, col3 = st.columns(3)
col1.metric("📡 Signal", "Strong")
col2.metric("🌍 GPS", "Active")
col3.metric("🧠 AI", "Online")

st.markdown("---")

# ===== MISSION ROUTE =====
st.subheader("🗺️ Mission Route Tracking")

mission_path = [
    (12.9716, 77.5946),
    (12.9720, 77.5955),
    (12.9730, 77.5950),
    (12.9725, 77.5938),
    (12.9716, 77.5946)
]

# ===== SESSION STATE =====
if "step" not in st.session_state:
    st.session_state.step = 0

if "path_travelled" not in st.session_state:
    st.session_state.path_travelled = [mission_path[0]]

if "running" not in st.session_state:
    st.session_state.running = False

# ===== CONTROL BUTTONS =====
colA, colB = st.columns(2)

if colA.button("▶️ Start Mission"):
    st.session_state.running = True

if colB.button("⏸️ Pause Mission"):
    st.session_state.running = False

# ===== DRONE MOVEMENT =====
if st.session_state.running:
    current_position = mission_path[st.session_state.step]
    st.session_state.path_travelled.append(current_position)
    st.session_state.step = (st.session_state.step + 1) % len(mission_path)
    time.sleep(1)
    st.rerun()
else:
    current_position = mission_path[st.session_state.step]

# ===== MAP =====
m = folium.Map(location=current_position, zoom_start=16)

folium.PolyLine(mission_path, color="gray", weight=2, dash_array="5").add_to(m)

if len(st.session_state.path_travelled) > 1:
    folium.PolyLine(st.session_state.path_travelled, color="blue", weight=4).add_to(m)

folium.Marker(
    location=current_position,
    tooltip="🚁 Drone",
    icon=folium.Icon(color="red")
).add_to(m)

st_folium(m, width=700, height=500)

st.success(f"📍 Current Location: {current_position}")

# ===== TELEMETRY =====
st.subheader("📊 Drone Telemetry")

telemetry = pd.DataFrame({
    "Altitude": np.random.randint(80, altitude, 10),
    "Battery": np.random.randint(20, battery, 10)
})

st.line_chart(telemetry)

# ===== CAMERA =====
st.subheader("📷 Camera Feed")

camera = st.selectbox("Camera Mode", ["Simulated", "Webcam"])

if camera == "Simulated":
    st.image("https://via.placeholder.com/600x300.png?text=Drone+Camera")
else:
    st.camera_input("Capture Image")

# ===== AGENT SYSTEM =====
st.markdown("---")
st.subheader("📥 Mission Control (Agent System)")

command = st.text_input("Enter command")

if st.button("▶ Execute Command"):

    if command:

        st.write("### 🤖 Agent Logs (Verbose Mode)")

        st.write("🧠 Planner Agent: Analyzing command...")
        time.sleep(1)

        st.write("📡 Navigation Agent: Planning route...")
        time.sleep(1)

        st.write("🎥 Vision Agent: Activating sensors...")
        time.sleep(1)

        if "fire" in command.lower():
            st.write("🔥 Detection Agent: Fire detected!")
            st.error("🚨 ALERT: Fire detected!")
        
        elif "scan" in command.lower():
            st.write("📡 Scan Agent: Area scanned successfully")
            st.success("Scan complete")

        elif "rescue" in command.lower():
            st.write("🚑 Rescue Agent: Deploying rescue protocol")
            st.warning("Rescue mission started")

        else:
            st.write("⚙️ General Agent: Executing command")
            st.info(f"Command executed: {command}")

        st.write("✅ Mission Completed")

    else:
        st.error("Enter command!")

# ===== ACTIONS =====
if takeoff:
    st.success("🚁 Drone Taking Off...")

if land:
    st.warning("🛬 Drone Landing...")

st.markdown("---")
st.caption("🚁 Final Year Project | AI Drone Monitoring System")
