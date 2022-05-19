from BA_model import BAmodel


if __name__ == '__main__':
    m = 2
    a = BAmodel(m)
    a.print_list()
    print('---\n')

    for i in range(10000):
        a.add_vertex()

    a.print_list()
    print(f'v = {a.v_count} e = {a.e_count}')
    print(a.vertex_deg(1))
    print(a.sum_deg_neighbors(1))
    print(a.avg_deg_neighbors(1))
    print(a.friendship_index(1))
    print(a.p())
