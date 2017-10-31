from graphene import InputObjectType, String, Int, Mutation, Boolean, Field
from graphene.types.datetime import DateTime

from tasks.models import Task, Category
from tasks.schemas import TaskNode, CategoryNode


class NameInput(InputObjectType):
    name = String(required=True)
    description = String()


class CreateCategoryInput(NameInput):
    pass


class CreateCategoryMutation(Mutation):
    ok = Boolean()
    category = Field(CategoryNode)

    class Arguments:
        category_data = CreateCategoryInput()

    def mutate(self, info, category_data):
        category = Category.objects.create(**category_data)
        return CreateCategoryMutation(ok=True, category=category)


class CreateTaskInput(NameInput):
    name = String(required=True)
    description = String()
    owner_id = Int(required=True)
    category_id = Int(required=True)
    deadline = DateTime()


class CreateTaskMutation(Mutation):
    ok = Boolean()
    task = Field(TaskNode)

    class Arguments:
        task_data = CreateTaskInput()

    def mutate(self, info, task_data):
        task = Task.objects.create(**task_data)
        return CreateTaskMutation(ok=True, task=task)
