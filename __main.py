import __cypher
import __langage

def cypher(key_text, msg, language:__langage.Langage):
    cnv = __cypher.Canvas.from_text(key_text)
    int_code = __cypher.encode_int(cnv, msg)

    int_code_normalized = []
    for val in int_code :
        val0, val1 = val//10, val%10
        int_code_normalized.append(val0) ; int_code_normalized.append(val1)

    str_code = language.paragraph(int_code_normalized)

    return str_code