from models.Journal import Journal
from models.Client import Client
from main import db
from flask import Blueprint, request, jsonify, abort
from schemas.JournalSchema import journals_schema, journal_schema
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from models.User import User
from sqlalchemy import text


journal = Blueprint("journal", __name__, url_prefix="/journal")


@journal.route("/", methods=["GET"])
@jwt_required
def get_journal_entries():
    # Return all journal entries for a user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    journals = Journal.query.filter_by(client_id_fk=user.id).all()
    return jsonify(journals_schema.dump(journals))


@journal.route("/recent", methods=["GET"])
@jwt_required
def get_recent_journal_entries():
    # Returns most recent journal entries for a user
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    journals = Journal.query.filter_by(client_id_fk=user.id).order_by(Journal.journal_date.desc()).limit(3).all()
    return jsonify(journals_schema.dump(journals))


@journal.route("/", methods=["POST"])
@jwt_required
def journal_entry_create():
    # Create a journal entry
    user_id = get_jwt_identity()
    user = Client.query.get(user_id)
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
def journal_entry_show(id):
    # Returns a single journal entry
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    journals = Journal.query.filter_by(id=id, client_id_fk=user.id).first()
    return jsonify(journal_schema.dump(journals))


@journal.route("/<int:year>/<int:month>/<int:day>", methods=["GET"])
@jwt_required
def journal_entries_date(year, month, day):
    # Returns journal entries for a selected date
    user_id = get_jwt_identity()
    user = Client.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    # sql_query = text(f"SELECT * FROM  journal WHERE DATE(journal_date) = '{year}-{month}-{day}' and client_id_fk='{user.id}';")
    # result = db.engine.execute(sql_query)
    result = Journal.date_filter(year, month, day, user.id)
    result_as_list = result.fetchall()

    journal_list = []
    for entry in result_as_list:
        journal_list.append({"id": entry.id, "journal_entry": entry.journal_entry})
    return jsonify(journal_list)


@journal.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
def journal_entry_update(id):
    # Update a journal entry
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    journal = Journal.query.filter_by(id=id, client_id_fk=user.id)
    journal_fields = journal_schema.load(request.json)
    journal.update(journal_fields)
    db.session.commit()
    return jsonify(journal_schema.dump(journal[0]))


@journal.route("/<int:id>", methods=["DELETE"])
@jwt_required
def journal_entry_delete(id):
    # delete a journal entry
    user_id = get_jwt_identity()
    user = Client.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    journal = Journal.query.filter_by(id=id, client_id_fk=user.id).first()
    print(journal)
    if not journal:
        return "deleted"
    db.session.delete(journal)
    db.session.commit()

    return jsonify(journal_schema.dump(journal))
