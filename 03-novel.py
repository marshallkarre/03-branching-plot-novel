#!/Library/Frameworks/Python.framework/Versions/3.6/bin

import sys

assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

def decode_response(user_input):
	return user_input

def finishm():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You dont want to leave behind your mission, even without the proper equipment. Youre sure you can')
	print('handle it. After all, you are one of the most notorious assassins in the nation. As you turn away from')
	print('the exit, an alarm begins to play with a female voice stating "Warning! Warning! A subject has escaped')
	print('and is loose in the building! I repeat. Subject 251 is loose!" You realize your black attire hoilstered that number')
	print('and that you were able to sneak in that knife and a compact pistol. You dont let this announcement frightnen you')
	print('as you proceed to find and eliminate the CEO.')
	print('CONGRADULATIONS! (I guess with this cliffhanger ending) YOU WIN. I wonder how long it took you...')
	user_input = decode_response(input('Restart (r)? '))
	if user_input == 'r':
		intro()
	else:
		valid_input = False
	print('Invalid Input')


def leave():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You decide that this job isnt for you. Youve even succumbed to the experimentation. Were they trying to')
	print('Convert you to their side with the drugs you were given, or were they using you as a guinea pig for ')
	print('drugs that could be used inn the medical field if correctly modified? You stop questioning and abandon')
	print('the building. You hotwire a vehicle in one of the lots and drive off. As you speed down the raod, the ')
	print('building explodes! Who couldve done it. You dont remember planting bombs. A familiar, female voice suddenly')
	print('emits from the radio of the car "Had a feeling theyd get to ya, but its fine, we got it."')
	print('CONGRADULATIONS! YOU WIN. I wonder how long it took you...')
	user_input = decode_response(input('Restart (r)? '))
	if user_input == 'r':
		intro()
	else:
		valid_input = False
	print('Invalid Input')

def fight():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You see the guard coming quickly towards you. You decide to use his momentum against him and filp him.')
	print('You wait for him to arise, and he comes at you slowly. His punches also came slow, so you dodged them wih ease.')
	print('Dodge, punch, dodge, dodge punch, dodge, punch, punch, as the fight went. The final punch he threw, you were able')
	print('to dodge under it, get behind him, and put him in a choke hold. As he gasped for air, you proceeded to snap his neck.')
	print('You look at the two dead bodies in amazement, as if this were an accomplishment. You cant see how youre able')
	print('to pul this off, but you are.You proceed to take the knife out of the dead guards head, ')
	print('and also borrow his assault rifle. You remove the safety and check the magazine for ammunition')
	print('but cant understand how you know about this. You then creep out of the door to find your way out.')
	print('You look around and you are somehow familiar with this building and the structure. You head forward, ')
	print('take two lefts, then a right towards the exit you somehow had mapped in your mind. As you approached')
	print('the exit, you saw various posters of wanted criminals, and to your surprise, you were on one.')
	print('"Super Assassin J" is what it stated. It was all clear now, you were captured on purpose. To take out the')
	print('CEO of this company, making a special trip to this experimental lab.')
	print('[1] Leave')
	print('[2] Finish your mission')
	user_input = decode_response(input('What will you do (q to quit)? '))
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
		print('You look over and pull the knife out of the dead guards head. The guard then rushes you but you use this')
		print('to your advantage. As he comes towards you, youre able to sidestep with a swift, elegant swipe to his throat.')
		print('He falls to the ground and you decide to give his skull a stab to keep the noise down. All of these skills')
		print('are flooding back into your mind and things still seem unclear. You try not to question it and wipe your knife ')
		print('and also borrow one of the guards assault rifles. You remove the safety and check the magazine for ammunition')
		print('but cant understand how you know about this. You then creep out of the door to find your way out.')
		print('You look around and you are somehow familiar with this building and the structure. You head forward, ')
		print('take two lefts, then a right towards the exit you somehow had mapped in your mind. As you approached')
		print('the exit, you saw various posters of wanted criminals, and to your surprise, you were on one.')
		print('"Super Assassin J" is what it stated. It was all clear now, you were captured on purpose. To take out the')
		print('CEO of this company, making a special trip to this experimental lab.')
		print('[1] Leave')
		print('[2] Finish your mission')
		user_input = decode_response(input('What will you do (q to quit)? '))
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
	print('You decide to charge him while he attempts to reload and you knock him to the floor. You get a few')
	print('hits in on him, but him pushes you off his 250lbs body. He comes at you with a strong right swing but')
	print('you dogde it by rolling to the floor. the end up next to the dead guard.')
	print('[1] Pull out the knife')
	print('[2] Proceed to fight')
	user_input = decode_response(input('What will you do (q to quit)? '))
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
	print('You run up to the guard, out of cover and smack him in the head with the chair. The chair wasnt')
	print('easily lifted, so you can assume hes knocked out. You Take the knife out of the dead guards head, ')
	print('and also borrow his assault rifle. You remove the safety and check the magazine for ammunition')
	print('but cant understand how you know about this. You then creep out of the door to find your way out.')
	print('You look around and you are somehow familiar with this building and the structure. You head forward, ')
	print('take two lefts, then a right towards the exit you somehow had mapped in your mind. As you approached')
	print('the exit, you saw various posters of wanted criminals, and to your surprise, you were on one.')
	print('"Super Assassin J" is what it stated. It was all clear now, you were captured on purpose. To take out the')
	print('CEO of this company, making a special trip to this experimental lab.')
	print('[1] Leave')
	print('[2] Finish your mission')
	user_input = decode_response(input('What will you do (q to quit)? '))
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
	print('You remember the chair you were tied to was some sort of metal. As the guard begins to fire,')
	print('you use the chair as a shield to block the ocean of bullets. You and the guard alike underestimated')
	print('the durability of the chair, so when the guard emptied his magazine, there was an opening.')
	print('[1] Charge him')
	print('[2] Use chair')
	print('[3] Throw the chair at a guard')
	user_input = decode_response(input('What will you do (q to quit)? '))
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
	print('You charge at the guard but cant manage to reach him before he can get a shot off on you.')
	print('You feel the adrenaline numbing your gunshot wound, but alas, the guard decides to go for the kill shot')
	print('YOU ARE DEAD')
	user_input = decode_response(input('Restart (r)? '))
	if user_input == 'r':
		intro()
	else:
		valid_input = False
	print('Invalid Input')

def throwchair2():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You pick up the chair and throw it at the guards. This is really just a minor')
	print('inconvenience to him. You try to charge him while hes staggered, but he ends up')
	print('just readying up his gun and turning you into bullet soup. YOU ARE DEAD')
	user_input = decode_response(input('Restart (r)? '))
	if user_input == 'r':
		intro()
	else:
		valid_input = False
	print('Invalid Input')

def throwknife():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('As the two argue, you sent the knife into one of their skulls. You have no clue how ')
	print('you pulled something like that off, but thats isnt your main priority. The other guard,')
	print('in complete shock, decides to ready up his assault rifle')
	print('[1] Charge him')
	print('[2] Use chair')
	print('[3] Throw the chair at a guard')
	user_input = decode_response(input('What will you do (q to quit)? '))
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
	print('You pick up the chair and throw it at one of the guards. This is really just a minor')
	print('inconvenience to him. Since you now pose as a threat, they have no choice but to act out')
	print('of self defense and turn you into a bullet souffle. YOU ARE DEAD')
	user_input = decode_response(input('Restart (r)? '))
	if user_input == 'r':
		intro()
	else:
		valid_input = False
	print('Invalid Input')

def calm():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You try to calm both of them down from their argument. They both look at you ')
	print('angrily. One picks up his gun and states "Quiet fugitive! Youre already in deep shit!"')
	print('The other guard provokes him, saying, "You wont do it. You wont shoot him.", with a smirk on his face')
	print('The armed guard argues back, "Oh really?" 1, 2, 3, rounds into your chest. ')
	print('Next, try not to negotiate with an angry armed man because now, YOU ARE DEAD')

	user_input = decode_response(input('Restart (r)? '))
	if user_input == 'r':
		intro()
	else:
		valid_input = False
	print('Invalid Input')

def cutropeh2():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You cut the rest of your ropes off. You stand up and stretch and exhale heavily.')
	print('Before you can blink, two guards bust through the door. "Told you I heard something",')
	print('One of them says. They start to bicker. They dont notice the knife youre holding...')
	print('[1] Calm the argument')
	print('[2] Throw the knife at a guard')
	print('[3] Throw the chair at a guard')
	print('[4] Use your hidden power')
	user_input = decode_response(input('What will you do (q to quit)? '))
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
	print('You manage to get the knife around your back and too your hands, due to your flexibility.')
	print('You cut the ropes off your hands fairly easily.')
	print('[1] Cut the ropes off your feet')
	print('[2] Wait')
	user_input = decode_response(input('What will you do (q to quit)? '))
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
	print('You decide to keep listening. "I w.. told .. is a n..io.al.. wa..ed ..im..al"')
	print('"W.it. What ... th.t?" The door suddenly opens, and, to their suprise, youre standing.')
	print('Before you can react, you are ridlled with bullets.')
	print('Shouldnt have been so nosey. Now, YOU ARE DEAD')
	user_input = decode_response(input('Restart (r)?'))
	if user_input == 'r':
		intro()
	else:
		valid_input = False
	print('Invalid Input')

def edrop():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You make your way to the door to see what the conversation is about. You can barely')
	print('Make out the words. ".. nee. .o g.a.. him at al. c.sts! .o telling ..at he ... do." .')
	print('You cant make out what they are saying, but thats none of you rconcern right now.')
	print('[1] Cut ropes off your hands')
	print('[2] Eavesdrop')
	user_input = decode_response(input('What will you do (q to quit)? '))

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
	print('You are flexible enough to lean down and proceed to cut the rope from your feet.')
	print('When you get the rope cut from your feet, you hear chatter from outside the door.')
	print('You are now in a state of confusion, but thats not the issue here.')
	print('[1] Cut ropes off your hands')
	print('[2] Eavesdrop')
	user_input = decode_response(input('What will you do (q to quit)? '))

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
	print('You wiggle some more. Now your face is right in front of the knife.')
	print('You decide to pick it up with your mouth by the hilt.')
	print('[1] Cut ropes off your hands')
	print('[2] Cut ropes off your feet')
	user_input = decode_response(input('What will you do (q to quit)? '))

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
	print('You wiggle around, trying to position your face towards the knife.')
	print('youve gotten closer to it.')
	print('[1] Wiggle face towards the knife')
	print('[2] Wiggle hands towards the knife')
	print('[3] Wiggle feet towards the knife')
	user_input = decode_response(input('What will you do (q to quit)? '))

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
	print('You close your eyes and start to grunt. The guards look in confusion.')
	print('They then decide to pick you up. One the guards proceeds to headbutt you.')
	print('Did you really think you had a super power? Really?')
	user_input = decode_response(input('Recover (r)? '))
	if user_input == 'r':
		intro()
	else:
		valid_input = False
	print('Invalid Input')

def negotiate():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You open your mouth to speak, but a guard covers your mouth. You struggle')
	print('to get loose, but th resistance is futile. You see some type of rag put over your')
	print('mouth and nose as the second guard stands idlly by. Your eyes get heavy, and you close them.')
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
	print('You struggle to rip the ropes off, but the guards rush up to you and')
	print('stomp on you repeatedly. You get a clear view of whats outside the door,')
	print('but before you can look over to it, you are kicked pretty hard in the head.')
	print('You really thought you had super strength, huh?')
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
	print('You decide to wait...')
	print('Before you know it, the door is flying open with two guards coming through.')
	print('Your heart is racing')
	print('[1] Rip off of the chair and take out the guards')
	print('[2] Negotiate')
	print('[3] Use your hidden power')
	user_input = decode_response(input('What will you do (q to quit)? '))

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
	print('You wiggle around, trying to position your hands towards the knife.')
	print('but you cant get any closer. your face, however, has.')
	print('[1] Wiggle face towards the knife')
	print('[2] Wait')
	user_input = decode_response(input('What will you do (q to quit)? '))
	if user_input == '1':
		wiggleface2()
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
	print('You wiggle around, trying to position your hands towards the knife.')
	print('Youre seemingly getting closer')
	print('[1] Wiggle hands towards the knife')
	print('[2] Wiggle face towards the knife')
	user_input = decode_response(input('What will you do (q to quit)? '))
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
	print('You attempt to wiggle your feet towards the knife but realize')
	print('its too far away. Maybe another method would make more sense.')
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
	print('You move around rampantly in the chair, and to your prevail,')
	print('you tip over and hit the ground. You hear a noise, as somethng hits the ground.')
	print('To your surprise, its a knife. You dont question it, but you do question')
	print('how you will get to the knife.')
	print('[1] Wiggle face towards the knife ')
	print('[2] Wiggle hands towards the knife')
	print('[3] Wiggle feet towards the knife')
	user_input = decode_response(input('What will you do (q to quit)? '))

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
	print('You struggle some more, twisting snd turning. The chair')
	print('starts to wobble, but still stays.')
	print('[1] Struggle ')
	print('[2] Wait')
	print('[3] Scream')
	user_input = decode_response(input('What will you do (q to quit)? '))

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
	print('You rock back and forth in the chair while wiggling, but')
	print('you only move slightly.')
	print('[1] Struggle ')
	print('[2] Wait')
	print('[3] Scream')
	user_input = decode_response(input('What will you do (q to quit)? '))

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
	print('You look around, but see nothing to galore. There are no windows,')
	print('the walls bare a dark tint, and the only exit is a door with some')
	print('light coming through, housing two shadows. You look down and wonder')
	print('why you are dressed in an all black attire.')
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
	print('You wait for some time, when suddenly, a guard comes through the door.')
	print('He then answers, "Are you sure?", as if he were confirming an order.')
	print('He then pulls out his revolver and shoots you straight between the eyes.')
	print('YOU ARE DEAD')

	user_input = decode_response(input('Restart (r)? '))
	if user_input == 'r':
		intro()

	else:
		valid_input = False
		print('Invalid Input')

def scream2 ():
	valid_input = False
	while valid_input == False:
		valid_input = True
	print('You scream again, this time a tad softer. As you finish,')
	print('two guards bust through the door. One hits you in the head')
	print('with his assault rifle, then holds your head up. The other')
	print('approaches and proceeds to slit your throat. YOU ARE DEAD')

	user_input = decode_response(input('Restart (r)? '))
	if user_input == 'r':
		intro()

	else:
		valid_input = False
		print('Invalid Input')

def scream():
		valid_input = False
		while valid_input == False:
			valid_input = True
		print('You scream at the top of your lungs...')
		print('Nothing happens...')

		print("[1] Scream again ")
		print('[2] Wait')


		user_input = decode_response(input('What will you do (q to quit)? '))

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
	print('You slowly open your eyes, feeling dazed and fatigued.')
	print('You look around and, with your blurred vision, see youre')
	print('in a dim lit room with a flickering light bulb just above you.')
	print('You try to move, but realize youre tied to a sturdy, metal chair,')
	print('hands and feet.')
	print("[1] Scream for help")
	print('[2] Struggle')
	print('[3] Observe the room more')

	user_input = decode_response(input('What will you do (q to quit)? '))

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


