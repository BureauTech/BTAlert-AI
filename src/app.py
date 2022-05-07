from flask import Flask, Response

from metrics.collector import Collector

collector = Collector()

app = Flask(__name__)

@app.route('/metrics')
def get_metrics():
    return Response(collector.get_metrics(), mimetype='text/plain') 

if __name__ == '__main__':
    app.run('localhost', 5050)
