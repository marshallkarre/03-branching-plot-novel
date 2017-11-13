#!/Library/Frameworks/Python.framework/Versions/3.6/bin

import sys

assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

def decode_response(user_input):
	return user_input

def finishm():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You don\'t want to leave behind your mission, even if you don\'t have proper equipment. You\'re sure you can handle it. After all, you are one of the most notorious assassins in the nation. As you turn away from the exit, an alarm begins to song throughout the building with a robotic voice blaring \n"Warning! Warning! A subject has escaped and is loose in the building! I repeat. Subject 251 is loose!" \nYou realize your black shirt displays that number on your lapel and that you were able to sneak in that knife and a compact pistol. You don\'t let this announcement frightnen you as you proceed to find and eliminate the CEO. \nCONGRADULATIONS! (I guess with this cliffhanger ending) YOU WIN. I wonder how long it took you... \n[r] Restart \n[q] Quit game')
	user_input = decode_response(input('What will you do now?'))
	if user_input == 'r':
		intro()
	if user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')


def leave():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You decide that this job isn\'t for you. You\'ve even succumbed to the experimentation. Were they trying to convert you to their side with the drugs you were given, or were they using you as a guinea pig for drugs that could be used in the medical field if correctly modified? You stop questioning and abandon the building. You hotwire a vehicle in one of the lots and drive off. As you speed down the road, the building explodes. This surprises you, since you didn\'t plant any bombs. A familiar female voice suddenly emits from the radio of the car \n"Had a feeling they\'d get to ya, but it\'s fine, we got it."\nCONGRADULATIONS! YOU WIN. I wonder how long it took you... \n[r] Restart \n[q] Quit')
	user_input = decode_response(input('What will you do now?'))
	if user_input == 'r':
		intro()
	if user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def fight():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You see the guard coming quickly towards you. You decide to use his momentum against him and flip him. You wait for him to stand up, and he comes at you slowly. His punches also come slow, so you dodge them wih ease. Dodge, punch, dodge, dodge, punch, the fight goes on. The next punch he throws, you are able to dodge under it, get behind him, and put him in a choke hold. As he gasps for air, you proceed to snap his neck. You look at the two dead bodies in amazement, as if this were an accomplishment. You can\'t understand how you\'re able to pull this off, but you did.You proceed to take the knife out of the dead guard\'s head, and take his assault rifle. You remove the safety and check the magazine for ammunition but can\'t understand how you know about this. You then creep out of the door to find your way out. You look around and you are somehow familiar with this building and the structure. You head forward, take two lefts, then a right towards the exit you somehow know is there. As you approach the exit, you see various posters of wanted criminals, and to your surprise, you are on one. \n"Super Assassin J" \nis what it states. It is all clear now, you let yourself be captured for a reason. To take out the CEO of this company who is making a special trip to this experimental lab right now. \n[1] Abandon your mission \n[2] Finish your mission \n[q] Quit game')
	user_input = decode_response(input('you choose to...'))
	if user_input == '1':
		leave()
	elif user_input == '2':
		finishm()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def knifek():
		valid_input = False
		while valid_input == False:
			valid_input = True
		print('You look over and pull the knife out of the dead guard\'s head. The guard then rushes you but you use this to your advantage. As he comes towards you, you\'re able to sidestep with a swift, elegant swipe to his throat. He falls to the ground and you give his skull a stab to keep the noise down. All of these skills are flooding back into your mind and things still seem unclear. You try not to question it and wipe your knife and take one of the guard\'s assault rifles. You remove the safety and check the magazine for ammunition but can\'t understand how you know about this. You then creep out of the door to find your way out. You look around and you are somehow familiar with this building and the structure. You head forward, take two lefts, then a right towards the exit you somehow know is there. As you approach the exit, you se various posters of wanted criminals, and to your surprise, you are on one. \n"Super Assassin J" \nis what it states. It is all clear now, you let yourself be captured for a reason. To take out the CEO of this company who is making a special trip to this experimental lab right now. \n[1] Abandon your mission \n[2] Finish your mission \n[q] Quit game')
		user_input = decode_response(input('You choose to...'))
		if user_input == '1':
			leave()
		elif user_input == '2':
			finishm()
		elif user_input == 'q':
			exit_game()
		else:
			valid_input = False
		print('Invalid Input')

def charge2():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You decide to charge him while he attempts to reload and you knock him to the floor. You get a few hits in on him, but him pushes you off his 250lbs body. He comes at you with a strong right swing but you dodge it by rolling to the floor and end up next to the dead guard. \n[1] Pull out the knife \n[2] Fight him hand-to-hand \n[q] Quit game')
	user_input = decode_response(input('You choose to...'))
	if user_input == '1':
			knifek()
	elif user_input == '2':
			fight()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')


def usechair2():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You run up to the guard and smack him in the head with the chair. The chair is heavy and you knock him out easily. You take the knife out of the dead guard\'s head and take his assault rifle. You remove the safety and check the magazine for ammunition but can\'t understand how you know about this. You then creep out of the door to find your way out. You look around and you are somehow familiar with this building and its structure. You head forward, take two lefts, then a right towards the exit you somehow know is there. As you approach the exit, you see various posters of wanted criminals, and to your surprise, you are on one. \n"Super Assassin J"\n is what it states. It is all clear now, you let yourself be captured for a reason. To take out the CEO of this company, who is making a special trip to this experimental lab right now. \n[1] Abandon your mission  \n[2] Finish your mission \n[q] Quit game')
	user_input = decode_response(input('You choose to... '))
	if user_input == '1':
			leave()
	elif user_input == '2':
			finishm()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')


def usechair():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You remember the chair you were tied to was some sort of metal. As the guard begins to fire, you use the chair as a shield to block the ocean of bullets. You and the guard alike underestimate the durability of the chair, so when the guard empties his magazine, there is an opening. \n[1] Charge him \n[2] Use chair \n[3] Throw the chair at a guard \n[q] Quit game')
	user_input = decode_response(input('You choose to...'))
	if user_input == '1':
			charge2()
	elif user_input == '2':
			usechair2()
	elif user_input == '3':
			throwchair3()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def charge():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You charge at the guard but can\'t manage to reach him before he can get a shot off on you. His first shot isn\'t fatal, but the next one is.\nYOU ARE DEAD \n[r] Restart \n[q] Quit game')
	user_input = decode_response(input('What will you do now?'))
	if user_input == 'r':
		intro()
	if user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def throwchair2():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You pick up the chair and throw it at the guard. He easily knocks it out of the way. You try to charge him, but he just readies his gun and fills you with bullets. \nYOU ARE DEAD \n[r] Restart \n[q] Quit game')
	user_input = decode_response(input('What will you do now?'))
	if user_input == 'r':
		intro()
	if user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def throwknife():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('As the two argue, you throw the knife into one of their skulls. You have no clue how you pulled something like that off, but that\'s not what you are focused on right now. The other guard, in complete shock, decides to ready his assault rifle \n[1] Charge him \n[2] Use the chair as cover \n[3] Throw the chair at a guard \n[q] Quit game')
	user_input = decode_response(input('You choose to...'))
	if user_input == '1':
			charge()
	elif user_input == '2':
			usechair()
	elif user_input == '3':
			throwchair2()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def throwchair():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You pick up the chair and throw it at one of the guards. This is really just a minor inconvenience to him. Since you now pose a threat, they have no choice but to act out of self defense and use you for target practice. \nYOU ARE DEAD \n[r] Restart \n[q] Quit game')
	user_input = decode_response(input('What will you do now?'))
	if user_input == 'r':
		intro()
	if user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def calm():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You try to get their attention and tell them to stop arguing. They both look at you angrily. One picks up his gun and yells \n"Quiet fugitive! You\'re already in deep shit!"\nThe other guard provokes him, saying, \n"You won\'t do it. You won\'t shoot him."\n, with a smirk on his face. The armed guard growls back, \n"Oh really?" \n1, 2, 3 shots rip into your chest. Next time, try not to negotiate with an angry armed man because now, \nYOU ARE DEAD \n [r] Restart \n[q] Quit game')

	user_input = decode_response(input('What will you do now?'))
	if user_input == 'r':
		intro()
	if user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def cutropeh2():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You cut the rest of your ropes off. You stand up, stretch, and exhale heavily. In an instant, two guards bust through the door. \n"Told you I heard something" \nOne of them says. They start to bicker and seem to forget about you. They don\'t notice the knife you\'re holding... \n[1] Calm the argument n[2] Throw the knife at a guard \n[3] Throw the chair at a guard \n[4] Use your hidden power \n[q] Quit game')
	user_input = decode_response(input('You choose to...'))
	if user_input == '1':
			calm()
	elif user_input == '2':
			throwknife()
	elif user_input == '3':
			throwchair()
	elif user_input == '4':
			power()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def cutropeh():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You manage to get the knife around your back and to your hands, due to your flexibility. You cut the ropes off your hands fairly easily. \n[1] Cut the ropes off your feet \n[2] Wait \n[q] Quit Game')
	user_input = decode_response(input('You choose to... '))
	if user_input == '1':
		cutropeh2()
	elif user_input == '2':
		wait2()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def edrop2():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You decide to keep listening. \n"I w.. told .. is a n..io.al.. wa..ed ..im..alW.it. What ... th.t?" \nThe door suddenly opens, and, to their suprise, you\'re standing. Before you can react, you are riddled with bullets. You shouldn\'t have been so nosey. Now,\n YOU ARE DEAD\n[r] Restart \n[q] Quit game')
	user_input = decode_response(input('What will you do now?'))
	if user_input == 'r':
		intro()
	if user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def edrop():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You stand up and make your way to the door to see what the conversation is about. You can barely make out the words. \n".. nee. .o g.a.. him at al. c.sts! .o telling ..at he ... do." . \nYou can\'t make out what they are saying, but that\'s none of your concern right now. \n[1] Cut ropes off your hands \n[2] Eavesdrop \n[q] Quit game')
	user_input = decode_response(input('You choose to... '))

	if user_input == '1':
		cutropeh2()
	elif user_input == '2':
		edrop2()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def cutropef():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You are flexible enough to lean down and cut the rope from your feet. When you get the rope off, you hear chatter from outside the door. You want to listen to what they are saying outside, but you have to concentrate to get the rope off your hands. \n[1] Cut ropes off your hands \n[2] Eavesdrop \n[q] Quit game')
	user_input = decode_response(input('You choose to...'))

	if user_input == '1':
		cutropeh2()
	elif user_input == '2':
		edrop()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def wiggleface2():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You wiggle some more. Now your face is right in front of the knife. You manage to pick it up with your mouth by the hilt. \n[1] Cut ropes off your hands \n[2] Cut ropes off your feet \n[q] Quit game')
	user_input = decode_response(input('You choose to...'))

	if user_input == '1':
		cutropeh()
	elif user_input == '2':
		cutropef()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def wiggleface():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You wiggle around, trying to position your face towards the knife. You\'ve gotten closer to it. \n[1] Wiggle face towards the knife \n[2] Wiggle hands towards the knife \n[3] Wiggle feet towards the knife \n[q] Quit game')
	user_input = decode_response(input('You choose to...'))

	if user_input == '1':
		wiggleface2()
	elif user_input == '2':
		wigglehands()
	elif user_input == '3':
		wigglefeet()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def power():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You close your eyes and start to grunt. The guards look in confusion. They decide to pick you up and sit you back up-right. One the guards proceeds to headbutt you. Did you really think you had a super power?')
	user_input = decode_response(input('Recover (r) '))
	if user_input == 'r':
		intro()
	else:
		valid_input = False
	print('Invalid Input')

def negotiate():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You open your mouth to speak, but a guard covers your mouth and nose with a damp cloth that reeks of chemicals. You struggle to get loose, but you start to feel drowsy and disoriented. You eventually pass out.')
	user_input = decode_response(input('Recover (r) '))
	if user_input == 'r':
		intro()
	else:
		valid_input = False
	print('Invalid Input')

def ripoff():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You struggle to rip the ropes off, but the guards rush up to you and stomp on you repeatedly. You get a clear view of whats outside the door, but before you can see anything you are kicked in the head and pass out. You really thought you had super strength, huh?')
	user_input = decode_response(input('Recover (r) '))
	if user_input == 'r':
		intro()
	else:
		valid_input = False
	print('Invalid Input')

def wait2():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You decide to wait... \nBefore you know it, the door is flying open with two guards coming through. Your heart is racing. \n[1] Rip off of the chair and take out the guards \n[2] Negotiate \n[3] Use your hidden power \n[q] Quit game')
	user_input = decode_response(input('You choose to...'))

	if user_input == '1':
		ripoff()
	elif user_input == '2':
		negotiate()
	elif user_input == '3':
		power()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def wigglehands2():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You wiggle around, trying to position your hands towards the knife, but you can\'t get any closer. Your face, however, has. \n[1] Wiggle face towards the knife \n[2] Wait\n[q] Quit game')
	user_input = decode_response(input('You choose to...'))
	if user_input == '1':
		wiggleface()
	elif user_input == '2':
		wait2()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')


def wigglehands():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You wiggle around, trying to position your hands closer to the knife. You seem to move a bit. \n[1] Wiggle hands towards the knife\n[2] Wiggle face towards the knife\n[q] Quit game')
	user_input = decode_response(input('You choose to...'))
	if user_input == '1':
		wigglehands2()
	elif user_input == '2':
		wiggleface()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def wigglefeet():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You attempt to wiggle your feet towards the knife but realize it\'s too far away. Maybe another method would make more sense.')
	user_input = decode_response(input('Back (b) '))
	if user_input == 'b':
			struggle3()
	else:
		valid_input = False
	print('Invalid Input')

def struggle3():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You move around rampantly in the chair and, to your relief, you tip over and hit the ground. You hear a noise as somethng hits the floor. To your surprise, it\'s a knife. You decide not to question it for now, but you do concentrate on how you will get to the knife. \n[1] Wiggle face towards the knife \n[2] Wiggle hands towards the knife \n[3] Wiggle feet towards the knife\n[q] Quit game')
	user_input = decode_response(input('You choose to...'))

	if user_input == '1':
		wiggleface()
	elif user_input == '2':
		wigglehands()
	elif user_input == '3':
		wigglefeet()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def struggle2():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You struggle some more, twisting and turning. The chair starts to wobble, but still stays. \n[1] Struggle \n[2] Wait \n[3] Scream \n[q] Quit game')
	user_input = decode_response(input('You choose to...'))

	if user_input == '1':
		struggle3()
	elif user_input == '2':
		wait()
	elif user_input == '3':
		scream2()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')

def struggle():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You rock back and forth in the chair while wiggling, but the chair moves only slightly.\n[1] Struggle \n[2] Wait \n[3] Scream \n[q] Quite game')
	user_input = decode_response(input('You choose to...'))

	if user_input == '1':
		struggle2()
	elif user_input == '2':
		wait()
	elif user_input == '3':
		scream2()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')


def observe():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You look around, but see nothing in the room besides yourself, the chair, and the hanging lightbulb. There are no windows, the walls are a dark color, and the only exit is a door with some light seeping through the bottom gap, and you see two shadows from behind the door. You look down and wonder why you are dressed in all black.')
	user_input = decode_response(input('Back (b) '))
	if user_input == 'b':
		intro()

	else:
		valid_input = False
		print('Invalid Input')


def wait():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You wait for some time, when suddenly, a guard comes through the door. He then asks someone that you can\'t see outside the room\n"Are you sure?"\n. He then pulls out his revolver and shoots you straight between the eyes.\nYOU ARE DEAD\n[r] Restart\n[q] Quit game')

	user_input = decode_response(input('What will you do now?'))
	if user_input == 'r':
		intro()
	if user_input == 'q':
		exit_game()

	else:
		valid_input = False
		print('Invalid Input')

def scream2 ():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You scream again, this time a tad louder. As you stop to draw another breath, two guards bust through the door. One hits you in the head with his assault rifle before you can start screaming again, then holds your head up. The other approaches and proceeds to slit your throat.\nYOU ARE DEAD\n[r] Restart\n[q] Quit game')

	user_input = decode_response(input('What will you do now?'))
	if user_input == 'r':
		intro()
	if user_input == 'q':
		exit_game()

	else:
		valid_input = False
		print('Invalid Input')

def scream():
		valid_input = False
		while valid_input == False:
			valid_input = True
		print('You scream at the top of your lungs...\nNothing happens...\n[1] Scream again\n[2] Wait\n[q] Quit game')


		user_input = decode_response(input('You choose to...'))

		if user_input == '1':
			scream2()
		elif user_input == '2':
			wait()
		elif user_input == 'q':
			exit_game()
		else:
			valid_input = False
		print('Invalid Input')


def intro():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print("You slowly open your eyes, feeling dazed and fatigued. You look around and, with blurred vision, see you're in a dimly lit room, a flickering light bulb just above you. You try to move, but realize your hands and feet have been bound to a sturdy, metal chair.\n[1] Scream for help\n[2] Struggle\n[3] Observe the room more\n[q] Quit game")

	user_input = decode_response(input('You choose to...'))

	if user_input == '1':
		scream()
	elif user_input == '2':
		struggle()
	elif user_input == '3':
		observe()
	elif user_input == 'q':
		exit_game()
	else:
		valid_input = False
	print('Invalid Input')



exit_game = False


while not exit_game:
	intro()


