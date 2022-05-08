from flask import Flask, Response

from metrics.collector import Collector


app = Flask(__name__)
collector = Collector()

@app.route('/metrics')
def get_metrics():
    return Response(collector.get_metrics(), mimetype='text/plain')

if __name__ == '__main__':
    app.run('localhost', 5050)
