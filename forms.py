from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, RadioField, DecimalField, SelectField
from wtforms.validators import DataRequired, Length

class HeartDiseaseForm(FlaskForm):
    name = StringField("Name",
                        validators=[DataRequired(),
                                    Length(min=2, max=20)])

    age = IntegerField("Age",
                        validators=[DataRequired()])

    # sex = RadioField("Sex", choices=[(1,"Male"), (0,"Female")])
    sex = SelectField("Sex", choices = [(1, "Male"), (0, "Female")])

    cp = SelectField("Chest Pain Type",
                    choices=[(0, "Typical Angina"),
                             (1, "Atypical Angina"),
                             (2, "Non-Anginal Pain"),
                             (3, "Asymptomatic")])

    trestbps = IntegerField("Blood Pressure",
                            validators=[DataRequired()])

    chol = IntegerField("Cholestoral",
                        validators=[DataRequired()])

    fbs = SelectField(label="Fasting Blood Sugar",
                     choices=[(1, "True"),
                              (0, "False")])

    restecg = SelectField(label="Resting Electrocardiographic results",
                        choices=[(0, "Normal"),
                                 (1, "Having ST-T Wave Abnormality"),
                                 (2, "Showing probable or definite left ventricular hypertrophy by Estes' criteria")])

    thalach = IntegerField(label="Maximum Heart Rate",
                           validators=[DataRequired()])

    exang = SelectField(label="Exercise Induced Angina",
                       choices=[(1, "Yes"),
                                (0, "No")])

    oldpeak = DecimalField(label="ST Depression Induced By Exercise",
                           validators=[DataRequired()])

    slope = SelectField(label="The Slope Of The Peak Exercise ST Segment",
                       choices=[(0, "Upsolping"),
                                (1, "Flat"),
                                (2, "Downsloping")])

    ca = IntegerField(label="Number Of Major Vessels Colored By Flourosopy",
                      validators=[DataRequired()])
