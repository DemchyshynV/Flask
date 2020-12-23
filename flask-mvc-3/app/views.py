from app import app, db
from flask import render_template, request
from .forms import UserForm
from .models import UserModel


@app.route('/', methods=['GET', 'POST'])
def index():
    users = UserModel.query.all()
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        data = dict(request.form)
        data.pop('save')
        user = UserModel(**data)
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
    return render_template('index.html', form=form, users=users)
