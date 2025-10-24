from passlib.hash import sha256_crypt as bcrypt

def generate_hash(password: str) -> str:
    return bcrypt.hash(password)

def verify_hash(password: str, hash: str) -> bool:
    return bcrypt.verify(password, hash)