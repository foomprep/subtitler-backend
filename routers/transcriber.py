from fastapi import (
    APIRouter,
    UploadFile,
)
import aiofiles

router = APIRouter()

from transcription import Transcriber
transcriber = Transcriber(language="de", model_size="medium")

def generate_subtitles(transcription):
    subtitles = {'start': [], 'end': [], 'text': []}
    current_start = None
    sentence = ''
    matches = ['.', '?', '!', ',']
    for segment in transcription['segments']:
        for word in segment['words']:
            if not any([x in word['word'] for x in matches]):
                if current_start is None:
                    current_start = word['start']
                sentence += word['word']
            else:
                if current_start is None:
                    current_start = word['start']
                sentence += word['word']
                subtitles['start'].append(current_start)
                subtitles['end'].append(word['end'])
                subtitles['text'].append(sentence)
                sentence = ''
                current_start = None
    return subtitles

@router.post(
    "/transcribe",
)
async def transcribe_file(file: UploadFile):
    async with aiofiles.open('tmp', 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    transcription = transcriber.transcribe('tmp') 
    subtitles = generate_subtitles(transcription)
    return subtitles
