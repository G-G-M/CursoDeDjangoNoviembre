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

def lista5(request):
    """
        Eviamos un template con un contexto simple.
        Un nombre nombre de usuario y un estado que refleja
        si esta al dia o no con sus tareas. Ademas una lista de
        sus tareas con estilo!!.
    """
    context = {
        "userName" : "Diego",
        "state" : True,
        "todo" : ["Comprar tira de asado",
                    "Comprar fristas", 
                    "Comprar lechuga"]
    }
    return render(request, 
                "myapp2/lista5.html",
                context)

def lista6(request):
    """
        Eviamos un template con un contexto simple.
        Un nombre nombre de usuario y un estado que refleja
        si esta al dia o no con sus tareas. Ademas una lista de
        sus tareas con estilo!!. Complicar las cosas
    """
    context = {
        "userName" : "Diego",
        "state" : True,
        "todo" : [{ "id" : 1,"detail" : "Comprar tira de asado", "state" : False}, 
                    { "id" : 2,"detail" : "Comprar tira de lechuga", "state" :True},  
                    { "id" : 3,"detail" : "Comprar tira de cerveza", "state" : False}, ]
    }
    return render(request, 
                "myapp2/lista6.html",
                context)


def parametros(request, name):
    print(name)
    context = { "userName" : name}
    return render(request, "myapp2/parametros.html", context)