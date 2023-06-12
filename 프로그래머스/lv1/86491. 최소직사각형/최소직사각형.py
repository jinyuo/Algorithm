def solution(sizes):
    for size in sizes:
        if size[0] > size[1]:
            size[0], size[1] = size[1], size[0]
    w = max([size[0] for size in sizes])
    h = max([size[1] for size in sizes])
    return w * h