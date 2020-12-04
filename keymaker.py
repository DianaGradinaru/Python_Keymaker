def shift_characters(word, shift):
    result = ""
    for i in range(len(word)):
        char = word[i]
        result += chr((ord(char) + shift - 97) % 26 + 97)
    return result


print(shift_characters("abby", 5))


def pad_up_to(word, shift, n):
    new_word = word
    while len(new_word) < n:
        word = shift_characters(word, shift)
        new_word += word
    return new_word[0:n]


print(pad_up_to("abb", 5, 11))


def abc_mirror(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    omega = alphabet[::-1]
    result = ""
    for letter in word:
        result += omega[alphabet.index(letter)]
    return result


print(abc_mirror("abcd"))


def create_matrix(word1, word2):
    """
    >>> create_matrix('mamas', 'papas')
    ['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk']
    """
    pass


def zig_zag_concatenate(matrix):
    """
    >>> zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl'])
    'adgjkhebcfil'
    """
    pass


def rotate_right(word, n):
    return word[-n:] + word[:-n]


print(rotate_right("abcdefgh", 3))


def get_square_index_chars(word):
    result = []
    for i in range(len(word)):
        if (i ** 0.5) == int(i ** 0.5):
            result.append(word[i])
    return "".join(result)

print(get_square_index_chars("abcdefghijklm"))



def remove_odd_blocks(word, block_length):
    lst =  [word[i:i+block_length] for i in range(0, len(word), block_length)]
    result =[]
    for i in range(len(lst)):
        if i % 2 == 0:
            result.append(lst[i])
    return "".join(result)
        
print(remove_odd_blocks('abcdefghijklm', 3))



def reduce_to_fixed(word, n):
    cutoff = n // 3
    new_word = word[:n]
    new_word = new_word[(cutoff):]+new_word[:cutoff]
    return new_word[::-1]

print(reduce_to_fixed('abcdefghijklm', 6))


# def hash_it(word):
#     """
#     >>> hash_it('morpheus')
#     'trowdo'
#     """
#     padded = pad_up_to(word, 15, 19)
#     elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
#     rotated = rotate_right(elongated, 3000003)
#     cherry_picked = get_square_index_chars(rotated)
#     halved = remove_odd_blocks(cherry_picked, 3)
#     key = reduce_to_fixed(halved, 6)
#     return key


# if __name__ == "__main__":
#     name = input("Enter your name! ").lower()
#     print(f"Your key: {hash_it(name)}")
