import random


class Field(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

        # 根据x y的值生成矩阵
        self.matrix = []
        for i in range(y):
            self.matrix.append(["0"] * x)

        # 起点和终点
        self.start = [0, 0]
        self.end = [0, 0]

        # 标点属性
        self.required = []
        self.removed = []

    def __str__(self):
        field_map = ""
        for i in range(len(self.matrix)):
            field_map = field_map + "\r\n" + "  ".join(self.matrix[i])
        return field_map

    # 随机生成序列
    def random_path(self):
        # 先把所有的坐标点存到一个list里
        coordinates = []
        for x in range(self.x):
            for y in range(self.y):
                coordinates.append([x, y])
        # 打乱一下顺序
        random.shuffle(coordinates)

        # 随机一个起点
        self.start = self.random_pick()
        self.end = self.random_pick()

        # 起点和终点不能在一起
        while self.start == self.end:
            self.end = self.random_pick()

        self.required.append(self.start)
        self.required.append(self.end)

        # 坐标点要么必要，要么删除
        while len(self.required) + len(self.removed) < self.x * self.y:
            for coordinate in coordinates:
                # 只处理不在required和removed里的坐标
                if coordinate not in self.required and coordinate not in self.removed:
                    # 试着删除这个坐标
                    self.removed.append(coordinate)
                    # 如果find_path走不通，说明这个坐标必须存在
                    if self.find_path() is False:
                        self.required.append(coordinate)
                        self.removed.remove(coordinate)

        # 把required的坐标替换成 “*”
        for r in self.required:
            self.matrix[r[1]][r[0]] = "*"

        # 标记起点和终点
        self.matrix[self.start[1]][self.start[0]] = "S"
        self.matrix[self.end[1]][self.end[0]] = "E"

    # 随机取一个坐标点
    def random_pick(self):
        x = random.randrange(self.x)
        y = random.randrange(self.y)
        return [x, y]

    # 检测道路是否通行
    def find_path(self):

        marked = []
        temp = [self.start]

        while len(temp) > 0:
            marked = marked + temp
            temp = []
            # 获取坐标相邻点
            for coordinate in marked:
                neighbour = self.find_neighbour(coordinate)
                # 标记相邻点
                for neighbour_coordinate in neighbour:
                    # 如果是终点，返回True
                    if neighbour_coordinate == self.end:
                        return True
                    if neighbour_coordinate not in self.removed and neighbour_coordinate not in marked:
                        temp.append(neighbour_coordinate)
                        # 如果temp没有值，说明没有下一个可以走的点了，结束while循环
        return False

    # 返回相邻的坐标点
    def find_neighbour(self, coordinate):
        neighbour = []
        if coordinate[0] > 0:
            neighbour.append([coordinate[0] - 1, coordinate[1]])
        if coordinate[0] < self.x - 1:
            neighbour.append([coordinate[0] + 1, coordinate[1]])
        if coordinate[1] > 0:
            neighbour.append([coordinate[0], coordinate[1] - 1])
        if coordinate[1] < self.y - 1:
            neighbour.append([coordinate[0], coordinate[1] + 1])
        return neighbour


if __name__ == '__main__':
    playground = Field(10, 10)
    playground.random_path()
    print(playground)
