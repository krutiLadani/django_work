from import_export import resources
from django.contrib.auth.models import User
from import_export.fields import Field


class UserResource(resources.ModelResource):
    enrol_no = Field(column_name='enrol_no')
    contact = Field(column_name='contact')

    class Meta:
        model = User
        fields = ('id', 'password', 'first_name', 'last_name', 'email', 'is_staff',
                  'is_active','enrol_no','contact')
