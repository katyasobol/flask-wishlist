from flask_wtf.form import FlaskForm
from wtforms import StringField, URLField, SubmitField, EmailField, FileField, BooleanField, FloatField
from wtforms.validators import InputRequired, Length, Email

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

class PostForm(FlaskForm):
    title = StringField(validators=[InputRequired(), Length(max=20)], name='title')
    price = FloatField(name='price')
    comment = StringField(name='comment')
    url = URLField(name='url')
    image = FileField(name='image', id='file-input')
    submit = SubmitField("Сохранить")

class BookForm(FlaskForm):
    name = StringField(render_kw={"placeholder": "Введите свое имя"}, name='name')
    email = EmailField(validators=[Email(message='Некорректный email')], render_kw={"placeholder": "Введите свой email"}, name='email')
    book = BooleanField()
    submit = SubmitField("Забронировать")

def verify_img(filename):
    ext = filename.rsplit('.', 1)[1].lower()
    if ext in ALLOWED_EXTENSIONS:
        return True
    return False