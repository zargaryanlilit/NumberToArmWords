from mapping import mapping


def num_to_word(num: str) -> str:
    """"""
    num_len = len(num)
    if num_len == 1:
        if num[0] != '0':
            word = mapping[num_len][num]
        else:
            word = ''
    elif num_len == 2:
        if num[0] != '0':
            word = mapping[num_len][str(int(num[0])*10)] + num_to_word(num[1:])
        else:
            word = num_to_word(num[1:])
    elif num_len == 3:
        if num[0] != '0':
            word = num_to_word(num[:1]) + ' ' + mapping[num_len][str(100)] + ' ' + num_to_word(
                (num[1:]))
        else:
            word = num_to_word((num[1:]))
    elif 4 <= num_len <= 102:
        thous_num = list(mapping[num_len].keys())[0]
        thous_value = list(mapping[num_len].values())[0]
        i = num_len - len(thous_num) + 1
        if num[0] != '0':
            word = num_to_word(num[:i]) + ' ' + thous_value + ' ' + num_to_word(num[i:])
        else:
            word = num_to_word(num[:i]) + num_to_word(num[i:])
    else:
        raise Exception('Too big number')
    return word
