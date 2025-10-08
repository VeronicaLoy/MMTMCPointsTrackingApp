

def calculate_points(points_d, df, mentor, category, sub_category, activity, activity_points):
    """

    """

    mentor_df = df[df['Mentor'] == mentor]

    # get mentor's current points in the category, sub-category, and activity
    mentor_cat_point = mentor_df.groupby('Category')['Points'].sum().to_dict().get(category, 0)
    mentor_subcat_point = mentor_df.groupby('Sub-Category')['Points'].sum().to_dict().get(sub_category,0)
    mentor_activity_point = mentor_df.groupby(['Activity'])['Points'].sum().to_dict().get(activity,0)


    # get max points allowed in the category, sub-category, and activity
    max_cat_points = points_d[category]['Max']
    max_subcat_points = points_d[category][sub_category]['Max']
    max_activity_points = points_d[category][sub_category]['Activity'][activity]['Max']

    # calculate remaining points in each level
    cat_points_delta = max_cat_points - mentor_cat_point
    subcat_points_delta = max_subcat_points - mentor_subcat_point
    activity_points_delta = max_activity_points - mentor_activity_point

    # calculate awarded points
    # st.write(cat_points_delta, subcat_points_delta, activity_points_delta, activity_points)
    awarded_points = min(cat_points_delta, subcat_points_delta, activity_points_delta, activity_points)

    return awarded_points
