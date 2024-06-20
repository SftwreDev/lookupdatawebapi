import logging
from typing import List, Type, Union, Optional

from django.db.models import Q
from django.http import QueryDict

from api.lead.models import Lead

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
logger = logging.getLogger("default")
logger.setLevel(logging.DEBUG)


def leads_list_service(
    search: Optional[Union[Type[QueryDict], None]] = None
) -> Union[List[Lead], Exception]:
    """Fetches a list of leads from the database, optionally filtered by a search term.

    This service function retrieves all leads from the `Lead` model and can filter the
    results based on various fields if a search term is provided. The results are ordered
    by the `updated_at` field in descending order.

    Args:
        search (Optional[Union[Type[QueryDict], None]]): An optional search term to filter leads.
                                                     It can be a QueryDict type from Django's
                                                     request.GET or None.

    Returns:
        List[Lead]: A list of `Lead` objects matching the search criteria, ordered by `updated_at`.

    Raises:
        Exception: If an error occurs while fetching or filtering leads, it logs the error and
               re-raises the exception.
    """
    try:
        queryset = Lead.objects.all()
        if search:
            queryset = queryset.filter(
                Q(linkedin_url__icontains=search)
                | Q(is_demo_lead__icontains=search)
                | Q(urn__icontains=search)
                | Q(campaign_id__icontains=search)
                | Q(description__icontains=search)
                | Q(raw_json__name__icontains=search)
                | Q(raw_json__headquarter__icontains=search)
            )
        return queryset.order_by("-updated_at")
    except Exception as e:
        logger.error(f"Error getting leads list: {str(e)}")
        raise e
