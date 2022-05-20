from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.template import loader
from familia.forms import personaForm
from familia.models import Persona

# Create your views here.
def index(request):
    personas_tbl = Persona.objects.all()
    template = loader.get_template('index.html')
    context = {
        'personas': personas_tbl,
    }
    return HttpResponse(template.render(context, request))


def agregar(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = personaForm(request.POST)
        if form.is_valid():
            try:
                nombre = form.cleaned_data['firstname']
                apellido = form.cleaned_data['lastname']
                genero= form.cleaned_data['gender']
                edad= form.cleaned_data['age']
                fcumpleanios=form.cleaned_data['birthdate']
                relacion=form.cleaned_data['relation']
                email = form.cleaned_data['email']
                Persona(firstname=nombre, lastname=apellido,gender=genero,age=edad,birthdate=fcumpleanios,relation=relacion,email=email).save()
                messages.success(request,'La persona se agrego correctamente')
            except:
                messages.error(request,'Se produjo un error al guardar')    
            return HttpResponseRedirect("/familia/")
    elif request.method == "GET":
        form = personaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'agregarPersonaForm.html', {'form': form})


def borrar(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        persona = Persona.objects.filter(id=int(identificador)).first()
        if persona:
            try:
                persona.delete()
                messages.success(request, "La persona fue eliminada correctamente")

            except:
                messages.error(request, "Error al eliminar")

        return HttpResponseRedirect("/familia/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")    


def actualizar(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    #personaId= get_object_or_404(Persona, id=identificador)
    personaId= Persona.objects.get(id=identificador)
    #form = personaForm(initial= {'firstname':personaId.firstname,'lastname':personaId.lastname,'gender':personaId.gender,'age':personaId.age,'birthdate':personaId.birthdate,'email':personaId.email })
    
    if request.method == "POST":
       form = personaForm(request.POST)
       if form.is_valid():
           try:
               personaId.firstname = form.cleaned_data['firstname']
               personaId.lastname = form.cleaned_data['lastname']
               personaId.gender= form.cleaned_data['gender']
               personaId.age= form.cleaned_data['age']
               personaId.birthdate=form.cleaned_data['birthdate']
               personaId.relation=form.cleaned_data['relation']
               personaId.email = form.cleaned_data['email']
               personaId.save()
               messages.success(request,'La actualización es correcta')
           except (RuntimeError):
               messages.error(request, "Hubo un error al guardar")
            #return render(request, 'actualizarDatosPersona.html', context_instance=RequestContext(request))
    elif request.method == "GET":
        form = personaForm(initial= {'firstname':personaId.firstname,'lastname':personaId.lastname,'gender':personaId.gender,'age':personaId.age,'birthdate':personaId.birthdate,'relation':personaId.relation,'email':personaId.email })
        if form.is_valid():
           contexto={'form':form}        
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request "+ request.method)

    return render(request, 'actualizarDatosPersona.html', {'form':form})   
    
