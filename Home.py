import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.markdown("### 🐣 English Learning Applications (Spring 2025)")
st.markdown('This platform provides coding-based, customized apps that assist in learning English. More apps will be updated continuously. Welcome aboard.')

# URL of the raw audio file on GitHub
audio_url = 'https://github.com/MK316/Engpro-Class/raw/main/audio/confidence.wav'

# Display the audio player in Streamlit
st.audio(audio_url, format='audio/mp3', start_time=0)

# Add an image from GitHub
image_url = "https://github.com/MK316/Engpro-Class/raw/main/data/engpro-cover.png"

# Load and resize the image
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
img = img.resize((500, 500))  # Set custom width and height

st.image(img, caption="©️ MK316 English Pronunciation Practice: Practice Makes Perfect")

st.markdown("⛺Goto [MK316 home](https://mk316.github.io)")
