from django.shortcuts import render
from django.http import JsonResponse



# Create your views here.

def chatbot_response(user_input):
    responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "bye": "Goodbye! Have a great day!",
}
    return responses.get(user_input.lower(), "Sorry, I don't understand that.")

def chatbot_api(request):
    if request.method == "GET":
        user_message = request.GET.get("message", "")
        response = chatbot_response(user_message)
        return JsonResponse({"response": response})
    
def chatbot_page(request):
    return render(request, "chatbot_app/chat.html")