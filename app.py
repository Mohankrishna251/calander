import streamlit as st
import calendar
from datetime import datetime

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(month, year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return days_in_month[month - 1]

def get_day_of_week(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    day_of_week = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
    return (day_of_week + 6) % 7

def generate_month_calendar(month, year):
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    calendar_data = []
    header = f"{month_names[month - 1]} {year}"
    days_header = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
    
    days_in_month = get_days_in_month(month, year)
    start_day = get_day_of_week(year, month, 1)
    
    # Create calendar grid
    current_week = [""] * start_day
    day = 1
    
    while day <= days_in_month:
        while len(current_week) < 7 and day <= days_in_month:
            current_week.append(str(day))
            day += 1
        
        # Pad the last week with empty strings if needed
        while len(current_week) < 7:
            current_week.append("")
            
        calendar_data.append(current_week)
        current_week = []
    
    return header, days_header, calendar_data

def main():
    st.set_page_config(page_title="Calendar Viewer", layout="wide")
    
    st.title("📅 Calendar Viewer")
    
    # Year selection
    current_year = datetime.now().year
    year = st.slider("Select Year", min_value=1900, max_value=2100, value=current_year)
    
    # Display option
    display_option = st.radio(
        "Display Mode",
        ["Full Year", "Single Month"],
        horizontal=True
    )
    
    if display_option == "Single Month":
        month = st.selectbox(
            "Select Month",
            range(1, 13),
            format_func=lambda x: calendar.month_name[x]
        )
        
        header, days_header, calendar_data = generate_month_calendar(month, year)
        
        # Create a single month display
        st.subheader(header, anchor=False)
        
        # Create calendar grid
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            # Create the calendar table with CSS
            table_html = f"""
            <style>
                .calendar-table {{
                    width: 100%;
                    border-collapse: collapse;
                    text-align: center;
                }}
                .calendar-table th {{
                    background-color: #f0f2f6;
                    padding: 10px;
                    border: 1px solid #ddd;
                }}
                .calendar-table td {{
                    padding: 10px;
                    border: 1px solid #ddd;
                }}
                .calendar-table td:empty {{
                    background-color: #f9f9f9;
                }}
            </style>
            <table class="calendar-table">
                <tr>
            """
            
            # Add days header
            for day in days_header:
                table_html += f"<th>{day}</th>"
            table_html += "</tr>"
            
            # Add calendar data
            for week in calendar_data:
                table_html += "<tr>"
                for day in week:
                    table_html += f"<td>{day}</td>"
                table_html += "</tr>"
            
            table_html += "</table>"
            st.markdown(table_html, unsafe_allow_html=True)
    
    else:
        # Display full year
        st.subheader(f"Calendar for {year}", anchor=False)
        
        # Create 4 rows of 3 months each
        for quarter in range(4):
            cols = st.columns(3)
            for i in range(3):
                month = quarter * 3 + i + 1
                header, days_header, calendar_data = generate_month_calendar(month, year)
                
                with cols[i]:
                    st.markdown(f"#### {header}")
                    
                    # Create the calendar table with CSS
                    table_html = f"""
                    <style>
                        .calendar-table {{
                            width: 100%;
                            border-collapse: collapse;
                            text-align: center;
                            font-size: 0.8em;
                        }}
                        .calendar-table th {{
                            background-color: #f0f2f6;
                            padding: 5px;
                            border: 1px solid #ddd;
                        }}
                        .calendar-table td {{
                            padding: 5px;
                            border: 1px solid #ddd;
                        }}
                        .calendar-table td:empty {{
                            background-color: #f9f9f9;
                        }}
                    </style>
                    <table class="calendar-table">
                        <tr>
                    """
                    
                    # Add days header
                    for day in days_header:
                        table_html += f"<th>{day}</th>"
                    table_html += "</tr>"
                    
                    # Add calendar data
                    for week in calendar_data:
                        table_html += "<tr>"
                        for day in week:
                            table_html += f"<td>{day}</td>"
                        table_html += "</tr>"
                    
                    table_html += "</table>"
                    st.markdown(table_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
