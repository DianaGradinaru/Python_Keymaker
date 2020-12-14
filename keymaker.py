from string import ascii_lowercase as alphabet


def shift_characters(word, shift):
    result = ""
    for i in range(len(word)):
        char = word[i]
        result += chr((ord(char) + shift - 97) % 26 + 97)
    return result


def pad_up_to(word, shift, n):
    new_word = word
    while len(new_word) < n:
        word = shift_characters(word, shift)
        new_word += word
    return new_word[:n]


def abc_mirror(word):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    omega = alpha[::-1]
    result = ""
    for letter in word:
        result += omega[alpha.index(letter)]
    return result


def create_matrix(word1, word2):
    values = []
    for char in word2:
        for index, letter in enumerate(alphabet):
            if char == letter:
                values.append(shift_characters(word1, index))
    return values


def zig_zag_concatenate(matrix):
    result = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix)):
            result.append(matrix[j][i])
    slicey = len(matrix)
    result = (
        result[:slicey]
        + list(reversed(result[slicey : (slicey * 2)]))
        + result[(slicey * 2) :]
    )
    return "".join(result)


def rotate_right(word, n):
    return word[-n:] + word[:-n]


def get_square_index_chars(word):
    result = []
    for i in range(len(word)):
        if (i ** 0.5) == int(i ** 0.5):
            result.append(word[i])
    return "".join(result)


def remove_odd_blocks(word, block_length):
    lst = [word[i : i + block_length] for i in range(0, len(word), block_length)]
    result = []
    for i in range(len(lst)):
        if i % 2 == 0:
            result.append(lst[i])
    return "".join(result)


def reduce_to_fixed(word, n):
    cutoff = n // 3
    new_word = word[:n]
    new_word = new_word[(cutoff):] + new_word[:cutoff]
    return new_word[::-1]


def hash_it(word):

    padded = pad_up_to(word, 15, 19)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    rotated = rotate_right(elongated, 3000003)
    cherry_picked = get_square_index_chars(rotated)
    halved = remove_odd_blocks(cherry_picked, 3)
    key = reduce_to_fixed(halved, 6)
    return key


if __name__ == "__main__":
    name = input("Enter your name! ").lower()
    print(f"Your key: {hash_it(name)}")
