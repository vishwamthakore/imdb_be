from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserRegisterAV(APIView):
    
    def post(self, request):
        print(request)
        username = request.data.get("username")
        password = request.data.get("password")
        # Add validation
        
        new_user = User(username=username, is_staff=False)
        new_user.set_password(password)
        new_user.save()
        
        token, created = Token.objects.get_or_create(user=new_user)
        
        data = {
            "status" : "User Registered",
            "username" : username,
            "token" : token.key 
        }
        
        return Response(data)
    
    
    