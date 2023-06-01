from random import randint as rand # мы импортируем из библиотеки random метод randint и сокращаем его название до ranf

def randbool(r, mxr): # эта функция будет принимать на вход отсечку r и максимальное число и будет возвращать True, если сгенерированное число меньше или равно отсечки
# r - отсечка; mxr - ограничитель
    t = rand(0, mxr)
    return (t <= r)

def randcell(w, h):
    tw = rand(0, w - 1)
    th = rand(0, h - 1)
    return (th, tw)

# 0 - наверх, 1 - направо, 2 - вниз, 3 - налево
def randcell2(x, y): # так как в этой функции 4 параметра, то для питона на считается уже другой функцией, она будет генерировать воду в 
#в зависимости от положение первое клетки с водой (х и у) в пределах поля (w h)
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    t = rand(0, 3)
    dx, dy = moves[t][0], moves[t][1]
    return (x + dx, y + dy)