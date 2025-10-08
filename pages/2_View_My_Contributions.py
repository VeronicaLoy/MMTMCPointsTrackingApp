import streamlit as st
import plotly.express as px
import pandas as pd
from google_sheets_helper import read_points, write_points
from points_config import gsheetname, mentors_list, category_list, core_list, non_core_list, points_d

st.title('View My Contributions')

data = read_points(gsheetname)
df = pd.DataFrame(data)

# TODO: put in a separate config file
mentors_list = mentors_list
mentor = st.selectbox('Filter by Mentor', mentors_list)

if mentor:
    df_mentor = df[df['Mentor']==mentor]
    st.dataframe(df_mentor)
else:
    st.dataframe(df)