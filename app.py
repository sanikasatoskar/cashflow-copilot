import streamlit as st

st.title("Cash-Flow Copilot")
import requests

BASE = "https://api-m.sandbox.paypal.com"

def get_token():
    resp = requests.post(
        f"{BASE}/v1/oauth2/token",
        auth=(st.secrets["PAYPAL_CLIENT_ID"], st.secrets["PAYPAL_SECRET"]),
        data={"grant_type": "client_credentials"},
    )
    return resp.json()["access_token"]

token = get_token()
st.write("Connected to PayPal ✅")
