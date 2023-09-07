import streamlit as st
def model_transparency():

    # Home page title
    st.markdown(
        """
        <div style="background-color: rgba(0,0,0,0.6); padding: 20px;">
            <h1 style="font-size: 50px;color: #1fddff;"> <b> Model Transparency: Understanding How We Detect Plastic Pollution </b> </h1>
        <div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background-color: rgba(0,0,0,0.6); padding: 20px;">
            <p style="font-size: 20px;">At PlasticMapper, we care deeply about transparency. We want you to understand how our technology works to detect plastic pollution and how we strive to protect our environment. Here's a simple overview of how our system identifies plastic waste using machine learning.</p>
        <div>
        """,
        unsafe_allow_html=True
    )

    # Introduction section
    st.markdown(
        """
        <div style="background-color: rgba(0,0,0,0.6); padding: 20px; color: #6fe36d;">
            <h2 style="font-size: 30px; color: #bbeff2;">YOLOv5 - Our Detective:</h2>
        <div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background-color: rgba(0,0,0,0.6); padding: 20px;">
            <p style="font-size: 20px;">Imagine YOLOv5 as our detective. YOLO stands for "You Only Look Once," version 5. It's a smart tool that can recognize objects, like plastic waste, in images from drones. YOLOv5 helps us quickly spot plastics across different areas and keep our planet clean.</p>
        <div>
        """,
        unsafe_allow_html=True
    )

    # What is PlasticMapper section
    st.markdown(
        """
        <div style="background-color: rgba(0,0,0,0.6); padding: 20px; color: #6fe36d;">
            <h2 style="font-size: 30px; color: #bbeff2;"> Training with Annotated Images:</h2>
        <div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background-color: rgba(0,0,0,0.6); padding: 20px;">
            <p style="font-size: 20px;">
Before YOLOv5 can detect plastics, we teach it with annotated images. These images show where plastic items are in the pictures. This way, YOLOv5 learns to recognize plastics and helps us build a powerful tool for identifying them.</p>
        <div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style="background-color: rgba(0,0,0,0.6); padding: 20px; color: #6fe36d;">
            <h2 style="font-size: 30px; color: #bbeff2;"> Detecting Plastics with Confidence:</h2>
        <div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background-color: rgba(0,0,0,0.6); padding: 20px;">
            <p style="font-size: 20px;">
When YOLOv5 spots plastics in the drone images, it also gives us a "confidence score." This score tells us how sure YOLOv5 is about its findings. The higher the score, the more confident we are that plastics are there.
</p>
        <div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style="background-color: rgba(0,0,0,0.6); padding: 20px; color: #6fe36d;">
            <h2 style="font-size: 30px; color: #bbeff2;"> Balancing Precision and Recall:</h2>
        <div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background-color: rgba(0,0,0,0.6); padding: 20px;">
            <p style="font-size: 20px;">
To ensure accurate detections, we set a "confidence threshold." This threshold helps us balance between being very precise (few mistakes) and having good coverage (finding most plastics). Our goal is to catch as many plastics as possible while avoiding false alarms.
</p>
        <div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style="background-color: rgba(0,0,0,0.6); padding: 20px; color: #6fe36d;">
            <h2 style="font-size: 30px; color: #bbeff2;"> Understanding Limitations:</h2>
        <div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background-color: rgba(0,0,0,0.6); padding: 20px;">
            <p style="font-size: 20px;">
Like any detective, YOLOv5 has some limitations. It may struggle with certain plastics or challenging situations. We continuously work to improve its abilities and make it even better at spotting plastics.
</p>
        <div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style="background-color: rgba(0,0,0,0.6); padding: 20px; color: #6fe36d;">
            <h2 style="font-size: 30px; color: #bbeff2;"> Your Impact Matters:</h2>
        <div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background-color: rgba(0,0,0,0.6); padding: 20px;">
            <p style="font-size: 20px;">
By using PlasticMapper, you become part of our mission to protect the environment. Your contributions, along with YOLOv5's powerful detection, help us fight plastic pollution together.
</p>
        <div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background-color: rgba(0,0,0,0.6); padding: 20px;">
            <h1 style="font-size: 40px;color: #1fddff;"> Thank you for joining us in the battle against plastic pollution! </h1>
        <div>
        """,
        unsafe_allow_html=True
    )