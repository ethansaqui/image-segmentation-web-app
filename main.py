import filter
import streamlit as st

st.set_page_config(layout="wide")

image_upload = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
btn_slot = st.empty()   # Create empty slot for conditional button

# Display original image and segmented image only after source image upload
if image_upload:
    col_left, col_right = st.columns(2)

    image = None
    show_segmented = False

    with col_left:
        st.subheader("Original image")

        if image_upload is not None:
            image = image_upload

            st.image(image_upload, use_column_width=True)

            if btn_slot.button('Apply Image Segmentation'):
                show_segmented = True
                
        
    with col_right:
        st.subheader("Segmented Image")

        if show_segmented:
            new_image = filter.image_segmentation(image)
            
            if new_image is not None:
                st.image(new_image, use_column_width=True)