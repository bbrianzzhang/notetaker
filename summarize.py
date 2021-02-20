from summarizer import Summarizer

def get_notes(body):
    model = Summarizer()
    result = model(body, min_length=60)
    full = ''.join(result)
    print(full)
