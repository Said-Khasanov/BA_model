from BA_model import BAmodel


if __name__ == '__main__':
    m = 5
    a = BAmodel(m)
    a.print_list()
    print('---\n')

    for i in range(1):
        a.add_vertex()

    a.print_list()
    print(f'v = {a.v_count} e = {a.e_count}')

    i = 5  # Вершина для теста
    print('d_i =', a.vertex_deg(i))
    print('S_i =', a.sum_deg_neighbors(i))
    print('alpha_i =', a.avg_deg_neighbors(i))
    print('p_i =', a.friendship_index(i))

    print('p =', a.p())
