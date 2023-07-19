from flask import Flask, render_template, request, jsonify
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
    return jsonify(state)

@app.route('/action', methods=['POST'])
def action():
    # Get the action from the request body
    action = int(request.data)

    # Apply the action to the Lunar Lander simulation and store results
    results = []
    done = False
    while not done:
        observation, reward, done, info = lunar_lander.lunar_lander.step(action)
        results.append({
            'observation': observation.tolist(),  # JSONify observation
            'reward': reward,
            'done': done
        })

    # If game is done, reset the environment
    if done:
        lunar_lander.lunar_lander.reset()

    # Return results
    return jsonify(results)

if __name__ == '__main__':
    app.run()
