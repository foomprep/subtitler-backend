from fastapi import (
    APIRouter,
)

import whisper

router = APIRouter()

from transcription import Transcriber
transcriber = Transcriber()

@router.post(
    "/transcribe",
)
async def transcribe_file():
    pass
