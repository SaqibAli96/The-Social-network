from django.conf import settings  
from django.shortcuts import redirect

class LoginRequiredMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response 

    def process_view(self, request, view_func,view_args,view_kwargs):
        
        authenticated = request.user.is_authenticated 
        url = request.path

        if authenticated and url == settings.HOME_URL:

            return redirect(settings.HOMEPAGE_URL)
        
        #if not authenticated and  url != settings.HOME_URL:
           
        #return redirect(settings.HOME_URL)

        