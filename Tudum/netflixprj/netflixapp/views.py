from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required

class Home(View):
    def get(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('netflixapp:profile-list')
        return render(request, 'index.html')


    


