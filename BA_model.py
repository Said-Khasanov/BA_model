from random import choices

from graph import Graph


class BAmodel(Graph):
    """Модель Барабаши-Альберта"""

    def __init__(self, m=5):
        """
        :param m: Кол-во связей с новой вершиной, default = 5
        """
        super().__init__()
        self.m = m
        # self.t = self.m

    def add_vertex(self, edge: list = None):
        """Создание новой вершины"""
        if edge is None:
            edge = []

            # self.t += 1

            P_n = (self.e_count + self.m) * 2
            weights = [len(i) / P_n for i in self.edges]

            while True:
                edge = choices(self.vertex, weights, k=self.m)
                # Исключение повоторений
                if len(set(edge)) == self.m:
                    break

        super().add_vertex(edge)

    # Свойства графа
    def vertex_deg(self, i):
        """
        Степень вершины (d_i)
        :param i: вершина
        """
        return len(self.edges[i])

    def sum_deg_neighbors(self, i):
        """
        Сумма степеней соседей (S_i)
        :param i: вершина
        """
        return sum(
            [len(i) for i in
             self.edges[:i] + self.edges[i + 1:]
             ]
        )

    def avg_deg_neighbors(self, i):
        """
        Средняя степень соседей (alpha_i)
        :param i: вершина
        """
        return self.sum_deg_neighbors(i) / self.vertex_deg(i)

    def friendship_index(self, i):
        """
        Индекс дружбы (p_i)
        :param i: вершина
        :return:
        """
        return self.avg_deg_neighbors(i) / self.vertex_deg(i)

    def p(self):
        """
        Парадокс дружбы
        """
        return sum([self.friendship_index(i) for i in self.vertex]) / len(self.vertex)
