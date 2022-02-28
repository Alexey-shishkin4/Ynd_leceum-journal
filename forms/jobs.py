from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    tile = StringField('Tile', validators=[DataRequired()])
    team_lead = StringField('Team leader', validators=[DataRequired()])
    duration = StringField('Duration', validators=[DataRequired()])
    collaborators = StringField('List of collaborators', validators=[DataRequired()])
    is_finished = BooleanField("Is Finished")
    submit = SubmitField('Применить')