from django.shortcuts import render

# Create your views here.
def renderTienda(request):
    return render(request, 'appTemplate/tienda.html')

def renderElectronica(request):
    data = {'titulo': 'Electronica', 'p1':'Mac', 'p2':'Iphone', 'p3':'Playstation'}
    return render(request, 'appTemplate/productos.html', data)

def renderJuguetes(request):
    data = {'titulo': 'Juguetes', 'p1':'Auto', 'p2':'Pelota de Futbol', 'p3':'Figura de accion'}
    return render(request, 'appTemplate/productos.html', data)

def renderRopa(request):
    data = {'titulo': 'Ropa', 'p1':'Pantalones', 'p2':'Chaqueta', 'p3':'Camisa'}
    return render(request, 'appTemplate/productos.html', data)
#Aquí irán las 3 páginas, todas con un request a la misma pagina
#pero lo que cambia es la variable de data (Ahí ira la info correspondiente de cada una)