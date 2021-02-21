import io
#
from google.cloud import speech_v1p1beta1 as speech
import enum
import types
import wave

# from google.cloud import speech

def transcribe_file():
    client = speech.SpeechClient()
    w = wave.open('output.wav', 'w')
    w.setnchannels(1)
    w.close()
    speech_file = "output.wav"

    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
        enable_speaker_diarization=True,
        diarization_speaker_count=2,
        audio_channel_count=2,
    )

    print("Waiting for operation to complete...")
    response = client.recognize(config=config, audio=audio)

    # The transcript within each result is separate and sequential per result.
    # However, the words list within an alternative includes all the words
    # from all the results thus far. Thus, to get all the words with speaker
    # tags, you only have to take the words list from the last result:
    result = response.results[-1]

    words_info = result.alternatives[0].words

    # Printing out the output:
    for word_info in words_info:
        print(
            u"word: '{}', speaker_tag: {}".format(word_info.word, word_info.speaker_tag)
        )
