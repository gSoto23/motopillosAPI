from flask import Flask, request, jsonify
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import credential
from notifications import sendEmail

# Generate a flask instance
app = Flask(__name__)
CORS(app)
# Create an API object
api = Api(app)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(credential.dbuser, credential.dbpass,
                                                                              credential.dbhost, credential.dbport,
                                                                              credential.dbname)
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


@app.route('/products', methods=['GET'])
def get_products():
    res = db.engine.execute("SELECT * FROM products")
    prod_list = []
    for prd in res:
        prod_data = {'id': prd.id, 'code': prd.code, 'name': prd.name, 'price': prd.price, 'pricedist': prd.pricedist,
                     'stock': prd.stock,
                     'image': prd.image, 'description': prd.description, 'promo': prd.promo,
                     'preorder': prd.preorder, 'tag': prd.tag, 'modelo': prd.modelo, 'year': prd.year,
                     'color': prd.color, 'marca': prd.marca, 'origen': prd.origen}
        prod_list.append(prod_data)
    return {'products': prod_list}, 200


@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.get_json()
    received_email = data['mail']
    subject = data['subject']
    body_message = data['order']
    sendEmail(received_email, subject, body_message)
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run(debug=True)
