from django import template
from django.utils import timezone

SECOND = 0
MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR

register = template.Library()
# =================================================== FILTER FOR TEMPLATES

@register.filter
def model_type(value):
    """ Return the model of an object in a string form """
    return type(value).__name__


@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    """ Displays the right message 
        if the author is the current user or not """

    if user == context['user']:
        return 'Vous avez '
    return f"{user.username} a "

@register.simple_tag(takes_context=True)
def get_response_user(context, user):
    """ Displays the right message 
        if the author is the current user or not """

    if user == context['user']:
        return 'Vous répondez à votre demande '
    return f"Vous êtes en train de poster en réponse à {user.username} "

@register.filter
def get_posted_at_display(posted_at):
    """ Displays a nicer date and time for posts """

    seconds_ago = (timezone.now() - posted_at).total_seconds()
    if seconds_ago <= MINUTE:
        return f'Publié maintenant'
    if seconds_ago <= HOUR:
        return f'Publié il y a {int(seconds_ago // MINUTE)} minutes'
    elif seconds_ago <= DAY:
        return f'Publié il y a {int(seconds_ago // HOUR)} heures'
    return f'Publié le {posted_at.strftime("%d %b, %Y à %Hh%M")}'

