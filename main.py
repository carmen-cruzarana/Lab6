def encode_pass(old_pass):
        new_pass = ''
        for digit in old_pass:
            digit = int(digit)
            digit += 3
            new_pass += str(digit)
        return new_pass


def decode_pass(encoded_pass):
    orig_pass = ''
    for digit in encoded_pass:
        digit = int(digit)
        digit -= 3
        orig_pass += str(digit)
    return orig_pass

if __name__ == "__main__":
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')

        choice = int(input('Please enter an option: '))
        if choice == 1:
            original_pass = input('Please enter your password to encode: ')
            new_password = encode_pass(original_pass)
            print('Your password has been encoded and stored!\n')
        if choice == 2:
            decoded_pass = decode_pass(new_password)
            print(f'The encoded password is {new_password}, and the original password is {decoded_pass}.\n')
        if choice == 3:
            break

