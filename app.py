import streamlit as st
import cv2
import numpy as np
from detector import detect_objects
from describer import SceneDescriber

describer = SceneDescriber()

st.set_page_config(page_title="Smart Scene Understanding", layout="wide")

st.title("Smart Scene Understanding System")
st.markdown("Object detection, scene understanding, and risk analysis")

mode = st.radio("Choose Mode", ["📷 Webcam", "🖼️ Upload Image"])

# Upload Image
if mode == "🖼️ Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes, 1)

        objects = detect_objects(frame)
        description, risk, level = describer.analyze_scene(objects)

        st.image(frame, channels="BGR")

        st.markdown(f"**Objects:** {objects}")
        st.markdown(f"**Description:** {description}")
        st.markdown(f"**Risk:** {risk}")

        if level == "HIGH":
            st.error("⚠️ HIGH RISK")
        elif level == "MEDIUM":
            st.warning("⚠️ MEDIUM RISK")
        else:
            st.success("SAFE")

# Webcam
elif mode == "📷 Webcam":
    run = st.checkbox("Start Webcam")

    FRAME_WINDOW = st.image([])

    if run:
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if not ret:
                st.error("Camera not working")
                break

            objects = detect_objects(frame)
            description, risk, level = describer.analyze_scene(objects)

            FRAME_WINDOW.image(frame, channels="BGR")

            st.markdown(f"**Objects:** {objects}")
            st.markdown(f"**Description:** {description}")
            st.markdown(f"**Risk:** {risk}")

            if level == "HIGH":
                st.error("⚠️ HIGH RISK")
            elif level == "MEDIUM":
                st.warning("⚠️ MEDIUM RISK")
            else:
                st.success("SAFE")

        cap.release()
