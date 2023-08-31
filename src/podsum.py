import openai
import streamlit as st


def get_transcribe_podcast(audio):
        with st.spinner("Transcribing the Audio"):
            transcript = openai.Audio.transcribe(
                file = audio,
                model = "whisper-1",
                response_format="text",
                language="en"
            )
        return transcript
