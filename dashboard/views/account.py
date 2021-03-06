# import custom update forms
from dashboard.forms.account import (
    UpdatePasswordForm,
    UpdateUserInfoEmail,
    UpdateUserInfoUsername,
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


@login_required()
def Account_Settings(request):
    """
    Dashboard > Change Personal Info View
    """
    # intialize forms
    uname_form = UpdateUserInfoUsername(
        request.user,
        initial={"username": request.user.username, "action": "username"},
    )
    email_form = UpdateUserInfoEmail(
        request.user,
        initial={"email": request.user.email, "action": "email"},
    )

    if request.method == "POST":
        action = request.POST["action"]  # get what action to do

        # update username
        if action == "username":
            # needs to have similar name, think so, ..
            uname_form = UpdateUserInfoUsername(request.user, data=request.POST)
            if uname_form.is_valid():
                uname_form.save()

                messages.success(
                    request, "You have successfully updated your username!"
                )

                return redirect("account")

        # update email
        elif action == "email":
            # needs to have similar name, think so, ..
            email_form = UpdateUserInfoEmail(request.user, data=request.POST)
            if email_form.is_valid():
                email_form.save()

                messages.success(
                    request, "You have successfully updated your email address!"
                )

                return redirect("account")

    return render(
        request,
        "main/profile.html",
        {"uname_form": uname_form, "email_form": email_form},
    )


@method_decorator(login_required, name="dispatch")
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    """
    Dashboard > Change Password View
    """

    form_class = UpdatePasswordForm
    template_name = "main/change_password.html"
    success_url = reverse_lazy("account-password")
    success_message = "Your password have been successfully updated!"
