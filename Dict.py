#-------------------------------------------------END OF USER API-------------------------------------------------------



#------------------------------------------------SOCIAL API-------------------------------------------------------------


#--------------------------------------------END OF SOCIAL API----------------------------------------------------------


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
















"""

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


"""