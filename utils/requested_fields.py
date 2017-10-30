
def requested_fields(info):
    field = info.field_asts[0]
#     print(field, 'field', end='\n\n\n')
#     print(field.selection_set, 'selection set', end='\n\n')
    fields = {}
    for f in field.selection_set.selections:
        name = f.name.value
        print(name, 'name')
        subfields = []
        if f.selection_set:
            for sub_field in f.selection_set.selections:
                print(sub_field.name.value, 'j')
                subfields.append(f'{name}__{sub_field.name.value}')
        fields[name] = subfields
    print(fields, 'requested fields', end='\n\n')
    return fields
#     return tuple((f.name.value for f in field.selection_set.selections))
