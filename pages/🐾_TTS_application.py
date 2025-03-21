import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import qrcode
from PIL import Image
from wordcloud import WordCloud
import streamlit.components.v1 as components  # For embedding YouTube videos
from gtts import gTTS
import io

tabs = st.tabs(["🔊 Text-to-Speech", "📝 Listen by stentences"])

# Text-to-Speech tab
with tabs[0]:
    st.subheader("🔊 Text-to-Speech (using Google TTS)")
    text_input = st.text_area("Enter the text you want to convert to speech:")
    language = st.selectbox("Choose a language: 🇰🇷 🇺🇸 🇬🇧 🇷🇺 🇫🇷 🇪🇸 🇮🇹 🇯🇵 ", ["Korean", "English (American)", "English (British)", "Russian", "Spanish", "French", "Italian", "Japanese"])

    tts_button = st.button("Convert Text to Speech")
    
    if tts_button and text_input:
        lang_codes = {
            "Korean": ("ko", None),
            "English (American)": ("en", 'com'),
            "English (British)": ("en", 'co.uk'),
            "Russian": ("ru", None),
            "Spanish": ("es", None),
            "French": ("fr", None),
            "Italian": ("it", None),
            "Japanese": ("ja", None)
        }
        language_code, tld = lang_codes[language]
        
        if tld:
            tts = gTTS(text=text_input, lang=language_code, tld=tld, slow=False)
        else:
            tts = gTTS(text=text_input, lang=language_code, slow=False)
        
        speech = io.BytesIO()
        tts.write_to_fp(speech)
        speech.seek(0)
        st.audio(speech.getvalue(), format='audio/mp3')

# Sentence Split & Audio tab
with tabs[1]:
    st.subheader("📝 Read by Sentences")
    text_input = st.text_area("Enter the text you want to split and convert to audio per sentence:")
    language = st.selectbox("Choose a language for audio output:", ["Korean", "English (American)", "English (British)", "Russian", "Spanish", "French", "Italian", "Japanese"])

    split_button = st.button("Split Text & Generate Audio")
    
    if split_button and text_input:
        # Import the necessary function from nltk
        import nltk
        nltk.download('punkt')
        from nltk.tokenize import sent_tokenize

        # Selecting the language for nltk tokenizer
        if language in ["Russian", "Italian", "French", "Spanish"]:
            sentences = sent_tokenize(text_input, language=language.lower())
        else:
            sentences = sent_tokenize(text_input)

        for i, sentence in enumerate(sentences, 1):
            st.write(f"{i}. {sentence}")
            tts = gTTS(text=sentence, lang=lang_codes[language][0], slow=False)
            speech = io.BytesIO()
            tts.write_to_fp(speech)
            speech.seek(0)
            st.audio(speech.getvalue(), format='audio/mp3')
