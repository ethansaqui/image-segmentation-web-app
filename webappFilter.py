import streamlit as st
import numpy as np
import pandas as pd

image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if(image is not None):
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = "Test"
    st.write("%s (%.2f%%)" % (label, 100))