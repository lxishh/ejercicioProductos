from django.shortcuts import render

# Create your views here.
def renderTienda(request):
    return render(request, 'appTemplate/tienda.html')


#Aquí irán las 3 páginas, todas con un request a la misma pagina
#pero lo que cambia es la variable de data (Ahí ira la info correspondiente de cada una)