from models.Journal import Journal
from main import db
from flask import Blueprint, request, jsonify
from schemas.JournalSchema import journals_schema, journal_schema
journal = Blueprint("journal", __name__, url_prefix="/journal")


@journal.route("/", methods=["GET"])
def get_journal_entries():
    #Return journal entries
    journals = Journal.query.all()
    serialised_data = journals_schema.dump(journals)
    return jsonify(serialised_data)

@journal.route("/", methods=["POST"])
def journal_entry_create():
    #Create a journal entry
    journal_fields = journal_schema.load(request.json)
    new_journal = Journal()
    new_journal.journal_entry = journal_fields["journal_entry"]

    db.session.add(new_journal)
    db.session.commit()

    return jsonify(journal_schema.dump(new_journal))

@journal.route("/<int:id>", methods=["GET"])
def journal_entry_show(id):
    # Returns a single journal entry
    journal_entry = Journal.query.get(id)
    return jsonify(journal_schema.dump(journal_entry))

@journal.route("/<int:id>", methods=["PUT", "PATCH"])
def journal_entry_update(id):
    #Update a journal entry
    journal = Journal.query.filter_by(id=id)
    journal_fields = journal_schema.load(request.json)
    journal.update(journal_fields)
    db.session.commit()
    return jsonify(journal_schema.dump(journal[0]))

@journal.route("/<int:id>", methods=["DELETE"])
def journal_entry_delete(id):
    # delete a journal entry
    journal = Journal.query.get(id)
    if not journal:
        return "deleted"
    db.session.delete(journal)
    db.session.commit()

    return jsonify(journal_schema.dump(journal))