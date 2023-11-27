from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Property,Location,Owner,Agent # Import your Property model

def create_property(request):
    properties = Property.objects.select_related("owner","location").all()
    location = Location.objects.all()
    owner = Owner.objects.all()
    if request.method == 'POST':
        # Retrieve data from the POST request
        property_name = request.POST.get('propertyName')
        property_type = request.POST.get('propertyType')
        price = request.POST.get('propertyPrice')
        start_date = request.POST.get('StartDate')
        status = request.POST.get('propertyStatus')
        location_id = request.POST.get('propertySelect')  # Assuming location_id is submitted in the form
        owner_id = request.POST.get('ownerSelect')  # Assuming owner_id is submitted in the form
        print(property_name,property_type,price,start_date,owner_id)
        print(location_id, status)
        # Create a new Property object
        new_property = Property.objects.create(
            property_name=property_name,
            property_type=property_type,
            price=price,
            start_date=start_date,
            status=status,
            location_id=location_id,  # Assign the location ID
            owner_id=owner_id  # Assign the owner ID
        )

        # Save the new property
        new_property.save()


        # Redirect to the properties page or any other appropriate page
        return redirect('/properties') # Redirect to the properties page after creating the property

    else:
        # Handle GET request or render a form to create properties
        return render(request, 'properties.html', {'properties': properties,'location': location, 'owner':owner})  # Render a form for creating properties

def agnets(request):
    agnets = Agent.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        contact_number = request.POST.get('contactNumber')
        email = request.POST.get('emailAddress')
        print(first_name,last_name,contact_number,email)

        new_agent = Agent.objects.create(
            first_name=first_name,
            last_name=last_name,
            contact_number=contact_number,
            email=email,
            location_id=1
        )
        new_agent.save()

        return redirect('/agents')
    else:
        return render (request, 'agents.html', {'agents': agnets})
