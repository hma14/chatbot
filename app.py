from flask import Flask, request, render_template
from server.chat import start_chat
#import jsonify

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
  content = request.form.get('text')
  chat_reply = start_chat(content)
  return chat_reply


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
