import streamlit as st
from backend.DB import DB
import webbrowser

# Function to open Google Maps with a specific latitude and longitude
def open_google_maps(latitude, longitude):
    url = f"https://www.google.com/maps?q={latitude},{longitude}"
    webbrowser.open_new_tab(url)

# Main function to display plastic detection details
def details():
    # Retrieve the list of images from the database
    images = DB.images

    # Initialize the 'show_image' session state if it doesn't exist
    if 'show_image' not in st.session_state:
        st.session_state.show_image = {}

    # Check if there are any images in the database
    if len(images) == 0:
        st.info("Upload some images in the Detect Page!!!")
    else:
        # Display the header for the plastic detection overview
        st.header(":blue[Plastic Detection Overview]")
        cnt = 1

        # Loop through each image in the database and display its details
        for image in images:
            # Display a subheader with the image number
            st.subheader(f"Image {str(cnt)}:")
            cnt += 1

            # Retrieve the index of the image and its original image data
            i = image[0]
            original_image = image[1].copy().resize((489, 489))

            # Display the annotated image
            st.image(original_image, caption="Annotated Image")

            # Display the number of plastics detected for the current image
            st.markdown(f"***Number of Plastics Detected: {DB.cnt[i]}***")

            # Create a button to open Google Maps with the latitude and longitude of the detected plastics
            if st.button("Open in Google Maps", key=f"open_maps_{i}"):
                open_google_maps(DB.lat[i], DB.lon[i])