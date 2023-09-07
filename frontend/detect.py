import torch
import streamlit as st
import pandas as pd
from backend.location import get_location
from backend.image_processing import process_image
import folium
from folium.plugins import HeatMap
import streamlit.components.v1 as components
from backend.DB import DB
from PIL import Image
from backend.location import get_city_from_coordinates
import  altair as alt

lat = DB.lat  # latitude
lon = DB.lon  # longitude
sz = DB.sz  # size
clr = DB.clr  # color
con = DB.con  # confidence score
images = DB.images  # annotated images
raw_images = DB.raw_images  # raw images
cnt = DB.cnt  # count of plastics
city_cnt = DB.city_cnt  # count of city plastic count


def clear():
    # Function to clear all the elements in the list
    lat.clear()
    lon.clear()
    sz.clear()
    clr.clear()
    con.clear()
    images.clear()
    raw_images.clear()
    cnt.clear()
    city_cnt.clear()

def detect():
    st.header(":blue[Uncover Plastic Waste Hotspots with Interactive Mapping]")

    # Get the image files from the user
    uploaded_files = st.file_uploader("select a sample asset or upload an image", type=["jpg", "jpeg", "png"],
                                      accept_multiple_files=True)

    ok = 0
    if len(uploaded_files) > 0:
        ind = 0
        clear()
        success_placeholder = st.empty()
        success_placeholder.success("Images uploaded Successfully!")
        if st.button(label="Generate"):
            success_placeholder.empty()
            ok = 1
            with st.spinner("Processing images..."):

                warning_placeholder = st.empty()
                warning_placeholder.warning("Don't switch pages while processing images!")

                model = torch.hub.load("backend/yolov5l6_model", "custom", path="model.onnx", source="local")

                for uploaded_file in uploaded_files:
                    # Process the uploaded image
                    img = process_image(uploaded_file)

                    # Perform inference
                    results = model(img, size=640)

                    # Convert the results into dataframe format
                    df = results.pandas().xyxy[0]

                    # Filter the results based on the "plastic" class and confidence threshold
                    threshold = 0.3
                    res = df[(df["name"] == "plastic") & (df["confidence"] >= threshold)]

                    # Process the image and draw bounding boxes
                    img_with_boxes = process_image(uploaded_file, draw_boxes=True, result_df=res)

                    count = res.shape[0]
                    det = get_location(uploaded_file)

                    if det[0] != 0 or det[1] != 0:
                        lat.append(det[0])
                        lon.append(det[1])
                        con.append(res["confidence"])
                        sz.append(count)
                        cnt.append(count)
                        raw_images.append(Image.open(uploaded_file))
                        images.append([ind, img_with_boxes])

                        city = get_city_from_coordinates(det[0], det[1])

                        if city not in city_cnt:
                            city_cnt[city] = 0
                        city_cnt[city] += count

                        if (count > 5):
                            clr.append("#ff0000")

                        elif (count > 2):
                            clr.append("#ffff00")

                        else:
                            clr.append("#00ff00")

                        ind += 1
            warning_placeholder.empty()

    if (len(lat) > 0):
        try:
            df = pd.DataFrame()
            df["latitude"] = lat
            df["longitude"] = lon
            df["sz"] = sz
            df["clr"] = clr

            tot = df["sz"].sum()
            st.subheader("Total number of plastics detected: " + str(tot))

            # You can also display additional insights and visualizations based on your requirements.
            # Create a Folium map centered on a specific location (e.g., the average latitude and longitude of detections)
            map_center = [df["latitude"].mean(), df["longitude"].mean()]
            m = folium.Map(location=map_center, zoom_start=17)

            # Create a HeatMap layer using the geographical data (latitude, longitude) and the density of plastics (sz)
            heat_data = [[row["latitude"], row["longitude"], row["sz"]] for index, row in df.iterrows()]
            HeatMap(heat_data, radius=15, max_zoom=10).add_to(m)

            # Get the HTML code for the Folium map
            html_map = m.get_root().render()

            # Use the IFrame function to display the Folium map within Streamlit
            components.html(html_map, height=500)

            df = pd.DataFrame.from_dict(city_cnt, orient="index", columns=["Plastic_Count"])
            df.reset_index(inplace=True)
            df.rename(columns={'index': 'City'}, inplace=True)

            # Create the Altair chart
            bars = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X("Plastic_Count:Q", axis=alt.Axis(title="Plastic Count")),
                    y=alt.Y("City:N", axis=alt.Axis(title="City")),
                    size=alt.Size("Plastic_Count:Q", scale=alt.Scale(range=[20, 30])),
                    color=alt.Color("Plastic_Count:Q", scale=alt.Scale(scheme='viridis'),
                                    legend=alt.Legend(title="Plastic Count"))
                )
                .properties(width=600,height=200)
            )

            # Display the chart in Streamlit
            st.subheader("Plastic Counts by cities")
            st.altair_chart(bars, use_container_width=True)
        except:
            st.error("Something went wrong ☹️")

        if st.button(label="Clear"):
            clear()
            st.experimental_rerun()

    elif ok:
        st.error("Uploaded images doesn't contain metadata!")