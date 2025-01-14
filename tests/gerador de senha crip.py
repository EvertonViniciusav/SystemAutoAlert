from werkzeug.security import generate_password_hash

senha_plana = ""
hash_gerado = generate_password_hash(senha_plana, method="pbkdf2:sha256")

print(f"Hash gerado: {hash_gerado}")
