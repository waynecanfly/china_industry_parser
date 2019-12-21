# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Industry


class IndustrySerializer(serializers.ModelSerializer):
    # ModelSerializer和Django中ModelForm功能相似
    # Serializer和Django中Form功能相似
    class Meta:
        model = Industry
        # 和"__all__"等价
        fields = ('industry', 'security_code', 'company_name')