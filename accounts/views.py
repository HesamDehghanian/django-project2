from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import userProfileForm


@login_required
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


@login_required
@user_passes_test(lambda u: not u.is_staff and not u.is_superuser)
def user_dashboard(request):
    return render(request, 'user_dashboard.html')


@login_required
@user_passes_test(lambda u: u.is_staff and not u.is_superuser)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


@login_required
@user_passes_test(lambda u: u.is_superuser)
def superadmin_dashboard(request):
    return render(request, 'superadmin_dashboard.html')