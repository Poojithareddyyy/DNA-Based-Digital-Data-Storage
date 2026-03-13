import requests
import hashlib

# 1. Provide a minimal valid PDF content
minimal_pdf = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] >>\nendobj\nxref\n0 4\n0000000000 65535 f \n0000000009 00000 n \n0000000058 00000 n \n0000000115 00000 n \ntrailer\n<< /Size 4 /Root 1 0 R >>\nstartxref\n199\n%%EOF\n"

with open("dummy.pdf", "wb") as f:
    f.write(minimal_pdf)

# Encode
res = requests.post("http://localhost:8000/encode", files={"file": open("dummy.pdf", "rb")})
dna_file = res.json()["dna_file"]

# Decode
res2 = requests.post("http://localhost:8000/decode", files={"file": open(f"storage/dna_files/{dna_file}", "rb")})
dec_file = res2.json()["decoded_file"]

# Download
res3 = requests.get(f"http://localhost:8000/download/{dec_file}")
hash_orig = hashlib.md5(minimal_pdf).hexdigest()
hash_rec = hashlib.md5(res3.content).hexdigest()

print(f"Orig: {hash_orig}")
print(f"Rec : {hash_rec}")
if hash_orig == hash_rec:
    print("SUCCESS")
