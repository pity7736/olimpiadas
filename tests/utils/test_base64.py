from utils import base64_encode, model_instance_id_to_base64
from tests.factories.accounts_factories import UserFactory


def test_encode():
    assert base64_encode('hola') == 'aG9sYQ=='


def test_model_instance_id_to_base64():
    user = UserFactory.build(id=1)
    assert model_instance_id_to_base64(user) == 'VXNlck5vZGU6MQ=='
