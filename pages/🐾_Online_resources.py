# 🐾_Online_resources.py
import streamlit as st

# Dictionary containing online resources
resources = {
    "speechnotes.co": {
        "url": "https://www.speechnotes.co",
        "description": """
        Speechnotes is a powerful speech-enabled online notepad, designed to empower your ideas by implementing a clean & efficient design, so you can focus on your thoughts. This tool provides a user-friendly interface for continuous dictation, using advanced speech recognition technology to transcribe your speech into text in real-time. It's highly useful for quickly capturing long-form articles, blogs, and notes with your voice.
        """
    },
    "suno": {
        "url": "https://suno.com",
        "description": """
        Suno (if this is the intended 'Suno', please replace with the correct URL and description if different) is an innovative platform leveraging advanced audio processing technology. It offers a range of services from audio books and podcasts to comprehensive auditory tools for education and entertainment. This resource is excellent for users looking to access a broad spectrum of audio content for learning, entertainment, or professional development.
        """
    }
}

# Streamlit webpage layout
def main():
    st.title('Online Resources for Learning and Productivity')
    st.subheader('Explore these powerful online tools that can enhance your learning and productivity.')

    for resource_name, resource_info in resources.items():
        st.markdown(f"### {resource_name}")
        st.markdown(f"**URL:** [{resource_info['url']}]({resource_info['url']})")
        st.markdown(f"**Description:** {resource_info['description']}")

# Run the main function
if __name__ == "__main__":
    main()
