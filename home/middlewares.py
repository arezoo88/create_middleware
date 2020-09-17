from django.shortcuts import redirect
from django.contrib import messages

# def first(get_response):
#     def middleware(request):
#         print('before....')
#         response = get_response(request)
#         print('after....')
#         return response
#
#     return middleware
LOGIN_EXEMP_URLS = ['/', '/login/']


class Loginmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in LOGIN_EXEMP_URLS:
            messages.error(request, 'you should log in')
            return redirect('home:login')
        response = self.get_response(request)
        return response
