from flask import Flask, render_template, redirect, url_for, flash
from forms import loginForm, registrationForm
from models import User, db, login_manager
from flask_login import login_user, login_required, logout_user
