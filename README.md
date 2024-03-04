# SaraKIT with Voice ChatGPT

SaraKIT is equipped with three microphones and a specialized sound processor that cleanses the voice and supports speech recognition on Raspberry Pi from distances up to 16.4 feet (5 meters). Building a voice-operated ChatGPT is possible through various methods, with many examples available on GitHub. Here, I propose a solution based on the offline speech recognition tool Vosk, used for wake word detection and command recognition, and Piper for speech generation - both programs are currently the best offline Text to Speech (TTS) and Speech to Text (STT) solutions for Raspberry Pi. The offline approach means continuous internet connectivity is not required, ensuring privacy and a free solution.

<img src="https://github.com/SaraEye/SaraKIT-Voice-ChatGPT-Raspberry-Pi/assets/35704910/6d403cfd-8274-4f6f-aac1-2d18061a0d2b" width="350">
<img src="https://github.com/SaraEye/SaraKIT-Voice-ChatGPT-Raspberry-Pi/assets/35704910/02763830-c1da-48e3-aeb1-a0246703cd5e" width="350">

For more details on Piper, see here: [https://github.com/SaraEye/SaraKIT-Text-To-Speech-Piper-Raspberry-Pi](https://github.com/SaraEye/SaraKIT-Text-To-Speech-Piper-Raspberry-Pi)<br>
For more on Vosk, check out: [https://github.com/SaraEye/SaraKIT-Speech-Recognition-Vosk-Raspberry-Pi](https://github.com/SaraEye/SaraKIT-Speech-Recognition-Vosk-Raspberry-Pi)

## Installation on SaraKIT

Assuming the basic SaraKIT drivers are already installed ([Getting Started with SaraKIT](https://sarakit.saraai.com/getting-started/software)), follow these steps to install the required tools:

```bash
sudo apt-get update
sudo apt-get install -y python3-pip python3-pyaudio libasound2-dev libfmt-dev libspdlog-dev

sudo pip3 install vosk piper-tts openai

git clone https://github.com/SaraEye/SaraKIT-Voice-ChatGPT-Raspberry-Pi VoiceChatGPT
cd VoiceChatGPT
```

Before running, you'll need to insert your OpenAI API key, which you can obtain by registering on [OpenAI's website](https://openai.com/). <br>
Insert your API key in the line:

```python
client = OpenAI(api_key="YOUR_API_KEY_HERE")
```

Set your wake word in the line:

```python
WakeWord="sarah"
```

If you wish to change the language from English or adjust the voice for Piper or Vosk, download and load the appropriate models. See the descriptions on [Piper's GitHub](https://github.com/SaraEye/SaraKIT-Text-To-Speech-Piper-Raspberry-Pi) and [Vosk's GitHub](https://github.com/SaraEye/SaraKIT-Speech-Recognition-Vosk-Raspberry-Pi) for guidance.

To run:

```bash
python VoiceChatGPT.py
```

Initially, the chat waits for the wake word, by default "sarah". After recognizing it, you can ask ChatGPT anything, and it will respond verbally.

This setup creates a powerful, private, and interactive voice assistant using the capabilities of ChatGPT, SaraKIT and Raspberry Pi. Dive into creating your personalized voice-operated assistant today!

On our website, you can discover an even more advanced version we've dubbed SaraEye, where ChatGPT activation doesn't rely on a wake word but on gaze recognition, mimicking human interaction. When we look at someone, they know we're addressing them. Similarly, here, you simply look at ChatGPT to engage, eliminating the need for constant wake prompts like "Alexa, Alexa, Alexa..." :)

<img src="https://github.com/SaraEye/SaraKIT-Voice-ChatGPT-Raspberry-Pi/assets/35704910/b841da3d-4ae7-4aa2-9995-73d92b5b37fd" width="350">
<img src="https://github.com/SaraEye/SaraKIT-Voice-ChatGPT-Raspberry-Pi/assets/35704910/f5206b72-e3f5-498b-a1e6-212b0843cf69" width="350">

SaraEye: https://youtu.be/aLGZZ5pAoj0 <br>
Pan/Tilt Camera (or Turret Base): https://sarakit.saraai.com/example-of-use/camera-pan-tilt

SaraKIT Project Page: [https://sarakit.saraai.com](https://sarakit.saraai.com)
