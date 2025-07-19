from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from database import init_db, register_outing, check_in, get_pending_students, get_logs

app = Flask(__name__)
app.secret_key = 'your-very-secure-secret'  # Required for session

@app.route('/')
def index():
    return render_template('index.html', is_admin=session.get('is_admin'))

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    password = data.get('password')
    if password == "admin123":
        session['is_admin'] = True
        return jsonify({'message': 'Login successful'})
    return jsonify({'message': 'Incorrect password'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('is_admin', None)
    return jsonify({'message': 'Logged out'})

@app.route('/admin/pending')
def pending():
    if not session.get('is_admin'):
        return jsonify({'error': 'Unauthorized'}), 403
    return jsonify(get_pending_students())

@app.route('/student/logs/<student_id>')
def student_logs(student_id):
    return jsonify(get_logs(student_id))

@app.route('/student/register', methods=['POST'])
def register():
    student_id = request.json.get('student_id')
    register_outing(student_id)
    return jsonify({'message': 'Outing registered'})

@app.route('/student/checkin', methods=['POST'])
def checkin():
    student_id = request.json.get('student_id')
    check_in(student_id)
    return jsonify({'message': 'Checked in successfully'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
