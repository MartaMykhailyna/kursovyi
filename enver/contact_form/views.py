from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def send_email(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        subject = request.POST.get("subject", "")
        message = request.POST.get("message", "")

        # with open("data.txt", "w") as f:
        #     f.write(f"Name: {name},\nEmail: {email},\nSubject: {subject},\nMessage:\n{message}\n")

        send_mail(
            subject=f'Нове повідомлення від {name}',
            message=f'Ви отримали нове повідомлення від {name}. Звідки: {email}\nТема: {subject}\nПовідомлення: {message}',
            from_email=email,
            recipient_list=['martamykhailyna@gmail.com'],
        )

    return render(request, 'contact_form/contact-form.html')
