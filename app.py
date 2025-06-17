
import streamlit as st
import whisper
from io import BytesIO

st.set_page_config(page_title='Whisper Transcription', layout='centered')
st.title('🎙️ Whisper AI Audio Transcriber')
st.write('Upload an audio file to transcribe:')

audio_file = st.file_uploader('Upload Audio', type=['mp3', 'wav', 'm4a'])

model_option = st.sidebar.selectbox('Choose Whisper model:', ['tiny', 'base', 'small', 'medium', 'large'], index=1)

if audio_file is not None:
    st.audio(audio_file, format='audio/mp3')

    with st.spinner('Loading model...'):
        model = whisper.load_model(model_option)

    st.info('Transcribing...')
    audio_bytes = audio_file.read()
    audio_io = BytesIO(audio_bytes)

    result = model.transcribe(audio_io)

    st.success('Transcription Complete!')
    st.text_area('Transcript:', result['text'], height=300)
    st.download_button('📥 Download Transcript', result['text'], file_name='transcript.txt', mime='text/plain')
