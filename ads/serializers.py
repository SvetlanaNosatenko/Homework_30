from rest_framework import serializers

from ads.models import Ads, Selection


class AdsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ads
        fields = '__all__'


class SelectionDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ["id"]


class SelectionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ["id", "name"]


class SelectionDetailSerializer(serializers.ModelSerializer):
    ad = AdsSerializer(many=True, read_only=True)

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ["name", "owner", "ad"]


class SelectionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["name", "owner", "ad"]

