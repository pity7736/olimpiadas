from graphene import ObjectType, relay, Field, Int
from graphene_django.filter import DjangoFilterConnectionField

from accounts.models import User
from accounts.schemas import UserNode
from tasks.schemas import CategoryNode, TaskNode


class GlobalQuery(ObjectType):
    category = relay.Node.Field(CategoryNode)
    task = relay.Node.Field(TaskNode)
    user_relay = relay.Node.Field(UserNode)
    user = Field(UserNode, id=Int(required=True))
    users = DjangoFilterConnectionField(UserNode, extra_filter_meta={'exclude': 'password'})

    def resolve_user(self, info, id):
        return User.objects.get_user_graph_or_none(info, id=id)
