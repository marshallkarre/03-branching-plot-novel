		#!/Library/Frameworks/Python.framework/Versions/3.6/bin

		import sys
		import json

		assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

		with open('zork.json') as json_data:
			world = json.load(json_data)

		def get_response(response):
			''' Normalize user input and map to dictionary '''
			try :
				return int(response)-1
			except ValueError:
				return -1

		def print_response(count,responses):
			''' Print out the response option '''
			return str(count + 1)
			
		def check_quit(response):
			''' Checks if the user has quit the program '''
			response = str(response)
			if response.lower() == 'q' or response.lower == 'quit':
				return True
			return False

		location = 'west_of_house'

		game_is_running = True
		while game_is_running:

			#get the current location
			current = world[location]
			# print out the description of the current location
			print(current['description'])
			#print out the options
			if len(current['options']) == 0:
				continue
			for count,option in enumerate(current['options']):
				print('[' + print_response(count,current['options']) + '] ' + option['option'])
			print('[q] to quit')
			#get user response
			response = input('What would you like to do? ')
			#see if we need to quit
			if check_quit(response):
				game_is_running = False
				continue
			#normalize response, convert to int
			response = get_response(response)
			#check response against options
			for count,option in enumerate(current['options']):
				if (response == count):
					location = option['goto']

		print('Thanks for playing! See you next time!')