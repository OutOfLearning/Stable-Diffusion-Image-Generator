import re
def is_number_valid(number:str) ->bool:
    pattern = r"^(?:\+91|91|0)?[6-9]\d{9}$"
    result = re.match(pattern,number)
    return result is not None
is_number_valid(+916304886348)