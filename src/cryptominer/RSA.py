import itertools
import random

from .euler import Euler
from .factorization import Factorization
from .modmul_inverse import ModularMultiplicativeInverse
from .gcd import GreatestCommonDivisor

RSA_BLOCK_SIZE = 2


def batched(iterable, n):
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(itertools.islice(it, n)):
        yield batch


def get_code_from_letter(char: str) -> str:
    return str(10 + "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ".index(char))


def get_letter_from_code(code: str) -> str:
    return "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ "[int(code) - 10]


class KeypairRSA:
    def __init__(self, pq_size: int = 24) -> None:
        self.pq_size = pq_size

    def Generate(self):
        # 1
        p = random.randint(1 << self.pq_size, (1 << (self.pq_size + 1)) - 1)
        while len(Factorization(p).Dumb()) > 1:
            p = random.randint(1 << self.pq_size,
                               (1 << (self.pq_size + 1)) - 1)

        q = random.randint(1 << self.pq_size, (1 << (self.pq_size + 1)) - 1)
        while len(Factorization(p).Dumb()) > 1:
            q = random.randint(1 << self.pq_size,
                               (1 << (self.pq_size + 1)) - 1)

        mod = p*q

        # 2
        phi = Euler(mod).Euler()

        # 3
        exponent = 1 << self.pq_size+1
        while GreatestCommonDivisor(exponent, phi).Euclidean() != 1:
            exponent = random.randint(2, phi - 1)

        # 4
        d = ModularMultiplicativeInverse(exponent, phi).Knuth()

        public_key = (exponent, mod)
        private_key = (d, mod)

        return private_key, public_key


class EncodeRSA:
    def __init__(self, message: str, public_key, block_size: int = RSA_BLOCK_SIZE):
        self.message = message.strip().upper()
        self.exponent, self.mod = public_key
        self.block_size = block_size

    def Cipher(self) -> []:
        ciphered = []
        for block in batched(self.message, self.block_size):
            block_encoded = int(''.join(map(get_code_from_letter, block)))

            assert self.mod > block_encoded
            
            block_ciphered = str(pow(block_encoded, self.exponent, self.mod))

            ciphered.append(block_ciphered)
        return ciphered


class DecodeRSA:
    def __init__(self, message: str, private_key, block_size: int = RSA_BLOCK_SIZE):
        self.message = message
        self.d, self.mod = private_key
        self.block_size = block_size

    def Decipher(self) -> str:
        deciphered = ""
        for block in self.message:
            block_num = int(block)
            
            assert block_num < self.mod

            block_deciphered = pow(block_num, self.d, self.mod)

            decoded = ""
            while block_deciphered > 0:
                char = block_deciphered % 100
                decoded += get_letter_from_code(char)
                block_deciphered //= 100

            deciphered += decoded[::-1]
        return deciphered
