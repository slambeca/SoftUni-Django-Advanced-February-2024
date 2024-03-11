from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import mixins as auth_mixins
from django.views import generic as views


def index(request):
    print(request.user)
    print(request.user.is_superuser)
    print(request.user.is_anonymous)
    print(request.user.is_authenticated)
    print(request.user.get_username())
    # print(request.user.get_user_permissions())
    # print(request.user.get_full_name())
    # print(request.user.get_short_name())

    return HttpResponse('It works!')


@login_required
def about(request):
    return HttpResponse(f"It's about that, {request.user}!")


class TeamView(auth_mixins.LoginRequiredMixin, views.View):
    def get(self, request):
        return HttpResponse(f"{request.user}'s team!")