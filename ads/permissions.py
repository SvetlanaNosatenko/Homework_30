from rest_framework import permissions

from ads.models import User, Ads


class AdsPermission(permissions.BasePermission):
    message = 'Changing ad for non admin or non moderator user not allowed.'

    def has_permission(self, request, view):
        if request.user.role in [User.MODERATOR, User.ADMIN]:
            return True

        qs = Ads.objects.get(pk=view.kwargs["pk"])

        if qs.author_id_id == request.user.id:
            return True
        return False