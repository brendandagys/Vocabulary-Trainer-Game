import random
import json


class Word:
    '''Each instantiation represents one word in a user's game.'''

    def __init__(self, word, definition):
        self.word = word
        self.definition = definition

        self.length = len(word)

        self.letters_shown = 0
        self.cannot_score = False  # Turns True when a hint is provided

        self.done_guessing = False  # A Game will know to instantiate a new Word

    def take_guess(self, guess):
        guess = str(guess).strip().lower()

        # If the guess is correct and they are allowed to score (no hints), end guessing
        if guess == self.word.strip().lower() and self.cannot_score is False:
            self.done_guessing = True

        # If they want a hint...
        elif guess == '=':
            # Flag that they can now cannot score, and provide an extra letter
            self.cannot_score = True
            self.letters_shown += 1

            # If the hint reveals the full word, end guessing
            if self.letters_shown == self.length:
                self.done_guessing = True

        # If the guess is incorrect, flag score cancellation and end guessing
        else:
            self.cannot_score = True
            self.done_guessing = True


class Game:
    '''Takes a dictionary of word: definition and the count of words to train on.'''

    def __init__(self, game_id, definition_dict, num_words_to_play):
        self.game_id = game_id

        self.definition_list = list(definition_dict.items())  # [(,), (,)]

        if int(num_words_to_play) > len(self.definition_list):
            return '400 ERROR'

        self.num_words_to_play = int(num_words_to_play)
        self.current_word_number = 0

        self.words_used = []  # Only for end of game
        self.indexes_used = []

        self.current_index = None
        self.current_word_instance = None

        self.score = 0
        self.game_over = False

        self.instantiate_word()

    def get_random_index(self):
        '''Defined separately to allow recursion in `self.get_random_index()`'''
        return random.randint(0, len(self.definition_list) - 1)

    def set_random_index(self):
        '''Generate a new random index within the length of the provided dictionary.'''
        self.current_index = self.get_random_index()

        while self.current_index in self.indexes_used:
            self.current_index = self.get_random_index()

        self.indexes_used.append(self.current_index)

    def instantiate_word(self):
        '''Generates a new Word instance for the current game.'''
        self.set_random_index()
        self.current_word_number += 1

        # Returns tuple from a list of tuples
        word, definition = self.definition_list[self.current_index]

        self.current_word_instance = Word(word, definition)

    def take_client_input(self, input):
        '''Applies the body of the request to the current Word instance.'''
        self.current_word_instance.take_guess(input)

        # Never take input once the game is over
        if self.game_over:
            return self.send_response()

        # If guessing for the Word is over...
        if self.current_word_instance.done_guessing:
            # Only for end of game
            self.words_used.append(self.current_word_instance.word)

            # Increment the score if they guessed correctly with no hints...
            if not self.current_word_instance.cannot_score:
                self.score += 1

            # Initiate a new Word. This increments `self.current_word_number`
            self.instantiate_word()

            # If you've played all of your desired words, mark the game as over
            if self.current_word_number > self.num_words_to_play:
                self.current_word_number -= 1  # Otherwise it's 1-too-high in final results
                self.game_over = True

        return self.send_response()

    def send_response(self):
        return json.dumps({
            'game_id': self.game_id,
            'game_over': self.game_over,
            'word_letters_revealed': None if self.game_over else self.current_word_instance.word[:self.current_word_instance.letters_shown],
            'num_words_to_play': self.num_words_to_play,
            'words_used': self.words_used,
            'current_word_number': self.current_word_number,
            'definition': None if self.game_over else self.current_word_instance.definition,
            'score': self.score,
        })


if __name__ == '__main__':
    from definition_dict import definition_dict

    game = Game(definition_dict, 3)

    game.send_response()
    game.take_client_input('=')
    game.take_client_input('=')
    game.take_client_input('My guess')
