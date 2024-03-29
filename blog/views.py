from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Post, Comment, TeamMember
from .forms import CommentForm, RecipeForm
from django.views.generic.list import ListView
from django.urls import path


class RecipeList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(LoginRequiredMixin, View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class PostAdd(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """
    only loged in users can add a post
    """
    model = Post
    template_name = 'add_recipe.html'
    form_class = RecipeForm
    success_message = 'Recipe succesfully Added'

    def form_valid(self, form):
        """User who is signed in is set as the author of the posted recipe"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditRecipe(
    LoginRequiredMixin, SuccessMessageMixin,
    UserPassesTestMixin, generic.UpdateView
        ):
    """
    To update posts
    """
    model = Post
    form_class = RecipeForm
    template_name = 'edit_post.html'
    success_message = 'The post has been updated successfully!'

    def form_valid(self, form):
        """
        The user who is signed in is set to be the author of the post
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Only the author can Edit the post
        """
        recipe = self.get_object()
        return recipe.author == self.request.user


class DeleteRecipe(
        LoginRequiredMixin, SuccessMessageMixin,
        UserPassesTestMixin, generic.DeleteView
        ):
    """
    Allow user to delete a post
    Success message as user feedback
    """
    model = Post
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('home')
    success_message = 'Post Deleted'

    def delete(self, request, *args, **kwargs):
        """Generate success message on delete view"""
        messages.success(self.request, self.success_message)
        return super(DeleteRecipe, self).delete(request, *args, **kwargs)

    def test_func(self):
        """Test that logged in user is post author"""
        recipe = self.get_object()
        return recipe.author == self.request.user


class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'team.html'
    context_object_name = 'teammembers'


def handler404(request, exception):
    """
    Custom 404 page
    """
    return render(request, '404.html', status=404)


def handler500(request):
    """
    Custom 500 page
    """
    return render(request, '500.html', status=500)


def handler403(request, exception):
    """
    Custom 403 page
    """
    return render(request, '403.html', status=403)


def handler405(request, exception):
    """
    Custom 405 page
    """
    return render(request, '405.html', status=405)
