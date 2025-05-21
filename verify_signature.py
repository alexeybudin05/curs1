from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Загрузка публичного ключа
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(
        f.read(),
        backend=default_backend()
    )

# Загрузка подписи
with open("signature.bin", "rb") as f:
    signature = f.read()

# Чтение данных из файла
with open("data.txt", "rb") as f:
    data = f.read()

# Проверка подписи
try:
    public_key.verify(
        signature,
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("✅ Подпись верна! Файл data.txt не изменялся.")
except Exception as e:
    print("❌ Подпись неверна! Файл поврежден", e)