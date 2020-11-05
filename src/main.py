from flask import Flask, request, jsonify, abort
app = Flask(__name__)
import psycopg2

connection = psycopg2.connect(
    database="my_mood_diary",
    user="postgres",
    password="postgres",
    host="localhost"
)

cursor = connection.cursor()

cursor.execute("create table if not exists journal (journal_id serial PRIMARY KEY, journal_entry varchar, date date);")
connection.commit()

@app.route("/journal", methods=["GET"])
def get_journal_entries():
    #Return all journal entries
    sql = "SELECT * FROM journal"
    cursor.execute(sql)
    journal = cursor.fetchall()
    return jsonify(journal)

@app.route("/journal/<int:id>", methods=["GET"])
def book_show(id):
    #Return a single journal entry
    sql = "SELECT * FROM journal WHERE id = %s;"
    cursor.execute(sql, (id,))
    journal_entry = cursor.fetchone()
    return jsonify(journal_entry)

@app.route("/journal", methods=["POST"])
def journal_entry_create():
    #Create a journal entry
    sql = "INSERT INTO journal (journal_entry) VALUES (%s);"
    cursor.execute(sql, (request.json["journal_entry"]))
    connection.commit()

@app.route("/journal/<int:id>", methods=["DELETE"])
def journal_entry_delete(id):
    sql = "SELECT * FROM journal WHERE id = %s;"
    cursor.execute(sql, (id,))
    journal_entry = cursor.fetchone()
    
    if journal_entry:
        sql = "DELETE FROM journal WHERE id = %s;"
        cursor.execute(sql, (id,))
        connection.commit()

    return jsonify(journal_entry)

@app.route("/journal/<int:id>", methods=["PUT", "PATCH"])
def journal_entry_update(id):
    #Update a journal entry
    sql = "UPDATE journal SET journal_entry = %s WHERE id = %s;"
    cursor.execute(sql, (request.json["journal_entry"], id))
    connection.commit()

    sql = "SELECT * FROM journal WHERE id = %s"
    cursor.execute(sql, (id,))
    book = cursor.fetchone()
    return jsonify(book)