from graphene.test import Client
from pytest import mark

from api.schemas import schema
from tests.factories.accounts_factories import UserFactory


@mark.django_db
def test_user():
    client = Client(schema=schema)
    user = UserFactory.create()
    query = '''
        query($id: Int!) {
            user(id: $id) {
              username
              email
            }
        }
    '''
    result = client.execute(query, variable_values={'id': user.id})
    assert result == {
        'data': {
            'user': {
                'username': user.username,
                'email': user.email
            }
        }
    }
