from fastapi import (
    APIRouter,
    UploadFile,
)
import aiofiles

import whisper

router = APIRouter()

from transcription import Transcriber
transcriber = Transcriber()

@router.post(
    "/transcribe",
)
async def transcribe_file(file: UploadFile):
    async with aiofiles.open('tmp', 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    transcription = transcriber.transcribe('tmp') 
    return transcription
