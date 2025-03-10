# Star Wars Adventure Game

A "Choose Your Own Adventure" web application set in the Star Wars universe, built with Python and Flask.

## Features

- Interactive storytelling with multiple branching paths
- Three character paths: Jedi Padawan, Rebel Pilot, and Bounty Hunter
- Star Wars themed UI with animations and sound effects
- Responsive design that works on desktop and mobile devices

## Prerequisites

- Python 3.7 or higher
- Flask

## Installation

1. Clone this repository or download the source code.

2. Create a virtual environment (recommended):

   ```
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Make sure your virtual environment is activated.

2. Start the Flask development server:

   ```
   python app.py
   ```

3. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

- `app.py` - The main Flask application
- `game_data.py` - Contains all the game content and story paths
- `star_wars_adventure.py` - The original command-line version of the game
- `templates/` - HTML templates for the web interface
- `static/` - Static files (CSS, JavaScript, images, sounds)

## Adding Content

To add more story paths or modify existing ones, edit the `game_data.py` file. The game data is structured as a dictionary with scenes and choices.

## Credits

- Star Wars and all related characters, locations, and concepts are the property of Lucasfilm Ltd. and Disney.
- This is a fan project created for educational purposes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
