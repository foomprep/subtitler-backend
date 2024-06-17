import whisper

class Transcriber:
    def __init__(self, language="en", model_size="large-v3"):
        self.model = whisper.load_model(model_size)
        self.language = language

    def transcribe(self, media_path):
        options = {
            "fp16": False,
        }
        result = self.model.transcribe(media_path, word_timestamps=True, language=self.language, **options)
        return result
