from PIL import Image, ImageDraw

def process_image(img_path, draw_boxes=False, result_df=None):
    """
    Process the image by resizing it and optionally drawing bounding boxes based on the result dataframe.

    Args:
        img_path (str): Path to the image file.
        draw_boxes (bool): Whether to draw bounding boxes on the image. Default is False.
        result_df (pandas.DataFrame): DataFrame containing the results of object detection. Default is None.

    Returns:
        PIL.Image.Image: Processed image.

    """
    # Open the image file
    img = Image.open(img_path)

    # Resize the image to a fixed size of 640x640 pixels
    img = img.resize((640, 640))

    # Check if bounding boxes need to be drawn and if result dataframe is provided
    if draw_boxes and result_df is not None:
        # Create a drawing object
        draw = ImageDraw.Draw(img)

        # Iterate over each row in the result dataframe
        for _, row in result_df.iterrows():
            # Extract the coordinates of the bounding box
            xmin, ymin, xmax, ymax = row["xmin"], row["ymin"], row["xmax"], row["ymax"]

            # Extract the confidence score and name of the object
            confidence_score, name = row["confidence"], row["name"]

            # Draw the bounding box rectangle on the image
            draw.rectangle([(xmin, ymin), (xmax, ymax)], outline="red", width=3)

            # Create the text to display (object name and confidence score)
            text = f"{name}"

            # Specify the position to display the text (just above the bounding box)
            text_position = (xmin, ymin - 15)

            # Draw the text on the image
            draw.text(text_position, text, fill="cyan")

    # Return the processed image
    return img