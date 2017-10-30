from pytest import mark

from tests.factories import TaskFactory
from utils import model_instance_id_to_base64


@mark.django_db
def test_task(graph_client):
    query = '''
        query($id: ID!) {
            task(id: $id) {
                name
                description
                owner {
                    username
                }
                category {
                    name
                }
            }
        }
    '''
    task = TaskFactory.create()
    result = graph_client.execute(query, variable_values={'id': model_instance_id_to_base64(task)})
    assert result == {
        'data': {
            'task': {
                'name': task.name,
                'description': task.description,
                'owner': {
                    'username': task.owner.username
                },
                'category': {
                    'name': task.category.name
                }
            }
        }
    }
