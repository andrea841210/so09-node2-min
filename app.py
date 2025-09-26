import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smoke Test", layout="wide")
st.title("Streamlit Cloud • Smoke Test")
st.write("If you see this, the environment built correctly ✅")

uploaded = st.file_uploader("Upload a small CSV to plot", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df.head())
    if df.shape[1] >= 2:
        col = df.columns[1]
        fig, ax = plt.subplots()
        ax.plot(df.index, df[col])
        st.pyplot(fig)
