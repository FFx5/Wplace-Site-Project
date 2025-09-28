import random
from pyscript import Element

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
	 'Yamame', 'Komachi', 'Kutaka', 'Mima', 'Miko', 'Joon', 'Chimata']

# --- Game state ---
random_2hu = None
guess_count = 0
hints_given = 0

def start_game(event=None):
    global random_2hu, guess_count, hints_given
    random_2hu = random.choice(_2hus)
    guess_count = 0
    hints_given = 0
    Element("game-output").write("Game started! Guess the 2hu!")

def submit_guess(event=None):
    global random_2hu, guess_count, hints_given
    guess = Element("user-input").element.value.strip()
    Element("user-input").element.value = ""  # clear box
    guess_count += 1

    if guess.lower() == random_2hu.lower():
        Element("game-output").write(f"Nice! It was {random_2hu}!")
    elif guess.lower() == "idk":
        Element("game-output").write(f"Too bad! I was thinking of {random_2hu}.")
    elif guess_count % 5 == 0 and hints_given < 3:
        hints_given += 1
        if hints_given == 1:
            Element("game-output").write(f"Hint: The name has {len(random_2hu)} letters.")
        elif hints_given == 2:
            Element("game-output").write(f"Hint: The first letter is {random_2hu[0]}.")
        elif hints_given == 3:
            Element("game-output").write(f"Hint: The last letter is {random_2hu[-1]}. (Last hint!)")
    else:
        Element("game-output").write("Nope, try again!")

# Bind buttons to functions
Element("start-btn").element.onclick = start_game
Element("submit-btn").element.onclick = submit_guess
