from pymongo import MongoClient


def iterate_mod_questions_in_mongo(mongo_connection,separator=False):
    mongo_client = MongoClient(mongo_connection)
    bankdomain_db = mongo_client.bankdomain
    mod_questions_coll = bankdomain_db.mod_questions
    mod_questions_in_db = mod_questions_coll .find()
    for el in mod_questions_in_db:
        text_totl = el["question"].lower() + "\n"+ el["answer"].lower()+"\n"
        text_tokens = text_totl.split()
        yield text_tokens

