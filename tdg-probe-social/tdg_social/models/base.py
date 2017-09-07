# -*- coding: utf-8 -*-
__author__ = 'himanshujain.2792'

from tdg_social import db

class Base(db.Model):
    __abstract__ = True

    id = db.Column('id', db.Integer, primary_key=True)
    created_at = db.Column('created_at', db.DateTime(timezone=True), default=db.func.current_timestamp())
    updated_at = db.Column('updated_at', db.DateTime(timezone=True),default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())

    def create(self):
        db.session.add(self)
        db.session.commit()
        db.session.flush()

    def update(self):
        db.session.commit()
        db.session.flush()

    def bulk_insert(self, data):
        db.session.bulk_insert_mappings(self, data)
        db.session.commit()
        db.session.flush()

    def last_updated_id(self, class_name):
        return db.session.query(class_name).order_by(class_name.id.desc()).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()