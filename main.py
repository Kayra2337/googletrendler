import streamlit as st
import xml.etree.ElementTree as et
import sqlitecloud
import sqlite3
import requests
from datetime import date
from google import genai
from pydantic import BaseModel
import fonksiyonlar

conn = sqlitecloud.connect('sqlitecloud://cwyir6txnk.g4.sqlite.cloud:8860/chinook.sqlite?apikey=AmFPZIWsoYnglTnSVZ3taxbHswEiWP44FRygTmD1hNg')
c = conn.cursor()

c.execute("SELECT * FROM haberler ORDER BY trend_id LIMIT 99")
haberler = c.fetchall()

for i in range(haberler):
    st.image(haberler[i][3])
    st.write(haberler[i][1])
    st.link_button("habelere git", haberler[i][2])
