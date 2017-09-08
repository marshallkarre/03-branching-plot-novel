#!/Library/Frameworks/Python.framework/Versions/3.6/bin

import sys

assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

def decode_response(user_input):
	return user_input


exit_game = False


while not exit_game:
	print('It was a dark and stormy night…')
	print("[1] Interrupt Snoopy's writing session")
	print('[2] Ask Mrs. Who what a tesseract means')
	print('[3] Research the life of Edward Bulwer-Lytton')
	user_input = decode_response(input('What do you choose (q to quit)? '))
	if user_input == 'q':
		exit_game = True