def generate_sequence(size):
    list = [0, 1]
    if size < 3:
        return list[0: size]
    for index in range(2, size):
        list.append(list[index - 2] + list[index - 1])
    return list