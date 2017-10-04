from flask import Flask, abort, request,jsonify,render_template
import json
import time
import os

app = Flask(__name__)



# global json data 

user1 = {"id": "1",
         "Name ": "Ankit Tiwari",
         "Age": "25",

         "city": "Bangalore",
         "email": "ankit.tiwari@test.com"

         }

user2 = {"Name ": "Karan",
         "Age": "22",
         "id": "2",
         "city": "Mumbai",
         "email": "karan@kk.com"

         }

user3 ={"Name ": "Amit",
         "Age": "12",
         "id": "3",
         "city": "Bhopal",
         "email": "amit@amit.com"}



user4= {"Name ": "Ram",
         "Age": "28",
         "id": "4",
         "city": "Varanasi",
         "email": "ram@ram.com"}


@app.route('/')
def my_form():
    return render_template("index.html")



"""Customer API TEMP """

@app.route('/Apidoc1')
def render():
    return render_template("Apidoc1.html")


@app.route('/adduser', methods=['POST'])


def foo():

    error_dic = {"error":"Id can not be empty"}
    error_dic2 = {"error": "Name can not be empty"}
    error_di3= {"error":"Key missing", "Read":"http://sasasa.com"}

    # if len(request.form) < 2:
    #     return jsonify(error_di3)
    ts = time.ctime()
    # if request.form['id']=="":
    #      return jsonify(error_dic)
    # if request.form['name']=="":
    #     return jsonify(error_dic2)
    #
    #
    # else:

    data = request.form.to_dict()
    data['created at'] = ts
    return jsonify(data=data)



"""                     USER APIS   GET method """
#-----------------------------------------------------------------------------------------


@app.route('/listusers', methods=['GET'])

def list_alluser():

    userlist= []
    userlist.append(user1)
    userlist.append(user2)
    userlist.append(user3)
    userlist.append(user4)
    return jsonify(data=userlist)

@app.route('/listusers/1',methods = ['GET'])
def listuser1():

    return jsonify(data=user1)



@app.route('/listusers/2',methods = ['GET'])
def listuser2():

    return jsonify(data=user2)

@app.route('/listusers/3',methods = ['GET'])
def listuser3():

    return jsonify(data=user3)

@app.route('/listusers/4',methods = ['GET'])
def listuser4():

    return jsonify(data=user4)


#--------------------------------------------------



"""DELETE METHOD """
@app.route('/deleteuser/4',methods = ['DELETE'])
def deleteuser4():
    data = 204
    return jsonify(data)

@app.route('/deleteuser/3',methods = ['DELETE'])
def deleteuser3():
    data = 204
    return jsonify(data)

@app.route('/deleteuser/2',methods = ['DELETE'])
def deleteuser2():
    data = 204
    return jsonify(data)

@app.route('/deleteuser/1',methods = ['DELETE'])
def deleteuser1():
    data = 204
    return jsonify(data)















#----------------------------------

#DELAY res


# @app.route('/delay',methods = ['GET'])
# def delay():
#
#     time.sleep(3)
#     return jsonify(data=user4)
#
#
#



"""PUT METHOD"""

@app.route('/updateuser/1', methods=['PUT'])
def userupdate():
    ts = time.ctime()
    data = request.get_json()
    data= dict(data)
    data['updated at']=ts
    return jsonify(data=data)


@app.route('/updateuser/2', methods=['PUT'])
def userupdate1():
    ts = time.ctime()
    data = request.get_json()
    data= dict(data)
    data['updated at']=ts
    return jsonify(data=data)


@app.route('/updateuser/3', methods=['PUT'])
def userupdate2():
    ts = time.ctime()
    data = request.get_json()
    data= dict(data)
    data['updated at']=ts
    return jsonify(data=data)



@app.route('/updateuser/4', methods=['PUT'])
def userupdate3():
    ts = time.ctime()
    data = request.get_json()
    data= dict(data)
    data['updated at']=ts
    return jsonify(data=data)


@app.route('/login', methods=['POST'])


# def login(email="",password=""):
#
#     error_dic = {"error":"Id can not be empty"}
#     error_dic2 = {"error": "Name can not be empty"}
#     error_di3= {"error":"Key missing", "Read":"http://sasasa.com"}
#
#
#          #print "Email NOT found"
#     # if data['email']=="":
#     #       return jsonify(error_dic)
#     #
#     # if data['password']=="":
#     #     return jsonify(error_dic2)
#
#     try:
#         data = request.form.to_dict()
#
#     # password = request.form['password']
#     #
#     # if email==None:
#     #     return jsonify(data=error_dic)
#     # if password==None:
#     #     return jsonify(data=error_dic2)
#     #
#     # else:
#         data['token'] = "KXR"+str(time.time())
#         return jsonify(data=data)
#     except:
#         return jsonify(data=error_dic)
#




@app.errorhandler(404)

def render_404(e):
    error_di3 = {"error": "Id not found"}
    return jsonify(data = error_di3),404

@app.errorhandler(400)
def render_400(e):
    error_di3 = {"error": "Value error"}
    return jsonify(data = error_di3),400





























if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
