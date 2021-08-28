from .models import UrlWithAccount, UrlWithoutAccount
from .form import RegisterForm, UpdateLinkForm, UserUpdateFrom
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.paginator import Paginator
import random, string
from django.contrib.auth.decorators import login_required

def hashcode(length=5):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def error_404(request, exception):
        return render(request,'error/404.html')

def error_500(request):
        data = {}
        return render(request,'error/500.html', data)

def error_403(request, exception):
        data = {}
        return render(request,'error/404.html', data)

def error_400(request,  exception):
        data = {}
        return render(request,'error/500.html', data)

def index(request):
    context={'addLinkActive':'color-text-green_active'}

    if request.user.is_authenticated:
        return render(request,'pages/add_link.html',context)

    if request.method == 'POST':
        url = request.POST["url"]
        hash = hashcode()
        while True:
            lenght = 5
            hash = hashcode(lenght)
            try:
                link = UrlWithoutAccount.objects.create(url=url,shorthen_link_id=hash)
                break
            except:
                lenght += 1
                link = None

        context={'addLinkActive':'color-text-green_active','link':link}
        return render(request,'pages/index.html',context)

    return render(request,'pages/index.html',context)


@login_required
def addlink(request):
    context={'addLinkActive':'color-text-green_active'}
    if request.method == 'POST':
        current_user = request.user
        url = request.POST["url"]
        hash = request.POST["hash"]
        if '/' in hash or '\\' in hash:
            messages.warning(request,"invalide hash code.")
            return redirect('index')
        try:
            link = UrlWithAccount.objects.create(url=url,shorthen_link_id=hash,user=current_user)
            messages.success(request,"Your link added successfully.")
        except:
            link = None
            messages.warning(request,"Exist hash code")
        context={'addLinkActive':'color-text-green_active','link':link}
        return render(request,'pages/add_link.html',context)

    return redirect('index')

def go(request,hash):

    try:
        link = UrlWithoutAccount.objects.get(shorthen_link_id=hash)
    except:
        link = get_object_or_404(UrlWithAccount,shorthen_link_id=hash)
        link.seen += 1
        link.save()

    return redirect(link.url)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    context={'form':form}
    return render(request,'registration/signup.html',context)


@login_required
def YourLinks(request):
    current_user = request.user
    links = UrlWithAccount.objects.filter(user=current_user)
    paginator = Paginator(links, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'links':page_obj,'yourLinksActive':'color-text-second_active'}
    return render(request,'pages/your_links.html',context)


@login_required
def UpdateLink(request,id):
    current_user = request.user
    link = get_object_or_404(UrlWithAccount,id=id,user=current_user)
    if request.method == 'POST':
        form = UpdateLinkForm(request.POST,instance=link)
        if form.is_valid:
            form.save()
            messages.success(request, 'Link updated successfully.')
            return redirect('your_links')
    context={'link':link,'yourLinksActive':'color-text-second_active'}
    return render(request,'pages/update_link.html',context)


@login_required
def DeleteLink(request,id):
    current_user = request.user
    link = get_object_or_404(UrlWithAccount,id=id,user=current_user)
    link.delete()
    messages.success(request, 'Link deleted successfully.')
    return redirect('your_links')

@login_required
def YourProfile(request):
    current_user = request.user
    form = UserUpdateFrom(instance=current_user)
    if request.method == 'POST':
        form = UserUpdateFrom(request.POST,instance=current_user)
        if form.is_valid:
            form.save()
            messages.success(request,'Your account updated successfully.')
            return redirect('your_profile')
    context={'form':form,'yourProfileActive':'color-text-second_active'}
    return render(request,'pages/your_profile.html',context)

@login_required
def UpdateProfile(request):
    current_user = request.user
    form = UserUpdateFrom(instance=current_user)
    if request.method == 'POST':
        form = UserUpdateFrom(request.POST,instance=current_user)
        if form.is_valid:
            form.save()
            messages.success(request,'Your account updated successfully.')
            return redirect('your_profile')
    context={'form':form,'yourProfileActive':'color-text-second_active'}
    return render(request,'pages/your_profile.html',context)