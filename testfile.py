# import requests
# import json
#
# # res= requests.get("http://0.0.0.0:5010/listusers/3")
#
# #print res.content
#
#
# # json1 = {"name ":"ankit",
# #         "id": "10"}
# #
# # data = json.dumps(json1)
# # print data
# #
# # ress = requests.post("http://0.0.0.0:5210/adduser",data=data)
# #
# # print ress.content
#
# import urllib2
# #
# # pr = {
# #     "name": "morpheus",
# #     "job": "zion resident",
# #     "id":"10"
# # }
#
# # res2 = requests.delete("http://0.0.0.0:5010/deleteuser/4")
# # print res2.content
# # print res2.status_code
# # payload_data = json.dumps(json1)
# #
# # resm= requests.post(url='http://0.0.0.0:5010/adduser',data=payload_data)
# # print resm.content
# # print res.status_code
#
#
# data = {"id":"3",
#         "Name":"Shu"
# }
#
# res3 = requests.put("https://reqres.in/api/users/2",data=data)
#
# print res3.content














url = "http://naveenaws.mynewtonhq.com"

url_stage = "https://staging.mynewtonhq.com"


import webbrowser
import requests
import requests.exceptions


try:
        status = requests.get(url)
        print status.status_code


except:
        print "Server might not be running "
        webbrowser.open(url_stage)



