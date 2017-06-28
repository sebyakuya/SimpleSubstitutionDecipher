# SimpleSubstitutionDecipher

After having done a frequency analysis of an encrypted text, with this you can substitute the text letter by letter.
frec.txt is where the frecuencies will be
text.txt is where the encrypted text will be

To run it:

python SSD.py text.txt frec.txt

Example:

frec.txt

THBONKFREGJVUMIYDALCSQWZPX
EAORSNITUCMDLPGQBYVAZFJXKW

This means that T will be E, H will be A, etc.
The first one is the frecuency of the encrypted text, the second one is your language frecuency (in this case, it's spanish without Ñ)

text.txt
asdflñkjasef lasnf sñadfj lñasnflkasnfkl nasklñh foñkjasñkfjasjdfasf

The output will be the decrypted text.
