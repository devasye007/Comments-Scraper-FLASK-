import sys
sys.path.insert(0, './')  # Add root directory to Python path

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
