from flask import Flask, Blueprint, render_template,redirect, request
import datetime as dt
supply_app= Blueprint('supply_app',__name__)

supply_list=[]
sno=1

@supply_app.route("/")
def home():
    return render_template("index.html")

@supply_app.route("/supply/list")
def supply_view():
	return render_template("supply/list.html",supply_list=supply_list)

@supply_app.route("/supply/read", methods=['GET'])
def supply_read():
	sno= int(request.args.get('sno','0'))
	for supply_dict in supply_list:
		if supply_dict['sno']==sno:
			return render_template("supply/read.html",supply_dict=supply_dict)
	return redirect("/supply/list")


@supply_app.route("/supply/process", methods=['GET','POST'])
def supply_process():
	global sno
	if request.method=="GET":
		return render_template("supply/write.html")
	elif request.method=="POST":
		item = request.form.get('item')
		date= request.form.get('date')
		count= int(request.form.get('count'))
		supply_dict={'sno':sno, 'item':item, 'count':count,'date':date}
		supply_list.append(supply_dict)
		sno+=1
		return redirect("/supply/list")

@supply_app.route("/supply/count_plus",methods=['post'])
def supply_plus():
	
	sno = int(request.form.get('sno','0'))
	for supply_dict in supply_list:
		if supply_dict['sno']==sno:
			supply_dict['count']+=1
	return redirect(f"/supply/read?sno={sno}")

@supply_app.route("/supply/count_minus",methods=['post'])
def count_minus():
	
	sno = int(request.form.get('sno','0'))
	for supply_dict in supply_list:
		if supply_dict['sno']==sno:
			supply_dict['count']-=1
	return redirect(f"/supply/read?sno={sno}")

@supply_app.route('/supply/delete',methods=['post'])
def delete():
	sno = int(request.form.get('sno','0'))
	for supply_dict in supply_list:
		if supply_dict['sno']==sno:
			supply_list.remove(supply_dict)
	return redirect("/supply/list")









