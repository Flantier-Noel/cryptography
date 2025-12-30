import __cypher

def cypher(key_text, msg):
    cnv = __cypher.Canvas.from_text(key_text)
    return __cypher.encode_int(cnv, msg)