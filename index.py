from wtforms import Form, StringField, validators
from flask import Flask, request, render_template, url_for, make_response
import pysolr

# Create a client instance. The timeout and authentication options are not required.
solr = pysolr.Solr('http://127.0.0.1:8983/solr/lyric_core', always_commit=True)

app = Flask(__name__)

#Routes
class KeyWordForm(Form):
    results = list()
    key_word = StringField('Keyword', [validators.Length(min=1,)])


@app.route('/', methods=['GET', 'POST'])
def search():
    form = KeyWordForm(request.form)

    #initialize results to list
    form.results = list()

    if request.method == 'POST' and form.validate():
       
        print(form.key_word.data)
        result = solr.search(form.key_word.data, df="corpus")

        for res in result:
            form.results.append(res)
        

        return render_template('display.html', form=form)
    return render_template('index.html', form=form)



