import hashlib
import requests

import sys
import json

def proof_of_work(block):
    """
    Simple Proof of Work Algorithm
    Stringify the block and look for a proof.
    Loop through possibilities, checking each one against `valid_proof`
    in an effort to find a number that is a valid proof
    :return: A valid proof for the provided block
    """
    # TODO: Make this work for miner
    # One line version of code to stringify a block
    last_proof = json.dumps(block, sort_keys=True)
    proof = 0
    while valid_proof(last_proof, proof) is False:
        proof += 1

    return proof


    
def valid_proof(last_proof, proof):
    """
    Validates the Proof:  Does hash(last_proof, proof) contain 6
    leading zeroes?  Return true if the proof is valid
    :param last_proof: <string> The stringified block to use to
    check in combination with `proof`
    :param proof: <int?> The value that when combined with the
    stringified previous block results in a hash that has the
    correct number of leading zeroes.
    :return: True if the resulting hash is a valid proof, False otherwise
    """
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:6] == "000000"


# print(proof_of_work(1996659))


print(valid_proof(1996659,1365222))
