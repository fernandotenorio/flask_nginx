import random
import time
from flask import Flask
app = Flask(__name__)

def do_nothing(n=1000):
	for _ in range(n):
		x = (random.random() - random.random())**2		
		

@app.route('/')
def hello_world():
    do_nothing()
    time.sleep(0.1)
    return 'Hello world, again!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')