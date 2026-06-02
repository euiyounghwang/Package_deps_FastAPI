from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import asyncio
from fastapi.responses import StreamingResponse
import time
from injector import logger
from contextlib import asynccontextmanager


# 1. Define global variable for your index and model
faiss_index = None
FAISS_INDEX_PATH = "models/my_faiss_index.bin"

# 2. Define lifespan event to handle startup and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    ''' 
    To load a FAISS index and an embedding model efficiently in FastAPI, 
    you should use FastAPI's lifespan event handler to load them into memory exactly once when the server starts. 
    This prevents the severe performance penalty of re-loading the models on every single API request.
    '''
    # Load the embedding model and FAISS index on startup
    ''' To reload a FAISS model (or vector index) in FastAPI without restarting the server, create a dedicated endpoint that triggers a reload function. This function reloads the FAISS index into a global variable or shared'''
    global faiss_index
    try:
        # print("Loading ML models and FAISS index...")
        # ml_models["encoder"] = SentenceTransformer("all-MiniLM-L6-v2")
        # ml_models["faiss_index"] = faiss.read_index("my_vector_store.index")

        # faiss_index = faiss.read_index(FAISS_INDEX_PATH)
        logger.info(f"startup eventing..")
    except Exception as e:
        print(f"Error loading models: {e}")
        raise RuntimeError("Startup failed: Models could not be loaded.")
        
    yield
    # Clean up on shutdown
    # ml_models.clear()
    logger.info(f"shutdown..")


# @app.on_event("startup")
# def startup_event():
#     logger.info(f"startup eventing..")


# app = FastAPI()

app = FastAPI(
    title="ES Package Deps Service",
    description="ES Package Deps Service",
    version="0.0.1",
    # terms_of_service="http://example.com/terms/",
    lifespan=lifespan
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