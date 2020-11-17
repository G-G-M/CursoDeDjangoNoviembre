from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hola, es la segunda clase2!!")

def lista(request):
    """
        Enviamos un template como respuesta, pero sin
        pasar ningun dato (contexto).
    """
    return render(request, "myapp2/lista.html")

def lista2(request):
    """
        Eviamos un template con un contexto simple.
        Un nombre nombre de usuario.
    """
    context = {
        "userName" : "Diego"
    }
    return render(request, 
                "myapp2/lista2.html",
                context)

def lista3(request):
    """
        Eviamos un template con un contexto simple.
        Un nombre nombre de usuario y un estado que refleja
        si esta al dia o no con sus tareas.
    """
    context = {
        "userName" : "Diego",
        "state" : True
    }
    return render(request, 
                "myapp2/lista3.html",
                context)

def lista4(request):
    """
        Eviamos un template con un contexto simple.
        Un nombre nombre de usuario y un estado que refleja
        si esta al dia o no con sus tareas. Ademas una lista de
        sus tareas.
    """
    context = {
        "userName" : "Diego",
        "state" : True,
        "todo" : ["Comprar tira de asado",
                    "Comprar fristas", 
                    "Comprar lechuga"]
    }
    return render(request, 
                "myapp2/lista4.html",
                context)
