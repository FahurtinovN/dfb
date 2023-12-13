from django.shortcuts import render, redirect
from .models import Person
from .forms import AddForm
# Create your views here.

def index(request):
    makeMen()
    people = Person.objects.all()
    return render(request, 'user/index.html', context={'people': people})

def create(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        #print(request.POST.get('birthDay'))
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            birthDay = form.cleaned_data['birthDay']
            men, _ = Person.objects.get_or_create(name=name, surname=surname,
                                                  age=age, gender=gender, birthDay=birthDay)
            return redirect('home')
        else:
            form = AddForm()
            return render(request, 'user/create.html', context={'form': form})
    else:
        form = AddForm()
        return render(request, 'user/create.html', context={'form': form})

def update(request, id):
    try:
        men = Person.objects.get(id=id)
        if request.method == "POSt":
            men.name = request.POST.get('name')
            men.surname = request.POST.get('surname')
            men.age = request.POST.get('age')
            men.gender = request.POST.get('gender')
            men.birthDay = request.POST.get('birthDay')
            men.save()
            return redirect('home')
        else:
            return render(request, 'user/update.html', context={'men': men})
    except:
        return redirect('create')

#def delete(request, id):
    #try:



def makeMen():
    p, _ = Person.objects.get_or_create(name='Tom', surname='nviufdnvfdu', age=17, gender=True, birthDay='2011-12-23')
    p, _ = Person.objects.get_or_create(name='Nurik', surname='nviufvfdu', age=25, gender=True, birthDay='2011-12-23')
    p, _ = Person.objects.get_or_create(name='Stepan', surname='nvidnvidu', age=11, gender=True, birthDay='2011-12-23')
    p, _ = Person.objects.get_or_create(name='scd', surname='nviufdnvifu', age=15, gender=True, birthDay='2011-12-23')
    p, _ = Person.objects.get_or_create(name='ujk', surname='nviufdnvifd', age=26, gender=True, birthDay='2011-12-23')
