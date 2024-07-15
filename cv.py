import streamlit as st
import cv2

st.title("OpenCV Test")

# Test if OpenCV can be imported and used
def test_opencv():
    img = cv2.imread('a.png')  # Provide a valid image path
    if img is not None:
        st.success("OpenCV imported and image read successfully!")
    else:
        st.error("Failed to read image using OpenCV.")

if st.button("Test OpenCV"):
    test_opencv()
