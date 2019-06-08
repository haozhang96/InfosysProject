from .models import User, Address, BillingInfo

from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.core.serializers.json import DjangoJSONEncoder
from django.core.validators import validate_email
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import View

#import datetime
import json
# datetime.datetime.strptime(json, "%Y-%m-%dT%H:%M:%S.%fZ")

class GetUsers(View):
    def get(self, request, *args, **kwargs):
        # Generate a list of limited user information.
        users = [{
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        } for user in User.objects.all()]

        # Return a JSON-encoded object.
        return HttpResponse(json.dumps(users, cls=DjangoJSONEncoder))

class RegisterUser(View):
    def post(self, request, *args, **kwargs):
        try:
            # Decode the JSON body.
            data = json.loads(request.body.decode("utf-8"))

            # Make sure that the username has not already been taken.
            if User.objects.filter(username=data["userName"]).count():
                return HttpResponseBadRequest(
                    "The username has already been taken!"
                )

            # Call the email validator which will raise an error if it's
            #   invalid.
            validate_email(data["email"])

            # Create the model instances from the given user data.
            address, billing_address, billing_info = createUserInfo(data)

            # Create the user model instance.
            user = User(
                username=data["userName"],
                email=data["email"],
                password=make_password(data["password"]),
                first_name=data["firstName"],
                last_name=data["lastName"],
                phone_number=data["phone"],
                address=address,
                billing_info=billing_info,
            )
            user.save()

            # User registration was successful. Return their email address.
            return HttpResponse(status=200)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON body!")
        except ValidationError:
            return HttpResponseBadRequest("Invalid email!")

class UpdateUser(View):
    def patch(self, request, *args, **kwargs):
        try:
            # Decode the JSON body.
            data = json.loads(request.body.decode("utf-8"))

            # Call the email validator which will raise an error if it's
            #   invalid.
            validate_email(data["email"])

            # Create the model instances from the given user data.
            address, billing_address, billing_info = createUserInfo(data)

            # Update the user model instance.
            user = User.objects.get(username=data["userName"])
            user.email=data["email"]
            user.password=make_password(data["password"])
            user.first_name=data["firstName"]
            user.last_name=data["lastName"]
            user.address=address
            user.phone_number=data["phone"]
            user.billing_info=billing_info
            user.save()

            # User registration was successful. Return their email address.
            return HttpResponse(status=200)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON body!")
        except ValidationError:
            return HttpResponseBadRequest("Invalid email!")

def createUserInfo(data):
    # Create the address model instance.
    address = Address(
        address=data["homeAddress"]["street"],
        city=data["homeAddress"]["city"],
        state=data["homeAddress"]["state"],
        zip_code=data["homeAddress"]["zip"],
    )
    address.save()

    billing_address = Address(
        address=data["billingAddress"]["street"],
        city=data["billingAddress"]["city"],
        state=data["billingAddress"]["state"],
        zip_code=data["billingAddress"]["zip"],
    )
    billing_address.save()

    # Create the billing info model instance.
    billing_info = BillingInfo(
        first_name=data["billingAddress"]["nameFirst"],
        last_name=data["billingAddress"]["nameLast"],
        card_number=data["billingCardNumber"],
        expiration_date=data["billingCardExpiration"],
        address=billing_address,
    )
    billing_info.save()

    return address, billing_address, billing_info