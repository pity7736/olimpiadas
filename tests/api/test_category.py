from pytest import mark

from tests.factories import CategoryFactory
from utils import model_instance_id_to_base64


@mark.django_db
def test_category(graph_client):
    query = '''
        query($id: ID!) {
            category(id: $id) {
                name
                description
            }
        }
    '''
    category = CategoryFactory.create()
    result = graph_client.execute(query, variable_values={'id': model_instance_id_to_base64(category)})
    assert result == {
        'data': {
            'category': {
                'name': category.name,
                'description': category.description
            }
        }
    }
