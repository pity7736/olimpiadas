from graphene import ObjectType

from tasks.mutations import CreateTaskMutation, CreateCategoryMutation


class GlobalMutation(ObjectType):
    create_category = CreateCategoryMutation.Field()
    create_task = CreateTaskMutation.Field()
