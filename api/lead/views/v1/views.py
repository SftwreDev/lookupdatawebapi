from typing import List

from django.http import HttpRequest
from ninja import NinjaAPI
from ninja.pagination import paginate

from api.lead.schema import LeadSchema
from api.lead.views.v1.services import leads_list_service
from api.utils import CustomPagination

# Create your views here.
api = NinjaAPI(urls_namespace="leads_api_v1")


@api.get("/leads", response=List[LeadSchema])
@paginate(CustomPagination)
def leads_list(request: HttpRequest):
    """Retrieve a paginated list of leads, optionally filtered by a search term.

    Args::
        request (HttpRequest): The HTTP request object containing potential query parameters.

    Returns:
        List[LeadSchema]: A list of leads matching the search criteria, paginated.
        dict: An error message if an exception occurs during processing.

    Exceptions:
        Handles any exception by returning a dictionary with the error message.
    """
    try:
        search = request.GET["search"]
        return leads_list_service(search)
    except Exception as e:
        return {"message": str(e)}
