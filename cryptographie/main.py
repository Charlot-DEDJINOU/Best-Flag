import argparse
import rotn
import offset
import aes
import ascii
import substitution

def displayMethodError() :
    print('Error: Invalid method. Please provide a valid method (crypt or decrypt).')

# Définition des arguments attendus depuis le terminal
parser = argparse.ArgumentParser(description='Encrypt or decrypt a file using different methods.')
parser.add_argument('-f', '--function', type=str, help='Name of the function to call (rotn, offset, aes, ascii, substitution)')
parser.add_argument('-u', '--input', type=str, help='Input file name')
parser.add_argument('-o', '--output', type=str, help='Output file name')
parser.add_argument('-k', '--key', type=str, help='Key for encryption/decryption')
parser.add_argument('-a', '--alphabet', type=str, help='Alphabet for substitution cipher')
parser.add_argument('-m', '--method', type=str, help='Method to use (crypt or decrypt)')

# Parsing des arguments fournis par l'utilisateur
args = parser.parse_args()

# Vérification des arguments et appel des fonctions correspondantes
if args.function.lower() == 'rotn':
    if args.method == 'crypt':
        rotn.crypt(args.input, args.output, int(args.key), args.alphabet)
    elif args.method == 'decrypt':
        rotn.decrypt(args.input, args.output, int(args.key), args.alphabet)
    else:
        displayMethodError()
elif args.function.lower() == 'offset':
    if args.method == 'crypt':
        offset.crypt(args.input, args.output, int(args.key))
    elif args.method == 'decrypt':
        offset.decrypt(args.input, args.output, int(args.key))
    else:
        displayMethodError()
elif args.function.lower() == 'aes':
    if args.method == 'crypt':
        aes.crypt(args.input, args.output, args.key.encode())
    elif args.method == 'decrypt':
        aes.decrypt(args.input, args.output, args.key.encode())
    else:
        displayMethodError()
elif args.function.lower() == 'ascii':
    if args.method == 'crypt':
        ascii.crypt(args.input, args.output, int(args.key))
    elif args.method == 'decrypt':
        ascii.decrypt(args.input, args.output, int(args.key))
    else:
        displayMethodError()
elif args.function.lower() == 'substitution':
    if args.method == 'crypt':
        substitution.crypt(args.input, args.output, args.key)
    elif args.method == 'decrypt':
        substitution.decrypt(args.input, args.output, args.key)
    else:
        displayMethodError()
else:
    print('Error: Invalid function name. Please provide a valid function name (rotn, offset, aes, ascii, substitution).')