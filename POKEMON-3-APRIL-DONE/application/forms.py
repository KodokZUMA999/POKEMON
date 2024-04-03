from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, EmailField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import IntegerField
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField, IntegerField
from wtforms.validators import DataRequired, Length
from application.utils import exists_email, not_exists_email, exists_username
    

class LoginForm(FlaskForm):
    username            = StringField("username", validators=[DataRequired()])
    password            = PasswordField("password", validators=[DataRequired()])
    submit              = SubmitField("login")

class AddFavoritePokemonForm(FlaskForm):
    pokemon_id = IntegerField("Pokemon ID", validators=[DataRequired()])
    submit = SubmitField("Add to Favorites")


class SignUpForm(FlaskForm):
    username            = StringField("username", validators=[DataRequired(), Length(min=4, max=12), exists_username])
    fullname            = StringField("full name", validators=[DataRequired(), Length(min=4, max=16)])
    email               = EmailField("email", validators=[DataRequired(), Email(), exists_email])
    password            = PasswordField("password", validators=[DataRequired(), Length(min=8)])
    confirm_password    = PasswordField("confirm password", validators=[DataRequired(), Length(min=8), EqualTo("password")])
    submit              = SubmitField("sign up")

class EditProfileForm(FlaskForm):
    username            = StringField("username", validators=[DataRequired(), Length(min=4, max=12), exists_username])
    fullname            = StringField("full name", validators=[DataRequired(), Length(min=4, max=16)])
    submit              = SubmitField("update profile")

class ResetPasswordForm(FlaskForm):
    old_password        = PasswordField("old password", validators=[DataRequired(), Length(min=8)])
    new_password        = PasswordField("new password", validators=[DataRequired(), Length(min=8)])
    confirm_new_password = PasswordField("confirm new password", validators=[DataRequired(), Length(min=8), EqualTo("new_password")])
    submit              = SubmitField("reset password")

class ForgotPasswordForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), not_exists_email])
    new_password = PasswordField("New Password", validators=[DataRequired(), Length(min=8)])
    confirm_new_password = PasswordField("Confirm New Password", validators=[DataRequired(), Length(min=8), EqualTo("new_password")])
    submit = SubmitField("Change Password")





class VerificationResetPasswordForm(FlaskForm):
    password            = PasswordField("new password", validators=[DataRequired(), Length(min=8)])
    confirm_password    = PasswordField("confirm new password", validators=[DataRequired(), Length(min=8), EqualTo("password")])
    submit              = SubmitField("reset password")

class CreatePostForm(FlaskForm):
    pokemon_id = IntegerField("Pokemon ID", validators=[DataRequired()])
    post_pic = FileField("Picture", validators=[DataRequired()])
    caption = TextAreaField("Caption")
    submit = SubmitField("Post")

class EditPostForm(FlaskForm):
    caption             = StringField("caption")
    submit              = SubmitField("update post")