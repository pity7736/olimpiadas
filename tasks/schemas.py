from graphene import relay, String
from graphene_django import DjangoObjectType

from tasks.models import Category, Task


class CategoryNode(DjangoObjectType):

    class Meta:
        interfaces = (relay.Node,)
        model = Category


class TaskNode(DjangoObjectType):
    test = String()
    status = String()

    class Meta:
        interfaces = (relay.Node,)
        model = Task

    @classmethod
    def get_node(cls, info, task_id):
        return Task.objects.get_user_graph_or_none(info, id=task_id)

    def resolve_test(self, info):
        return 'hola'
