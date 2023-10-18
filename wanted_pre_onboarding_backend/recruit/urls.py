from django.urls import path

from .views import RecruitListView, RecruitCreateView,RecruitUpdateView, RecruitDeleteView
# from .views import

urlpatterns = [
    path('list/', RecruitListView.as_view(), name='recruit_list'),
    path('upload/', RecruitCreateView.as_view(), name='upload_recruit'),
    path('update/<int:id>/', RecruitUpdateView.as_view(), name='update_recruit'),
    path('delete/<int:id>/', RecruitDeleteView.as_view(), name='delete_recruit'),
]
