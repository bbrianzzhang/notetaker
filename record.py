import sounddevice as sd
from scipy.io.wavfile import write
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)
sd.default.device = ["Stereo Mix", 1]
import sys
import time
import requests

fs=44100
seconds=59


def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data


def generate_recording():
    myrecording=sd.rec(int(seconds*fs), samplerate=fs, channels=2)
    sd.wait()
    write('output.wav', fs, myrecording)
    filename = "output.wav"

    endpoint = "https://api.assemblyai.com/v2/transcript"
    headers = {'authorization': "5ca9d5f40ec842038e248e0d5587ab50"}
    response = requests.post('https://api.assemblyai.com/v2/upload',
                             headers=headers,
                             data=read_file(filename))
    print("Recording sent!")
    url=response.json()['upload_url']

    json = {
      "audio_url": url
    }
    headers = {
        "authorization": "5ca9d5f40ec842038e248e0d5587ab50",
        "content-type": "application/json"
    }
    response = requests.post(endpoint, json=json, headers=headers)
    id=response.json()['id']

    #receiving the transcription
    endpoint = "https://api.assemblyai.com/v2/transcript/" + id
    headers = {
        "authorization": "5ca9d5f40ec842038e248e0d5587ab50",
    }
    finished = False
    while not finished:
        response = requests.get(endpoint, headers=headers)
        if response.json()['status'] == 'completed':
            finished = True
            print(response.json()['text'])
            notes = open('transcription.txt', 'a')
            notes.write(response.json()['text'])
            notes.close()

