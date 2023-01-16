import psycopg2
from base64 import b64encode, b64decode
from flask import render_template, redirect, request, url_for
from flask_login import current_user, login_required

from app import db
from app.posts import blueprint
from app.posts.forms import PostForm, BookForm, verify_img
from app.posts.models import Post, Book

@blueprint.route('/wish', methods=['POST', 'GET'])
@login_required
def new_post():
    form = PostForm()
    if request.method == "POST" and form.validate_on_submit() and verify_img(request.files['image'].filename):
        try:
            image = b64encode(request.files['image'].read())
            p = Post(title=request.form['title'], price=request.form['price'], url=request.form['url'], image=image, user_id=current_user.id, comment=request.form['comment'])
            db.session.add(p)
            db.session.commit()
        except:
            db.session.rollback()
            return render_template('layout/page-404.html')
        return redirect(url_for('profiles.profile', user_id=current_user.id))
    return render_template('posts/new_post.html', form=form)

@blueprint.route('/wish/<int:post_id>', methods=['POST', 'GET'])
def post(post_id):
    forms = None
    image = None
    for form in db.session.query(Post).where(Post.id == post_id):
        forms = form
        image = b64decode(form.image)
    return render_template('posts/post.html', form=forms, image=image, post_id=post_id)

@blueprint.route('/<int:posts_id>', methods=['POST', 'GET'])
def posts(posts_id):
    books = []
    user_id = None
    post_id = None
    post = db.session.query(Post).where(Post.user_id == posts_id)
    for u in post:
        user_id = u.user_id
        post_id = u.id
    for p in db.session.query(Book).where(Book.book == True):
        books.append(p.post_id)
    return render_template('posts/posts.html', form=post, book=books, user_id=user_id, post_id=post_id)

@blueprint.route('/<int:post_id>/update', methods=['POST', 'GET'])
@login_required
def post_upd(post_id):
    post_id = None
    if request.method == 'POST':
        try:
            for post in db.session.query(Post).where(Post.user_id == current_user.id):
                post.title = request.form.get('title') if request.form.get('title') else post.title
                post.price = request.form.get('price') if request.form.get('price') else post.price
                post.comment = request.form.get('comment') if request.form.get('comment') else post.comment
                post.url = request.form.get('url') if request.form.get('url') else post.url
                post.image = b64encode(request.files['image'].read()) if request.files['image'] and verify_img(request.files['image'].filename) else post.image
                post_id = post.id
                db.session.commit()
                return redirect(url_for('profiles.profile', user_id=current_user.id))
        except:
                return render_template('layout/page-404.html')
    return render_template('posts/post_upd.html', post_id=post_id)

@blueprint.route('/<int:post_id>/delete', methods=['POST', 'GET'])
@login_required
def delete(post_id):
    try:
        book_id = None
        post = Post.query.get(post_id)
        for p in db.session.query(Book).where(Book.post_id == post.id):
            book_id = p.id
        if book_id != None:
            book = Book.query.get(book_id)
            db.session.delete(book)
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('posts', post_id=post_id))
    except:
        db.session.rollback()
        return 'mistake'

@blueprint.route('/book/<int:post_id>', methods=['POST', 'GET'])
def book(post_id):
    form = BookForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            booked = True if request.form['book'] else False
            for post in db.session.query(Post).where(Post.id == post_id):
                postid = post.id
                p = Book(name=request.form['name'], email=request.form['email'], book=booked, post_id=postid)
                db.session.add(p)
                db.session.commit()
            return redirect(url_for('posts.post', post_id=post_id))
        except:
            db.session.rollback()
            print("Ошибка добавления в БД")
            return render_template('layout/page-404.html')
    return render_template('posts/book.html', form=form)

@blueprint.route('/no_wish', methods=['POST', 'GET'])
def no_wish():
    return render_template('posts/no_wish.html')

