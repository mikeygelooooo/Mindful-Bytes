from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def home(request):
    posts = Post.objects.all().order_by("-date_posted")

    formatted_posts = [
        {
            "author": post.author,
            "slug": post.slug,
            "title": post.title,
            "content": post.content,
            "category": post.category,
            "date_posted": format_time(post.date_posted),
        }
        for post in posts
    ]

    return render(request, "blog/home.html", {"posts": formatted_posts})


def full_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, "blog/full_post.html", {"post": post})


def format_time(date):
    if not date:
        return ""

    now = timezone.now()
    diff = now - date

    seconds = diff.total_seconds()

    if seconds < 60:
        return "just now"

    minutes = int(seconds / 60)
    if minutes < 60:
        return f"{minutes}m"

    hours = int(minutes / 60)
    if hours < 24:
        return f"{hours}h"

    days = int(hours / 24)
    if days < 30:
        return f"{days}d"

    months = int(days / 30)
    if months < 12:
        return f"{months}mo"

    years = int(months / 12)
    return f"{years}y"
