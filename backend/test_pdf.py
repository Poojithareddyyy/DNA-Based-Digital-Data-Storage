from decoder_secure import decode_file
import sys
try:
    decode_file("Sample File 2.pdf.dna")
    print("Done decoding Sample File 2.pdf.dna")
except Exception as e:
    print("Error:", e)
