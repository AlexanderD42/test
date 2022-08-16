import json
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'zawxescrdvftbgynuhm'

class taskform(FlaskForm):
    task = StringField('Input Task', validators = [DataRequired()])
    add = SubmitField('Add')

@app.route('/', methods=['POST', 'GET'])
def index():
    formapp = taskform()

    data = None

    with open('tasks.txt', 'r') as file:
        data = file.read()

        if data != '':
            data = json.loads(data)
        else:
            data = {'tasks': []}

        tasks = data.get('tasks')
        session['tasks'] = tasks
    


    if formapp.validate_on_submit():
        
        with open('tasks.txt', 'w') as file:
            data.get('tasks').append(formapp.task.data)

            
           

            strData = json.dumps(data)
            file.write(strData)

    
        return redirect(url_for('index'))


    return render_template('layout.html', form=formapp, tasks=session['tasks'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 