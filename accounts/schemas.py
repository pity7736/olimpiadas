from graphene import relay
from graphene_django import DjangoObjectType

from accounts.models import User


class UserNode(DjangoObjectType):

    class Meta:
        model = User
        exclude_fields = ('password',)
        interfaces = (relay.Node,)

    @classmethod
    def get_node(cls, info, user_id):
        return User.objects.get_user_graph_or_none(info, id=user_id)
