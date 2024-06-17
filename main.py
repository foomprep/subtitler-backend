import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import transcriber, translator

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(transcriber.router)
app.include_router(translator.router)

@app.get("/ping")
async def pong():
    return { "message": "pong" }

def main():
    uvicorn.run(
        "main:app", 
        reload=True,
        port=5001
    )

if __name__ == '__main__':
    main()
