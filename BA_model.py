from random import choices

from graph import Graph


class BAmodel(Graph):
    """Модель Барабаши-Альберт"""

    def __init__(self, m=5):
        """
        :param m: Кол-во связей с новой вершиной, default = 5
        """
        super().__init__()
        self.m = m

    def add_vertex(self, edge: list = None):
        """Создание новой вершины"""
        if edge is None:
            edge = []

            P_n = (self.e_count + self.m) * 2
            weights = [len(i) / P_n for i in self.edges]

            while len(set(edge)) != self.m:  # Исключение повоторений
                edge = choices(self.vertex, weights, k=self.m)

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
        sum = 0
        for j in self.edges:
            if i in j:
                sum += len(j)

        return sum


    def avg_deg_neighbors(self, i):
        """
        Средняя степень соседей (alpha_i)
        :param i: вершина
        """
        return self.sum_deg_neighbors(i) / self.vertex_deg(i)

    def friendship_index(self, i):
        """
        Индекс дружбы (beta_i)
        :param i: вершина
        :return:
        """
        return self.avg_deg_neighbors(i) / self.vertex_deg(i)

    def paradox(self):
        """
        Парадокс дружбы (p_f)
        """
        return sum([self.friendship_index(i) for i in self.vertex]) / len(self.vertex)
