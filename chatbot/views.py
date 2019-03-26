from django.shortcuts import render
from django.http import JsonResponse
import requests, json
from pprint import pprint

def chatbot(request):
	return render(request, 'chatbot/chatbot.html')

def chatbotResponse(request):
	query = request.GET['query']
	data = {'reply': 'chatbot could\'nt respond due to network issue!! Try Again'}

	url = 'http://localhost:5002/webhooks/rest/webhook'
	payload = {'sender': 'Rasa', 'message': query}
	headers = {'Content-Type': 'application/json'}

	response = requests.post(url, data=json.dumps(payload), headers=headers)
	data = response.text.strip().replace('[','').replace(']','')
	# pprint(json.dumps(response.text))
	# print(data)

	return JsonResponse(data, safe=False)