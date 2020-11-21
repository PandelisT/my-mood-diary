from models.Journal import Journal
from main import db
from flask import Blueprint, request, jsonify, abort
from schemas.JournalSchema import journals_schema, journal_schema
from schemas.ClientSchema import clients_schema, client_schema
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from models.User import User
from models.Client import Client
from sqlalchemy import text


clients = Blueprint("clients", __name__, url_prefix="/clients")

@clients.route("/", methods=["POST"])
@jwt_required
def clients_create():
    
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return abort(401, description="User not found")
    
    client_fields = client_schema.load(request.json)

    is_client = Client.query.get(user.id)

    if not is_client:
    
        new_client = Client()
        new_client.username = client_fields["username"]
        new_client.fname = client_fields["fname"]
        new_client.lname = client_fields["lname"]
        
        user.client_id.append(new_client) # user = defined above; client_id is linked as relationship to user: client_id = db.relationship("Client", backref=backref("users", uselist=False)) in users table
        
        db.session.add(new_client)
        db.session.commit()
        
        return jsonify(client_schema.dump(new_client))
    
    else:
        return abort(401, description='Client Profile already exists')


@clients.route("/", methods=["GET"])
@jwt_required
def get_client_details():
    # Return client details
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    details = Client.query.filter_by(id=user.id).first()

    return jsonify(client_schema.dump(details))

@clients.route("/", methods=["PUT", "PATCH"])
@jwt_required
def client_details_update():
    # Update a journal entry
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    details = Client.query.filter_by(id=user.id)
    detail_fields = client_schema.load(request.json)
    details.update(detail_fields)
    db.session.commit()
    return jsonify(journal_schema.dump(details[0]))


# @clients.route("/", methods=["DELETE"])
# @jwt_required
# def cleint_details_delete(id):
#     # delete a journal entry
#     user_id = get_jwt_identity()
#     user = Client.query.get(user_id)
#     if not user:
#         return abort(401, description="Invalid user")
#     journal = Journal.query.filter_by(id=id, client_id_fk=user.id).first()
#     print(journal)
#     if not journal:
#         return "deleted"
#     db.session.delete(journal)
#     db.session.commit()

#     return jsonify(journal_schema.dump(journal))
