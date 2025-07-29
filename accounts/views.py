from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import userProfileForm


def edit_user_profile(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = userProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_dashboard')
        return HttpResponse(form.errors, status=400)
    else:
        form = userProfileForm(instance=profile)
        return render(request, 'edit_profile.html', {'form': form})




