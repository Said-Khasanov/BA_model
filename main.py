from time import time

import matplotlib.pyplot as plt
import multiprocessing

from BA_model import BAmodel


def part1():
    m = 5

    graph = BAmodel(m)
    graph.print_list()
    print('---\n')

    for i in range(10000):
        graph.add_vertex()

    # a.print_list()
    print(f'v = {graph.v_count} e = {graph.e_count}')

    i = 5  # Вершина для теста
    print('d_i =', graph.vertex_deg(i))
    print('S_i =', graph.sum_deg_neighbors(i))
    print('alpha_i =', graph.avg_deg_neighbors(i))
    print('beta_i =', graph.friendship_index(i))

    print('p_f =', graph.paradox())


def part2():
    # Параметры
    m = 5  # Кол-во связей с новой вершиной
    n = 100000  # Кол-во вершин в графе
    n_g = 100  # Кол-во графов
    h = 250  # Шаг
    x = [i for i in range(h, n_g*h+1, h)]  # Знач. координат на оси X
    div = len(x)  # Делитель для среднего знач.
    v_i = [5, 50, 100]  # Тестируемые вершины

    d_i = [[0 for _ in range(n_g)] for _ in range(3)]
    s_i = [[0 for _ in range(n_g)] for _ in range(3)]
    alpha_i = [[0 for _ in range(n_g)] for _ in range(3)]
    beta_i = [[0 for _ in range(n_g)] for _ in range(3)]
    p_f = [0 for _ in range(n_g)]

    start_time = time()

    for i in range(n_g):
        G = BAmodel(m)
        for j in range(1, n - 4):
            G.add_vertex()  # Новая вершина

            if j % h == 0:
                # Вычисление свойств
                for k in range(3):
                    d_i[k][i] += G.vertex_deg(v_i[k])
                    s_i[k][i] += G.sum_deg_neighbors(v_i[k])
                    alpha_i[k][i] += G.avg_deg_neighbors(v_i[k])
                    beta_i[k][i] += G.friendship_index(v_i[k])

        # Вычисление средних значений
        for k in range(3):
            d_i[k][i] /= div
            s_i[k][i] /= div
            alpha_i[k][i] /= div
            beta_i[k][i] /= div

        p_f[i] += G.paradox()

    p_f = sum(p_f) / len(p_f)  # Парадокс дружбы
    print('--- %s seconds ---' % (time() - start_time))
    print(f'Среднее значение p_f = {p_f}')

    # Построение графиков
    plt.subplot(221)
    plt.title('Степень вершины')
    plt.xlabel('t')
    plt.ylabel('d_i')
    plt.grid()
    plt.plot(x, d_i[0], '.-r', label='i=5')
    plt.plot(x, d_i[1], '.-y', label='i=50')
    plt.plot(x, d_i[2], '.-b', label='i=100')
    plt.legend(fontsize=10, shadow=True, framealpha=1)

    plt.subplot(222)
    plt.title('Сумма степеней соседей')
    plt.xlabel('t')
    plt.ylabel('s_i')
    plt.grid()
    plt.plot(x, s_i[0], '.-r', label='i=5')
    plt.plot(x, s_i[1], '.-y', label='i=50')
    plt.plot(x, s_i[2], '.-b', label='i=100')
    plt.legend(fontsize=10, shadow=True, framealpha=1)

    plt.subplot(223)
    plt.title('Средняя степень соседей')
    plt.xlabel('t')
    plt.ylabel('alpha_i')
    plt.grid()
    plt.plot(x, alpha_i[0], '.-r', label='i=5')
    plt.plot(x, alpha_i[1], '.-y', label='i=50')
    plt.plot(x, alpha_i[2], '.-b', label='i=100')
    plt.legend(fontsize=10, shadow=True, framealpha=1)

    plt.subplot(224)
    plt.title('Индекс дружбы')
    plt.xlabel('t')
    plt.ylabel('alpha_i')
    plt.grid()
    plt.plot(x, beta_i[0], '.-r', label='i=5')
    plt.plot(x, beta_i[1], '.-y', label='i=50')
    plt.plot(x, beta_i[2], '.-b', label='i=100')
    plt.legend(fontsize=10, shadow=True, framealpha=1)
    plt.show()  # Вывод


if __name__ == '__main__':
    part2()
