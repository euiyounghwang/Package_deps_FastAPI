
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import yaml
import json
import os, sys
import logging

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("FastAPI_Deps_REST_API")


def get_headers():
    ''' Elasticsearch Header '''
    return {'Content-type': 'application/json', 'Connection': 'close'}


load_dotenv()

es_client = Elasticsearch(hosts= os.getenv("ELASTICSEARCH_HOST", "localhost:9200"),
                          headers=get_headers(),
                          verify_certs=False,
                          timeout=600
)