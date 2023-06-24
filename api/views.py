from django.shortcuts import render
from rest_framework import generics 
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework import filters
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
	queryset=ArticleModel.objects.all()
	serializer_class = ArticleSerializer
	lookup_field='slug'
	filterset_fields=['author','status']
	filter_backends = [filters.SearchFilter,filters.OrderingFilter]
	ordering_fields=['title','published']
	ordering='-published'
	search_fields=['title','=author__username','=author__last_name','=author__first_name','content']
	# permission_classes=[IsAuthorOrReadOnly]
	def get_permissions(self):
		return [IsAuthorOrReadOnly()]

	# def get_queryset(self):
	# 	queryset=ArticleModel.objects.all()
	# 	status=self.request.query_params.get('status')
	# 	author=self.request.query_params.get('author')
	# 	if status is not None:
	# 		queryset=queryset.filter(status=status)
	# 	if author is not None:
	# 		queryset=queryset.filter(author=author)

		return queryset




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
	permission_classes=[IsSuperUserOrAdminReadOnly]



class DestroyToken(APIView):
	permission_classes=[IsSuperUser]
	def delete(self,request, *args, **kwargs):
		request.auth.delete()
		# return Response({'destroyed':'ok'})
		return Response(status=status.HTTP_204_NO_CONTENT)
		