import os
import sys
import json
import time
import contextlib
import pyaudio
import io
from vosk import Model, KaldiRecognizer
from openai import OpenAI
from piper import PiperVoice
import numpy as np

WakeWord="sarah"
#=============================================================================


#Enter your api key
#=============================================================================
client = OpenAI(api_key="YOUR_API_KEY_HERE")


#Select the language and voice (Text To Speech) for ChatGPT
#=============================================================================
#voice = PiperVoice.load("models/piper/pl/gosia/pl_PL-gosia-medium.onnx", "models/piper/pl/gosia/pl_PL-gosia-medium.onnx.json")
voice = PiperVoice.load("models/piper/en/amy/en_US-amy-medium.onnx", "models/piper/en/amy/en_US-amy-medium.onnx.json")


#Select the language and model for Speech Recognition
#=============================================================================
#model_path = "models/vosk-model-small-pl-0.22/"
model_path = "models/vosk-model-small-en-us-0.15/"
if not os.path.exists(model_path):
    print(f"Model '{model_path}' was not found. Please check the path.")
    exit(1)
model = Model(model_path)



# Initialization of PyAudio and speech recognition
p = pyaudio.PyAudio()
chunk_size=8192
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=chunk_size)
recognizer = KaldiRecognizer(model, 16000)



def text_to_speech(voice, text):
    audio_stream = voice.synthesize_stream_raw(text)
    pTTS = pyaudio.PyAudio()
    stream = pTTS.open(format=pTTS.get_format_from_width(width=2),  # Assuming the audio is 16-bit
                    channels=1,
                    rate=22050,
                    output=True,
                    output_device_index=1)
                    
    # Calculate the number of silence samples to prepend
    silence_duration=0.6
    silence_samples = int(silence_duration * 22050)
    silence_data = (np.zeros(silence_samples, dtype=np.int16)).tobytes()
    # Play the silence
    stream.write(silence_data)                    

    # Play the stream chunk by chunk
    for audio_bytes in audio_stream:
        stream.write(audio_bytes)

    stream.stop_stream()
    stream.close()
    pTTS.terminate()



def askChatGPT(pytanie):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": pytanie},
        ],
    )  
    # Wyświetlanie odpowiedzi
    resp=completion.choices[0].message.content
    print(resp)
    text_to_speech(voice, resp)



os.system('clear')
print("\nWaiting for WakeWord...")

isChatActive=False
last_sound_time = time.time()
while True:
    data = stream.read(chunk_size)
    if recognizer.AcceptWaveform(data):
        result_json = json.loads(recognizer.Result())
        text = result_json.get('text', '')
        if text:
            print("\r" + text, end='\n')
            last_sound_time = time.time()

            if isChatActive:
                stream.stop_stream()
                askChatGPT(text)
                print("\n")
                stream.start_stream()
                last_sound_time = time.time()
                continue

            if partial.lower()==WakeWord:
                print("\nSpeak now...")
                isChatActive=True                
    else:
        partial_json = json.loads(recognizer.PartialResult())
        partial = partial_json.get('partial', '')
        sys.stdout.write('\r' + partial)
        sys.stdout.flush()

    if time.time() - last_sound_time > 4 and isChatActive:
        isChatActive = False
        print("\nWaiting for WakeWord...")
