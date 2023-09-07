import streamlit as st
import pandas as pd
from backend.DB import DB
import plotly.graph_objects as go

# Function to display insights and visualizations based on detected plastics
def insights():
    # Retrieve data from the database (assuming the DB class provides these attributes)
    sz = DB.sz         # List of number of plastics detected in each image
    lat = DB.lat       # List of latitude coordinates for each image
    lon = DB.lon       # List of longitude coordinates for each image
    con = DB.con       # List of confidence scores for plastic detection in each image
    clr = DB.clr       # List of colors for each image (may represent different categories)

    # Check if there are any images with detected plastics
    if len(sz) > 0:
        # Create a DataFrame to store the data
        df = pd.DataFrame({"sz": sz, "latitude": lat, "longitude": lon, "confidence": con, "clr": clr})

        # Calculate the total number of plastics detected
        total_plastics = df["sz"].sum()

        # Calculate the average plastic density (plastics per image)
        average_density = total_plastics / len(df)

        # Calculate the distribution of plastics based on the number of plastics detected in each image
        plastic_count_distribution = df["sz"].value_counts().sort_index()

        # Calculate the percentage of images with no plastics detected
        no_plastic_images = len(df[df["sz"] == 0])
        percentage_no_plastic = (no_plastic_images / len(df)) * 100

        # Display insights
        st.header(":blue[Insights:]")
        s1 = f"**Total number of plastics detected:** {total_plastics}"
        s2 = f"**Average plastic density (plastics per image):** {average_density:.2f}"
        s3 = f"**Percentage of images with no plastics detected:** {percentage_no_plastic:.2f}%"
        s4 = f"**Total number of images given:** {len(lat)}"
        st.markdown(s4)
        st.markdown(s1)
        st.markdown(s2)
        st.markdown(s3)

        # Display plastic count distribution as a bar chart
        st.header(":blue[Plastic Count Distribution:]")
        st.markdown("**Visualize the distribution of plastics based on the number of plastics detected in each image.**")
        st.bar_chart(plastic_count_distribution)

        # Display the geographical distribution of plastic hotspots on an interactive map
        st.header(":blue[Plastic Distribution on Map:]")
        st.markdown("**See the geographical distribution of plastic hotspots on an interactive map.**")
        st.map(df, size=5, color="clr", zoom=17)

        # Display the distribution of plastic detection confidence scores as a pie chart
        st.header(":blue[Confidence Score Distribution:]")
        st.markdown("**Observe the distribution of plastic detection confidence scores.**")
        confidence_scores = []

        # Prepare the data for the pie chart

        bins = [0.0, 0.3, 0.6, 1.0]
        labels = ["0.00-0.30", "0.31-0.60", "0.61-1.00"]
        for l in df["confidence"]:
            for j in l:
                confidence_scores.append(j)

        # Count the number of confidence scores in each bin
        counts = pd.cut(confidence_scores, bins=bins, labels=labels, include_lowest=True, right=False).value_counts().sort_index().values
        # Create and customize the Pie chart using Plotly
        fig = go.Figure(data=[go.Pie(labels=labels, values=counts, textinfo='percent+label', hole=0.3)])
        fig.update_layout(autosize=True, width=700, height=700) #
        st.plotly_chart(fig)

    else:
        # Inform the user if no images with plastics were uploaded
        st.info("Upload some images in the Detect Page!!!")