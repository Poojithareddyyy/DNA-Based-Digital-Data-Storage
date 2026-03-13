import os
from encoder_secure import encode_file
from decoder_secure import decode_file

with open("test.txt", "w") as f:
    f.write("Hello world testfile.")

dna_filename = encode_file("test.txt")
print("encoded to:", dna_filename)
decode_file(dna_filename)

with open("storage/reconstructed/test.txt", "r") as f:
    print("Reconstructed:", f.read())
