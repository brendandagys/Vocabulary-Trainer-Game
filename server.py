from flask import Flask, request
from flask_cors import CORS

from vocabulary_trainer import Game
from definition_dict import definition_dict

import json
import os
import uuid


games_dict = {}


ORIGIN = os.environ['ORIGIN'] if 'ORIGIN' in os.environ else 'http://localhost:3000'
PORT = os.environ['PORT'] if 'PORT' in os.environ else 5000


app = Flask(__name__)
CORS(app, resources={
     r'/api/*': {'origins': ORIGIN}})  # https://brendandagys.com


@app.route('/api/health', methods=['GET'])
def health():
    return 'Healthy!'


@app.route('/api/games', methods=['GET'])
def get_games():
    return json.dumps(len(games_dict))


@app.route('/api/get-game-id', methods=['GET'])
def get_game_id():
    ''' Creates and stores a new Game based on a UUID, and returns the UUID. '''
    game_id = str(uuid.uuid1())
    games_dict[game_id] = None
    return game_id


@app.route('/api/check-if-game-is-started', methods=['POST'])
def check_if_game_is_started():
    request_body_dict = json.loads(request.data)

    if 'game_id' not in request_body_dict:
        return 'Please provide a `game_id`.', 400

    game_id = request_body_dict['game_id']

    if game_id not in games_dict:
        return 'Please provide a valid `game_id`.', 400

    # print(games_dict[game_id])
    if games_dict[game_id]:
        return json.dumps(True)
    return json.dumps(False)


@app.route('/api/get-game', methods=['POST'])
def get_game():
    ''' If a valid `game_id` is provided, returns the Game. '''
    request_body_dict = json.loads(request.data)

    if 'game_id' not in request_body_dict:
        return 'Please provide a `game_id`.', 400

    game_id = request_body_dict['game_id']

    if game_id not in games_dict:
        return 'Please provide a valid `game_id`.', 400

    return games_dict[game_id].send_data()


@app.route('/api/start-game', methods=['POST'])
def start_game():
    '''
        - Creates and returns a Game when provided with a valid `game_id` and `num_words_to_play` 
    '''
    request_body_dict = json.loads(request.data)

    game_id = request_body_dict['game_id'] if 'game_id' in request_body_dict else None

    num_words_to_play = request_body_dict['num_words_to_play'] if 'num_words_to_play' in request_body_dict else None

    # If both fields are sufficiently given...create, store, and return a Game
    if game_id and num_words_to_play:
        if game_id not in games_dict:
            return 'Please provide a valid `game_id`.', 400

        if not num_words_to_play.isnumeric() or int(num_words_to_play) < 1:
            return 'Please provide a numeric value > 0 for `num_words_to_play`.', 400

        game = Game(game_id, definition_dict, int(num_words_to_play))
        games_dict[game_id] = game

        return game.send_data()

    # Determine which or both are missing and send 400 response
    else:
        separator = ' and ' if not game_id and not num_words_to_play else ''
        game_id = game_id if game_id else ''
        num_words_to_play = num_words_to_play if num_words_to_play else ''

        return f'Please provide {game_id}{separator}{num_words_to_play}.'


@app.route('/api/make-guess', methods=['POST'])
def handle_guess():
    ''' 
        - `game_id` identifies a unique game. Not required in first request.
        - If `num_words_to_play` is ever provided, existing games are replaced
        - Either `num_words_to_play` or `guess` must be provided with `game_id`
    '''
    # print(request.data) # Raw binary..?
    request_body_dict = json.loads(request.data)

    game_id = request_body_dict['game_id'] if 'game_id' in request_body_dict else None

    guess = request_body_dict['guess'] if 'guess' in request_body_dict else None

    if game_id and guess:
        if game_id not in games_dict:
            return 'Please provide a valid `game_id`.', 400

        game = games_dict[game_id]
        return game.take_client_input(guess)

    # Determine which or both are missing and send 400 response
    else:
        separator = ' and ' if not game_id and not guess else ''
        game_id = game_id if game_id else ''
        guess = guess if guess else ''

        return f'Please provide {game_id}{separator}{guess}.'


if __name__ == '__main__':
    print(f'API server running on port {PORT}...')

    from waitress import serve
    serve(app, listen=f'*:{PORT}')  # IPv4 and IPv6
    # serve(app, host='0.0.0.0', port=PORT)  # IPv4 only

    # app.run(host='0.0.0.0', port=PORT)
