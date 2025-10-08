import streamlit as st
import pandas as pd
from google_sheets_helper import read_points, write_points
from points_config import gsheetname, mentors_list, category_list, core_list, non_core_list, points_d
from points_calculator import calculate_points
from datetime import datetime


@st.cache_data(ttl=600)
def read_cached_points(gsheetname, refresh_time):
    return read_points(gsheetname)

st.title('Submit Points')
core_list = points_d['Core'].keys()
non_core_list = points_d['Non-Core'].keys()


if st.session_state.get('last_refresh_time') is None:
    st.session_state['last_refresh_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

data = read_cached_points(gsheetname, st.session_state['last_refresh_time'])
df = pd.DataFrame(data)


# with st.form("add_user_form"):
mentor = st.selectbox("Name:", mentors_list)
category = st.radio("Category:", points_d.keys())
subcat_keys = [k for k in points_d[category].keys() if k != 'Max']
sub_category = st.radio("Sub-Category:", subcat_keys)
activity = st.radio("Activity:", points_d[category][sub_category]['Activity'].keys())
notes = st.text_input("Notes (e.g. date, contribution):",
                placeholder='E.g. On 5th Oct, I was the timer.')

activity_points = points_d[category][sub_category]['Activity'][activity]['Points']

awarded_points = calculate_points(points_d, df, mentor, category, sub_category, activity,activity_points)
st.write(f"Awarded Points (capped): {awarded_points}")

if st.button("Submit"):
    if mentor and category and sub_category and activity and notes:
        data = {
            'Datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'Mentor': mentor,
            'Category': category,
            'Sub-Category': sub_category,
            'Activity': activity,
            'Notes': notes,
            'Points': awarded_points
        }
        write_points(gsheetname, [data])
        st.session_state['last_refresh_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.balloons()
        st.success(f"You have been awarded {awarded_points} points for this activity.")
    else:
        st.error("Please fill in all fields before submitting.")
