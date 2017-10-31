from graphene import Schema

from .mutations import GlobalMutation
from .schemas import GlobalQuery


schema = Schema(query=GlobalQuery, mutation=GlobalMutation)
