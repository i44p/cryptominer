import cryptominer
import pytest

from helpers import *


def test_RSA():
    message = 'ЗМЕЙ ГОРЫНЫЧ'
    for _ in range(1):
        public_key, private_key = cryptominer.KeypairRSA(pq_size=24).Generate()

        # max encode size = (1<<pq_size)**2
        # public_key, private_key = ((55847289989431, 948425708075781), (394439629876615, 948425708075781))

        encoded = cryptominer.EncodeRSA(message, public_key).Cipher()
        decoded = cryptominer.DecodeRSA(encoded, private_key).Decipher()

        assert message == decoded
