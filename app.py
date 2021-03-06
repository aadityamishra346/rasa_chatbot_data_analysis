from flask import Flask , render_template

# creates a Flask application, named app
app = Flask(__name__)

# a route to display our html page gotten from [react-chat-widget](https://github.com/mrbot-ai/rasa-webchat)
@app.route("/")
def index():  
    return render_template('jumbotron.html')

# run the application
if __name__ == "__main__":  
    app.run(debug=True)


  