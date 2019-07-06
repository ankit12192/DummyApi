from flask import Flask, request,jsonify,render_template
import json
import time
import os
from Dict import users

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")


@app.route('/Apidoc1')
def render():
    return render_template("Apidoc1.html")



@app.route('/sitemap.xml')
def renderw():
    return render_template("sitemap.xml")





@app.route('/adduser', methods=['POST'])


def foo():

    ts = time.ctime()
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


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run( port=port, debug=True)
