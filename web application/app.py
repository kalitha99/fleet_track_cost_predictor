import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/predictCost/*": {"origins": "*"}})


def prediction(lst):
    filename = './model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
        print(lst)
    pred_value = model.predict([lst])
    return pred_value


@app.post("/predictCost")
def index():
    pred_value = 0
    numberOfServices = request.get_json().get('service')
    numberOfInsuarance = request.get_json().get('insurance')
    numberOfLicense = request.get_json().get('revenue')

    print(numberOfServices)

    feature_list = [int(numberOfServices), int(numberOfInsuarance), int(numberOfLicense)]
    print(feature_list)
    pred_value = prediction(feature_list)
    print(pred_value[0])
    val = {"prediction": pred_value[0]}
    return jsonify(val)


if __name__ == '__main__':
    app.run(port=50505)
