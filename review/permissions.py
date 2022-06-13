from rest_framework.permissions import SAFE_METHODS,BasePermission


class isAdminOrReadOnly(BasePermission):
	def has_permission(self,request,view):
		if request.method in SAFE_METHODS:
			return True
		else:
			return request.user.is_staff

class isAuthenticatedOrReadOnly(BasePermission):
	def has_permission(self,request,view):
		if request.method in SAFE_METHODS:
			return True
		else:
			return request.user.is_staff