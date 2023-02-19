from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def index():
  return "<h1>from myhome22222, Flask!</h1>"

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(host="0.0.0.0", port=port, debug=True) 
