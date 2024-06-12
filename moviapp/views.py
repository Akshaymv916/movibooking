from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from moviapp.models import Movie,Navbar,Cinema,Show,Booking


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    navbar=Navbar.objects.all()
    context = {
        'movie': movies,
        'navbar':navbar
    }
    return render(request,"index.html", context)

def details(request,id):
    movi=Movie.objects.get(movie=id)
    cine = Cinema.objects.filter(cinema_shows__movi=movi).prefetch_related('cinema_shows').distinct()
    show=Show.objects.filter(movi=id)
    context={
        'movi':movi,
        'cine':cine,
        'show':show
    }
    return  render(request,'details.html',context)



def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Username/Password is incorrect')
                return redirect('login')
        else:
            return render(request, "login.html")

def signup(request):

        if request.method == 'POST':
            username = request.POST['username']
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'username already exist')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'email already exist')
                else:
                    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                    email=email, password=password1)
                    user.save()
                    messages.info(request, 'User created')
                    return redirect('login')
            else:
                messages.info(request, 'Password not match')
            return redirect('signup')
        else:
            return render(request, "signup.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def seating(request,id):
    show=Show.objects.get(shows=id)
    seat = Booking.objects.filter(shows=id)
    return render(request,"seating.html", {'show':show,'seat':seat})

def movibook(request):
    if request.method == 'POST':
        user=request.user
        useat = ','.join(request.POST.getlist('check'))
        show=request.POST['show']
        book=Booking(seat=useat,shows_id=show,user=user)
        book.save()
        books=Booking.objects.filter(user=user)
        return render(request,"bookings.html",{'book':books})

def bookings(request):
    user=request.user
    books = Booking.objects.filter(user=user)
    return render(request, "bookings.html", {'book': books})


def moviticket(request, id):
    ticket = Booking.objects.get(id=id)
    print(ticket.shows.price)
    return render(request,"moviticket.html", {'ticket':ticket})


def dashboard(request):
    user=request.user
    movi=Cinema.objects.all()
    return render(request,'dashboard.html',{'movie':movi})

def showadd(request):

    if request.method == 'POST':
        m = request.POST['m']
        k = request.POST['k']
        t = request.POST['t']
        d = request.POST['d']
        p = request.POST['p']
        show = Show(cinema_id=k,movi_id=m, date=d, time=t, price=p)
        show.save()
        messages.success(request, 'Show Added')
        return redirect('dashboard')
    else:
        m = Show.objects.all()
        sh = Movie.objects.all()

        data = {
            'mov':m,
            's':sh
        }
        return render(request,"showadd.html", data)




def addshow(request,id):
    movi=Show.objects.filter(cinema_id=id)
    m=Cinema.objects.filter(movi_name=id)
    c=Cinema.objects.all()
    s=Movie.objects.all()
    movi={
        'movi':movi,
        'm':m,
        's':s,
        'c':c
    }
    return render(request,'showadd.html',movi)


def remove(request,id):
    shows=Show.objects.get(pk=id)
    shows.delete()
    return redirect('dashboard')


def search(request):
    query = request.GET.get('query')
    movie = Movie.objects.all().filter(Q(name__contains=query) | Q(movi_desc__contains=query))

    context = {
        'movie': movie
    }
    return render(request, 'search.html', context)