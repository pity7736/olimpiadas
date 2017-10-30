import base64


def model_instance_id_to_base64(instance):
    return base64_encode(f'{instance.__class__.__name__}Node:{instance.id}')


def base64_encode(string):
    return base64.b64encode(bytes(string, 'utf-8')).decode('utf-8')
