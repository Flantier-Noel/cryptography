from lorem_text import lorem

import random
random.text = lorem.words

from __main import*

N = 10
canvas_key = random.text(N)
canvas = Canvas.from_text(canvas_key)

print(canvas)

msg_int = [2, 7, 1, 8, 2, 8, 1]