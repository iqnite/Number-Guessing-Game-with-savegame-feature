from random import randint

version = "1.2.0"
saveslot = None
savepoint = "autosave.txt"
name = ""
top = 0
num = 0
trial = 0
count = 0

def factorial(user):
    factors = []
    counter = 2
    while counter <= user:
        if user%counter == 0:
            user = user/counter
            factors.append(counter)
        else:
            counter += 1
    return factors

def start():
    global saveslot, savepoint, name, top, num, trial, count
    name =  input("Please enter your name: ")
    top = int(input("Please enter the maximum number: "))
    num = randint(1, top)
    trial = 0
    count = 0
    input("🕹️ {}, are you ready to begin?\n".format(name))

def save(savepoint):
    global saveslot, name, num, count, version
    print("⌛ Saving...")
    saveslot = open(savepoint, "w")
    saveslot.write(name + "\n" + str(num*sum(factorial(123456789))) + "\n" + str(count) + "\n" + str(sum(factorial(count))+987654321*num) + "\n" + "Number Guessing savegame file, v{} (only the last digit of the version number affects the save/load compatibility)".format(version) + "\n" + "Please do not edit this file, as you might not be able to load it after editing.\n")
    saveslot.flush()
    saveslot.close()
    print("✅ Progress saved in ./{}.\nYou can now close this window.".format(savepoint))

print("\n🔮 ### Welcome to the Number Guessing game! ### 🔮")
print("v{}\n".format(version))

if input('''💾 Load previous save point?
    [y]-[Enter] .. Load save point from file
    [Enter] ...... Start new game
    [Ctrl]+[c] ... Quit
    ''') == "y":
    savepoint = input("Please enter relative file path (leave empty to load from autosave.txt): ")
    if savepoint == "":
        savepoint = "autosave.txt"

    try:    
        saveslot = open(savepoint, "r")
        print("⌛ Checking savegame hash...")
        name = saveslot.readline().strip("\n")
        num = int(int(saveslot.readline().strip("\n"))/sum(factorial(123456789)))
        count = int(saveslot.readline().strip("\n"))
        if sum(factorial(count))+987654321*num == float(saveslot.readline()):
            print("✅ Save slot loaded successfully!\n")
        else:
            input('''❌ Invalid hash.
            This usually happens if you tried to cheat by changing the amount of trials in the file.
                [Enter] ..... Start new game
                [Ctrl]+[c] .. Cancel
                ''')
            start()
    except:
        input('''❌ File not found or corrupted.
        Maybe you selected the wrong file? If not, please check if the version of the file is compatible with the game's version and if you didn't edit the file.
            [Enter] ..... Start new game
            [Ctrl]+[c] .. Cancel
            ''')
        start()
else:
    savepoint = "autosave.txt"
    start()

while True:
    trial = input("❓ Type a number or leave empty to exit: ")
    try:
        trial = int(trial)
        count += 1
        if trial > num:
            print("➖ No, my number is lower!")
        elif trial < num:
            print("➕ No, my number is higher!")
        else:
            print("🏆 Yes, that's my number!")
            print(f"🤩 Good job, {name}! You did it in {count} trials!\n")

            '''
            if count <= round(top/2):
                print(f"🤩Good job, {name}! You did it in {count} trials!")
            else:
                print(f"😉{name}, you did it in {count} trials. Not the best score, I'm sure you can do better!")
            '''
            
            input("Press [Enter] to continue.")
            break
    except:
        break

savepoint = input('''💾 Enter the name of the savegame file (leave empty to autosave).
⚠️ WARNING: If the file exists, it will be overwritten. All data that was previously in it will be PERMANENTLY DELETED. Please check the file name before submitting it.
''')
if savepoint == "":
    savepoint = "autosave.txt"

save(savepoint)