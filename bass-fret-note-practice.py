import random

bass_string_dict = {
    "estring_notes": "E string",
    "astring_notes": "A string",
    "dstring_notes": "D string",
    "gstring_notes": "G string"
}

estring_notes = {
    "F": 1,
    "F#": 2,
    "G": 3,
    "G#": 4,
    "A": 5,
    "A#": 6,
    "B": 7,
    "C": 8,
    "C#": 9,
    "D": 10,
    "D#": 11,
}

astring_notes = {
    "A#": 1,
    "B": 2,
    "C": 3,
    "C#": 4,
    "D": 5,
    "D#": 6,
    "E": 7,
    "F": 8,
    "F#": 9,
    "G": 10,
    "G#": 11,
}

dstring_notes = {
    "D#": 1,
    "E": 2,
    "F": 3,
    "F#": 4,
    "G": 5,
    "G#": 6,
    "A": 7,
    "A#": 8,
    "B": 9,
    "C": 10,
    "C#": 11,
}

gstring_notes = {
    "G#": 1,
    "A": 2,
    "A#": 3,
    "B": 4,
    "C": 5,
    "C#": 6,
    "D": 7,
    "D#": 8,
    "E": 9,
    "F": 10,
    "F#": 11,
}

def generate_note(bass_string):
    if bass_string == "estring_notes":
        bass_string = estring_notes

    elif bass_string == "astring_notes":
        bass_string = astring_notes

    elif bass_string == "dstring_notes":
        bass_string = dstring_notes
        
    elif bass_string == "gstring_notes":
        bass_string = gstring_notes

    note = random.choice(list(bass_string.keys()))
    return [note, bass_string[note]];

def random_string():
    string = random.choice(list(bass_string_dict.keys()))
    return string;

def guess_note():
    current_string = random_string() 
    note_to_find = generate_note(current_string)

    print(f'On the {bass_string_dict[current_string]}')
    print(f'Find: {note_to_find[0]}')
    for i in range(2):
        answer = input(f'Enter your answer here: ')

        if answer == '':
            print('Please input a number...')

        else:
            if int(answer) == note_to_find[1]:
                print("Correct answer!")
                return True
            else:
                print("Try again...")


def main():

#TODO: add mode for fret -> note mode as well

    score = 0
    guess_amount = int(input("How many notes do you want to guess: "))

    for i in range(guess_amount):
        if guess_note() == True:
            score += 1

    print(f'Your final score was {score} / {guess_amount}')

if __name__ == "__main__":
    main()
