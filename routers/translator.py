from fastapi import (
    APIRouter,
    UploadFile,
    Body
)
from pydantic import BaseModel

router = APIRouter()

class TranslationRequest(BaseModel):
    text: str

from translation import Translator
translator = Translator()

@router.post(
    "/translate",
)
async def translate(request: TranslationRequest):
    return translator.translate(request.text)
