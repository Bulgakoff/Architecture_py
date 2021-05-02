from cources_framework2.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


class About:
    def __call__(self, request):
        return '200 OK', 'about'

class Cont:
    def __call__(self, request):
        return '200 OK', render('contacts.html', data=request.get('data', None))

class Cont1:
    def __call__(self, request):
        return '200 OK', render('cont_1.html', data=request.get('data', None))

class NotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'
