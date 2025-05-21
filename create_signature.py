from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Загрузка приватного ключа
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None,
        backend=default_backend()
    )

# Чтение данных из файла
with open("data.txt", "rb") as f:
    data = f.read()

# Создание подписи
signature = private_key.sign(
    data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Сохранение подписи
with open("signature.bin", "wb") as f:
    f.write(signature)

print(f"✅ Подпись для файла data.txt сохранена в signature.bin")