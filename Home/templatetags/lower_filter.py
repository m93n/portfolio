from django import template
  
register = template.Library()

@register.filter
def skill_name0(query, row):
    name = query[row*2].name
    return name

@register.filter
def skill_name1(query, row):
    try:
        name = query[(row*2)+1].name
    except:
        name = None
    return name

@register.filter
def skill_value0(query, row):
    value = query[row*2].value
    return value

@register.filter
def skill_value1(query, row):
    try:
        value = query[(row*2)+1].value
    except:
        name = None
    return value

@register.filter
def skill_duration0(query, row):
    duration = query[row*2].duration
    return duration

@register.filter
def skill_duration1(query, row):
    try:
        duration = query[(row*2)+1].duration
    except:
        name = None
    return duration
