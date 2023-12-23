from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    task_text = data['task']
    tasks.append(task_text)
    return jsonify({'success': True})

@app.route('/get_tasks')
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/remove_task', methods=['POST'])
def remove_task():
    data = request.get_json()
    task_text = data['task']
    tasks.remove(task_text)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
