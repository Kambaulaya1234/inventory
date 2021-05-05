
from django.conf import settings
from django.contrib.auth.models import User,Group
from django.db.models import Avg
from django import template
from notifications.models import Notification
register = template.Library()


# User=settings.AUTH_USER_MODEL

# @register.inclusion_tag('shop/_order_items.html',takes_context=True)
# def order_panel(context):
#     request = context['request']
#     order=Order.objects.filter(user=request.user,ordered=True)
#     return {
#                     'orders':order[0],
#                     'ordersitems':order[0].items.all()
#     }


@register.simple_tag(takes_context=True)
def order_panel(context):
    request = context['request']
    order=Order.objects.filter(user=request.user,ordered=False)
    if order.exists():
        return {
                        'orders':order[0],
                        'ordersitems':order[0].items.all()
        }



@register.simple_tag()
def wishlists():
    wishlist_count=Wishlist.objects.all().count()
    return {'wishlist_count':wishlist_count}

@register.inclusion_tag('shop/_recently_items.html')
def recently_items():
    items=Item.objects.order_by('-timestamp')[:4]
    return {
                'recently_items':items
    }


@register.inclusion_tag('shop/_order_panel.html')
def odered_list():
    items=Item.objects.order_by('-timestamp')[:3]
    return {
                'recently_items':items
    }


@register.inclusion_tag('shop/_items.html')
def top_items():
    items=Item.objects.all()
    return {
                'items':items
    }

@register.inclusion_tag('shop/_arrival.html')
def arrival_products():
    items=Item.objects.order_by('-timestamp')
    return {
                'items':items
    }


@register.inclusion_tag('blog/_recently_posts.html')
def post_recents():
    posts=Post.objects.order_by('-created_at')[:4]
    return {
                'recents':posts
    }


   
@register.filter(name='range') 
def filter_range(number):
    data = int(number)
    return range(data )


@register.simple_tag(takes_context=True, name='user_count') 
def user_count(context):
    request=context['request']
    users=User.objects.filter(is_superuser=False).count()
    return users

@register.simple_tag(takes_context=True, name='notifications_count') 
def notifications_count(context):
    request=context['request']
    users=Notification.objects.filter(recipient=request.user).count()
    return users

@register.simple_tag( name='group_count') 
def group_count():
    groups=Group.objects.count()
    return groups

@register.simple_tag(takes_context=True, name='groups_name') 
def groups_name(context):
    request=context['request']
    for group in request.user.groups:
        return{
            'groups_name':groups_name
        }
         

@register.simple_tag( name='orders_count') 
def orders_count():
    orders=Order.objects.count()
    return orders

@register.simple_tag( name='subscribers_count') 
def subscribers_count():
    subscribers=Subscriber.objects.count()
    return subscribers

@register.simple_tag( name='rate_avg',takes_context=True) 
def rate_avg(context):
    item=Item.objects.filter(slug=context['item'].slug)[0]
    rates=item.rates.aggregate(rate_average=Avg('rate'))
    return rates

@register.simple_tag( name='rate_avg_rev',takes_context=True) 
def rate_avg_rev(context):
    item=Item.objects.filter(slug=context['item'].slug)[0]
    rates=item.rates.aggregate(rate_average_rev=5-Avg('rate'))
    return rates

@register.simple_tag( name='rateCountEach',takes_context=True) 
def rateCountEach(context):
    item=Item.objects.filter(slug=context['item'].slug)[0]
    fiverates=item.rates.filter(rate=5).count()
    four_rates=item.rates.filter(rate=4).count()
    three_rates=item.rates.filter(rate=3).count()
    two_rates=item.rates.filter(rate=2).count()
    one_rates=item.rates.filter(rate=1).count()
    data={
        'fiverates':fiverates,
        'four_rates':four_rates,
        'three_rates':three_rates,
        'two_rates':two_rates,
        'one_rates':one_rates,
    }
    return data

