import requests
import hashlib
import os

with open("test_binary.bin", "wb") as f:
    f.write(os.urandom(1024))

hash1 = hashlib.md5(open("test_binary.bin", "rb").read()).hexdigest()

res1 = requests.post("http://localhost:8000/encode", files={"file": open("test_binary.bin", "rb")})
dna_file = res1.json()["dna_file"]

res2 = requests.post("http://localhost:8000/decode", files={"file": open(f"storage/dna_files/{dna_file}", "rb")})
decoded_file = res2.json()["decoded_file"]

res3 = requests.get(f"http://localhost:8000/download/{decoded_file}")
with open("test_binary_downloaded.bin", "wb") as f:
    f.write(res3.content)

hash2 = hashlib.md5(open("test_binary_downloaded.bin", "rb").read()).hexdigest()

print("Original hash:", hash1)
print("Decoded hash: ", hash2)
if hash1 == hash2:
    print("SUCCESS: Exact match!")
else:
    print("ERROR: Corrupted data!")
