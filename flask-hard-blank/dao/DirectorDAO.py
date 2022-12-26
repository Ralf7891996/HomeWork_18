from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def create(self, director):
        self.session.add(director)
        self.session.commit()
        return director

    def update(self, update_director):
        self.session.add(update_director)
        self.session.commit()
        return update_director

    def delete(self, did):
        delete_movie = self.get_one(did)
        self.session.delete(delete_movie)
        self.session.commit()