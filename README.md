# SaraKIT with Voice ChatGPT

SaraKIT is equipped with three microphones and a specialized sound processor that cleanses the voice and supports speech recognition on Raspberry Pi from distances up to 16.4 feet (5 meters). Building a voice-activated ChatGPT can be achieved in various ways, and while there are numerous examples on GitHub, this guide proposes a solution based on the offline speech recognition tool Vosk for wake word detection and command recognition. For speech generation, we utilize Piper, an offline text-to-speech program. Both of these tools currently represent the best offline solutions for Raspberry Pi concerning Text to Speech and Speech to Text functionality. The offline aspect means constant internet connectivity is not required, ensuring privacy and security within your home environment, and importantly, it's a free solution.

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

Before running, you need to enter your OpenAI API key, which you can obtain by registering on the OpenAI website. Insert your API key in the line:

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

This setup offers a potent way to integrate advanced voice interaction into your Raspberry Pi projects, leveraging the capabilities of SaraKIT and the intelligence of ChatGPT without the need for an always-on internet connection.


Replace `YOUR_API_KEY_HERE` with your actual OpenAI API key. This README provides a comprehensive guide to setting up voice-activated ChatGPT with SaraKIT, emphasizing the project's offline capabilities and privacy advantages.
