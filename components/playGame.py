from components.gameLogic import Countdown
from components.userActions import UserActions


class PlayGame:
    def __init__(self):
        self.countdown = Countdown()
        self.user = UserActions(None, self.countdown)

    def set_guess(self):
        guess = input("Please input a guess...\n")
        self.user.guess = guess

    def begin_challenge(self):
        self.countdown.generate_challenge_letters(3, 6)
        print(self.countdown.show_the_user_countdown_letters())
        self.set_guess()

    def start(self):
        self.begin_challenge()
        print(self.user.take_a_guess())