from flask import Flask
app = Flask(__name__)
thisdict = {
  "tasks": [
    {
      "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
      "done": 0,
      "id": 1,
      "title": "Buy groceries"
    },
    {
      "description": "Need to find a good Python tutorial on the web",
      "done": 0,
      "id": 2,
      "title": "Learn Python"
    },
    {
      "description": "",
      "done": 0,
      "id": 3,
      "title": "Read a book"
    }
  ]
}




@app.route('/')
def index():
    return thisdict

@app.route('/gett/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, thisdict["tasks"])
    if len(task) == 0:
        Flask(404)
    return Flask({'task': task[0]})


if __name__ == '__main__':
    app.run(debug=True)