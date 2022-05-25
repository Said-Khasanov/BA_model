from time import time

import matplotlib.pyplot as plt

from BA_model import BAmodel


# Параметры
m = 5  # Кол-во связей с новой вершиной
n = 10000  # Кол-во вершин в графе
n_g = 100  # Кол-во графов
h = 250  # Шаг
n_d = int(n / h)  # Кол-во точек
x = [i for i in range(h, n + 1, h)]  # Знач. координат на оси X
v_i = [5, 50, 100]  # Тестируемые вершины
n_v_i = len(v_i)  # Кол-во тестируемых вершин
G = [BAmodel(m) for _ in range(n_g)]  # Список графов

# Списки для хранения свойств графов
d_i = [[0 for _ in range(n_d)] for _ in range(n_v_i)]
s_i = [[0 for _ in range(n_d)] for _ in range(n_v_i)]
alpha_i = [[0 for _ in range(n_d)] for _ in range(n_v_i)]
beta_i = [[0 for _ in range(n_d)] for _ in range(n_v_i)]
p_f = 0  # Итоговое значение парадокса


def calc():
    global p_f
    for i in range(6, n+1):
        print(i*100/n)
        n_d_i = int(i * n_d / n) - 1  # Индекс точки
        for j in range(n_g):
            G[j].add_vertex()
            if i % h == 0:
                # Вычисление свойств
                for k in range(n_v_i):
                    d_i_ = G[j].vertex_deg(v_i[k])
                    s_i_ = G[j].sum_deg_neighbors(v_i[k])
                    alpha_i_ = s_i_ / d_i_
                    # Сумма по каждому i в точках из x
                    d_i[k][n_d_i] += d_i_
                    s_i[k][n_d_i] += s_i_
                    alpha_i[k][n_d_i] += alpha_i_
                    beta_i[k][n_d_i] += alpha_i_ / d_i_
                p_f += G[j].paradox()

        if i % h == 0:
            # Вычисление средних значений
            for k in range(n_v_i):
                d_i[k][n_d_i] /= n_g
                s_i[k][n_d_i] /= n_g
                alpha_i[k][n_d_i] /= n_g
                beta_i[k][n_d_i] /= n_g


def plt_show():
    """
    Вывод графиков
    """
    global p_f
    p_f = p_f / (n_d * n_g)  # Парадокс дружбы
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
    start_time = time()

    calc()

    print('--- %s seconds ---' % (time() - start_time))
    plt_show()
