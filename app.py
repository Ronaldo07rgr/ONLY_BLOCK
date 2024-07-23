from flask import Flask, request, render_template
from scraper.scraper import login_and_scrape

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        username = request.form['username']
        password = request.form['password']
        content = login_and_scrape(url, username, password)
        return render_template('content.html', content=content)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
