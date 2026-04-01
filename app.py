import pandas as pd
import streamlit as st
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTLbdvkYr6oO84hHnfC0TrsL3kdTFvhlVa98gKGUVksVsJL6o1XuqACt6-rd7sySS6ATvW48johSOAV/pubhtml"
df = pd.read_csv(url)
st.title("Monitoramento IoT")
st.line_chart(df[['temperatura', 'umidade']])
st.dataframe(df)
