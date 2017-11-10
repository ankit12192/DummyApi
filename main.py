from flask import Flask, abort, request,jsonify,render_template
import json
import time
import os

app = Flask(__name__)

# global json data 

users = {"data":[

    {

         "id": 1,
         "Name ": "Ankit Tiwari",
         "Age": "25",

         "city": "Bangalore",
         "email": "ankit.tiwari@test.com",
          },
    {
        "Name ": "Karan",
         "Age": "22",
         "id": 2,
         "city": "Mumbai",
         "email": "karan@kk.com",
         },

         {
         "Name ": "Amit",
         "Age": "12",
         "id": 4,
         "city": "Bhopal",
         "email": "amit@amit.com",
         },

         { "Name ": "Ram",
         "Age": "28",
         "id": 4,
         "city": "Varanasi",
         "email": "ram@ram.com"

          }]}

"""--------------------------------------------------------------------------------------------------------------"""


Profile = { "id":"1",
            "Name":"Ankit",
            "Age" :"25",
            "Total friends":"322",
            "Profil pic":"http://somepic.com",
            "Last updated ":"jan 12 2017",
            "Total photos":"200",
            "Followed by":"70",
            "Status":"Hey Social media is using me  "
}







#---------------------------------------------------USER DATA API CODE --------------------------------------------------



@app.route('/')
def my_form():
    return render_template("index.html")



"""Customer API TEMP """

@app.route('/Apidoc1')
def render():
    return render_template("Apidoc1.html")




@app.route('/sitemap.xml')
def renderw():
    return render_template("sitemap.xml")




@app.route('/adduser', methods=['POST'])


def foo():

    # error_dic = {"error":"Id can not be empty"}
    # error_dic2 = {"error": "Name can not be empty"}
    # error_di3= {"error":"Key missing", "Read":"http://sasasa.com"}

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

    return jsonify(users)

@app.route('/listuser/<int:user_id>')
def listuser1(user_id):

        return jsonify(users['data'][user_id-1])

#--------------------------------------------------


"""DELETE METHOD """

@app.route('/deleteuser/<int:user_id>',methods = ['DELETE'])
def delete_user(user_id):
    data = 204
    return jsonify(data)

#----------------------------------



"""PUT METHOD"""

@app.route('/updateuser/<int:user_id>', methods=['PUT'])
def userupdate1(user_id):

    ts = time.ctime()
    data = request.form.to_dict()
    data= dict(data)
    data['updated at']=ts
    return jsonify(data=data)




@app.route('/delay/<int:sleep>')
def delayres(sleep):
    time.sleep(sleep)
    return jsonify(users)




# @app.route('/login', methods=['POST'])
#
#
# def login(email="",password=""):
#
#     error_dic = {"error":"Id can not be empty"}
#     error_dic2 = {"error": "Name can not be empty"}
#     error_di3= {"error":"Key missing", "Read":"http://sasasa.com"}
#
#     data= request.form['id']
#     print data
#
#     if data['id']=="":
#           return jsonify(error_dic)
#
#     if data['password']=="":
#         return jsonify(error_dic2)
#
#     return "sasa"
#
#     # try:
#     #     data = request.form.to_dict()
#     #
#     #     password = request.form['password']
#     #
#     # if email==None:
#     #     return jsonify(data=error_dic)
#     # if password==None:
#     #     return jsonify(data=error_dic2)
#     #
#     # else:
#     #     data['token'] = "KXR"+str(time.time())
#     #     return jsonify(data=data)
#     # except:
#     #     return jsonify(data=error_dic)
#


@app.errorhandler(404)

def render_404(e):
    error_di3 = {"error": "Id not found"}
    return jsonify(data = error_di3),404

@app.errorhandler(400)
def render_400(e):
    error_di3 = {"error": "Value error"}
    return jsonify(data = error_di3),400


@app.errorhandler(500)
def render_500(e):
    error_di3 = {"error": "Value error"}
    return jsonify(data = error_di3),500


#-------------------------------------------------END OF USER API-------------------------------------------------------



#------------------------------------------------SOCIAL API-------------------------------------------------------------




















































#--------------------------------------------END OF SOCIAL API----------------------------------------------------------




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
