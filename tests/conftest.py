from graphene.test import Client
from pytest import fixture

from api.schemas import schema


@fixture
def graph_client():
    return Client(schema=schema)
