class Graph:
    """Простой граф"""

    def __init__(self, n=5):
        """
        Конструктор создаёт сильно связный граф из n вершин
        """
        self.vertex: list = [i for i in range(n)]
        self.v_count = n  # Кол-во вершин
        self.e_count = 0  # Кол-во рёбер

        self.edges = []
        for i in range(n):
            self.edges.append([i for i in range(n)])
            self.edges[i].remove(i)
            self.e_count += n-1

        self.e_count /= 2

    def add_vertex(self, edge: list):
        """
        Добавление вершины
        :param edge: список смежных вершин
        """
        x = self.vertex[-1] + 1

        self.vertex.append(x)
        self.v_count += 1

        self.edges.append(edge)
        for i in edge:
            self.edges[i].append(x)

        self.e_count += len(edge)

    def print_list(self):
        """
        Печать списка смежности
        """
        for i, j in enumerate(self.edges):
            print(f'v{i}: {j}')

