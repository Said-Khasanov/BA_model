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
    print('d_i =', a.vertex_deg(1))
    print('S_i =', a.sum_deg_neighbors(1))
    print('alpha_i =', a.avg_deg_neighbors(1))
    print('p_i =', a.friendship_index(1))
    print('p =', a.p())
