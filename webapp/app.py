from flask import Flask, render_template, request, redirect, session, url_for
from database import (
    register_user,
    login_user,
    add_group,
    add_person,
    add_hardware,
    list_hardware,
)

app = Flask(__name__)
app.secret_key = 'changeme'


@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    hardware = list_hardware()
    return render_template('index.html', hardware=hardware, user=session['user'])


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login_user(username, password):
            session['user'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Login failed')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if register_user(username, password):
            session['user'] = username
            return redirect(url_for('index'))
        else:
            return render_template('register.html', error='Username exists')
    return render_template('register.html')


@app.route('/add_hardware', methods=['GET', 'POST'])
def add_hw():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        group_id = request.form.get('group_id') or None
        person_id = request.form.get('person_id') or None
        group_id = int(group_id) if group_id else None
        person_id = int(person_id) if person_id else None
        add_hardware(name, group_id, person_id)
        return redirect(url_for('index'))
    return render_template('add_hardware.html')


@app.route('/add_group', methods=['POST'])
def add_grp():
    name = request.form['name']
    add_group(name)
    return redirect(url_for('add_hw'))


@app.route('/add_person', methods=['POST'])
def add_prs():
    name = request.form['name']
    add_person(name)
    return redirect(url_for('add_hw'))


if __name__ == '__main__':
    app.run(debug=True)
