from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

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
   

''' Enter the host name of the master node in the spark cluster to collect the list of running spark jobs. '''
# app.include_router(es_config_controller.app, tags=["Prometheus Configuration API"], )