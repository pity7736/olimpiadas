from pytest import mark

from tests.factories import UserFactory


@mark.django_db
def test_user(graph_client):
    query = '''
        query($id: Int!) {
            user(id: $id) {
              username
              email
            }
        }
    '''
    user = UserFactory.create()
    result = graph_client.execute(query, variable_values={'id': user.id})
    assert result == {
        'data': {
            'user': {
                'username': user.username,
                'email': user.email
            }
        }
    }
