import streamlit as st

def calculate_points(points_d, df, mentor, category, sub_category, activity, meeting_date, activity_points):
    """

    """

    mentor_df = df[df['Mentor'] == mentor]

    # get mentor's cumulative / current points in the category, sub-category, and activity
    meeting_point = mentor_df.groupby('Meeting Date')['Points'].sum().to_dict().get(meeting_date,0)
    mentor_cat_point = mentor_df.groupby('Category')['Points'].sum().to_dict().get(category, 0)
    mentor_subcat_point = mentor_df.groupby('Sub-Category')['Points'].sum().to_dict().get(sub_category,0)
    mentor_activity_point = mentor_df.groupby(['Activity'])['Points'].sum().to_dict().get(activity,0)

    # get max points allowed in the category, sub-category, and activity
    if meeting_date:
        max_meeting_points = 3
    else:
        max_meeting_points = 100 # arbitrarily high if no meeting date
    max_cat_points = points_d[category]['Max']
    max_subcat_points = points_d[category][sub_category]['Max']
    max_activity_points = points_d[category][sub_category]['Activity'][activity]['Max']

    # calculate remaining points in each level
    meeting_points_delta = max_meeting_points - meeting_point
    cat_points_delta = max_cat_points - mentor_cat_point
    subcat_points_delta = max_subcat_points - mentor_subcat_point
    activity_points_delta = max_activity_points - mentor_activity_point

    # calculate awarded points
    awarded_points = min(meeting_points_delta, cat_points_delta, subcat_points_delta, activity_points_delta, activity_points)

    return awarded_points
