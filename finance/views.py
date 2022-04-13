from django.shortcuts import render


def index(request):
    return render(request, 'users.html')


def users_view(request):
    return render(request, 'users.html')


def create_user(request):
    return render(request, 'createUser.html')


def user_detailview(request):
    return render(request, 'userdetailview.html')


def roles_view(request):
    return render(request, 'rolesview.html')


def create_role(request):
    return render(request, 'createroleview.html')


def cmspages_view(request):
    return render(request, 'CMSpagesview.html')


def cmsfaq_view(request):
    return render(request, 'CMSfaqview.html')


def blogpost_view(request):
    return render(request, 'blogpostview.html')


def announcement_view(request):
    return render(request, 'announcementview.html')


def newsletter_view(request):
    return render(request, 'newsletterview.html')
