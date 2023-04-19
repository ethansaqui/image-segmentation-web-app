import filter
import streamlit as st
import base64




st.title("Image Segmentation App")

image_upload = st.file_uploader("Upload an image to perform image segmentation on!", type=["png", "jpg", "jpeg"])
btn_slot = st.empty()   # Create empty slot for conditional button

with st.sidebar:
    st.title("How to Use")
    st.text("1. Upload an image.")
    st.text("2. Click the 'Apply Image Segmentation' button.")
    st.text("3. Enjoy your segmented image!")
    file_ = open("instructions.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif" style=width:430px>',
        unsafe_allow_html=True,
    )


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
                
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by Cruz, Fernandez, Posadas, Saquilayan </p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)