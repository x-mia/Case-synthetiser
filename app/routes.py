from app import app
from flask import render_template, url_for, redirect, flash
from app.forms import WordForm, SubstantiiviForm, VerbiForm
from app.backend import get_postag_cls, Substantiivi, Verbi


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = WordForm()
    if form.validate_on_submit():
        return redirect(url_for('synthesis', word=form.word.data))
    return render_template('index.html', form=form)

@app.route('/synthesis/<word>', methods=['GET', 'POST'])
def synthesis(word):
    cls = get_postag_cls(word)
    form = cls.form
    if form.validate_on_submit():
        
        data = cls.get_data(form)
        synthesized = cls.synthetise(data)
        return render_template('synthesis.html', form=form, cls=cls, synthesized=synthesized)

    return render_template('synthesis.html', form=form, cls=cls)
