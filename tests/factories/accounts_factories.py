from factory import DjangoModelFactory, Sequence


class UserFactory(DjangoModelFactory):
    first_name = 'John'
    last_name = 'Doe'
    username = Sequence(lambda n: f'username-{n}')
    email = Sequence(lambda n: f'useremail{n}')

    class Meta:
        model = 'accounts.User'
