from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, FileField
from wtforms.validators import InputRequired, Length, Email, EqualTo, Regexp

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Введите свой юзернейм"}, name='username')
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": " Введите пароль"}, name='psw')
    submit = SubmitField("Войти")

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Введите свой юзернейм"}, name='username')
    email = EmailField(validators=[Email(message='Некорректный email')], render_kw={"placeholder": "Введите свой email"}, name='email')
    password = PasswordField(validators=[InputRequired()], render_kw={"placeholder": " Введите пароль"}, name='password')
    password2 = PasswordField(validators=[InputRequired(), EqualTo('password', message="Пароли не совпадают")], render_kw={"placeholder": "Повторите пароль"})
    firstname = StringField(validators=[InputRequired(), Length(max=20)], render_kw={"placeholder": "Введите имя"}, name='firstname')
    lastname = StringField(validators=[InputRequired(), Length(max=20)], render_kw={"placeholder": "Введите Фамилию"}, name='lastname')
    birthdate = StringField(validators=[InputRequired(), Length(max=10), Regexp(r'\d\d.\d\d.\d{4}', message='Дата вида дд.мм.гггг')], render_kw={"placeholder": "Введите дату рождения"}, name='birthdate')
    img = FileField(name='img', id='file-input')
    submit = SubmitField("Зарегистрироваться")