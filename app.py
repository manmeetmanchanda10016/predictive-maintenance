
import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Predictive Maintenance AI",
    page_icon="⚙️",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #101827;
    color: #f8fafc;
}

.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}

h1, h2, h3, p, label {
    color: #f8fafc !important;
}

[data-testid="stSidebar"] {
    background: #172033;
}

[data-testid="stSidebar"] * {
    color: #e2e8f0;
}

[data-testid="stMetric"] {
    background: #202b48;
    border: 1px solid #334155;
    padding: 18px;
    border-radius: 14px;
}

[data-testid="stMetricLabel"] {
    color: #bfdbfe !important;
}

[data-testid="stMetricValue"] {
    color: #60a5fa !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #182337;
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 18px;
}

div.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white;
    border: none;
    border-radius: 10px;
    height: 3em;
    font-weight: bold;
}

div.stButton > button:hover {
    border: 1px solid #93c5fd;
    color: white;
}

hr {
    border-color: #334155;
}
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_model():
    return joblib.load("predictive_maintenance_model.pkl")


st.sidebar.markdown("# ⚙️ Machine AI")
st.sidebar.caption("PREDICTIVE INTELLIGENCE")
st.sidebar.divider()
st.sidebar.markdown("### 🏠 Dashboard")
st.sidebar.markdown("### 🔍 Failure Prediction")
st.sidebar.markdown("### 📈 Machine Parameters")
st.sidebar.divider()
st.sidebar.info("Monitor machine operating conditions using your trained ML model.")

st.markdown("# ⚙️ Predictive Maintenance")
st.markdown("AI-powered equipment health dashboard")
st.markdown("Identify potential machine failures using operating parameters.")

st.divider()

try:
    model = load_model()
except Exception as e:
    st.error("Unable to load the saved model.")
    st.code(str(e))
    st.info("Check that the model file and scikit-learn version match.")
    st.stop()

# Machine input section
st.markdown("## 🛠️ Machine Configuration")

with st.container(border=True):
    col1, col2 = st.columns(2)

    with col1:
        machine_type = st.selectbox(
            "Machine Type",
            ["L", "M", "H"]
        )

        air_temp = st.number_input(
            "🌡️ Air Temperature (K)",
            min_value=0.0,
            value=300.0,
            step=0.1
        )

        process_temp = st.number_input(
            "🔥 Process Temperature (K)",
            min_value=0.0,
            value=310.0,
            step=0.1
        )

    with col2:
        rot_speed = st.number_input(
            "⚙️ Rotational Speed (rpm)",
            min_value=0,
            value=1500,
            step=10
        )

        torque = st.number_input(
            "🔧 Torque (Nm)",
            min_value=0.0,
            value=40.0,
            step=0.5
        )

        tool_wear = st.number_input(
            "⏱️ Tool Wear (min)",
            min_value=0,
            value=100,
            step=1
        )

st.markdown("## 📊 Machine Health Overview")

# These cards show the current input values, not measured health scores.
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div style="background:#173B36;padding:20px;border-radius:14px;
    border:1px solid #166534;min-height:125px">
    <div style="color:#86efac;font-size:14px">🌡️ AIR TEMPERATURE</div>
    <div style="color:#4ade80;font-size:30px;font-weight:700">
    """ + f"{air_temp:g} K" + """</div>
    <div style="color:#a7f3d0;font-size:12px">Current input</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div style="background:#392D19;padding:20px;border-radius:14px;
    border:1px solid #92400e;min-height:125px">
    <div style="color:#fcd34d;font-size:14px">⚙️ ROTATIONAL SPEED</div>
    <div style="color:#fbbf24;font-size:30px;font-weight:700">
    """ + f"{rot_speed:,} rpm" + """</div>
    <div style="color:#fde68a;font-size:12px">Current input</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div style="background:#202B48;padding:20px;border-radius:14px;
    border:1px solid #1d4ed8;min-height:125px">
    <div style="color:#93c5fd;font-size:14px">🔧 TOOL WEAR</div>
    <div style="color:#60a5fa;font-size:30px;font-weight:700">
    """ + f"{tool_wear} min" + """</div>
    <div style="color:#bfdbfe;font-size:12px">Current input</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

with st.container(border=True):
    st.markdown("### 🔩 Operating Parameters")

    p1, p2, p3 = st.columns(3)

    p1.metric("Machine Type", machine_type)
    p2.metric("Process Temperature", f"{process_temp:g} K")
    p3.metric("Torque", f"{torque:g} Nm")

st.write("")

if st.button("🔍  PREDICT MACHINE FAILURE"):
    data = pd.DataFrame([{
        "Type": machine_type,
        "Air temperature [K]": air_temp,
        "Process temperature [K]": process_temp,
        "Rotational speed [rpm]": rot_speed,
        "Torque [Nm]": torque,
        "Tool wear [min]": tool_wear
    }])

    try:
        prediction = model.predict(data)[0]

        st.markdown("## 🩺 Prediction Result")

        if prediction == 1:
            st.markdown("""
            <div style="background:#451f28;padding:25px;border-radius:16px;
            border:1px solid #ef4444">
            <div style="font-size:28px;color:#f87171;font-weight:700">
            ⚠️ MACHINE FAILURE PREDICTED
            </div>
            <p style="color:#fecaca">
            The model predicts a potential machine failure.
            Inspect the equipment and investigate the cause.
            </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="background:#173b36;padding:25px;border-radius:16px;
            border:1px solid #22c55e">
            <div style="font-size:28px;color:#4ade80;font-weight:700">
            ✅ NO MACHINE FAILURE PREDICTED
            </div>
            <p style="color:#a7f3d0">
            The model predicts no failure for the supplied parameters.
            Continue normal monitoring.
            </p>
            </div>
            """, unsafe_allow_html=True)

        with st.expander("📋 View Prediction Input Details"):
            st.dataframe(data, use_container_width=True)

    except Exception as e:
        st.error("Prediction failed.")
        st.code(str(e))

st.divider()
st.caption("Predictive Maintenance AI | Machine Learning Project")
