from operator import attrgetter


class Thing:
    def __init__(self, name, size, points):
        self.name = name
        self.size = size
        self.points = points

    def __repr__(self):
        return "{" + self.name + ", " + str(self.size) + ", " + str(self.points) + "}"


stuff_list = [
    Thing("r", 3, 25),
    Thing("p", 2, 15),
    Thing("a", 2, 15),
    Thing("m", 2, 20),
    Thing("i", 1, 5),
    Thing("k", 1, 15),
    Thing("x", 3, 20),
    Thing("t", 1, 25),
    Thing("f", 1, 15),
    Thing("d", 1, 10),
    Thing("s", 2, 20),
    Thing("c", 2, 20),
]

inventory = [[0 for i in range(3)] for j in range(3)]
unused_points = sum([i.points for i in stuff_list])
score = 10
used_slots = 0

stuff_list.sort(key=lambda x: (-(x.points / x.size)))

for item in stuff_list:
    if used_slots + item.size <= 9:
        used_slots += item.size
        item_len = item.size
        for i in range(len(inventory)):
            for j in range(len(inventory[i])):
                if inventory[i][j] == 0 and item_len > 0:
                    inventory[i][j] = item.name
                    item_len -= 1
                    if item.size - item_len == 1:
                        score += item.points
                        unused_points = unused_points - item.points

    if used_slots == 9:
        for i in inventory:
            print(i)
        print("Итоговые очки выживания:", score - unused_points)

    else:
        continue
