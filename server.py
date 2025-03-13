from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Path to the game files
GAME_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Project1')

@app.route('/')
def index():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    # Check if the requested file is in the root directory
    root_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists(os.path.join(root_dir, path)):
        return send_from_directory(root_dir, path)
    
    # Otherwise check in the game directory
    return send_from_directory(GAME_PATH, path)

if __name__ == '__main__':
    port = 5000
    print(f"Game server running at http://localhost:{port}/")
    app.run(host='0.0.0.0', port=port, debug=True)