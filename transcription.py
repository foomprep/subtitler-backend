import whisper

class Transcriber:
    def __init__(self):
        self.model = whisper.load_model('base')

    def transcribe(self, media_path):
        result = self.model.transcribe(media_path)
        return result
