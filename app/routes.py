from app import app
from flask import render_template, url_for, redirect, flash
from app.forms import WordForm, SubstantiiviForm, VerbiForm
from app.backend import get_postag_cls, Substantiivi, Verbi
from app.word_finding import get_meaning
from pandas import read_csv


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/synthesis', methods=['GET', 'POST'])
def synthesis_intro():
    form = WordForm()
    if form.validate_on_submit():
        return redirect(url_for('synthesis', word=form.word.data))
    return render_template('synthesis_intro.html', form=form)

@app.route('/synthesis/<word>', methods=['GET', 'POST'])
def synthesis(word):
    cls = get_postag_cls(word)
    form = cls.form
    if form.validate_on_submit():

        data = cls.get_data(form)
        synthesized = cls.synthetise(data)
        return render_template('synthesis.html', form=form, cls=cls, synthesized=synthesized)

    return render_template('synthesis.html', form=form, cls=cls)

@app.route("/dictionary", methods=['GET', 'POST'])
def dict_intro():
    form = WordForm()
    if form.validate_on_submit():
        return redirect(url_for('dictionary', word=form.word.data))
    return render_template('dict_intro.html', form=form)

@app.route('/dictionary/<word>')
def dictionary(word):
    data = read_csv("sonaraamat4.csv")
    entry = get_meaning(word, data)
    return render_template('dictionary.html', word=word, entry=entry)
