from utils import randbool 
from utils import randcell
from utils import randcell2

# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд-шоп
# 5 - огонь

CELL_TYPES = "🟩🌲🌊🏥🏬🔥"
TREE_BONUS = 100
UPGRADE_COST = 5000
LIFE_COST = 10000

class Map:
    
    def __init__(self, w, h): # инициализатор для нашей карты
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)] # сами клеточки, h - количество рядов, и в каждом ряде будет w клеточек
        self.generate_forest(5, 10)
        self.generate_river(10)
        self.generate_river(10)
        self.generate_upgrade_shop()
        self.generate_hospital()

    def check_bounds (self, x, y): # проверяет, принадлежит ли клеточка с такими то координатами нашему полю
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True

    def print_map(self, helico, clouds): # функция, которая будет выводить нашу карту
        print("⬛" * (self.w + 2))
        for ri in range(self.h): # row на каждом шаге будет принимать очередное значение из списка cells, то есть значение ряда
            print("⬛", end='')
            for ci in range(self.w): # этим циклом мы в каждом ряду перебираем клеточку и будем её выводить
                cells = self.cells[ri][ci]
                if (helico.x == ri and helico.y == ci):
                    print("🚁", end='')
                elif (cells >= 0 and cells < len(CELL_TYPES)):
                    print(CELL_TYPES[cells], end='')
                if (clouds.cells[ri][ci] == 1):
                    print("X", end='')
                elif (clouds.cells[ri][ci] == 2):
                    print("X", end='')
            print("⬛")
        print("⬛" * (self.w + 2))

    def generate_river(self, l):# функция которая будет генерировать изначальное положение рек
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.check_bounds(rx2, ry2)):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1
    def generate_forest(self, r, mxr):# функция которая будет генерировать лес  
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1
    def generate_tree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 1
    
    def generate_upgrade_shop(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4

    def generate_hospital(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 4:
            self.cells[cx][cy] = 3
        else:
            self.generate_hospital()

    def add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5
    def update_fires(self): #будет убирать те огни, которые сгорели и добавлять новые
        for ri in range(self.h):
            for ci in range(self.w):
                cells = self.cells[ri][ci]
                if cells == 5:
                    self.cells[ri][ci] = 0
        for i in range(10): #может появиться до 5ти огней и только в тех клеточках, где есть дерево
            self.add_fire()

    def process_helicopter(self, helico, clouds):
        c = self.cells[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]
        if (c == 2):
            helico.tank = helico.mxtank
        if (c == 5 and helico.tank > 0):
            helico.tank -= 1
            helico.score += TREE_BONUS
            self.cells[helico.x][helico.y] = 1
        if (c == 4 and helico.score >= UPGRADE_COST):
            helico.mxtank += 1
            helico.score -= UPGRADE_COST
        if (c == 4 and helico.score >= LIFE_COST):
            helico.lives += 1000
            helico.score -= LIFE_COST
        if (d == 2):
            helico.lives -= 1
            if (helico.lives == 0):
                helico.game_over()
    

