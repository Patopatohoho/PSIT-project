"""Training_EuclideanDistance"""
def distance(alls, res):
    """input: times(int), point(x y)(str)
        output: summary of distance two point float(str)"""
    for i in xrange(alls):
        x_2, y_2 = map(int, raw_input().split())
        if i == 0:
            x_1, y_1 = x_2, y_2
        res += ((x_1-x_2)**2+(y_1-y_2)**2)**0.5
        x_1, y_1 = x_2, y_2
    print '%.2f' % res
distance(input(), 0)

