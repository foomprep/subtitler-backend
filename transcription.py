import whisper

class Transcriber:
    def __init__(self):
        self.model = whisper.load_model('small')

    def transcribe(self, media_path):
        options = {
            "fp16": False,
        }
        result = self.model.transcribe(media_path, word_timestamps=True, **options)
        return result
