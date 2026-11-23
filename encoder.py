
complete_alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode(number):
    result = []

    if number == 0:
        result.append(complete_alphabet[0])
    else:
        while number > 0:
            remainder = number % 62 
            char = complete_alphabet[remainder]
            result.append(char)
            number = number // 62 

    string_result = "".join(result[::-1]) # to put in reverse / left right order

    return string_result


def decode(code):
    total = 0

    for char in code:
        value = complete_alphabet.index(char)
        total = total * 62 + value
        
    return total




