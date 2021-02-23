from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#init
app = Flask(__name__)

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://webadmin:FMZkon18745@10.100.2.193:5432/KitchenWare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#init db
db = SQLAlchemy(app)
#init
ma = Marshmallow(app)

#catergory Class/Model
class Catergorys(db.Model):
    id = db.Column(db.String(4), primary_key=True, unique=True)
    name = db.Column(db.String(50))
    size = db.Column(db.String(10))
    
    
    def __init__(self, id, name, size):
        self.id = id
        self.name = name
        self.size = size
       

# catergory Schema
class CatergorySchema(ma.Schema):
    class Meta:
        fields =('id','name' , 'size')

# Init Schema 
catergory_schema = CatergorySchema()
catergorys_schema = CatergorySchema(many=True)

# Get All catergory
@app.route('/catergory', methods=['GET'])
def get_catergorys():
    all_catergorys = Catergorys.query.all()
    result = catergorys_schema.dump(all_catergorys)
    return jsonify(result)

# # Get Single catergory
# @app.route('/catergory/<id>', methods=['GET'])
# def get_catergory(id):
#     catergory = catergory.query.get(id)
#     return catergory_schema.jsonify(catergory)

# # Create a catergory
# @app.route('/catergory', methods=['POST'])
# def add_catergory():
#     id = request.json['id']
#     name = request.json['name']
#     size = request.json['size']

#     new_catergory = catergory(id, name, size)

#     db.session.add(new_catergory)
#     db.session.commit()

#     return catergory_schema.jsonify(new_catergory)

# # Update a catergory
# @app.route('/catergory/<id>', methods=['PUT'])
# def update_catergory(id):
#     catergory = catergory.query.get(id)
    
#     name = request.json['name']
#     size = request.json['size']

#     catergory.name = name
#     catergory.size = size

#     db.session.commit()

#     return catergory_schema.jsonify(catergory)

# # Delete catergory
# @app.route('/catergory/<id>', methods=['DELETE'])
# def delete_catergory(id):
#     catergory = catergory.query.get(id)
#     db.session.delete(catergory)
#     db.session.commit()
    
#     return catergory_schema.jsonify(catergory)

# Web Root Hello
@app.route('/', methods=['GET'])
def get():
    return jsonify({'WELCOME TO KITCHEN WARE STORE'})

# Run Server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)