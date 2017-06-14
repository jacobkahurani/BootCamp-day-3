def words(s):
    w = s.split()
    a = []
    for i in w:
        a.append((i,w.count(i)))
    b = [i for i in set(a)]
    return dict(b)
    