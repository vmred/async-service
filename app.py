import random

from flask import Flask, request

app = Flask(__name__)


@app.route('/get_document')
def hello():
    r = random.randint(1, 5)
    print('--->', request.url)
    if r == 3:
        return {'status': 'success', 'url': 'https://google.com'}
    return {'status': 'pending'}


if __name__ == '__main__':
    app.run()
