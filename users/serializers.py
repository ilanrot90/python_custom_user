from rest_framework import serializers
from django_countries import Countries
from users.models import CustomUser


class SerializableCountryField(serializers.ChoiceField):
    def to_representation(self, value):
        if value in ('', None):
            return ''  # instead of `value` as Country(u'') is not serializable
        return super(SerializableCountryField, self).to_representation(value)


class UserSerializer(serializers.ModelSerializer):
    country = SerializableCountryField(allow_blank=True, choices=Countries())

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'country', 'date_of_birth']
