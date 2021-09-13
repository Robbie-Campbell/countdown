from decouple import config
import itertools
import requests
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

    def get_all_permutations(self):
        for combo in itertools.permutations(''.join(self.challenge_arr[:x])):
            print(combo)


class UserActions:
    def __init__(self, guess):
        self.guess = guess.upper()
        self.countdown = Countdown()

    def take_a_guess(self):
        dictionary = DictionaryCheckup(self.guess)
        valid_guess = self.check_guess_is_valid() and dictionary.check_word_is_in_dictionary()
        if valid_guess:
            return f"Congratulations! You guessed right with a word of length: {len(self.guess)}"
        return "That was not a valid guess sadly."

    def check_guess_is_valid(self):
        for letter in self.guess:
            if letter in countdown.challenge_arr:
                continue
            else:
                return False
        return True


class DictionaryCheckup:
    def __init__(self, word):
        self.app_key = config('SECRET_DICTIONARY_API_KEY')
        self.word = word

    def check_word_is_in_dictionary(self):
        response = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{self.word}"
                                f"?key={self.app_key}")
        return True if "meta" in response.json()[0] else False


if __name__ == "__main__":
    countdown = Countdown()
    countdown.generate_challenge_letters(3, 6)
    print(countdown.show_the_user_countdown_letters())
    user_guess = input("Please input a guess")
    user = UserActions(user_guess)
    print(user.take_a_guess())
    print(countdown.get_all_permutations())
