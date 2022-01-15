#This script is for encoding and decoding text using ROT13
import codecs
data="Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}"

ddata=codecs.encode(data, 'rot13')
print(data)
print(ddata)
