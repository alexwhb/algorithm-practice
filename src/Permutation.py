__author__ = 'Winston'


def permutations(string, step=0):
    if step == len(string):
        print ''.join(string)

    for i in range(step, len(string)):
        string_copy = [character for character in string]
        string_copy[step], string_copy[i] = reverse_char(string_copy[step], string_copy[i])
        permutations(string_copy, step + 1)


def reverse_char(a, b):
    return b, a


if __name__ == '__main__':
    permutations("abc")
