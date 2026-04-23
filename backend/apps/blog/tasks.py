from celery import shared_task
from .models import PostAnalytics
import logging

logger = logging.getLogger(__name__)


@shared_task
def increment_post_impressions(post_id):
    """
    Incrementa las imporesiones del post asociado
    """
    try:
        analytics, created = PostAnalytics.objects.get_or_create(post__id = post_id)
        analytics.increment_impression()
    except Exception as e:
        logger.info(f"Error incrementing impressions for Post ID {post_id}: {str(e)}")