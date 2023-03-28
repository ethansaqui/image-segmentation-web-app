import filter
import streamlit as st


image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if image is not None:
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    if(st.button('Image Segmentation')):
        newImage = filter.image_segmentation(image)
    
        if(newImage is not None):
            st.image(newImage, caption='Segmented Image.', use_column_width=True)
    
