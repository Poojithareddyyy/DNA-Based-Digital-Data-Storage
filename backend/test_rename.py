import requests
import json
import os

with open("test3.txt", "w") as f:
    f.write("Hello world renamed API test!")

requests.post("http://localhost:8000/encode", files={"file": open("test3.txt", "rb")})
os.rename("storage/dna_files/test3.txt.dna", "renamed_test.dna")

res = requests.post("http://localhost:8000/decode", files={"file": open("renamed_test.dna", "rb")})
print("Decode resp:", res.json())

res2 = requests.get(f"http://localhost:8000{res.json()['download_link']}")
print("Downloaded content:", res2.content)
