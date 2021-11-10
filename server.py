from flask import Flask, request

from vocabulary_trainer import Game
from definition_dict import definition_dict

import json


games_dict = {}


app = Flask(__name__)


@app.route('/', methods=['POST'])
def start_game():
    ''' - `client_id` must be always provided, to either begin or resume a game.
        - If `num_words_to_play` is ever provided, existing games are replaced
        - Either `num_words_to_play` or `guess` must be provided with `client_id`
    '''
    request_body_dict = json.loads(request.data)
    # print(request.data) # Raw binary..?

    if 'client_id' not in request_body_dict:
        return 'Please provide `client_id`.', 400

    client_id = request_body_dict['client_id']

    # If a game already exists...
    if client_id in games_dict:
        game = games_dict[client_id]

        # If a game exists and we aren't restarting, continue playing...
        if 'num_words_to_play' not in request_body_dict:
            if 'guess' not in request_body_dict:
                return 'Please provide `guess`.', 400

            guess = request_body_dict['guess']

            return game.take_client_input(guess)

    # Otherwise, create a brand new game
    if 'num_words_to_play' not in request_body_dict:
        return 'Please provide `num_words_to_play`.', 400

    num_words_to_play = request_body_dict['num_words_to_play']

    if not num_words_to_play.isnumeric() or num_words_to_play < 1:
        return 'Please provide a numeric value > 0 for `num_words_to_play`.'

    game = Game(definition_dict, num_words_to_play)
    games_dict[client_id] = game

    return game.send_response()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
