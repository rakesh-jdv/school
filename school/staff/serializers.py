from rest_framework import serializers
from staff.models import staff

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = staff
        fields = "__all__"


