from rest_framework import serializers

from api.models import Staffs

class StaffsSerializer(serializers.ModelSerializer):

    class Meta:

        model=Staffs

        fields="__all__"

        read_only_fields=["id"]