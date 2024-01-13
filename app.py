from flask import Flask, render_template, request

from src.conversation_ai_fun import  ChatBot

app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    # gets a response of the AI bot
    response= chatbot.get_reply(userText)
    return response


if __name__ == "__main__":
    chatbot = ChatBot()
    app.run(debug=True)
