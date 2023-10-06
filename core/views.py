from flask import render_template, Blueprint, redirect, url_for
import numpy as np
from core.forms import COVIDForm
from keras.models import load_model

core = Blueprint('core', __name__)

@core.route('/')
def index():
    return render_template('home.html')

@core.route('/about')
def about():
    return render_template('about.html')

@core.route('/assess', methods=['GET','POST'])
def assess():

    form = COVIDForm()

    if form.validate_on_submit():
        print("hello")
        responses = np.zeros(20)
        responses[0] = form.breathing.data
        responses[1] = form.fever.data
        responses[2] = form.dry_cough.data
        responses[3] = form.sore_throat.data
        responses[4] = form.running.data
        responses[5] = form.asthma.data
        responses[6] = form.lung_disease.data
        responses[7] = form.headaches.data
        responses[8] = form.heart_disease.data
        responses[9] = form.diabetes.data
        responses[10] = form.hyper_tension.data
        responses[11] = form.fatigue.data
        responses[12] = form.gastrointestinal.data
        responses[13] = form.abroad.data
        responses[14] = form.exposed.data
        responses[15]= form.gathering.data
        responses[16] = form.public.data
        responses[17] = form.family.data
        responses[18] = form.mask.data
        responses[19] = form.sanitization.data

        model = load_model('tfmodel')
        responses.shape = (1,20)

        prediction = model.predict(responses)

        print("\n")
        print(prediction)
        print("\n")
        if(prediction<0.5):
            prediction = 0
        else:
            prediction = 1

        return redirect(url_for('core.result',prediction=prediction))

    
    return render_template('assess.html', form=form)

@core.route('/result/<float:prediction>')
def result(prediction):
    return render_template('result.html',prediction=prediction)