from graphene import relay
from graphene_django import DjangoObjectType

from tasks.models import Category


class CategoryNode(DjangoObjectType):

    class Meta:
        interfaces = (relay.Node,)
        model = Category
