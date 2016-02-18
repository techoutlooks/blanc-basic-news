from django import template
from django.utils import timezone
from blanc_basic_news import get_post_model, get_category_model
from django.conf import settings
from blanc_basic_news.models import Category

register = template.Library()


@register.assignment_tag
def get_news_categories():
    return get_category_model().objects.all()


@register.assignment_tag
def get_news_months():
    return get_post_model().objects.filter(
        published=True, date__lte=timezone.now()).dates('date_url', 'month')


@register.assignment_tag
def get_latest_news(count, category=None):
    post_list = get_post_model().objects.select_related().filter(
        published=True, date__lte=timezone.now())

    # Optional filter by category
    if category is not None:
        post_list = post_list.filter(category__slug=category)

    return post_list[:count]
