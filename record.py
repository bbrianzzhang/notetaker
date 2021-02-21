import sounddevice as sd
from scipy.io.wavfile import write
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)

sd.default.device = ["Stereo Mix", 1]

fs=44100
seconds=10

myrecording=sd.rec(int(seconds*fs), samplerate=fs, channels=2)
sd.wait()
write('output.wav', fs, myrecording)


# import pyaudio, wave, sys
#
# def generate_recording():
#     CHUNK = 8192
#     FORMAT = pyaudio.paInt16
#     CHANNELS = 1
#     RATE = 44100
#     RECORD_SECONDS = 59
#
#     WAVE_OUTPUT_FILENAME = 'output.wav'
#     p = pyaudio.PyAudio()
#     stream = p.open(format=FORMAT,
#                     channels = CHANNELS,
#                     rate = RATE,
#                     input = True,
#                     input_device_index = 0,
#                     frames_per_buffer = CHUNK)
#
#     print("* recording")
#
#     frames = []
#     for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#         data = stream.read(CHUNK)
#         frames.append(data)
#     print("* done recording")
#
#     stream.stop_stream()
#     stream.close()
#     p.terminate()
#
#     wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(p.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(frames))
#     wf.close()
