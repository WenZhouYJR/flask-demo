from flask_wtf import Form

from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid')
    remember_me = BooleanField('remember_me', default=False)
    zhy_name = StringField('zhy_name', validators=[DataRequired()])
    zhy_email = StringField('zhy_email', validators=[DataRequired()])