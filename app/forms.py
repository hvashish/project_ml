from flask_wtf import Form
from flask_wtf import Form as FlaskForm
from wtforms import TextField, StringField, PasswordField, HiddenField, validators, DateField,TextAreaField,SelectField,\
    MultipleFileField,IntegerField,FieldList, FormField, BooleanField
from flask_wtf.file import FileField, FileAllowed,FileRequired
from wtforms.fields.html5 import DateField, DateTimeField,DateTimeLocalField
from wtforms.validators import DataRequired, Optional,Email, Length, NumberRange
from wtforms.widgets import HiddenInput,TextArea
import datetime

class BIGOS_form(Form):
    gsmData = FileField(validators=[FileRequired(), FileAllowed(['xlsx', 'csv'])], id="content_area")
    umtsData = FileField(validators=[FileRequired(), FileAllowed(['xls', 'xlsx', 'csv'])], id="content-area", )
    lteData = FileField(validators=[FileRequired(), FileAllowed(['xls', 'xlsx', 'csv'])], id="content-area", )
    nrData = FileField(validators=[FileRequired(), FileAllowed(['xls', 'xlsx', 'csv'])], id="content-area", )

