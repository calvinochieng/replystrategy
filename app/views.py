from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseBadRequest
from .forms import EmailSubmissionForm
from .models import *


# Gumroad URL
GUMROAD_URL = "https://calvinochieng.gumroad.com/l/5MUnlocked"

def submit_email(request):
    if request.method == "POST":
        form = EmailSubmissionForm(request.POST)
        if form.is_valid():
            # Honeypot validation
            birthday = form.cleaned_data.get("birthday", "")
            if birthday:  # If the honeypot field is filled, block the request
                messages.error(request, "Invalid submission detected.")
                return redirect("submit_email")  # Redirect back to the form

            # Save the email
            email = form.cleaned_data.get("email")
            _, created = EmailSubmission.objects.get_or_create(email=email)

            if created:
                messages.success(request, "Email successfully submitted!")
            else:
                messages.info(request, "This email is already registered.")

            # Redirect to Gumroad
            return redirect(GUMROAD_URL)
        else:
            # If form is invalid, display error message
            messages.error(request, "Invalid form submission. Please try again.")

    else:
        form = EmailSubmissionForm()

    return render(request, "email_form.html", {"form": form})


def index(request): 
    return render(request, 'index.html')


def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'article/list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article/detail.html', {'article': article})

