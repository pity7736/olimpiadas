from django.db import models
from utils.requested_fields import requested_fields
from django.db.models.fields.related_descriptors import ForwardManyToOneDescriptor


class BaseManager(models.Manager):

    def get_user_graph_or_none(self, info, **kwargs):
        fields = requested_fields(info=info)
        return self.get_or_none(fields=fields, **kwargs)

    def get_or_none(self, fields=(), **kwargs):
        print(fields, 'before')
        fields = self.filter_model_fields(fields)
        print(fields, 'after', end='\n\n')
        queryset = self.get_queryset_with_related(fields)
        try:
            return queryset.only(*fields).get(**kwargs)
        except self.model.DoesNotExist:
            return None

    def filter_model_fields(self, fields):
        new_fields = []
        for graph_field, graph_subfields in fields.items():
            print(graph_field, 'gf')
            if graph_field in map(lambda field: field.name, self.model._meta.fields):
                print(graph_subfields, 'gsf')
                new_fields.append(graph_field)
#                 new_fields.extend(graph_subfields)
        return new_fields

    def get_queryset_with_related(self, fields):
        related = []
        for field_name in fields:
            field = getattr(self.model, field_name, None)
            if type(field) is ForwardManyToOneDescriptor:
                related.append(field_name)

        queryset = self.get_queryset()
        if related:
            queryset = self.select_related(*related)
        return queryset
