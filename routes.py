from flask import Blueprint, render_template, request, send_file
from .scraper import scrape_comments

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            csv_file = scrape_comments(url)
            return send_file(csv_file, as_attachment=True)
        except Exception as e:
            return f"<h3>Error: {str(e)}</h3>"
    return render_template('index.html')
