from django.db import models
from utils.requested_fields import requested_fields


class BaseManager(models.Manager):

    def get_user_graph_or_none(self, info, **kwargs):
        fields = requested_fields(info=info)
        return self.get_or_none(fields=fields, **kwargs)

    def get_or_none(self, fields=(), **kwargs):
        try:
            return self.only(*fields).get(**kwargs)
        except self.model.DoesNotExist:
            return None
