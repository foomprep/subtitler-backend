from transformers import pipeline

class Translator:
    def __init__(self, model_name='Helsinki-NLP/opus-mt-de-en'):
        self.pipe = pipeline('translation', model=model_name)

    def translate(self, text: str):
        return self.pipe(text)[0]
