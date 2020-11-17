from models.Journal import Journal
from main import db
from flask import Blueprint, request, jsonify
from schemas.JournalSchema import journals_schema, journal_schema
from flask_jwt_extended import jwt_required
from services.auth_service import verify_user
import boto3
from main import db
from pathlib import Path
from  flask_jwt_extended import get_jwt_identity
from models.User import User
from sqlalchemy.orm import joinedload

journal = Blueprint("journal", __name__, url_prefix="/journal")

# Journal routes 

@journal.route("/", methods=["GET"])
@jwt_required
def get_journal_entries():
    #Return journal entries
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    journals = Journal.query.filter_by(user_id_fk=user.id).all()
    return jsonify(journals_schema.dump(journals))

@journal.route("/", methods=["POST"])
@jwt_required
def journal_entry_create():
    #Create a journal entry
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    journal_fields = journal_schema.load(request.json)
    new_journal = Journal()
    new_journal.journal_entry = journal_fields["journal_entry"]

    user.journal_entries.append(new_journal)

    db.session.add(new_journal)
    db.session.commit()

    return jsonify(journal_schema.dump(new_journal))

@journal.route("/<int:id>", methods=["GET"])
@jwt_required
# @verify_user
def journal_entry_show(id):
    # Returns a single journal entry
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    # journal_entry = Journal.query.get(id)
    journals = Journal.query.filter_by(id=id, user_id_fk=user.id).first()
    return jsonify(journal_schema.dump(journals))

@journal.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
@verify_user
def journal_entry_update(id):
    #Update a journal entry
    journal = Journal.query.filter_by(id=id)
    journal_fields = journal_schema.load(request.json)
    journal.update(journal_fields)
    db.session.commit()
    return jsonify(journal_schema.dump(journal[0]))

@journal.route("/<int:id>", methods=["DELETE"])
@jwt_required
@verify_user
def journal_entry_delete(id):
    # delete a journal entry
    journal = Journal.query.get(id)
    if not journal:
        return "deleted"
    db.session.delete(journal)
    db.session.commit()

    return jsonify(journal_schema.dump(journal))