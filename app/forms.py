from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class WordForm(FlaskForm):
    word = StringField('Write word', validators=[DataRequired()])
    submit = SubmitField('Next')

class VerbiForm(FlaskForm):
    number = SelectField('Number', [DataRequired()],
                        choices=[('ma', 'MA infinitive'), ('da', 'DA infinitive'), ('des', 'DES form'), ('n', '1. person sg active'),('b', '3. person sg active'),
                                ('o', '2. person sg imperative'), ('ge', '2. person pl imperative'), ('neg o', 'Negative 2. person sg imperative'),
                                ('neg ge', 'Negative 2. person pl imperative') , ('ks', 'Conditional'), ('neg nuks', 'Conditional negative'), ('neg', 'Negative'),
                                ('nud', 'NUD-participe'), ('tud', 'TUD-participe'), ('v', 'Active participe'), ('tav', 'Active impersonal participe'), ('sin', '1. person sg past simple'),
                                ('sid', '2. person sg or 3. person pl past simple'), ('s', '3. person sg past simple'), ('takse', 'Impersonal'),
                                ('ta', 'Impersonal negative'), ('ti', 'Impersonal past simple')])

    submit = SubmitField('Next')

class SubstantiiviForm(FlaskForm):
    number = SelectField('Number', [DataRequired()],
                        choices=[('sg', 'Singular'),
                                 ('pl', 'Plural')])

    case = SelectField('Case', [DataRequired()],
                        choices=[( 'n', 'Nominative'), ('g', 'Genitive'), ('p', 'Partitive'), ('ill', 'Illative'), ('adt', 'Illative shortform'),
                                 ('in', 'Inessive'), ('el', 'Elative'), ('all', 'Allative'), ('ad', 'Adessive'), ('abl', 'Ablative'), ('ab', 'Abessive'),
                                 ('kom', 'Komitative'), ('es', 'Essive'), ('ter', 'Terminative'), ('tr', 'Translative')])

    submit = SubmitField('Next')
