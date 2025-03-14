from flask import Blueprint, render_template, redirect, request

contact_app=Blueprint('contact_app',__name__)

contacts=[]
cno=1

@contact_app.route("/")
def index():
    return render_template("index.html")

@contact_app.route('/contact/list')
def con_list():
    return render_template('contact/list.html', contacts=contacts)

@contact_app.route('/contact/write', methods=['GET','POST'])
def write():
     global cno
     if request.method=='GET':
        return render_template("contact/write.html")
     elif request.method=='POST':
         name=request.form.get('name')
         tel=request.form.get('tel')
         address=request.form.get('address')
         new_con={'cno':cno, 'name':name, 'tel':tel, 'address':address}
         contacts.append(new_con)
         cno+=1
         return redirect('/contact/list')

@contact_app.route('/contact/read')
def read():
    cno=int(request.args.get('cno','0'))
    for con in contacts:
        if con['cno']==cno:
            return render_template('contact/read.html', con=con)
    return redirect('/contact/list')

@contact_app.route('/contact/update', methods=['POST'])
def update():
    cno=int(request.form.get('cno','0'))
    tel=request.form.get('tel')
    address=request.form.get('address')
    for con in contacts:
        print(cno, con)
        if con['cno']==cno:
            con['tel']=tel
            con['address']=address
    return redirect(f'/contact/read?cno={cno}')

@contact_app.route('/contact/delete', methods=['POST'])
def delete():
    cno=int(request.form.get('cno','0'))
    for con in contacts:
        if con['cno']==cno:
            contacts.remove(con)
    return redirect('/contact/list')
