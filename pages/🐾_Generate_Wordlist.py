import streamlit as st
import pandas as pd
from collections import Counter
import base64
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from gtts import gTTS
from io import BytesIO
import io
import string
import random


def preprocess_text(word, proper_nouns):
    proper_noun_map = {pn.lower(): pn for pn in proper_nouns}
    contractions = ["'s", "'ve", "'d", "'ll", "'re", "'m", "'nt"]
    for contraction in contractions:
        if word.endswith(contraction):
            word = word[:-len(contraction)]
            break
    cleaned_word = word.translate(str.maketrans('', '', string.punctuation))
    return proper_noun_map.get(cleaned_word.lower(), cleaned_word.lower())
def create_word_frequency_dataframe(text, stopwords, proper_nouns):
    words = text.split()
    clean_text = [preprocess_text(word, proper_nouns) for word in words]
    filtered_words = [word for word in clean_text if word.lower() not in stopwords]
    counter = Counter(filtered_words)
    df = pd.DataFrame(counter.items(), columns=['Word', 'Frequency'])
    df = df.sort_values(by='Frequency', ascending=False)
    return df

def get_table_download_link_csv(df):
    towrite = io.StringIO()
    df.to_csv(towrite, index=False)
    towrite.seek(0)
    b64 = base64.b64encode(towrite.getvalue().encode()).decode()
    return f'<a href="data:file/csv;base64,{b64}" download="word_frequency.csv">Download CSV file</a>'

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    st.pyplot(plt)

st.set_page_config(page_title="Text Analysis Tools", page_icon="📝")
st.markdown('## 🌼 Try apps with your story')

tab1, tab2 = st.tabs(["🌱 Word Frequency", "💬 Word Cloud"])


with tab1:
    st.write("Generate Word Frequency Excel file (csv worksheet)")
    text_input_wf = st.text_area("1️⃣ Paste your text here:", key="wf_input")
    stopword_input = st.text_area("2️⃣ (Optional) Enter stopwords (words to exclude in the list - e.g., a, the, to, he, ...) separated by commas:", key="stopword_input")
    stopwords = {word.strip().lower() for word in stopword_input.split(',')} if stopword_input else set()
    proper_noun_input = st.text_area("3️⃣ (Optional) Enter proper nouns separated by commas:", key="proper_noun_input")
    proper_nouns = {word.strip() for word in proper_noun_input.split(',')} if proper_noun_input else set()
    if st.button("Create Wordlist (Excel file)", key="create_df_wf"):
        if text_input_wf:
            df = create_word_frequency_dataframe(text_input_wf, stopwords, proper_nouns)
            st.dataframe(df)
            st.markdown(get_table_download_link_csv(df), unsafe_allow_html=True)
        else:
            st.error("Please paste some text to generate the dataframe.")

with tab2:
    st.header("Generate a Word Cloud")
    text_input_wc = st.text_area("Paste your text here:", key="wc_input")
    if st.button("Generate Word Cloud", key="generate_wc"):
        if text_input_wc:
            generate_wordcloud(text_input_wc)
        else:
            st.error("Please paste some text to generate the word cloud.")
