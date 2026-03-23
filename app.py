import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Smart Grid DSM", layout="centered")

st.title("⚡ Smart Grid DSM Platform with Smart Meter")

# ⏰ Time Selection
hour = st.slider("Select Hour of the Day", 0, 23, 16)

# 💰 Dynamic Pricing
if 18 <= hour <= 22:
    price = 8
    status = "Peak Hour 🔴"
elif 10 <= hour <= 17:
    price = 6
    status = "Medium Load 🟡"
else:
    price = 4
    status = "Normal Hour 🟢"

st.write(f"Current Hour: {hour}")
st.write(f"Status: {status}")
st.write(f"Electricity Price: ₹{price}/kWh")

# 🔌 Smart Devices
st.subheader("Smart Devices")

ac = st.checkbox("Air Conditioner (1.5 kW)", True)
ev = st.checkbox("EV Charger (3 kW)", True)
lights = st.checkbox("Lights (0.5 kW)", True)
fan = st.checkbox("Fan (0.2 kW)", True)

# ⚡ Load Calculation
total_load = 0
if ac: total_load += 1.5
if ev: total_load += 3
if lights: total_load += 0.5
if fan: total_load += 0.2

# 🚨 Smart Control Logic
control_msg = ""
if total_load > 5:
    if ev:
        total_load -= 3
        ev = False
        control_msg = "⚠️ EV Charger turned OFF (Auto Load Control)"

# 💰 Cost Calculation
cost = total_load * price

# 📊 Smart Meter Display
st.subheader("📊 Smart Meter")

col1, col2 = st.columns(2)
col1.metric("⚡ Total Load", f"{total_load} kW")
col2.metric("💰 Cost / Hour", f"₹{round(cost, 2)}")

# 📈 Graph
st.subheader("📈 Power Usage Trend")

data = [round(total_load + random.uniform(-0.5, 0.5), 2) for _ in range(10)]
df = pd.DataFrame(data, columns=["Load (kW)"])
st.line_chart(df)

# 🧠 Prediction
predicted_load = round(total_load + random.uniform(-0.3, 0.7), 2)
st.info(f"🔮 Predicted Next Hour Load: {predicted_load} kW")

# 💸 Cost Comparison
off_peak_cost = total_load * 4
extra_cost = cost - off_peak_cost

if extra_cost > 0:
    st.warning(f"⚠️ You are paying ₹{round(extra_cost,2)} extra due to peak pricing")

# 🔋 Efficiency Score
efficiency = max(0, 100 - total_load * 10)
st.progress(efficiency / 100)  # FIXED
st.write(f"🔋 Energy Efficiency Score: {round(efficiency,1)}%")

# 🚦 Load Status
if total_load < 3:
    st.success("🟢 Load is Normal")
elif total_load < 5:
    st.warning("🟡 Load is High")
else:
    st.error("🔴 Critical Load!")

# ⚠️ Control Message
if control_msg:
    st.warning(control_msg)

# 💡 Suggestion
if price >= 8:
    st.info("💡 Tip: Shift heavy loads to off-peak hours")

# ✅ System Status
st.success("☁️ Cloud System Running Successfully")

# 🏁 Footer
st.caption("⚙️ Developed as part of Cloud-Based Smart Grid DSM using IoT simulation")