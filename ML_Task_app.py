import streamlit as st
import pickle
import numpy as np
import cv2
from skimage.color import rgb2gray
from skimage.io import imread
from scipy.fftpack import fft

st.title("Generate DON concentration")
uploaded_img= st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])


if uploaded_img is not None:
    image = imread(uploaded_img)
    st.image(image=image,use_column_width=True)

    gray_image = rgb2gray(image)       #convert the image into grayscale

    image_vector = gray_image.flatten()
    spectral_features = np.abs(image_vector)[:448]        # used to convert spaatial into spectral component

    def load_data():
        with open("model.pkl","rb") as file1:
            data = pickle.load(file1)
            return data
    
    data_pickle = load_data()
    model = data_pickle["model"]
    pca = data_pickle["pca"]
    scaler = data_pickle["scaler"]
    

    scaled_data = scaler.transform([spectral_features])


    pca_features = pca.transform(scaled_data)


    # Predict using the model
    prediction = model.predict(pca_features)

    st.write("the predcted DON concetration",prediction)

    

