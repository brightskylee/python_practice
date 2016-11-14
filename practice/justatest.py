def extsort(ext_list):
    return sorted(ext_list, key=lambda x: x.split(".")[1])


def test1(n):
    return [(x, y, z) for x in range(1, n) for y in range(x, n) for z in range(y, n) if x*x + y*y == z*z]


def similar(list_of_words):
    dict_list = {}
    for word in list_of_words:
        temp = "".join(sorted(word))
        word_list = dict_list.get(temp, [])
        word_list.append(word)
        dict_list[temp] = word_list

    return dict_list.values()

if __name__ == "__main__":
    dict1 = {"x": 1, "y": 2}
    print(dict1.get("c"))
    print(dict1)
