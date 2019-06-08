from .models import User, Address, BillingInfo

from django.contrib.auth.hashers import make_password
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
            if User.objects.filter(username=data["username"]).count():
                return HttpResponseBadRequest(
                    "The username has already been taken!"
                )

            # Call the email validator which will raise an error if it's
            #   invalid.
            validate_email(data["userName"])

            # Create the address model instance.
            address = Address.objects.get_or_create(
                address=data["addressNameFirst"],
                city=data["addressNameLast"],
                state=data["addressState"],
                zip_code=data["addressZip"],
            )

            billing_address = Address.objects.get_or_create(
                address=data["billingAddressStreet"],
                city=data["billingAddressCity"],
                state=data["billingAddressState"],
                zip_code=data["billingAddressZip"],
            )

            # Create the billing info model instance.
            billing_info = BillingInfo.objects.get_or_create(
                first_name=data["billingAddressNameFirst"],
                last_name=data["billingAddressNameFirst"],
                card_number=data["billingCardNumber"],
                expiration_date=data["billingCardExpiration"],
                address=billing_address,
                phone_number=data["billingPhone"],
            )

            # Create the user model instance.
            user = User.objects.create(
                username=data["userName"],
                email=data["email"],
                password=make_password(data["password"]),
                first_name=data["nameFirst"],
                last_name=data["nameLast"],
                phone_number=data["phone"],
                address=address,
                billing_info=billing_info,
            )

            # Save the model instances to the database.
            address.save()
            billing_address.save()
            billing_info.save()
            user.save()

            # User registration was successful. Return their email address.
            return HttpResponse(status_code=200)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON body!")
        except validate_email.ValidationError:
            return HttpResponseBadRequest("Invalid email!")

class UpdateUser(View):
    def patch(self, request, *args, **kwargs):
        try:
            # Decode the JSON body.
            data = json.loads(request.body.decode("utf-8"))

            # Call the email validator which will raise an error if it's
            #   invalid.
            validate_email(username)

            # Create the address model instance.
            address = Address.objects.get_or_create(
                address=data["addressNameFirst"],
                city=data["addressNameLast"],
                state=data["addressState"],
                zip_code=data["addressZip"],
            )

            billing_address = Address.objects.get_or_create(
                address=data["billingAddressStreet"],
                city=data["billingAddressCity"],
                state=data["billingAddressState"],
                zip_code=data["billingAddressZip"],
            )

            # Create the billing info model instance.
            billing_info = BillingInfo.objects.get_or_create(
                first_name=data["billingAddressNameFirst"],
                last_name=data["billingAddressNameFirst"],
                card_number=data["billingCardNumber"],
                expiration_date=data["billingCardExpiration"],
                address=billing_address,
                phone_number=data["billingPhone"],
            )

            # Update the user model instance.
            user = User.objects.get(username=data["username"])
            user.email=data["email"],
            user.password=make_password(data["password"]),
            user.first_name=data["nameFirst"],
            user.last_name=data["nameLast"],
            user.address=address,
            user.phone_number=data["phone"],
            user.billing_info=billing_info,
            
            # Save the model instances to the database.
            address.save()
            billing_address.save()
            billing_info.save()
            user.save()

            # User registration was successful. Return their email address.
            return HttpResponse(status_code=200)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON body!")
        except validate_email.ValidationError:
            return HttpResponseBadRequest("Invalid email!")
