from django.shortcuts import render,redirect

#User details page libraries
from .admin import AdminPanel
from django.contrib.auth.decorators import login_required

#Signup form and errors libraries
from django.contrib.auth import login as auth_login

#API token and authenticated libraries for process_text
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import BertAPI.API.functions as BertFunctions


#User details page functions
@login_required(login_url='/login')
def user_details(request):
    user = request.user
    #auth_token = user.auth_token.key if hasattr(user, 'auth_token') else None
    auth_token = AdminPanel.token(user,user)
    context = {'user': user, 'auth_token': auth_token}
    return render(request, 'userdetails.html', context)

#API request for input text

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def process_v1(request):

    if request.user.is_authenticated:
            text = request.GET.get('text', '') 
            if text == '':
                result = {
                    "error_result" : "Text parameter is null."
                }
                return Response(result, status=status.HTTP_200_OK)
            else: 
                return Response(BertFunctions.predict(text), status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)



