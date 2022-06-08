#https://docs.djangoproject.com/en/dev/topics/db/aggregation/
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotAllowed, HttpResponseRedirect
from  django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Count

from .models import Projection,Ticket
from app.forms import TicketForm, CreateProjectionForm,UpdateProjectionForm,DeleteProjectionForm



# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"hello.html")

def welcome(request):
    return render(request,'welcome.html',{'data':['prvi','drugi','treci']})


def projections(request):
    projections=Projection.objects.all()
    tickets=Ticket.objects.all()
    user=request.user
    form=TicketForm()
    if request.method=="POST":
        formData=TicketForm(request.POST)
        if formData.is_valid():
            tik=Ticket(customer=request.user,movieName=formData.cleaned_data['movieName'],seatNumber=formData.cleaned_data['seatNumber'])
            tik.save()
    numTicket={}
    userTickets={}
    for movies in projections:
        count = 0
        users=[]
        for tiktemp in tickets:
            if movies==tiktemp.movieName:
                if tiktemp.customer.username not in users:
                    users.append(tiktemp.customer.username)
                count +=1        
            movies.cinemaHallCapacity -= count
            numTicket[movies.id]= count
            userTickets[movies.id]=users
        
    return render(request,'projections.html',{'projections':projections,
                                             'ticket':tickets,'user':user,
                                             'form':form,'brTicket':numTicket,
                                             'users':userTickets})

def createData(request):
    currentUser=User.objects.all()
    projections=Projection.objects.all()
    s1=Projection(movieName="Madagaskar",screeningTime='18:00',cinemaHallCapacity=20)
    s1.save()
    s2=Projection(movieName="Ice Age",screeningTime='19:00',cinemaHallCapacity=20)
    s2.save()
    u1=Ticket(customer=currentUser[0],movieName=projections[1],seatNumber=2)
    u1.save()
    u2=Ticket(customer=currentUser[1],movieName=projections[2],seatNumber=3)
    u2.save()
    
    return HttpResponse('<h1>Done</h1>')

def register(request):
    if request.method=='GET':
        userForm=UserCreationForm()
        return render(request,'register.html',{'form':userForm})
    elif request.method == 'POST':
        userForm=UserCreationForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            print("")
            print("***")
            print(userForm)
            print("")
            print("***")
            cleaned_data=userForm.cleaned_data
            print(cleaned_data)
            print("")
            print("***")
            return redirect('login')
        else:
            return redirect('register')
    else:
        return HttpResponseNotAllowed('Cannot save!')
    
def logoutView(request):
    logout(request)
    return render(request,'logout.html')

def createProjection(request):
    createForm=CreateProjectionForm()
    if request.method == "POST":
        formData= CreateProjectionForm(request.POST)
        if formData.is_valid():
            p=Projection(movieName=formData.cleaned_data['movieName'],
                         screeningTime=formData.cleaned_data['screeningTime'],
                         cinemaHallCapacity=formData.cleaned_data['movieSeats'])
            p.save()
            
    return render(request,'create.html',{'createForm':createForm})

def updateProjection(request):
    if request.method == "POST":
        form = UpdateProjectionForm(request.POST)
        if form.is_valid():
            nID = form.cleaned_data['projSelect']
            nName = form.cleaned_data['newMovieName']
            nTime = form.cleaned_data['newScreeningTime']
            nSeats = form.cleaned_data['newMovieSeats']
            p = Projection(id=nID.id,movieName=nName,screeningTime=nTime,cinemaHallCapacity=nSeats)
            p.save()
    form = UpdateProjectionForm()
    return render(request,'update.html',{'updateForm':form})

def deleteProjection(request):
    if request.method == "POST":
        form = DeleteProjectionForm(request.POST)
        if form.is_valid():
            p = form.cleaned_data["projSelect"]
            p.delete()
    form = DeleteProjectionForm()
    return render(request,'delete.html',{'deleteForm':form})


# @login_required
# def obrana(request):

#     total = 0
#     lst = []
#     users = User.objects.all()

    # for user in users:
    #     tickets = Ticket.objects.filter(customer=user)
        
    #     for ticket in tickets:
    #         total = total+1

    #     if total >= 5:
    #         status = "True"
    #     elif  total >= 2 and total <= 4:
    #         status = "False"
    #     else:
    #         continue

    #     tempdict = {
    #         'name': user.username,
    #         'total': total,
    #         'status':status
    #     }
    #     lst.append(tempdict)
    #     total = 0

    # return render(request, 'obrana.html', {'tickets': lst,'users':users})
    

def obrana(request):
    count=0
    lst=[]
    user=User.objects.all()
    c=Ticket.objects.annotate(Count('id')).order_by('customer')
    for i in user:
        for j in c:
            if i==j.customer:
                count=count+1
                continue
            else:
                continue
        
        tempdict={
                'user':i.username,
                'broj':count
                }
        lst.append(tempdict)
        count=0    
            
                 
    return render(request, "obrana.html", {'ticket': lst})