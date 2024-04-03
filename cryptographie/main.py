import argparse
import ROTN
import Offset
import AES
import ASCII
import Substitution

def displayMethodError() :
    print('Error: Invalid method. Please provide a valid method (crypt or decrypt).')

# Définition des arguments attendus depuis le terminal
parser = argparse.ArgumentParser(description='Encrypt or decrypt a file using different methods.')
parser.add_argument('-f', '--function', type=str, help='Name of the function to call (ROTN, Offset, AES, ASCII, Substitution)')
parser.add_argument('-u', '--input', type=str, help='Input file name')
parser.add_argument('-o', '--output', type=str, help='Output file name')
parser.add_argument('-k', '--key', type=str, help='Key for encryption/decryption')
parser.add_argument('-a', '--alphabet', type=str, help='Alphabet for substitution cipher')
parser.add_argument('-m', '--method', type=str, help='Method to use (crypt or decrypt)')

# Parsing des arguments fournis par l'utilisateur
args = parser.parse_args()

# Vérification des arguments et appel des fonctions correspondantes
if args.function == 'ROTN':
    if args.method == 'crypt':
        ROTN.crypt(args.input, args.output, int(args.key), args.alphabet)
    elif args.method == 'decrypt':
        ROTN.decrypt(args.input, args.output, int(args.key), args.alphabet)
    else:
        displayMethodError()
elif args.function == 'Offset':
    if args.method == 'crypt':
        Offset.crypt(args.input, args.output, int(args.key))
    elif args.method == 'decrypt':
        Offset.decrypt(args.input, args.output, int(args.key))
    else:
        displayMethodError()
elif args.function == 'AES':
    if args.method == 'crypt':
        AES.crypt(args.input, args.output, args.key.encode())
    elif args.method == 'decrypt':
        AES.decrypt(args.input, args.output, args.key.encode())
    else:
        displayMethodError()
elif args.function == 'ASCII':
    if args.method == 'crypt':
        ASCII.crypt(args.input, args.output, int(args.key))
    elif args.method == 'decrypt':
        ASCII.decrypt(args.input, args.output, int(args.key))
    else:
        displayMethodError()
elif args.function == 'Substitution':
    if args.method == 'crypt':
        Substitution.crypt(args.input, args.output, int(args.key))
    elif args.method == 'decrypt':
        Substitution.decrypt(args.input, args.output, int(args.key))
    else:
        displayMethodError()
else:
    print('Error: Invalid function name. Please provide a valid function name (ROTN, Offset, AES, ASCII, Substitution).')