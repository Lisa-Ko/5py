def convert_string(input_str):
    symbol = None
    len_of_series = 0
    result = ""
    for letter in input_str:
        if symbol and letter != symbol:
            result = result + f"{symbol}{len_of_series}"
            len_of_series = 1
        else:
            len_of_series += 1
        symbol = letter
    return result + f"{symbol}{len_of_series}" if symbol else ""
input_str = input()
print(convert_string(input_str))