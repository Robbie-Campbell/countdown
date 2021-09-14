from components.lookups import Lookup


class UserActions:
    def __init__(self, guess, countdown):
        self.guess = guess
        self.countdown = countdown

    def take_a_guess(self):
        dictionary = Lookup(self.guess, self.countdown.challenge_arr)
        longest_word = dictionary.get_longest_possible_word()
        valid_guess = self.check_guess_is_valid() and dictionary.check_word_is_in_dictionary()
        if valid_guess:
            return f"Congratulations! You guessed right with a word of length: {len(self.guess)}\n" \
                   f"The longest word i could find was: {longest_word} at a length of {len(longest_word)}"
        return f"That was not a valid guess sadly.\nThe longest word i could find was: {longest_word} at a length of " \
               f"{len(longest_word)}"

    def check_guess_is_valid(self):
        self.guess = self.guess.upper()
        for letter in self.guess:
            if letter in self.countdown.challenge_arr:
                self.countdown.challenge_arr.remove(letter)
                continue
            else:
                return False
        return True
