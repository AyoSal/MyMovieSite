
# A very simple Flask Hello World app for you to get started with...

from Flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def main():
    return render_template('fresh_tomatoes.html')
    
    
    if __name__ == "__main__":
          app.run()