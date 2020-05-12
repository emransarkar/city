from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login

def view_map(request):
    return render('request','map.html')