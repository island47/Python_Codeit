def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        # some_list에서 value를 찾으면 True를 리턴
        if some_list[i] == value:
            return True
        i = i + 1