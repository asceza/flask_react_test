# https://www.youtube.com/watch?v=YW8VG_U-m48
# https://www.youtube.com/watch?v=7LNl2JlZKHA
# https://www.youtube.com/watch?v=Q2eafQYgglM
# https://stackoverflow-com.translate.goog/questions/60544939/cors-issues-for-flask-api-call-from-react-both-in-localhost?_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=ru&_x_tr_pto=sc



from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/data', methods=['POST', 'GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def main():
    if request.method == "OPTIONS":
        # return jsonify({"data": "send OPTIONS from flask server"})
        pass
    elif request.method == "POST":
        data = request.json
        word = data['word']
        synonyms = data['synonyms']
        text = data['text']
        print(word)
        return jsonify({"data": f"{text} modified"})
        # return jsonify({"data": "send POST from flask server"})


# @app.route('/', methods=['POST', 'GET'])
# def index():
#     return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
