from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def create(self, genre):
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, update_genre):
        self.session.add(update_genre)
        self.session.commit()
        return update_genre

    def delete(self, gid):
        delete_genre = self.get_one(gid)
        self.session.delete(delete_genre)
        self.session.commit()