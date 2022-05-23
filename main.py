from logging import INFO
from multiprocessing import Pool, log_to_stderr
from time import time

import matplotlib.pyplot as plt

from BA_model import BAmodel


logger = log_to_stderr()
logger.setLevel(INFO)

# Параметры
m = 5  # Кол-во связей с новой вершиной
n = 100000  # Кол-во вершин в графе
n_g = 100  # Кол-во графов
h = 250  # Шаг
x = [i for i in range(h, n_g * h + 1, h)]  # Знач. координат на оси X
div = float(len(x))  # Делитель для среднего знач.
v_i = [5, 50, 100]  # Тестируемые вершины
n_v_i = len(v_i)  # Кол-во тестируемых вершин

# Списки для хранения свойств графов
d_i = [[0 for _ in range(n_g)] for _ in range(n_v_i)]
s_i = [[0 for _ in range(n_g)] for _ in range(n_v_i)]
alpha_i = [[0 for _ in range(n_g)] for _ in range(n_v_i)]
beta_i = [[0 for _ in range(n_g)] for _ in range(n_v_i)]
p_f = [0 for _ in range(n_g)]


def cycle(i):
    """
    Функция вычисления свойств и ср. значений
    """
    d_i_ = [i for i in range(n_v_i)]
    s_i_ = [i for i in range(n_v_i)]
    alpha_i_ = [i for i in range(n_v_i)]
    beta_i_ = [i for i in range(n_v_i)]

    G = BAmodel(m)
    for j in range(1, n - 4):
        G.add_vertex()  # Новая вершина

        if j % h == 0:
            # Вычисление свойств
            for k in range(n_v_i):
                d_i_[k] += G.vertex_deg(v_i[k])
                s_i_[k] += G.sum_deg_neighbors(v_i[k])
                alpha_i_[k] += s_i_[k] / d_i_[k]
                beta_i_[k] += alpha_i_[k] / d_i_[k]

    # Вычисление средних значений
    for k in range(n_v_i):
        d_i_[k] /= div
        s_i_[k] /= div
        alpha_i_[k] /= div
        beta_i_[k] /= div

    return [d_i_, s_i_, alpha_i_, beta_i_, G.paradox()]


def plt_show():
    """
    Вывод графиков
    """
    pf = sum(p_f) / len(p_f)  # Парадокс дружбы
    print(f'Среднее значение p_f = {pf}')

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

    # Распределение цикла на процессы
    with Pool() as p:  # os.cpu_count()
        res = p.map(cycle, range(n_g))

    # Распаковка результата вычислений
    for i in range(n_g):
        for k in range(n_v_i):
            d_i[k][i] = res[i][0][k]
            s_i[k][i] = res[i][1][k]
            alpha_i[k][i] = res[i][2][k]
            beta_i[k][i] = res[i][3][k]
        p_f[i] = res[i][4]

    print('--- %s seconds ---' % (time() - start_time))

    plt_show()
