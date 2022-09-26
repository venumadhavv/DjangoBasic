from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse

from .models import Project
from .forms import ProjectForm
def html(request):
    movies=Project.objects.all()
    return render(request,'myapp/prjct1.html',{'movies':movies})

# def project(request,pk):
#     obj=Project.objects.get(id=pk)
#     return render(request,'myapp/prjct2.html',{'mve':obj})




def create_project(request):
    forms=ProjectForm()
    if(request.method == 'POST'):
        forms=ProjectForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('project1')
    return render(request,"myapp/project_form.html",{'forms':forms})

def update_project(request,pk):
    
    project=Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method=='POST':
        form=ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('project1')
    return render(request,"myapp/project_form.html",{'forms':form})

def delete_project(request,pk):
    delete_proj=Project.objects.get(id=pk)

    if request.method=='POST':
         delete_proj.delete()
         return redirect('project1')
    return render(request,'myapp/delete.html',{'name':delete_proj.title})