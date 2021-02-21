from summarizer import Summarizer

def get_notes(body):
    model = Summarizer()
    result = model(body, ratio=0.2)
    full = ''.join(result)
    return full
