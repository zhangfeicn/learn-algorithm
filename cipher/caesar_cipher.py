"""
Caesar cipher:

The Caesar cipher involves replacing each letter in a message with the letter
that is a certain number of letters after it in the alphabet
"""

_created = "2020-04-17"


class CaesarCipher:
    """
    Class for doing encryption and decryption using a Caesar cipher.

    Upper case and lower case is in the scope
    """
    def __init__(self, key):
        """
        Construct Caesar cipher using given integer key for rotation
        """
        encoder = [None] * 52
        decoder = [None] * 52
        # process the upper case character
        for i in range(26):
            encoder[i] = chr((i + key) % 26 + ord('A'))
            decoder[i] = chr((i - key) % 26 + ord('A'))
        # process the lower case character
        for i in range(26):
            encoder[i+26] = chr((i + key) % 26 + ord('a'))
            decoder[i+26] = chr((i - key) % 26 + ord('a'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message: str):
        """
        Return string representing encripted message
        """
        return self._transform(message, self._forward)

    def decrypt(self, message: str):
        """
        Return decrypted message given encrypted secret
        """
        return self._transform(message, self._backward)

    def _transform(self, message: str, code: str):
        """
        Utility to perform transformation based on given code string
        """
        results = ''
        for c in message:
            if not c.isalpha():
                results += c
            elif c.isupper():
                j = ord(c) - ord('A')
                results += code[j]
            elif c.islower():
                j = ord(c) - ord('a') + 26
                results += code[j]
        return results


def brute_force(message):
    key = 1
    result = ""
    while key < 26:
        cipher = CaesarCipher(key)
        answer = cipher.decrypt(message)
        print(f"Key: {key}\t| Message: {answer}")
        result = ""
        key += 1


def _main():
    print("Caesar Cipher Demonstration:")
    cipher = CaesarCipher(4)
    message = "Microsoft;Corporation."
    print('Original:', message)
    coded = cipher.encrypt(message)
    print('Encoded:', coded)
    answer = cipher.decrypt(coded)
    print('Decoded:', answer)
    print('Brute Force:')
    brute_force(coded)


if __name__ == "__main__":
    _main()
