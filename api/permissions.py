from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS



class IsSuperUserOrAdminReadOnly(BasePermission):
	"""
	The request is authenticated as a superuser, or authenticated as a admin and read-only request.
	"""

	def has_permission(self, request, view):
		return bool(
			request.method in SAFE_METHODS  and
			request.user.is_staff or
			request.user and
			request.user.is_superuser
		)


class IsAuthorOrReadOnly(BasePermission):
	"""
	The request is authenticated as a Author, or read-only request.
	"""

	def has_permission(self, request, view):
		if request.method in SAFE_METHODS or request.user.is_authenticated and  request.user.is_author or request.user.is_superuser:
			return True