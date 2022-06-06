def add_tuple(tuple_a=(), tuple_b=()):
    result = tuple(map(lamba i, j: i + j, tuple_a, tuple_b))
    print("the tuple after addition is: ")
    print(result)
