import io

def transcribe_file():
    """Transcribe the given audio file asynchronously."""
    from google.cloud import speech

    client = speech.SpeechClient()

    with io.open("output.wav", "rb") as audio_file:
        content = audio_file.read()

    """
     Note that transcription is limited to a 60 seconds audio file.
     Use a GCS file for audio longer than 1 minute.
    """
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
        audio_channel_count=1,
        sample_rate_hertz=44100,
        enable_automatic_punctuation=True
    )


    operation = client.long_running_recognize(config=config, audio=audio)

    #print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    transcription = ""
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        transcription+=result.alternatives[0].transcript
    f = open("transcription.txt", "a")
    f.write(transcription)
    f.close()
    print(transcription)
