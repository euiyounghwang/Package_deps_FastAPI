from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import asyncio
from fastapi.responses import StreamingResponse
import time

# app = FastAPI()

app = FastAPI(
    title="ES Package Deps Service",
    description="ES Package Deps Service",
    version="0.0.1",
    # terms_of_service="http://example.com/terms/",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
   

async def event_stream():
    """Yields events in the required SSE format: 'data: <message>\\n\\n'"""
    while True:
        # Simulate real-time data update
        # data = f"The time is {asyncio.get_event_loop().time()}"
        # yield f"data: {data}\n\n"
        # await asyncio.sleep(1)
        yield f"data: The time is {time.strftime('%X')}\n\n"
        # time.sleep(1)
        await asyncio.sleep(1)

@app.get("/stream")
async def stream_events():
    return StreamingResponse(event_stream(), media_type="text/event-stream")

''' Enter the host name of the master node in the spark cluster to collect the list of running spark jobs. '''
# app.include_router(es_config_controller.app, tags=["Prometheus Configuration API"], )