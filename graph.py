class Graph:
    """Простой граф"""
    vertex: list = [i for i in range(5)]
    edges = [
        [1, 2, 3, 4, 5],
        [0, 2, 3, 4, 5],
        [0, 1, 3, 4, 5],
        [0, 1, 2, 4, 5],
        [0, 1, 2, 3, 5],
    ]
    v_count = 3
    e_count = 3

    def add_vertex(self, edge: list):
        """ Добавление вершины
        :param edge: список смежных вершин
        :return:
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
        :return:
        """
        for i, j in enumerate(self.edges):
            print(f'v{i}: {j}')
