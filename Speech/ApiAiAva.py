import os.path
import sys
import apiai

CLIENT_ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'



ai = apiai.ApiAI("ff102f7e5edc413cba616b2cc52b46de")
def apiAiResponse(userIn):
	request = ai.text_request()

	request.lang = 'en'  # optional, default value equal 'en'


	request.session_id = "0b4d9d04ac344a7bb61239d901ee249e"
	request.query = userIn

	response = request.getresponse()

	res = str(response.read())
	res = res[res.find('"speech":')+11:res.find('"',res.find('"speech":')+12)]
	if "}," in res and '"' in res and len(res) == 13:
		return "I cannot repsond to that command"
	return res


print (apiAiResponse("Hello"))









