from imp import new_module
from rest_framework import serializers
from .models import *

class test_Serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = demo
        fields = ('title','description')