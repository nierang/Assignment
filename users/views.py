
import requests
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Create your views here.
def home(request):
    return render(request,"users/home.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def upload_photo(request):
    if request.method == 'POST':
        # Get the photo file from the request
        photo = request.FILES.get['photo']
        # Upload the photo to Facebook using the Graph API
        url = 'https://graph.facebook.com/v7.0/me/photos'

        response = requests.post(
            url,
            params={'access_token': EAAabof5vpNgBAMAjAffiB66PsR9lf84crBjZCRsUX7gOsIa8EEUSvJZBzI6OHRYYlKZC6sZCC2Jm1AyU6w9xO4bmaxA8ToI5b3xl4wOYof2dtinnJG6oXDZB2Dj19AFVDZCOkZBWbEQEk7CclNn0EGzXQ5L9gwZA4mexxl4Am8aJppAH9ekYELw7},
            files={'source': photo}
        )

        # Check if the photo was successfully uploaded
        if response.status_code == 200:
            # The photo was uploaded successfully
            successload_url = reverse_lazy("upload_success")

        else:
            # The photo upload failed
            failload_url = reverse_lazy("users/upload_success.html")
            
    return render(request, "users/home.html")

