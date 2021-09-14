import random


class Countdown:
    def __init__(self):
        self.vowels = ['A', 'E', 'I', 'O', 'U']
        self.consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
                           'S', 'T', 'V', 'W', 'X', 'Z']
        self.challenge_arr = []
        self.longest_word = ""

    def generate_challenge_letters(self, number_of_vowels, number_of_consonants):
        for vowel in range(0, number_of_vowels):
            self.challenge_arr += self.vowels[random.randint(0, len(self.vowels) - 1)]
        for consonant in range(0, number_of_consonants):
            self.challenge_arr += self.consonants[random.randint(0, len(self.consonants) - 1)]

    def shuffle_array_and_check_valid(self):
        if len(self.challenge_arr) == 9:
            random.shuffle(self.challenge_arr)
            return True
        self.challenge_arr = []
        return False

    def show_the_user_countdown_letters(self):
        if self.shuffle_array_and_check_valid():
            return f"Rachel: Start the clock: \n{self.challenge_arr}"
        return "Rachel: Your going to need to pick a few more letters!"
