import whisper

class Transcriber:
    def __init__(self):
        self.model = whisper.load_model('base')

    # audio_clip -> numpy.ndarray (Int16Array) OR torch.tensor
    def transcribe(self, audio_clip) -> str:
        options = {
            "fp16": False,
            "language": "es",
        }
        result = whisper.transcribe(self.model, audio_clip, **options) 
        return result
