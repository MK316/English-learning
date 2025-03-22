# 🐾_Online_resources.py
import streamlit as st

# Dictionary containing online resources
resources = {
    "speechnotes.co": {
        "url": "https://www.speechnotes.co",
        "description": """
        Speechnotes offers a streamlined, speech-to-text notepad to capture your thoughts quickly and efficiently. Ideal for dictating essays or notes on the go!
        """
    },
    "suno": {
        "url": "https://suno.com",
        "description": """
        Suno AI revolutionizes learning and entertainment with its advanced audio tools, including audio books, podcasts, and innovative song generation for an immersive audio experience.
        """
    }
}

# Streamlit webpage layout
def main():
    st.markdown('### 🐳 Online Resources for Learning and Productivity')
    st.write('Explore these powerful online tools that can enhance your learning and productivity.')

    for resource_name, resource_info in resources.items():
        st.markdown(f"### 🎹 {resource_name}")
        st.markdown(f"**URL:** [{resource_info['url']}]({resource_info['url']})")
        st.markdown(f"**Description:** {resource_info['description']}")

# Run the main function
if __name__ == "__main__":
    main()
