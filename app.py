import streamlit as st
from streamlit_option_menu import option_menu

from frontend.detect import detect
from frontend.details import details
from frontend.insights import insights
from frontend.styles import styles
from frontend.home import home
from frontend.model_transparency import  model_transparency

# Initialize the selected option to "HOME"
selected = "HOME"

# Create a sidebar using Streamlit to display navigation options
with st.sidebar:
    # Use the custom option_menu function to display a menu with icons
    selected = option_menu(
        menu_title=None,
        options=["HOME", "DETECT", "DETAILS", "INSIGHTS", "MODEL TRANSPARENCY"],  # List of navigation options
        icons=["house-fill", "cloud-arrow-up-fill", "box-fill", "bar-chart-fill","bezier"],  # Icons corresponding to each option
        menu_icon="cast",  # Icon for the menu title
        default_index=0,  # Default selected index (0 is "HOME" in this case)
        styles={
            # Custom styling for the sidebar container
            "container": {
                "background-color": "#012121",  # Background color of the sidebar
                "filter": "blur(0px)"  # Apply a blur effect to the sidebar (0px means no blur)
            },
            # Custom styling for the selected navigation option
            "nav-link-selected": {
                "background-color": " #1fddff",  # Background color of the selected option
            },
        }
    )

# Based on the selected option, display the corresponding content
if selected == "HOME":
    styles(True)  # Apply custom styles for the HOME page
    home()  # Display the content of the HOME page
else:
    styles(False)  # Apply custom styles for other frontend

    if selected == "DETECT":
        detect()  # Display the content of the DETECT page

    if selected == "DETAILS":
        try:
            details()  # Display the content of the DETAILS page
        except:
            st.error("Something went wrong ☹️")

    if selected == "INSIGHTS":
        try:
            insights()  # Display the content of the INSIGHTS page
        except:
            st.error("Something went wrong ☹️")

    if selected == "MODEL TRANSPARENCY":
        model_transparency()