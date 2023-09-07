import base64
import streamlit as st
import plotly.express as px

# Function to apply custom styles to the Streamlit app based on a given parameter 'sub'
def styles(sub):
    # Define image paths and opacity values
    img_path = "assets/homeimg.jpg"    # Default image path for the background
    po = "1"                          # Default opacity for the main background
    so = "0.6"                        # Default opacity for the sidebar background

    # If 'sub' is True, update the image path and opacity values
    if not sub:
        img_path = "assets/subimg.jpg"    # Custom image path for the background
        po = "1"                         # Custom opacity for the main background (no change)
        so = "0.6"                       # Custom opacity for the sidebar background

    # Load example data (this seems to be unused in this specific code snippet)
    df = px.data.iris()

    # Function to convert an image file to a base64 encoded string
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    # Get the base64 encoded strings for the images
    home_img = get_img_as_base64(img_path)  # Main background image
    img = get_img_as_base64(img_path)       # Sidebar background image

    # Define CSS style to apply custom backgrounds and opacity
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{home_img}");
    background-size: 100%;
    background-position: top left;
    background-repeat: repeat;
    background-attachment: fixed;
    opacity : {po};
    }}

    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100%;
    background-position: top left;
    background-repeat: repeat;
    background-attachment: fixed;
    opacity : {so};
    }}

    [data-testid="stVerticalBlock"] > .main {{
        filter : blur(0px)
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
    right: 2rem;
    }}

    </style>
    """

    # Apply the custom CSS styles to the Streamlit app
    st.markdown(page_bg_img, unsafe_allow_html=True)