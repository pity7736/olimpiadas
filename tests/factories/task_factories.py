import datetime

from factory import DjangoModelFactory, Faker, Sequence, SubFactory, LazyFunction


class CategoryFactory(DjangoModelFactory):
    name = Sequence(lambda n: f'category{n}')
    description = Faker('text')

    class Meta:
        model = 'tasks.Category'


class TaskFactory(DjangoModelFactory):
    name = Sequence(lambda n: f'task{n}')
    description = Faker('text')
    owner = SubFactory('tests.factories.accounts_factories.UserFactory')
    category = SubFactory(CategoryFactory)
    deadline = LazyFunction(datetime.datetime.now)

    class Meta:
        model = 'tasks.Task'
