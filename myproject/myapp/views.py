from django.shortcuts import HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("¡ADIOS, MUNDO!!!")

def index90(request):
    return HttpResponse(' ¡¡Hola <em> Sebas </em>!!')

def lista(request):
    mipag = """
        <html>
            <head>
                <title> MI pag </title>
            </head>
            <body>
                <ul>
                    <li> valor </li>
                    <li> LEchuga </li>
                </ul>
            </body>
        </html>
    """
    return HttpResponse(mipag)

def json(request):
    return JsonResponse([{'curso' : 'python'}, {'curso' : 'Java'}], safe=False)
