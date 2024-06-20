from typing import List

from django.http import HttpRequest
from ninja import NinjaAPI
from ninja.pagination import paginate

from api.employee.schema import EmployeeSchema
from api.employee.views.v1.services import employees_list_service
from api.utils import CustomPagination

# Create your views here.
api = NinjaAPI(urls_namespace="employee_api_v1")


@api.get("/employee", response=List[EmployeeSchema])
@paginate(CustomPagination)
def employee_list(request: HttpRequest):
    """API endpoint to retrieve a paginated list of employees.

    Retrieves employees from the database, optionally filtering by a search term.
    The results are paginated using a custom pagination class.

    Args:
        request (HttpRequest): The HTTP request object. It may contain a "search" query parameter
            used to filter the list of employees.

    Returns:
        Union[List[EmployeeSchema], dict]: A paginated list of `EmployeeSchema` objects if successful.
            If an error occurs, returns a dictionary with a "message" key containing the error details.

    Raises:
        Exception: If an error occurs during employee retrieval, it is caught and returned
            in the response as a dictionary.
    """
    try:
        search = request.GET["search"]
        return employees_list_service(search)
    except Exception as e:
        return {"message": str(e)}
