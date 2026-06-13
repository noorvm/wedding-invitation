from django.shortcuts import render
from .forms import RSVPForm
from .models import RSVP

def home(request):

    message = ""

    if request.method == "POST":

        form = RSVPForm(request.POST)

        if form.is_valid():

            family_name = form.cleaned_data['family_name']

            if RSVP.objects.filter(
                family_name=family_name
            ).exists():

                message = (
                    "Response already submitted "
                    "for this family."
                )

            else:

                form.save()

                message = (
                    "Thank you for confirming!"
                )

    else:

        form = RSVPForm()

    return render(
        request,
        'invitation/home.html',
        {
            'form': form,
            'message': message
        }
    )