import random

# Inisyalize kantite chans itilizate a
CHANS = 5

# Chwa odinatè a, aleyatwa
chwa = random.randrange(10, 50)

# Tanke itilizatè gen chans
while CHANS > 0: # while user_choice != chwa: # while True
	user_choice = input("Tape nonb ou a nan mitan [10, 50]: ")
	# 1st try:						# or int(user_choice) < 10 or int(user_choice) > 50
	while not user_choice.isdigit() or int(user_choice) not in range(10, 51):
		print('Ou pa tape yon bon chif. Oubyen li pa nan enteval 10-50...')
		user_choice = input("Tape nonm ou a: ")

	# 2nd try:
	'''
	try:
		user_choice = int(user_choice)
	except ValueError:
		user_choice = input("Tape nonm ou a: ")
	'''

	user_choice = int(user_choice)

	# Si chwa pi piti
	if user_choice < chwa:
		print('Sa w chwazi a pi piti ke Chwa a.')
		# CHANS = CHANS - 1
		CHANS -= 1
		print('Ou rete {0} chans'.format(CHANS))

	# Si chwa pi gwo
	elif user_choice > chwa:
		 print('Sa w chwazi a pi gwo ke Chwa a.')
		 CHANS -= 1
		 print('Ou rete {0} chans'.format(CHANS))

	# Si itilizate genyen
	else:
		print('Bravo! Ou genyen ak {0} chans'.format(CHANS))








