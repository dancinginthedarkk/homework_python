class Matrix():
    def __init__(self, m):
        n = 1
        for i in range(1, len(m)):
            if len(m[0]) == len(m[i]):
                n += 1
        if n == len(m):
            self.m = m
        else:
            print("Невозможно решить")
        self.m = m
    def transpose(self):
        new_m = [[] for _ in self.m [0]]
        for i in range(len(self.m[0])):
            for j in range(len(self.m)):
                new_m[i].append(self.m[j][i])
        self.m = new_m
        return self.m

m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m1.transpose())