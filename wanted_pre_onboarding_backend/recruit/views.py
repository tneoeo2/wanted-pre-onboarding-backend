from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from .models import Recruit, Apply, Company
from .serializers import RecruitSerializer, RecruitUpdateSerializer, RecruitFilter

class RecruitListView(generics.ListAPIView):   #채용공고 목록보기
    queryset = Recruit.objects.all()
    serializer_class = RecruitSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecruitFilter
    
class RecruitCreateView(generics.CreateAPIView):   #채용공고 등록
    queryset = Recruit.objects.all()
    serializer_class = RecruitSerializer
    
    def perform_create(self, serializer):
        # 클라이언트가 제출한 회사 이름을 가져옴
        company_name = serializer.validated_data['company']
        # 회사 이름을 기반으로 회사를 찾음
        company, created = Company.objects.get_or_create(name=company_name)
        # 채용공고 정보에 회사 ID를 할당
        serializer.validated_data['company'] = company
        # 채용공고를 저장
        serializer.save()

class RecruitUpdateView(generics.UpdateAPIView):
    queryset = Recruit.objects.all()
    serializer_class = RecruitUpdateSerializer

    def get(self, request, *args, **kwargs):
        recruit = self.get_object()
        serializer = self.get_serializer(recruit)
        return Response(serializer.data)
    
    def perform_update(self, serializer):
        # 채용공고의 고유 ID를 가져옴
        recruit_id = self.kwargs['id']  # id는 URL에서 추출한 채용공고의 고유 ID
        # 채용공고를 찾아서 업데이트
        recruit = Recruit.objects.get(id=recruit_id)
        serializer.save()

    def get_object(self):
        # 기존의 채용공고를 반환
        recruit_id = self.kwargs['id']
        recruit = Recruit.objects.get(id=recruit_id)
        return recruit


class RecruitDeleteView(generics.DestroyAPIView):
    queryset = Recruit.objects.all()
    serializer_class = RecruitSerializer
    
    def get(self, request, *args, **kwargs):
        recruit = self.get_object()
        serializer = self.get_serializer(recruit)
        return Response(serializer.data)

    def get_object(self):
        recruit_id = self.kwargs['id']
        return get_object_or_404(self.queryset, id=recruit_id)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # 채용공고삭제
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)