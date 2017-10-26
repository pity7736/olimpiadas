from graphene import ObjectType, Schema, relay, Field, Int
from graphene_django.filter import DjangoFilterConnectionField

from accounts.schemas import UserNode
from accounts.models import User


class GlobalQuery(ObjectType):
    user = relay.Node.Field(UserNode)
#     user = Field(UserNode, id=Int())
    users = DjangoFilterConnectionField(UserNode, extra_filter_meta={'exclude': 'password'})

    def resolve_user(self, info, id, **data):
        print(dir(info), 'dir info')
        print(info.field_asts, 'fields')
        print(len(info.field_asts), 'len fields')
        field = info.field_asts[0]
        fields = (f.name.value for f in field.selection_set.selections)
        print(data, 'data')
        print(fields, 'fields')
        user = User.objects.only(*fields).get(id=id)
        print(user, 'user')
        return user


schema = Schema(query=GlobalQuery)


# SelectionSet(
#     selections=[
#         Field(
#             alias=None,
#             name=Name(value='username'),
#             arguments=[],
#             directives=[],
#             selection_set=None
#         ),
#         Field(
#             alias=None,
#             name=Name(value='email'),
#             arguments=[],
#             directives=[],
#             selection_set=None)
#     ]
# )
