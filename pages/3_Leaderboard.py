import streamlit as st
import plotly.express as px
import plotly.colors as pc
import pandas as pd
from google_sheets_helper import read_points, write_points
from points_config import gsheetname, mentors_list, category_list, core_list, non_core_list, points_d



st.title('Leaderboard')

# Example: custom shades for each category
blues = pc.sequential.Blues[3:]  # several blue shades
greens = pc.sequential.Greens[3:]

core_colors = blues[:len(core_list)]
non_core_colors = greens[:len(non_core_list)]  
sub_cat_color_map = dict(zip(core_list + non_core_list, core_colors + non_core_colors))

df = read_points(gsheetname)
df = pd.DataFrame(df)

fig = px.bar(df, y="Mentor", x="Points", color="Sub-Category", barmode="stack", pattern_shape="Category",  color_discrete_map=sub_cat_color_map)


fig = fig.update_layout(
    legend=dict(
        orientation="h",
        yanchor="top",
        y=-0.2,
        xanchor="center",
        x=0.35
    ),
)


st.plotly_chart(fig, use_container_width=True)