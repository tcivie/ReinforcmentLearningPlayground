from flask import Flask, render_template, request
from simulations import lunar_lander

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lunar_lander')
def lunar_lander_route():
    # Reset the Lunar Lander simulation
    lunar_lander.lunar_lander.reset()

    # Render a template that includes the game interface
    return render_template('simulation.html', sim_name='Lunar Lander')

@app.route('/game_frame')
def game_frame():
    # Get the current state of the Lunar Lander simulation
    state = lunar_lander.lunar_lander.get_state()

    # Return it as a JSON object
    return state

@app.route('/action', methods=['POST'])
def action():
    # Get the action from the request body
    action = int(request.data)

    # Apply the action to the Lunar Lander simulation
    lunar_lander.lunar_lander.step(action)

    # Return an empty response
    return '', 204

if __name__ == '__main__':
    app.run()
