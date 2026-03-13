import requests
import os

print("--- Testing Encode ---")
with open("test2.txt", "w") as f:
    f.write("Hello world API test! 1234")

res = requests.post("http://localhost:8000/encode", files={"file": open("test2.txt", "rb")})
print("Encode resp:", res.json())

res = requests.post("http://localhost:8000/decode", files={"file": open("storage/dna_files/test2.txt.dna", "rb")})
print("Decode resp:", res.json())

res = requests.get("http://localhost:8000/download/test2.txt")
with open("downloaded_test2.txt", "wb") as f:
    f.write(res.content)

print("Downloaded content:", open("downloaded_test2.txt", "r").read())
