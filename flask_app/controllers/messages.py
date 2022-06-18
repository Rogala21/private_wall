from flask import render_template, redirect, request, session
from flask_app.__init__ import app
from flask_app.models.messages import message
from flask_app.models.login_register import user
from flask_bcrypt import Bcrypt
from flask import flash 
bcrypt = Bcrypt(app)

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template('dashboard.html', user = user.get_by_id(data), users = user.get_all_users(data['id']), messages = message.all_messages_for_me(data['id']), num_of_sent = message.number_of_messages_sent(data['id']))


@app.route('/dashboard/process', methods=['POST'])
def dashboard_process():
    message.new_message(request.form)
    return redirect('/dashboard')

@app.route('/dashboard/process/delete', methods=['POST'])
def dashboard_process_delete():
    message.delete_message(request.form)
    return redirect('/dashboard')