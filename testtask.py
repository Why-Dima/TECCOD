def unique_elements(lis):
    lis = set(lis)
    return list(lis)

print(unique_elements([1,2,3,1,5,6,7,1]))

def min_and_max_num(min, max):
    res = []
    for i in range(min, max+1):
        for k in range(2, i):
            if i % k == 0:
                break
        else:
            res.append(i)
    return res

print(min_and_max_num(1, 17))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coor(self):
        return (self.x, self.y)

    def distance(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return (dx**2 + dy**2) ** 0.5

    def change_coor(self, x, y):
        self.x = x
        self.y = y

g = Point(2, 3)
print(g.get_coor())
g2 = Point(1, 4)
print(g.distance(g2))
g.change_coor(3, 7)
print(g.get_coor())

def sort_list(lis):
    for i in range(len(lis)):
        cur_in = lis[i]
        for j in range(i+1, len(lis)):
            if len(cur_in) > len(lis[j]):
                lis[i], lis[j], cur_in = lis[j], cur_in, lis[j]            
    return f'Сортированный список - {lis}', '\n', f'Обратная сортировка - {list(reversed(lis))}'

print(sort_list(['qweqw', 'dw', 'aaaaaa', 'aa', 'sss', 'fdsfsdafasfs', 'fdsafd', 's']))

