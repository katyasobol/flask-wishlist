from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    price = db.Column(db.Float)
    comment = db.Column(db.String(140))
    url = db.Column(db.String)
    image = db.Column(db.LargeBinary)

    def __init__(self, title, user_id, price, comment, url, image):
        self.title = title
        self.user_id = user_id
        self.price = price
        self.comment = comment
        self.url = url
        self.image = image
    
    def __repr__(self):
        return f'<post {self.id}>'

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120),nullable=False)
    book = db.Column(db.Boolean)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __init__(self, name, email, book, post_id):
        self.name = name
        self.email = email
        self.book = book
        self.post_id = post_id
    
    def __repr__(self):
        return f'<post {self.id}>'
