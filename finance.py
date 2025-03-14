from flask import Flask, Blueprint, render_template,redirect, request
import datetime as dt
finance_app= Blueprint('finance_app',__name__)

finance_list=[]
fno=1
price_total=0



@finance_app.route("/finance/list")
def finance_view():
	global price_total
	price_total=0
	for finance_dict in finance_list:
		price_total += finance_dict['price']
	return render_template("finance/list.html",finance_list=finance_list,price_total= price_total)

@finance_app.route("/finance/read", methods=['GET'])
def finance_read():
	fno= int(request.args.get('fno'))
	for finance_dict in finance_list:
		if finance_dict['fno']==fno:
			return render_template("finance/read.html",finance_dict=finance_dict)
	return redirect("/finance/list")

@finance_app.route("/finance/process", methods=['GET','post'])
def finance_process():
	global fno 
	if request.method=='GET':
		return render_template("finance/write.html")
	elif request.method=='POST':
		item = request.form.get('item')
		price= int(request.form.get('price'))
		date = request.form.get('date')
		finance_dict={'fno':fno, 'item':item, 'price':price, 'date':date}
		finance_list.append(finance_dict)
		fno+=1
		return redirect("/finance/list")

@finance_app.route("/finance/update", methods=['POST'])
def finance_update():
	fno = int(request.form.get('fno','0'))
	date = request.form.get('date')
	price= int(request.form.get('price'))
	for finance_dict in finance_list:
		if finance_dict['fno']==fno:
			finance_dict['price']=price
			finance_dict['date']=date
			return redirect(f"/finance/list?fno={fno}")
	return redirect("/finance/list")

@finance_app.route('/finance/delete',methods=['POST'])
def delete():
	fno= int(request.form.get('fno','0'))
	for finance_dict in finance_list:
		if finance_dict['fno']==fno:
			finance_list.remove(finance_dict)
	return redirect("/finance/list")






