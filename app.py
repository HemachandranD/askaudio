import streamlit as st
from src.podsum import get_transcribe_podcast

st.set_page_config(
    page_title="Food Sight",
    page_icon=":pizza",
    initial_sidebar_state="expanded",
    menu_items={"About": "# This is an *extremely* cool Food Sight app!"},
)

def setup():
    html_temp = """
    <img src="https://i.ibb.co/pjdrLS8/casette.png" alt="casette" border="0" class="rotate linear infinite center" width="150" height="150"/>
    <h3 class = "css-els2uy"> PodSum 🍕👀 </h3>
	"""
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write("""PODSUM""")  # description and instructions
    audio = st.file_uploader("Upload the podcast to be summarized\n", type=["mp3", "wav"])
    return  audio

def load_css(file_name):
    with open(file_name) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

def main():
    load_css("src/style.css")
    audio = setup()
    if audio is None:
        st.text("")
    else:
        st.header("Play Audio")
        st.audio(audio)
        transcript = get_transcribe_podcast(audio)
        st.header("Audio transcribed")
        st.write(transcript)


if __name__ == "__main__":
    main()
