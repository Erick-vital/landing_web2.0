from django.conf import settings
from .forms import ContactoForm

"""
    Los Constest processors sirven para crear contextos globales y poderlos usar en las plantillas
    en ves de un contexto creado en una vista, recuerda que tienes que agregar los contextos creados en el apartado templates de las 
    settings
"""
def base_data(request):
    return {
        'form': ContactoForm
    }