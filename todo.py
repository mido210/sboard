from flask import Blueprint, redirect, render_template, request
import datetime as dt

todo_app = Blueprint('todo_app',__name__)

todos = []
tno = 1

@todo_app.route("/")
def home():
    return render_template("index.html")

@todo_app.route("/todo/list")
def index():
    return render_template('todo/list.html', todos=todos)

# 할일 작성
@todo_app.route("/todo/write", methods=['get','post'])
def write():
    global tno
    if request.method=='GET':
        return render_template('todo/write.html', todos = todos)
    elif request.method=='POST':
        title = request.form.get('title')
        date_str = dt.datetime.now().strftime("%Y-%m-%d")
        deadline = request.form.get('date')
        content = request.form.get('content')
        new_todo = {'tno':tno, 'title':title, 'date_str':date_str, 'deadline':deadline, 'content':content, 'finish':False}
        todos.append(new_todo)
        tno+=1
        return redirect('/todo/list')

# 할일 항목 출력
@todo_app.route("/todo/read", methods=['get'])
def read():
    tno = int(request.args.get('tno'))
    for todo in todos:
        if todo['tno']==tno:
            return render_template('todo/read.html', todo=todo)
    return redirect("/todo/list")

# 완료 처리
@todo_app.route("/todo/finish", methods=['post'])
def finish():
    tno = int(request.form.get('tno'))
    for todo in todos:
        if todo['tno']==tno:
            todo['finish']=True
    return redirect(f"/todo/read?tno={tno}")

# 삭제
@todo_app.route("/todo/delete", methods=['post'])
def delete():
    tno = int(request.form.get('tno'))
    for todo in todos:
        if todo['tno']==tno:
            todos.remove(todo)
    return redirect("/todo/list")