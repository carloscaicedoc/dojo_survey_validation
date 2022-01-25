from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def save(cls, data):
        query = """INSERT INTO dojos (location, name, language, comment) 
            VALUES (%(location)s, %(name)s, %(language)s, %(comment)s);"""
        return connectToMySQL("dojo_survey_schema").query_db(query, data)
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL("dojo_survey_schema").query_db(query, data)
        return cls(results[0])
    
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['location']) < 3:
            flash("ERROR: A location needs to be selected!")
            is_valid = False
        if len(dojo['name']) < 3:
            flash("ERROR: Name must be at least 3 characters!")
            is_valid = False
        if len(dojo['language']) < 2:
            flash("ERROR: Language must be at least 4 characters!")
            is_valid = False
        if len(dojo['comment']) < 4:
            flash("ERROR: Comment must be at least 5 characters!")
            is_valid = False
        return is_valid
        