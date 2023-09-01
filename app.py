import streamlit as st
import time
from src.askaudio import get_transcribe_audio, get_custom_response

st.set_page_config(
    layout="wide",
    page_title=" Ask Audio",
    page_icon=":robot_face:",
    initial_sidebar_state="expanded",
    menu_items={"About": "# This is an *extremely* cool Audio GPT app!"},
)

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)
left, right = st.columns(2)

def load_css(file_name):
    with open(file_name) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

def setup():
    transcript=''
    custom_prompt= ''

    with left:
        html_temp = """
        <img src="https://i.ibb.co/B6MsdFT/casette.png" alt="casette" border="0" class="rotate linear infinite center" width="150" height="150"/>
        <h3 class = "css-els2uy"> Ask Audio 🤖 </h3>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
        st.write(""" """)  # description and instructions
        audio = st.file_uploader("Upload the audio to be analyzed and ask Questions\n", type=["mp3", "wav"], label_visibility="visible")

        if audio is None:
            st.text("")
        else:
            with left:
                if 'transcript' not in st.session_state:
                    st.session_state['transcript'] = get_transcribe_audio(audio)
                transcript = st.session_state['transcript']
                st.subheader("Play Audio")
                st.audio(audio)

        with st.form("Launch_form"):
                task=st.radio('What would you like me to do?', options=['Transcribe :speech_balloon:', 'Summary :memo:', 'Highlights :chart_with_upwards_trend:', ':rainbow[Custom] :rocket:'], horizontal=False, \
                        captions=["Get the transcription of the complete Audio. ", "Get the Summary of the Transcribed Audio.",\
                                "Get the Highlights of the Audio.", "Ask questions about the Audio and get the Answers from Powerful GPT."])

                custom_prompt = st.text_input("Enter the message")

                # Every form must have a submit button.
                submitted = st.form_submit_button("Launch", type='primary')

        return submitted, task, transcript, custom_prompt

def launch_task(task, transcript, custom_prompt):
    message = st.chat_message("assistant")

    if task == "Transcribe :speech_balloon:":
                message.write("Transcription")
                message.write(transcript)

    elif task == 'Summary :memo:':
        with st.spinner("Summarizing the content..."):
                instruction_prompt="Summarize the following"
                request= instruction_prompt + transcript
                if 'summary' not in st.session_state:
                    st.session_state['summary'] = get_custom_response(request=request)
                summary=st.session_state['summary']
        message.write("Summary")
        message.write(summary)

    elif task == 'Highlights :chart_with_upwards_trend:':
        with st.spinner("Picking up the Highlights..."):
            highlights_request= "Extract the Highlights from the following" + transcript
            if 'highlights' not in st.session_state:
                    st.session_state['highlights'] = get_custom_response(request=highlights_request)
            highlights=st.session_state['highlights']
        message.write("Audio Highlights")
        message.write(highlights)

    elif task == ':rainbow[Custom] :rocket:' and custom_prompt!='':
        with st.spinner("Generating the Response..."):
            oofContext_prompt= "Don’t give information not mentioned in the request"
            custom_request= oofContext_prompt+custom_prompt +' '+ transcript[:100]
            answer = get_custom_response(request=custom_request)
        message.write("Hello Human")
        message.write(answer)

def main():
    load_css("src/style.css")
    submitted, task, transcript, custom_prompt = setup()
    with right:
            if submitted and transcript != '':
                st.toast(f'Your task for {task} is submitted', icon='🚀')
                time.sleep(.5)
                launch_task(task, transcript, custom_prompt)
            else:
                 with left:
                    st.write("")


if __name__ == "__main__":
        main()