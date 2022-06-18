from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 

db = "private_wall"

class message: 
    def __init__(self, data):
        self.id = data['id']
        self.message = data['message']
        self.receiver = data['receiver']
        self.user_id = data['user_id']
        self.sender_name = data['sender_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def new_message(cls, data):
        query = "INSERT INTO private_wall.messages (message, receiver, user_id, sender_name) VALUES (%(message)s, %(receiver)s, %(user_id)s, %(sender_name)s)"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def all_messages_for_me(cls, id):
        query = "SELECT * FROM private_wall.messages WHERE receiver = %(id)s; "
        results = connectToMySQL(db).query_db(query, {'id': id})
        messages = []
        for message in results:
            messages.append(cls(message))
        return messages

    @classmethod
    def number_of_messages_sent(cls, id):
        query = "SELECT * FROM private_wall.messages WHERE user_id = %(id)s"
        results = connectToMySQL(db).query_db(query, {'id': id})
        return len(results)

    @classmethod
    def delete_message(cls, data):
        query = "DELETE FROM private_wall.messages WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        return results
