import streamlit as st
import plotly.express as px
import pandas as pd
from google_sheets_helper import read_points, write_points
from points_config import gsheetname, mentors_list, category_list, core_list, non_core_list, points_d



st.title('Leaderboard')

df = read_points(gsheetname)
df = pd.DataFrame(df)
# st.dataframe(df)


fig = px.bar(df, y="Mentor", x="Points", color="Sub-Category", barmode="stack",
             pattern_shape="Category")
st.plotly_chart(fig, use_container_width=True)