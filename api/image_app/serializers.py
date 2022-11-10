from rest_framework import serializers
from api.image_app.models import Imageaws

class ImageawsSerializer(serializers.ModelSerializer):

    document = serializers.ImageField(required=False)

    class Meta:
        model = Imageaws
        fields = ['title','document']
