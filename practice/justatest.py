def extsort(ext_list):
    return sorted(ext_list, key=lambda x: x.split(".")[1])


def test1(n):
    return [(x, y, z) for x in range(1, n) for y in range(x, n) for z in range(y, n) if x*x + y*y == z*z]

if __name__ == "__main__":
    print(test1(25))
