from django.shortcuts import render
from rest_framework import generics 
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from .permissions import IsSuperUserOrAdminReadOnly,IsAuthorOrReadOnly,IsSuperUser
from .serializers import ArticleSerializer,UserSerializer
from blog.models import ArticleModel


# class ArticleAPIList(generics.ListCreateAPIView):
# 	queryset = ArticleModel.objects.filter(status=True)
# 	serializer_class = ArticleSerializer
# 	permission_classes=[IsAuthorOrReadOnly]

# class ArticleAPIDetail(generics.RetrieveUpdateAPIView):
# 	queryset = ArticleModel.objects.filter(status=True)
# 	# lookup_field='slug'
# 	multiple_lookup_fields=['slug',]
# 	serializer_class = ArticleSerializer
# 	permission_classes=[IsAuthorOrReadOnly]

# 	def get_object(self):
# 		queryset = self.get_queryset()
# 		filter = {}
# 		for field in self.multiple_lookup_fields:
# 			filter[field] = self.kwargs[field]

# 		obj = get_object_or_404(queryset, **filter)
# 		self.check_object_permissions(self.request, obj)
# 		return obj

class ArticleAPIViewset(viewsets.ModelViewSet):
	queryset=ArticleModel.objects.filter(status=True)
 	serializer_class = ArticleSerializer
 	lookup_field='slug'



# class UserAPIList(generics.ListCreateAPIView):
# 	queryset=get_user_model().objects.all()
# 	serializer_class = UserSerializer
# 	permission_classes=[IsSuperUserOrAdminReadOnly]

# class UserAPIDetail(generics.RetrieveAPIView):
# 	queryset=get_user_model().objects.all()
# 	serializer_class = UserSerializer
# 	permission_classes=[IsSuperUserOrAdminReadOnly]

class UserAPIViewset(viewsets.ModelViewSet):
	queryset=get_user_model().objects.all()
	serializer_class = UserSerializer



class DestroyToken(APIView):
	permission_classes=[IsSuperUser]
	def delete(self,request, *args, **kwargs):
		request.auth.delete()
		# return Response({'destroyed':'ok'})
		return Response(status=status.HTTP_204_NO_CONTENT)
		