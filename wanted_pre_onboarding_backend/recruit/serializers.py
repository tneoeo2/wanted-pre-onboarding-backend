import django_filters

from django.db.models import Q
from rest_framework import serializers

from .models import Company, Recruit, Apply


class RecruitFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='custom_filter')

    def custom_filter(self, queryset, name, value):
        company_results = Company.objects.filter(
            Q(name__icontains=value) |
            Q(country__icontains=value) |
            Q(region__icontains=value)
        )

        recruit_results = Recruit.objects.filter(
            Q(position__icontains=value) |
            Q(skill__icontains=value)
        )

        # 두 결과를 연결하여 반환
        return queryset.filter(Q(id__in=company_results.values('id')) | Q(id__in=recruit_results.values('id')))


    class Meta:
        model = Recruit
        fields = []
        
        
class RecruitSerializer(serializers.ModelSerializer):
    # company = serializers.CharField(source='company.name', label='회사명') 
    company = serializers.CharField(label='회사명') 
    class Meta:
        model = Recruit
        fields = ['id','company', 'position', 'reward', 'detail', 'skill']


class RecruitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruit
        fields = ['position', 'reward', 'detail', 'skill']


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = '__all__'