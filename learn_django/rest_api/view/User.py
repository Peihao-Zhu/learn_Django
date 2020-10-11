
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from rest_api.models import User
from rest_api.serializer.UserSerializer import UserSerializer

# 查询所有用户列表
class UserList(APIView):

    def get(self, request, id=0):
        # 将Django自带的ORM框架 返回的QuerySet对象进行序列化
        serializer = UserSerializer(User.objects.all(), many=True)
        data = serializer.data
        return JsonResponse({'code': status.HTTP_200_OK , 'message': 'success', 'data': data})


# 对单个用户的增改查
class UserDetail(APIView):

    def get(self, request):
        id = request.GET.get('id')
        # 将Django自带的ORM框架 返回的QuerySet对象进行序列化
        serializer = UserSerializer(User.objects.get(id=id))
        data = serializer.data
        return JsonResponse({'code': status.HTTP_200_OK , 'message': 'success', 'data': data})

    def put(self, request):
        id = request.GET.get('id')
        print(id)
        user = User.objects.get(id=id)
        # partial 为True 表示只传递要修改的那部分值
        obj = UserSerializer(data=request.data, instance=user, partial=True)
        if obj.is_valid():
            obj.save()
            return JsonResponse({'code': status.HTTP_200_OK , 'message': 'success'})
        return  JsonResponse({'code': status.HTTP_400_BAD_REQUEST , 'message': obj.errors})

    def post(self, request):
        # 对获取到的Json请求体 进行反序列化
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'code': status.HTTP_200_OK, 'message': 'success'})
        return JsonResponse({'code': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors})