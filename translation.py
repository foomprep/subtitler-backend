from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

class Translator:
    def __init__(self, source_lang: str):
        self.model = M2M100ForConditionalGeneration.from_pretrained('facebook/m2m100_418M')
        self.tokenizer = M2M100Tokenizer.from_pretrained('facebook/m2m100_418M')
        self.tokenizer.src_lang = source_lang

    def translate(self, text: str):
        encoded_text = self.tokenizer(text, return_tensors='pt')
        generated_tokens = self.model.generate(
            **encoded_text,
            forced_bos_token_id=self.tokenizer.get_lang_id('en')
        )
        translation = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        return translation[0].lower()
