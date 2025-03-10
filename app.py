from flask import Flask, render_template, request, session, redirect, url_for
import os
import json
from star_wars.game_data import get_game_data

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

# Add enumerate function to Jinja2 environment
app.jinja_env.globals.update(enumerate=enumerate)

# Load game data
game_data = get_game_data()

@app.route('/')
def index():
    """Display the home page with game introduction."""
    # Reset game state
    session.clear()
    return render_template('index.html')

@app.route('/character_select')
def character_select():
    """Display character selection screen."""
    return render_template('character_select.html', characters=game_data['characters'])

@app.route('/start_game', methods=['POST'])
def start_game():
    """Start the game with the selected character."""
    character_id = request.form.get('character')
    if not character_id or character_id not in game_data['characters']:
        return redirect(url_for('character_select'))
    
    # Initialize game state
    session['character'] = character_id
    session['story_path'] = []
    
    # Start with the first scene for this character
    first_scene = game_data['characters'][character_id]['first_scene']
    return redirect(url_for('scene', scene_id=first_scene))

@app.route('/scene/<scene_id>')
def scene(scene_id):
    """Display a scene with its description and choices."""
    if 'character' not in session:
        return redirect(url_for('index'))
    
    if scene_id not in game_data['scenes']:
        return redirect(url_for('game_over', ending="Error: Scene not found"))
    
    current_scene = game_data['scenes'][scene_id]
    
    # Record path taken
    if 'story_path' in session:
        session['story_path'].append(scene_id)
    
    # Check if this is an ending scene
    if 'ending' in current_scene:
        return redirect(url_for('game_over', ending=current_scene['ending']))
    
    return render_template('scene.html', 
                          scene=current_scene,
                          character=game_data['characters'][session['character']])

@app.route('/choice/<scene_id>', methods=['POST'])
def make_choice(scene_id):
    """Process the player's choice and redirect to the next scene."""
    if 'character' not in session or scene_id not in game_data['scenes']:
        return redirect(url_for('index'))
    
    choice = request.form.get('choice')
    current_scene = game_data['scenes'][scene_id]
    
    if not choice or int(choice) < 1 or int(choice) > len(current_scene['choices']):
        return redirect(url_for('scene', scene_id=scene_id))
    
    # Get the next scene based on the choice
    next_scene = current_scene['choices'][int(choice)-1]['next_scene']
    return redirect(url_for('scene', scene_id=next_scene))

@app.route('/game_over')
def game_over():
    """Display game over screen with the ending and option to play again."""
    ending = request.args.get('ending', 'Your journey has come to an end.')
    return render_template('game_over.html', ending=ending)

if __name__ == '__main__':
    app.run(debug=True) 