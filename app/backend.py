from estnltk.vabamorf.morf import synthesize
from estnltk import Text
from app.forms import VerbiForm, SubstantiiviForm

def get_postag_cls(word):
    postag = get_postag(word)
    if postag == "S" or postag == "A" or postag == "H" or postag == "C" or postag == "N" or postag == "O" or postag == "P":
        return Substantiivi(word)
    elif postag == "V":
        return Verbi(word)
    else:
        print("Postag not supported")
        return None

def get_postag(word):
    word = Text(word)
    postag = word.tag_layer().morph_analysis["partofspeech"][0][0]
    return postag

class Substantiivi:
    def __init__(self, word):
        word = Text(word)
        self.word = word.tag_layer().morph_analysis["lemma"][0][0]
        self.form = SubstantiiviForm()

    def get_data(self, form):
        return form.number.data + ' ' + form.case.data

    def synthetise(self, case):
        return synthesize(self.word, case)

class Verbi:
    def __init__(self, word):
        word = Text(word)
        self.word = word.tag_layer().morph_analysis["lemma"][0][0]
        self.form = VerbiForm()

    def get_data(self, form):
        return form.number.data

    def synthetise(self, case):
        return synthesize(self.word, case)
