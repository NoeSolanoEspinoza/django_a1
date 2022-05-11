from django.http import HttpResponse


#primera vista
def view1(req):
    return HttpResponse("hola pinches perros")


def view2(req):
    return HttpResponse("otra vez pinches perros")