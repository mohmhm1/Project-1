from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the pre-trained model and tokenizer
# Here we are using GPT2 which isnt as good as GPT3 or 4 but you can preload it. If you want to run GPT3 or GPT4, youll need to use the API which i can show you how to do if your interested.

model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Define a function to generate text
# This generates text from GPT2
def generate_text(prompt, max_length=50, temperature=1.0):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=max_length, temperature=temperature, pad_token_id=tokenizer.eos_token_id)
    text = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return text

# Define the game scenarios
# add whatever you want to the games plot. You can change the prompts to GPT to make it a bit better in its reponses. 
def left_path():
    answer = input("The path you chose takes you down a hallway with a suspicious button at the end. Will you press it? ")
    if answer == "yes":
        print("The button triggered a trap which shot you with blow darts. You died. ")
    elif answer == "no":
        print("You choose to return back to where you came from but stepped on a pressure plate you missed and ended up dying to a spike trap. ")
    else:
        print("Invalid choice. Game over. ")

def right_path():
    answer = input("The path you chose takes you to an open cave with two chests in the middle. Will you open the left or right chest? ")
    if answer == "left":
        answer = input("You find a key with a red jewel in it. After proceeding through the cave you find a gate with a similar jewel imbedded at the top of it and a key slot. Do you want to insert the key and continue or return? (continue/return) ")
        if answer == "continue":
            # Generate text for this scenario
            prompt = "You open the gate and find yourself in a room with several statues and a man dressed as a mage at the end of it. He calls out to you adversarliy and says:"
            print(generate_text(prompt, max_length=100, temperature=0.8))
            while True:
                user_input = input("Choose one Rock/Paper/Scissors or flee to leave: ").lower()
                if user_input == "flee":
                    prompt = "The mage is upset and wants to fight you. He says:"
                    print(generate_text(prompt, max_length=100, temperature=0.8))
                    print("You tried to leave, angering the Mage resulting in your death.")
                    break
                elif user_input not in ["rock", "paper", "scissors"]:
                    continue
                # Continue with the rest of the game logic...

# Start the game
# game is in a while loop that will run to inifinity. Hit ctrl c to exit. 
while True:
    print(
    """
            
     ______            _        _______  _______  _______  _          _______           _       
    (  __  \ |\     /|( (    /|(  ____ \(  ____ \(  ___  )( (    /|  (  ____ )|\     /|( (    /|
    | (  \  )| )   ( ||  \  ( || (    \/| (    \/| (   ) ||  \  ( |  | (    )|| )   ( ||  \  ( |
    | |   ) || |   | ||   \ | || |      | (__    | |   | ||   \ | |  | (____)|| |   | ||   \ | |
    | |   | || |   | || (\ \) || | ____ |  __)   | |   | || (\ \) |  |     __)| |   | || (\ \) |
    | |   ) || |   | || | \   || | \_  )| (      | |   | || | \   |  | (\ (   | |   | || | \   |
    | (__/  )| (___) || )  \  || (___) || (____/\| (___) || )  \  |  | ) \ \__| (___) || )  \  |
    (______/ (_______)|/    )_)(_______)(_______/(_______)|/    )_)  |/   \__/(_______)|/    )_)
                                                                                                

    """
    )
    name = input("Type your name: ")
    print("Welcome", name, "to your adventure!")

    answer = input("You're exploring a dungeon, you come to a split end with two pathways. Do you go left or right? ")
    if answer == "left":
        left_path()
    elif answer == "right":
        right_path()
    else:
        print("Invalid choice. Game over.")

    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() != "yes":
        break
