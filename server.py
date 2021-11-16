from flask import Flask, request
from flask_cors import CORS

from vocabulary_trainer import Game
from definition_dict import definition_dict

import json
import os
import uuid


games_dict = {}


app = Flask(__name__)
CORS(app)  # , resources={r'*': {'origins': '*'}})


@app.route('/api/health', methods=['GET'])
def health():
    return 'Healthy!'


@app.route('/api/games', methods=['GET'])
def get_games():
    return json.dumps(len(games_dict))


@app.route('/api', methods=['POST'])
def game_handler():
    ''' - `game_id` identifies a unique game. Not required in first request.
        - If `num_words_to_play` is ever provided, existing games are replaced
        - Either `num_words_to_play` or `guess` must be provided with `game_id`
    '''
    request_body_dict = json.loads(request.data)
    # print(request.data) # Raw binary..?

    # Ensure that `game_id` is set
    if 'game_id' in request_body_dict:
        # The client's initial status check. An ID or a Game will be returned
        if request_body_dict['game_id'] == '':
            return str(uuid.uuid1())
        else:
            game_id = request_body_dict['game_id']
    else:
        game_id = str(uuid.uuid1())

    # If a game already exists...
    if game_id in games_dict:
        game = games_dict[game_id]

        # AND we aren't restarting, continue playing...
        if 'num_words_to_play' not in request_body_dict:
            if 'guess' not in request_body_dict:
                return game.send_response()
                # return 'Please provide `guess`.', 400

            guess = request_body_dict['guess']

            return game.take_client_input(guess)

    # Game doesn't exist or does but is restarting
    if 'num_words_to_play' not in request_body_dict:
        return 'Please provide `num_words_to_play`.', 400

    num_words_to_play = str(request_body_dict['num_words_to_play'])

    if not num_words_to_play.isnumeric() or int(num_words_to_play) < 1:
        return 'Please provide a numeric value > 0 for `num_words_to_play`.'

    game = Game(game_id, definition_dict, int(num_words_to_play))
    games_dict[game_id] = game

    return game.send_response()


PORT = os.environ['PORT'] if 'PORT' in os.environ else 5000

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
