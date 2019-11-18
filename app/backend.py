from estnltk import synthesize
from estnltk import Text
from app.forms import VerbiForm, SubstantiiviForm

def get_postag_cls(word):
    postag = get_postag(word)
    if postag == "S":
        return Substantiivi(word)
    elif postag == "V":
        return Verbi(word)
    else:
        print("Postag not supported")
        return None

def get_postag(word):
    word = Text(word)
    word.tag_analysis()
    postag = word['words'][0]['analysis'][0]['partofspeech']
    return postag

class Substantiivi:
    def __init__(self, word):
        self.word = word
        self.form = SubstantiiviForm()

    def get_data(self, form):
        return form.number.data + ' ' + form.case.data

    def synthetise(self, case):
        return synthesize(self.word, case)

class Verbi:
    def __init__(self, word):
        self.word = word
        self.form = VerbiForm()

    def get_data(self, form):
        return form.number.data

    def synthetise(self, case):
        return synthesize(self.word, case)
