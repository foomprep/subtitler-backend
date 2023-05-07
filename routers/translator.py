from fastapi import (
    APIRouter,
)

router = APIRouter()

from translation import Translator
translator = Translator('es')

from pydantic import BaseModel

class Text(BaseModel):
    text: str

@router.post(
    "/translate",
)
async def translate_text(text: Text):
    return_dict = text.dict()
    translation = translator.translate(text.text)
    return_dict.update({"translation": translation})
    return return_dict
