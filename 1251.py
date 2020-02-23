def _map_to_dict(string):
    _dict = {}
    for char in string:
        if not str(ord(char)) in _dict:
            _dict[str(ord(char))] = 1
            continue
        _dict[str(ord(char))] += 1
    # sorting by value
    return _sort_by_value({k: v for k, v in sorted(_dict.items(), key=lambda item: item[1])})

def _sort_by_value(_dict):
    _list = list(_dict.items())
    n = len(_list)
    for i in range(n):
        for j in range(n):
            if _list[i][1] == _list[j][1] and int(_list[i][0]) > int(_list[j][0]):            
                aux = _list[i]
                _list[i] = _list[j]
                _list[j] = aux
    return _list

if __name__ == '__main__':

    while True:
        try:
            inline = _map_to_dict(input())
            # Compression                        
            [print ('{} {}'.format(tupla[0], tupla[1])) for tupla in inline]
            print()
        except EOFError:
            break