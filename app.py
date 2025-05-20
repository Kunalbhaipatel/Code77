import streamlit as st
st.set_page_config(page_title="Shaker Health Dashboard", layout="wide", initial_sidebar_state="expanded")

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import time

# Dark Mode Styles
st.markdown("""
<style>
    body {
        background-color: #121212;
        color: #FFFFFF;
    }
    .stApp {
        background-color: #1E1E1E;
    }
    .css-18e3th9 {
        background-color: #1E1E1E;
    }
    .css-1d391kg, .css-1v0mbdj, .css-1r6slb0, .css-1v0mbdj p {
        color: #FFFFFF;
    }
    .stButton>button {
        color: white;
        background-color: #2E86AB;
    }
</style>
""", unsafe_allow_html=True)

# Animation helper
with st.spinner('🔧 Loading Shaker Dashboard...'):
    time.sleep(1.5)

st.markdown("""
<h1 style='text-align: center; color: #2E86AB; animation: fadeInDown 1s;'>🛠️ Real-Time Shaker Monitoring Dashboard</h1>
<style>
@keyframes fadeInDown {
  from { opacity: 0; transform: translateY(-20px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)
