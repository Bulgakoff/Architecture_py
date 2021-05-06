from cources_framework3.templator import render_to_templ


class Index:
    def __call__(self, request):
        return '200 OK', render_to_templ('index.html', data=request.get('data', None))


class About:
    def __call__(self, request):
        return '200 OK', render_to_templ('about.html', data=request.get('data', None))

class Reg:
    def __call__(self, request):
        return '200 OK', render_to_templ('regs.html', data=request.get('data', None))

class Cont1:
    def __call__(self, request):
        return '200 OK', render_to_templ('cont_1.html', data=request.get('data', None))

class NotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'
