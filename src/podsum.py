import openai
import streamlit as st
import time


def get_transcribe_audio(audio):
        with st.spinner("Patience is the key to accurate analysis. Please wait while we process your audio"):
            transcript = openai.Audio.transcribe(
                file = audio,
                model = "whisper-1",
                response_format="text",
                language="en"
            )
        with st.spinner("Hold the line, we're diving deep into your audio."):
              time.sleep(1)
        st.toast('Your Audio File is analyzed', icon='😍')
        time.sleep(.5)
        return transcript

def get_audio_summary(request):
      chatOutput= openai.ChatCompletion.create(model="gpt-3.5-turbo-16k",messages=[{
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": request
      }])
      audioSummary = chatOutput.choices[0].message.content
      return audioSummary


def get_audio_highlights(request):
      chatOutput= openai.ChatCompletion.create(model="gpt-3.5-turbo-16k",messages=[{
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": request
      }])
      audioHighlights = chatOutput.choices[0].message.content
      return audioHighlights

def get_custom_response(request):
      chatOutput= openai.ChatCompletion.create(model="gpt-3.5-turbo-16k",messages=[{
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": request
      }])
      customResponse = chatOutput.choices[0].message.content
      return customResponse
