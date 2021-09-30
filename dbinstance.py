# from https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/firestore/cloud-client/snippets.py
#
import traceback
import logging
from datetime import datetime

# Singleton class for db
class DBInstance:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(DBInstance)
            return cls.instance
        return cls.instance

    def __init__(self):
        try:
            from google.cloud import firestore
            self.db = firestore.Client()
        except Exception as e:
            logging.error(traceback.format_exc())

    def logs_add(self, data):
        try:
            db = self.db
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            db.collection(u'logs').document(now).set(data)
        except Exception as e:
            logging.error(traceback.format_exc())

    def logs_get_all(self):
        try:
            db = self.db
            return db.collection(u'logs').stream()
        except Exception as e:
            logging.error(traceback.format_exc())

    def logs_get_ids(self):
        try:
            db = self.db
            return db.collection(u'logs')
        except Exception as e:
            logging.error(traceback.format_exc())

    def users_add(self, user_id, user):
        try:
            db = self.db
            db.collection(u'users').document(user_id).set(user)
        except Exception as e:
            logging.error(traceback.format_exc())

    def users_get_all(self):
        try:
            db = self.db
            return db.collection(u'users').stream()
        except Exception as e:
            logging.error(traceback.format_exc())

    def users_get_by_id(self, user_id):
        try:
            db = self.db
            user = db.collection(u'logs').document(user_id).get()
            if user.exists:
                return user.to_dict()
            return
        except Exception as e:
            logging.error(traceback.format_exc())
