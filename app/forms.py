from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email, Length

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Register")

# ✅ Login Form
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Login")

# ✅ Add Vehicle Form
class VehicleForm(FlaskForm):
    name = StringField("Vehicle Name", validators=[DataRequired()])
    model = StringField("Model")
    year = StringField("Year")
    submit = SubmitField("Add Vehicle")

# ✅ Maintenance Form
class MaintenanceForm(FlaskForm):
    service_type = StringField("Service Type", validators=[DataRequired()])
    date = DateField("Date", validators=[DataRequired()])
    cost = FloatField("Cost")
    notes = TextAreaField("Notes")
    submit = SubmitField("Add Maintenance")
