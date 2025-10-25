
gsheetname = 'Streamlit'

mentors_list = ['',
'Jei Sim',
'Dreamy',
'Jeffery',
'Raymond',
'Sophia',
'Arva',
'Barry',
'Boon Han',
'Chandran',
'Kelvin',
'Michell',
'Prakash',
'Qing Lin',
'Renee',
'Pei Shan',
'Thomas',
'Cheng',
'Darrell',
'Hui Ying',
'Janty',
'Mike',
'Raymond',
'Rebecca',
'Rika',
'Yuan Bin']

category_list = ['Core', 'Non-Core']
core_list = ['Mentoring','Speech','Roles']
non_core_list = ['Retreat Marketing','Meeting Attendance','Misc']

mentoring_d = {
    "Take on a mentee": {"Points": 2, "Max": 4},
    "Present for mentee's ice-breaker": {"Points": 1, "Max": 2},
    "Present with mentee at meeting": {"Points": 1, "Max": 3},
    "Present for mentee's 3 speeches": {"Points": 1, "Max": 2},
    "Present with mentee taking a new role": {"Points": 1, "Max": 3},
}
speech_d ={
    "Deliver a Speech": {"Points": 1, "Max": 3},
    "Attempt a Table Topic": {"Points": 1, "Max": 2, "Category": "Speech"},
    "Evaluator Role": {"Points": 1, "Max": 3, "Category": "Speech"},
    "Table Topics Master": {"Points": 1, "Max": 2, "Category": "Speech"},
    "Conduct a workshop (> 30 mins)": {"Points": 3, "Max": 6, "Category": "Speech"},
    "Join Speech Contest": {"Points": 1, "Max": 2, "Category": "Speech"},
    "Toastmaster of the Evening": {"Points": 1, "Max": 2, "Category": "Speech"} }

roles_d = {
    "SAA": {"Points": 1, "Max": 1},
    "Timer": {"Points": 1, "Max": 1},
    "Photographer": {"Points": 1, "Max": 1},
    "Videographer": {"Points": 1, "Max": 1},
    "OPC Feedback": {"Points": 1, "Max": 1},
}
attendance_d = {
    "Contest Supporter": {"Points": 1, "Max": 3},
    "AGM": {"Points": 1, "Max": 1},
    "Organize OPC": {"Points": 1, "Max": 2},
    "Invite non-TM guests to meeting": {"Points": 1, "Max": 3},
    "Club Anniversary": {"Points": 1, "Max": 1},
    "Convert Guest to Member": {"Points": 1, "Max": 3},
}

misc_d = {
    "Share personal video of retreat": {"Points": 3, "Max": 3},
    "Contest-Chair / Contest Toastmaster": {"Points": 2, "Max": 2},
    "Organize Social Activity (Min 12 pax)": {"Points": 2, "Max": 4},
    "Social Media Posts about Mentoring": {"Points": 1, "Max": 2},
}

marketing_d = {
    "Media": {"Points": 3, "Max": 3},
    "IT": {"Points": 3, "Max": 3},
    "Logistics and Itinerary": {"Points": 3, "Max": 3},
    "Blog articles / Media posts": {"Points": 1, "Max": 3},
}


core_d = {'Core':
            {'Mentoring': {
                'Activity': mentoring_d,
                'Max':8},
            'Speech': {
                'Activity': speech_d,
                'Max':6},
            'Roles':{
                'Activity': roles_d,
                'Max':4
                    },
            'Max':12
            }}

non_core_d = {
        'Non-Core':
            {'Retreat Marketing': {
                'Activity': marketing_d,
                'Max':9},
            'Meeting Attendance': {
                'Activity': attendance_d,
                'Max':3},
            'Misc': {
                'Activity': misc_d,
                'Max':5},
            'Max':9
            }}
points_d = {**core_d, **non_core_d}

