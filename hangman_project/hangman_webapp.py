import streamlit as st
import random
import json
import os

# --- CONFIGURATION & CONSTANTS ---
LEADERBOARD_FILE = 'leaderboard.json'
GAMEWORDS = ["owl","bunny","elephant","fox","camel","orangutan","zebra","antelope","baboon","cheetah","dolphin","elephant","flamingo","gorilla","hyena","iguana","jaguar","koala","lemur","meerkat","narwhal","ocelot","panda","quetzal","rhino","salamander","toucan"]
STAGES = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# --- LEADERBOARD FUNCTIONS ---
def load_leaderboard():
    try:
        with open(LEADERBOARD_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_leaderboard(word, attempts, result):
    leaderboard = load_leaderboard()
    leaderboard.append({'word': word, 'attempts': attempts, 'result': result})
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(leaderboard, f, indent=4)

def display_leaderboard():
    st.subheader("🏆 Leaderboard (Top 10 Wins)")
    leaderboard = load_leaderboard()
    wins = sorted([s for s in leaderboard if s['result'] == 'win'], key=lambda x: x['attempts'])
    if not wins:
        st.write("No wins recorded yet. Be the first!")
    else:
        for i, score in enumerate(wins[:10]):
            st.write(f"{i+1}. Guessed '{score['word']}' with {score['attempts']} wrong attempts.")

# --- GAME LOGIC ---
def initialize_game():
    """Sets up a new game in the session state."""
    st.session_state.randomword = random.choice(GAMEWORDS)
    st.session_state.hanglist = ["_"] * len(st.session_state.randomword)
    st.session_state.attempts = 0
    st.session_state.guesslist = []
    st.session_state.game_over = False
    st.session_state.message = ""

def handle_guess(guess):
    """Processes a single user guess."""
    if not guess.isalpha() or len(guess) != 1:
        st.session_state.message = "Please enter a single letter."
        return

    guess = guess.lower()

    if guess in st.session_state.guesslist:
        st.session_state.message = f"You already guessed '{guess}'. Try again."
        return

    st.session_state.guesslist.append(guess)

    if guess in st.session_state.randomword:
        st.session_state.message = f"Correct! '{guess}' is in the word."
        for i, letter in enumerate(st.session_state.randomword):
            if letter == guess:
                st.session_state.hanglist[i] = guess
    else:
        st.session_state.message = f"Incorrect! '{guess}' is not in the word."
        st.session_state.attempts += 1

    # Check for win/loss
    if "_" not in st.session_state.hanglist:
        st.session_state.game_over = True
        save_leaderboard(st.session_state.randomword, st.session_state.attempts, 'win')
    elif st.session_state.attempts >= 5:
        st.session_state.game_over = True
        save_leaderboard(st.session_state.randomword, st.session_state.attempts, 'loss')

# --- UI & APP LAYOUT ---
st.title("Hangman! - Animal Edition")

# Initialize game state if it doesn't exist
if 'randomword' not in st.session_state:
    initialize_game()

# --- Game Over View ---
if st.session_state.game_over:
    if "_" not in st.session_state.hanglist:
        st.success(f"CONGRATULATIONS, YOU WON! The word was '{st.session_state.randomword}'.")
    else:
        st.error(f"GAME OVER! The word was '{st.session_state.randomword}'.")
    
    st.code(STAGES[st.session_state.attempts], language='text')
    
    if st.button("Play Again?"):
        initialize_game()
        st.rerun()
    
    display_leaderboard()

# --- Active Game View ---
else:
    # Display Hangman ASCII art
    st.code(STAGES[st.session_state.attempts], language='text')

    # Display the word to guess
    st.header(" ".join(st.session_state.hanglist))

    # Display game message
    if st.session_state.message:
        st.info(st.session_state.message)

    # User input
    with st.form(key="guess_form", clear_on_submit=True):
        guess = st.text_input("Guess a letter:", max_chars=1, key="guess_input")
        submit_button = st.form_submit_button("Submit Guess")

        if submit_button:
            handle_guess(guess)
            st.rerun() # Use the modern rerun command

    # Display guessed letters
    st.write(f"**Guessed letters:** {', '.join(sorted(st.session_state.guesslist))}")
    st.write(f"**Wrong attempts:** {st.session_state.attempts} / 5")
