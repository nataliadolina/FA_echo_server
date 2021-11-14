def to_type(type, el):
    if type == "str":
        return str(el)
    if type == "int":
        return int(el)
    return el


def encode(string):
    return str.encode(string, "UTF-8")


def decode(bytes):
    return bytes.decode()
