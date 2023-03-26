def remove_empty_tuples(my_list):
    my_list[:] = [el for el in my_list if el != ()]


def mean_tuples(my_tuple):
    new_tuple = ()
    for element in my_tuple:
        mean = (sum(element)/len(element),)
        new_tuple = new_tuple + mean

    return new_tuple


def has_alphanum(my_list):
    return [el for el in my_list if any([char.isdigit() for char in el])
            and any([char.isalpha() for char in el])]


def has_all_chars(first_str, second_str):
    first_set = set(first_str)
    second_set = set(second_str)

    return second_set.issubset(first_set)


def mutiply_matrix(first_matrix, second_matrix):
    result_matrix = []
    for i in range(len(first_matrix)):
        result_row = []

        for j in range(len(second_matrix[0])):
            element = 0

            for k in range(len(second_matrix)):
                element += first_matrix[i][k] * second_matrix[k][j]

            result_row.append(element)
            element = 0

        result_matrix.append(result_row)
        result_row = []

    return result_matrix


def inverse_list(my_list):
    for el in my_list[::-1]:
        yield el


def primes_list():
    value = 2
    prime_list = [2]

    while True:
        yield value

        while any(value % prime == 0 for prime in prime_list):
            value += 1

        prime_list.append(value)


def filter_odd(my_list):
    return list(filter(lambda el: (el % 2 == 0), my_list))


def apply(func, matrix):
    return list(map(func, matrix))


if __name__ == "__main__":
    # my_list = [(), (), (1, 2, 3), (2, 3)]
    # remove_empty_tuples(my_list)
    # print(my_list)

    # my_tuple = ((2, 3, 4), (3, 4, 5, 6), (2, 4), (4, 8, 9))
    # mean_tuple = mean_tuples(my_tuple)
    # print(my_tuple, mean_tuple)

    # my_list_str = ["asbd", "asn23", "asdj:dsd23", "123123", "asd:.,", "123,."]
    # filtered_list = has_alphanum(my_list_str)
    # print(filtered_list)

    # str1 = "asdasdasdasda"
    # str2 = "aaaaaaaaaaaaaaaadddddddddddd"
    # str3 = "aaabb"
    # print(has_all_chars(str1, str2))
    # print(has_all_chars(str1, str3))

    # X = [[12, 7, 3],
    #      [4, 5, 6],
    #      [7, 8, 9]]
    # Y = [[5, 8, 1, 2],
    #      [6, 7, 3, 0],
    #      [4, 5, 9, 1]]
    # Z = mutiply_matrix(X, Y)
    # print(Z)

    # my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # [print(value) for value in inverse_list(my_list)]

    # fix error at end
    # [print(value) for value in primes_list() if value <= 997]

    # value = 0
    # primes = primes_list()
    # while value < 997:
    #   value = next(primes)
    #   print(value)

    # print(filter_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]
    print(apply(sum, X))
