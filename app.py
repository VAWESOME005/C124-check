from flask import Flask, jsonify, request

app = Flask(__name__)

task = [
    {
        'id' : 1,
        'title' : 'Math Homework',
        'desc' : 'Chapter 3.1',
        'done' : False
    },
    {
        'id' : 2,
        'title' : 'Science Homework',
        'desc' : 'Inertia Lab Report #1',
        'done' : True
    }
]

# print(task[-1])

@app.route('/test')
def test():
    return "Hello, this is a test"

@app.route('/')
def get_task():
    return jsonify({
        'data' : task
    })

@app.route('/add-data', methods = ["POST"])
def add_task():
    # checks if in json structure
    print(request.json)
    if not request.json:
        return jsonify({
            'status' : 'error',
            'message' : 'Please put data in JSON format'
    })
    
    new_task = {
        'id' : task[-1]['id'] + 1,
        'title' : request.json['title'],
        'desc' : request.json.get('desc', ''),
        'done' : False

    }

    task.append(new_task)

    return jsonify({
        'status' : 'success',
        'message': 'Task added succesfully!'
    })



if(__name__ == '__main__'):
    app.run(debug = True)