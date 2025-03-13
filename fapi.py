from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
import uvicorn

app = FastAPI()

# Path to the game files
GAME_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Project1')
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

@app.get("/")
def index():
    """Serve the index.html file"""
    if os.path.exists(os.path.join(GAME_PATH, 'index.html')):
        return FileResponse(os.path.join(GAME_PATH, 'index.html'))
    
    root_index = os.path.join(ROOT_DIR, 'index.html')
    if os.path.exists(root_index):
        return FileResponse(root_index)
    
    raise HTTPException(status_code=404, detail=str(os.listdir()))

@app.get("/{path:path}")
def serve_file(path: str):
    """Serve any requested file from either root or game directory"""
    # Check if the requested file is in the root directory
    root_path = os.path.join(ROOT_DIR, path)
    if os.path.exists(root_path) and os.path.isfile(root_path):
        return FileResponse(root_path)
    
    # Otherwise check in the game directory
    game_path = os.path.join(GAME_PATH, path)
    if os.path.exists(game_path) and os.path.isfile(game_path):
        return FileResponse(game_path)
    
    raise HTTPException(status_code=404, detail="File not found")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)