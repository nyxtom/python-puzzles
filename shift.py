import string
# Blatantly steal Lennart's UI design
first = unicode(raw_input("Please enter Plaintext to Cipher: "), "UTF-8")
k = int(raw_input("Please enter the shift: "))

in_alphabet = unicode(string.ascii_lowercase)
out_alphabet = in_alphabet[k:] + in_alphabet[:k]

translation_table = dict((ord(ic), oc) for ic, oc in zip(in_alphabet, out_alphabet))

print first.translate(translation_table)
