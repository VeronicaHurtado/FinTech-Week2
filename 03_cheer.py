import time;

# Create a variable named cheer and give it a word to cheer (i.e. Python or FinTech)
cheer = "Python"

# Below strings can be used to add fun
cheer_symbol = "*\O/*"
cheer_symbol_2 = "ヘ( ^o^)ノ＼(^_^ )"

# Loop through string and print each letter with a cheer
for letter in cheer:
    print(f"Give me a {letter}!")
    time.sleep(0.5)
    print(f"{letter}!")
    time.sleep(0.5)

# Print excitement to screen
print("\nWhat does that spell?!")
print(cheer + "!\nWoohoo! Go " + cheer + "!")
print(cheer_symbol * 3)
print(cheer_symbol_2)
