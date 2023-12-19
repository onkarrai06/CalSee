import streamlit as st
import cv2
from predict import predict
import numpy as np

def main():
    st.markdown("# <span style='color:red;'><u>Calorie Estimator</u></span>", unsafe_allow_html=True)

    # Upload pictures
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Upload A Top View Of The Food")
        picture1 = st.file_uploader("Choose a top view", type=["jpg", "jpeg", "png"])

    with col2:
        st.subheader("Upload A Side View Of The Food")
        picture2 = st.file_uploader("Choose a side view", type=["jpg", "jpeg", "png"])

    # Display uploaded pictures side by side
    if picture1 is not None and picture2 is not None:
        col1.image(picture1, caption="Top View", use_column_width=True)
        col2.image(picture2, caption="Side View", use_column_width=True)

        # Continue button
        if st.button("Continue"):
            process_pictures(picture1, picture2)


def process_pictures(top, side):
    if top and side:
        st.write("Processing  Pictures...")
        results, top_img, side_img = predict(top, side)
        show_result(results, top_img, side_img)


def show_result(results, top_img, side_img):
    total_calories = 0
    
    st.title("Food and Calories")
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(top_img, caption="Top View", use_column_width=True)
    with col2:
        st.image(side_img, caption="Side View", use_column_width=True)

    for item in results:
        st.markdown(f"#### {item[0].capitalize()} with Calories {item[1].round(2)}")
        total_calories += item[1]
    
    if total_calories != 0:
        total_calories = total_calories.round(2)

    st.markdown("## <span style='color:red;'><u>Total Calories: " + str(total_calories) + "</u></span>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
