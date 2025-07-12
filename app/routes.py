from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Vehicle, Maintenance
from .forms import VehicleForm, MaintenanceForm, LoginForm, RegisterForm
from . import db

main = Blueprint('main', __name__)

# 🔗 Home redirects to dashboard
@main.route('/')
def home():
    return redirect(url_for('main.register'))

# ✅ Dashboard
@main.route('/dashboard')
@login_required
def dashboard():
    vehicles = Vehicle.query.filter_by(owner_id=current_user.id).all()
    return render_template('dashboard.html', vehicles=vehicles)

# ✅ Add Vehicle
@main.route('/add-vehicle', methods=['GET', 'POST'])
@login_required
def add_vehicle():
    form = VehicleForm()
    if form.validate_on_submit():
        new_vehicle = Vehicle(
            name=form.name.data,
            model=form.model.data,
            year=form.year.data,
            owner_id=current_user.id
        )
        db.session.add(new_vehicle)
        db.session.commit()
        flash('✅ Vehicle added successfully!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('add_vehicle.html', form=form)

# ✅ Maintenance
@main.route('/maintenance/<int:vehicle_id>', methods=['GET', 'POST'])
@login_required
def maintenance(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    if vehicle.owner_id != current_user.id:
        flash('❌ Access denied!', 'danger')
        return redirect(url_for('main.dashboard'))

    form = MaintenanceForm()
    if form.validate_on_submit():
        new_record = Maintenance(
            vehicle_id=vehicle.id,
            service_type=form.service_type.data,
            date=form.date.data,
            cost=form.cost.data,
            notes=form.notes.data
        )
        db.session.add(new_record)
        db.session.commit()
        flash('🛠️ Maintenance record added!', 'success')
        return redirect(url_for('main.maintenance', vehicle_id=vehicle.id))

    maintenance_records = Maintenance.query.filter_by(vehicle_id=vehicle.id).order_by(Maintenance.date.desc()).all()
    return render_template('maintenance.html', form=form, vehicle=vehicle, maintenance=maintenance_records)

# ✅ Login
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('🔓 Logged in successfully!', 'success')
            return redirect(url_for('main.dashboard'))
        flash('❌ Invalid email or password', 'danger')
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Check if user already exists
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("Email already registered.", "danger")
            return redirect(url_for('main.register'))

        # Create new user
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful. Please log in.", "success")
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)


# ✅ Logout
@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('🔒 You have been logged out.', 'info')
    return redirect(url_for('main.login'))
