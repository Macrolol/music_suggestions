"""
hashing.py: This file handles all the hashing used in the project.
"""

__author__ = "Michael Dormon"


import bcrypt

DEFAULT_ROUNDS = 12

class Hashing(object):

    @staticmethod
    def hash(password, rounds=DEFAULT_ROUNDS):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds))

    @staticmethod
    def verify(password, hashed):
        return bcrypt.checkpw(password.encode('utf-8'), hashed)







if __name__ == '__main__':
    """ The main method is used to detemine number of rounds for the system

    I found on the internet that your system should take at least 250ms to hash a password
    so this method just loops, increasing the number of rounds until it takes longer than 250ms
    explanation of why:
    https://security.stackexchange.com/questions/17207/recommended-of-rounds-for-bcrypt
    """

    import time

    password = b"password"
    
    # the library wont let you use less than 4 or more than 31 rounds
    # 12 is good for most systems
    for i in range(4, 31):

        start = time.time()
        salt = bcrypt.gensalt(rounds=i)
        hashed = bcrypt.hashpw(password, salt)
        end = time.time()
        if (end - start) > 0.25:
            print("Preffered rounds: ", i)
            break

