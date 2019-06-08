
"""
try:
    validate_email(username)
    valid_email = True
except validate_email.ValidationError:
    valid_email = False
"""

from .models import User, Address, BillingInfo

from django.core.serializers.json import DjangoJSONEncoder
from django.core.validators import validate_email
from django.http import HttpResponse
from django.views.generic import View

import datetime
import json
# datetime.datetime.strptime(json, "%Y-%m-%dT%H:%M:%S.%fZ")

class GetUsers(View):
    def get(self, request, *args, **kwargs):
        users = [{
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        } for user in User.objects.all()]

        # return HttpResponse(json.dumps(users, cls=DjangoJSONEncoder))
        return HttpResponse(json.dumps(json.loads(request.body.decode("utf-8")), cls=DjangoJSONEncoder))

class RegisterUser(View):
    def post(self, request, *args, **kwargs):
        
        return HttpResponse()

class UpdateUser(View):
    def patch(self, *args, **kwargs):
        return HttpResponse("Update")
