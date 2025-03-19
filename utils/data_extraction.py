import pandas as pd
import os
import requests
import streamlit as st


@st.cache_data(ttl=3600)
def get_crypto_symbols():
    """
    This function scrapes the Yahoo Finance Cryptocurrency page and returns a dictionary of 
    Crypto symbols.
    """

    url = 'https://finance.yahoo.com/markets/crypto/all/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/90.0.4430.93 Safari/537.36 "
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    html = response.text
    df_list = pd.read_html(html)
    df = df_list[0]
    df = df[df['Symbol'] != 'Symbol']

    crypto_symbols = {
        f"{row['Name']} ({row['Symbol']})": f"{row['Symbol']}"
        for _, row in df.iterrows()
    }

    return crypto_symbols