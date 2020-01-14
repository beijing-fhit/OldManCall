# 区分两个数组的不同
def compareArrays(a, b):
    common=[x for x in a if x in b] # 相同元素
    _a_diff=[y for y in a if y not in common]
    _b_diff=[z for z in b if z not in common]
    print(_a_diff,_b_diff)
    return _a_diff,_b_diff
