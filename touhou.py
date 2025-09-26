import random

_2hus = ['Reimu', 'Marisa', 'Sanae', 'Suwako', 'Kanako', 'Yukari', 
	 'Ran', 'Chen', 'Yuyuko', 'Youmu', 'Satori', 'Koishi', 'Orin', 
	 'Okuu', 'Cirno', 'Daiyousei', 'Rumia', 'Meiling', 'Koakuma', 
	 'Patchouli', 'Sakuya', 'Remilia', 'Flandre', 'Parsee', 
	 'Yuuka', 'Resin', 'Tewi', 'Mokou', 'Kaguya', 'Eirin', 
	 'Keine', 'Mystia', 'Aya', 'Momiji', 'Futo', 'Iku', 'Tenshi', 
	 'Doremy', 'Yorihime', 'Toyohime', 'Nue', 'Kogasa', 'Alice', 
	 'Junko', 'Hecatia', 'Clownpiece', 'Okina', 'Wriggle', 
	 'Nareko', 'Aunn', 'Nitori', 'Hina', 'Eiki', 'Kasen', 'Seija', 
	 'Byakuren', 'Nazrin', 'Sekibanki', 'Kokoro', 'Yuugi', 
	 'Suika', 'Lily', 'Letty', 'Sunny', 'Luna', 'Star', 'Satono', 
	 'Mai', 'Mamizou', 'Minamitsu', 'Ichirin', 'Mike', 'Kisume', 
	 'Yamame', 'Komachi', 'Kutaka', 'Mima', 'Miko', 'Joon']

def play():
	random_2hu = random.choice(_2hus)
	guess_count = 1
	hints_given = 0
	guess = input('Guess the 2hu I\'m thinking of ("idk" to give up): ')
	
	while True:
		if guess.lower() == random_2hu.lower() or guess.lower() == 'idk':
			break
		elif guess_count % 5 == 0 and hints_given < 3:
			hint_ans = input('Do you want a hint? (y/n)')
			
			while True:
				if hint_ans.lower() == 'y':
					hints_given+=1
					
					if hints_given == 1:
						print(f'The name is {len(random_2hu)} letters long.')
						guess = input('Guess the 2hu I\'m thinking of ("idk" to give up): ')
						guess_count+=1
						break
					elif hints_given == 2:
						print(f'The first letter is {random_2hu[0].lower()}.')
						guess = input('Guess the 2hu I\'m thinking of ("idk" to give up): ')
						guess_count+=1
						break
					elif hints_given == 3:
						print(f'The last letter is {random_2hu[-1].lower()}. (This is the last hint.)')
						guess = input('Guess the 2hu I\'m thinking of ("idk" to give up): ')
						guess_count+=1
						break
				elif hint_ans.lower() == 'n':
					print('Suit yourself...')
					guess = input('Nope. Try again: ')
					guess_count+=1
					break
				else:
					hint_ans = input('No breaking this program on my watch. Try again. (y/n ONLY)')
		elif guess_count % 5 != 0 or hints_given == 3:
			guess = input('Nope. Try again: ')
			guess_count+=1
	
	if guess.lower() == 'idk':
		print(f'Too bad. I was thinking of {random_2hu}.')
	else:
		print(f'Nice! I was thinking of {random_2hu}!')

ans = input('Would you like to guess the 2hu? (y/n)')

while True:
	if ans.lower() == 'y':
		play()
		ans = input('Would you like to play again? (y/n)')
	elif ans.lower() == 'n':
		print('I see how it is... Then leave...')
		break
	else:
		ans = input('No breaking this program on my watch. Try again. (y/n ONLY)')
