# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.
with open('file_encode.txt', 'r') as file:
    decoded_string = file.read()


def encode(decoded_string):
    encoded_string = ''
    count = 1
    var = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == var:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + var
            var = decoded_string[i]
            count = 1
            encoded_string = encoded_string + str(count) + var

    return encoded_string


def decode(encoded_string):
    decoded_string = ''
    var_amount = ''
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            var_amount += encoded_string[i]
        else:
            decoded_string += encoded_string[i] * int(var_amount)
        var_amount = ''

    return decoded_string

with open('file_decode.txt', 'w') as file:
    encoded_string = encode(decoded_string)
    file.write(encoded_string)

print(decoded_string)
print(encode(decoded_string))

