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

for i in range(0,len(haberler)):
    col1,col2,col3=st.colums(3)
    with col1:
        st.image(haberler[i][3])
        st.write(haberler[i][1])
        st.link_button("habelere git", haberler[i][2])
    with col2:
        st.image(haberler[i+1][3])
        st.write(haberler[i+1][1])
        st.link_button("habelere git", haberler[i+1][2])
    with col3:
        st.image(haberler[i+2][3])
        st.write(haberler[i+2][1])
        st.link_button("habelere git", haberler[i+2][2])
