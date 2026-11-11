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
#Show your invoices on the page
import pandas as pd

headers = {"Authorization": f"Bearer {token}"}
r = requests.get(f"{BASE}/v2/invoicing/invoices?page_size=100", headers=headers)
invoices = r.json().get("items", [])

rows = []
for inv in invoices:
    rows.append({
        "Invoice #": inv["detail"].get("invoice_number"),
        "Status": inv["status"],
        "Amount ($)": float(inv["amount"]["value"]),
    })

df = pd.DataFrame(rows)
st.metric("Total invoiced", f"${df['Amount ($)'].sum():,.2f}" if not df.empty else "$0")
st.dataframe(df)
