import hashlib

def gen(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def verify(pw, db_pw):
    return gen(pw) == db_pw