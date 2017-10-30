from factory import DjangoModelFactory, Faker, Sequence


class CategoryFactory(DjangoModelFactory):
    name = Sequence(lambda n: f'category{n}')
    description = Faker('text')

    class Meta:
        model = 'tasks.Category'
