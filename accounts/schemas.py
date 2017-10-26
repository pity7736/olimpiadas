from graphene import relay
from graphene_django import DjangoObjectType

from accounts.models import User


class UserNode(DjangoObjectType):

    class Meta:
        model = User
        exclude_fields = ('password',)
        interfaces = (relay.Node,)
