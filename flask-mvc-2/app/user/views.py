from flask import Blueprint, render_template, request, redirect, url_for
from .models import User

user = Blueprint('user', __name__, 'static', template_folder='templates', url_prefix='/user')

users = []


@user.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        users.append(User(**request.form))
    return render_template('user/index.html', users=users)


@user.route('/<int:index>')
def delete(index):
    del users[index]
    return redirect(url_for('user.index'))
