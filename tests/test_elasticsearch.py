import pytest
from elasticsearch.client import Elasticsearch, IndicesClient
import json


# @pytest.fixture(scope="session")
def test_elasticsearch(mock_es_client):
    # ES 7 will be on 9200 and setup basic index with some datas into local elasticsearch cluster
    assert mock_es_client is not None