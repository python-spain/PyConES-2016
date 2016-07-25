from braces.views import CsrfExemptMixin
from braces.views import GroupRequiredMixin
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from reviewers import review_group_name
from reviewers.forms import SignInForm, ReviewForm
from reviewers.models import Review


class SignInView(CsrfExemptMixin, View):
    """View to allow  to login users into the platform."""
    template_name = "reviewers/sign_in.html"
    groups = (review_group_name, )

    @staticmethod
    def get_next_page(request):
        """Gets the page to go after log in."""
        default_redirect = reverse('reviewers:list')
        next_page = request.GET.get('next') or request.POST.get('next')
        return next_page or default_redirect

    def check_membership(self, user):
        """ Check required group(s) """
        if user.is_superuser:
            return True
        user_groups = user.groups.values_list("name", flat=True)
        return set(self.groups).intersection(set(user_groups))

    def get(self, request):
        data = {
            "form": SignInForm(),
            "next": request.GET.get('next')
        }
        return render(request, self.template_name, data)

    def post(self, request):
        next_page = self.get_next_page(request=request)
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
                request=request
            )
            if user is not None and self.check_membership(user):
                login(request, user)
                return redirect(next_page)
        data = {"form": form, "next": next_page}
        return render(request, self.template_name, data)


class BaseReviewerView(GroupRequiredMixin, View):
    group_required = review_group_name
    login_url = reverse_lazy("reviewers:sign-in")


class ReviewListView(BaseReviewerView):
    template_name = "reviewers/list.html"

    def get(self, request):
        if request.user.is_superuser:
            reviews = Review.objects.all()
        else:
            reviews = Review.objects.filter(user=request.user)
        data = {
            "reviews": reviews
        }
        return render(request, self.template_name, data)


class ReviewView(BaseReviewerView):
    template_name = "reviewers/details.html"

    def get(self, request, pk):
        if request.user.is_superuser:
            review = get_object_or_404(Review, pk=pk)
        else:
            review = get_object_or_404(Review, pk=pk, user=request.user)
        form = ReviewForm(instance=review)
        data = {
            "review": review,
            "proposal": review.proposal,
            "form": form
        }
        return render(request, self.template_name, data)

    def post(self, request, pk):
        if request.user.is_superuser:
            review = get_object_or_404(Review, pk=pk)
        else:
            review = get_object_or_404(Review, pk=pk, user=request.user)
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect(reverse("reviewers:details", kwargs={"pk": review.pk}))
        data = {
            "review": review,
            "proposal": review.proposal,
            "form": form
        }
        return render(request, self.template_name, data)
