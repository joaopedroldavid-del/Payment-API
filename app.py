from flask import Flask
from repository.database import db
from db_models.payment import Payment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
app.config['SECRET_HEY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app)

@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    return jsonify({"message": "The payment has been created"})

# Simulation route of a financial institution
@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confimation():
    return jsonify({"message": "The payment has been confirmed"})

@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    return 'pagamento pix'

if __name__ == '__main__':
    app.run(debug=True)