import whisper

class Transcriber:
    def __init__(self):
        self.model = whisper.load_model('small')

    def transcribe(self, media_path):
        result = self.model.transcribe(media_path, word_timestamps=True)
        return result
