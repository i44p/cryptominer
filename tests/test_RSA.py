import cryptominer
import pytest

from helpers import *


def test_RSA():
    message = 'ИВАН ГОРЫНЫЧ'
    for _ in range(10):
        public_key, private_key = cryptominer.KeypairRSA(pq_size=8).Generate()
        
        # public_key, private_key = ((158413, 428786), (158581, 428786))
        
        encoded = cryptominer.EncodeRSA(message, public_key).Cipher()
        decoded = cryptominer.DecodeRSA(encoded, private_key).Decipher()
        
        assert message == decoded
