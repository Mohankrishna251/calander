## Additional Features

- **Interactive UI**: The application provides an interactive user interface where users can easily select the year and month.
- **Customizable Display**: Users can choose between displaying a full year calendar or a single month calendar.
- **Responsive Design**: The calendar layout is designed to be responsive and visually appealing, ensuring a great user experience on different devices.

## Code Breakdown

- **Leap Year Calculation**: The `is_leap_year(year)` function determines if a given year is a leap year, which is essential for accurately calculating the number of days in February.
- **Days in Month Calculation**: The `get_days_in_month(month, year)` function returns the number of days in a given month and year, taking into account leap years.
- **Day of the Week Calculation**: The `get_day_of_week(year, month, day)` function calculates the day of the week for a given date using Zeller's Congruence algorithm.
- **Month Calendar Generation**: The `generate_month_calendar(month, year)` function generates the calendar data for a given month and year, including the header, days of the week, and the calendar grid.
- **Streamlit Application Setup**: The `main()` function sets up the Streamlit application, including the page configuration, title, year selection slider, display mode radio buttons, and the calendar display logic.

## How It Works

1. **Year Selection**: Users can select the year using a slider, which allows for easy navigation between different years.
2. **Display Mode**: Users can choose between displaying a full year calendar or a single month calendar using radio buttons.
3. **Month Selection**: If the single month display mode is selected, users can choose the month from a dropdown menu.
4. **Calendar Display**: The application generates and displays the calendar based on the selected year and month, using a responsive and visually appealing layout.

## Customization

- **CSS Styling**: The calendar table is styled using custom CSS to ensure a clean and professional look.
- **Layout Configuration**: The Streamlit layout is configured to be wide, providing ample space for the calendar display.

