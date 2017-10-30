
def requested_fields(info):
    field = info.field_asts[0]
    return tuple((f.name.value for f in field.selection_set.selections))
