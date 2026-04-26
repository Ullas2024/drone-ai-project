import streamlit as st
import time
import pandas as pd
import numpy as np

# Page config
st.set_page_config(page_title="Drone AI System", layout="wide")

st.title("🚁 Autonomous Drone AI Control Center")
st.caption("Final Year Project | Agentic AI + Real-Time Monitoring")

st.markdown("---")

# ===== SIDEBAR =====
st.sidebar.header("⚙️ Drone Controls")

mode = st.sidebar.selectbox(
    "Mode",
    ["Standby", "Surveillance", "Search & Rescue", "Fire Detection"]
)

altitude = st.sidebar.slider("Altitude (m)", 10, 500, 120)
speed = st.sidebar.slider("Speed (km/h)", 10, 120, 40)

battery_level = st.sidebar.slider("Battery Level (%)", 0, 100, 85)
st.sidebar.progress(battery_level)

takeoff = st.sidebar.button("🚀 Takeoff")
land = st.sidebar.button("🛬 Land")

# ===== STATUS =====
col1, col2, col3 = st.columns(3)
col1.metric("📡 Signal", "Strong")
col2.metric("🌍 GPS", "Active")
col3.metric("🧠 AI", "Online")

st.markdown("---")

# ===== LIVE MAP (MOVING) =====
st.subheader("🗺️ Live Drone Tracking")

# simulate movement
lat = 12.97 + np.random.randn() * 0.002
lon = 77.59 + np.random.randn() * 0.002

map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
st.map(map_data)

# ===== LIVE CHART =====
st.subheader("📊 Drone Telemetry")

chart_data = pd.DataFrame({
    "Altitude": np.random.randint(100, altitude, 10),
    "Battery": np.random.randint(20, battery_level, 10)
})

st.line_chart(chart_data)

# ===== CAMERA =====
st.subheader("📷 Live Camera Feed")

camera_option = st.selectbox("Camera Source", ["Simulated Feed", "Use Webcam"])

if camera_option == "Simulated Feed":
    st.image("https://via.placeholder.com/600x300.png?text=Drone+Camera+Live")

else:
    img = st.camera_input("Capture Live Feed")

# ===== AI COMMAND =====
st.markdown("---")
st.subheader("📥 Mission Control")

command = st.text_input("Enter command (scan, detect fire, patrol...)")

if st.button("▶ Execute Mission"):
    if command:
        with st.spinner("AI thinking..."):
            time.sleep(2)

        # simple intelligent response
        if "fire" in command.lower():
            st.error("🔥 Fire detected! Alert sent!")
        elif "scan" in command.lower():
            st.success("📡 Area scanned successfully")
        elif "rescue" in command.lower():
            st.warning("🚑 Rescue mode activated")
        else:
            st.info(f"Command executed: {command}")

        st.markdown("### 📊 Mission Report")
        st.write("✔ Path optimized")
        st.write("✔ No collision risk")
        st.write("✔ Task completed")

    else:
        st.error("Enter command!")

# ===== ACTIONS =====
if takeoff:
    st.success("🚁 Drone Taking Off...")

if land:
    st.warning("🛬 Drone Landing...")

st.markdown("---")
st.caption("🚁 AI Drone System | Built using Streamlit + Python")