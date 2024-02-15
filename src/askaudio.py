import streamlit as st
import time
from openai import OpenAI
import os

client = OpenAI()


def get_transcribe_audio(audio):
    with st.spinner(
        "Patience is the key to accurate analysis. Please wait while we process your audio"
    ):
        transcript = client.audio.transcriptions.create(
            file=audio, model="whisper-1", response_format="text", language="en"
        )
    with st.spinner("Hold the line, we're diving deep into your audio."):
        time.sleep(1)
    st.toast("Your Audio File is analyzed", icon="😍")
    time.sleep(0.5)
    return transcript


def get_custom_response(request):
    chatOutput = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": request},
        ],
    )
    customResponse = chatOutput.choices[0].message.content
    return customResponse
