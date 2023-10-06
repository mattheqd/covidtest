from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField
from wtforms.validators import DataRequired

class COVIDForm(FlaskForm):
    breathing = RadioField('Are you having difficulty breathing?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    fever = RadioField('Do you have a fever?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    dry_cough = RadioField('Do you have a dry cough?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    sore_throat = RadioField('Do you have a sore throat?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    running = RadioField('Do you have a runny nose?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    asthma = RadioField('Do you have asthma?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    lung_disease = RadioField('Do you have chronic lung disease?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    headaches = RadioField('Are you experiencing headaches?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    heart_disease = RadioField('Do you have heart disease?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    diabetes = RadioField('Are you diabetic?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    hyper_tension = RadioField('Do you have hyper tension?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    fatigue = RadioField('Have you felt fatigue?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    gastrointestinal = RadioField('Do you have gastrointenstinal issues?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    abroad = RadioField('Have you been abroad?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    exposed = RadioField('Have you had contact with a COVID patient', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    gathering = RadioField('Have you attended a large gathering?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    public =  RadioField('Have you often visited publically exposed places?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    family = RadioField('Do you have family working in exposed areas?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    mask = RadioField('Do you consistently wear a mask?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    sanitization = RadioField('Do you use sanitization at markets?', choices=[(1,'Yes'), (0,'No')], validators=[DataRequired()])
    submit = SubmitField('Submit')