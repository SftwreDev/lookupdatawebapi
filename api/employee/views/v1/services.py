import logging
from typing import List, Type, Union, Optional

from django.db.models import Q
from django.http import QueryDict

from api.employee.models import Employee

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
logger = logging.getLogger("default")
logger.setLevel(logging.DEBUG)


def employees_list_service(
    search: Optional[Union[Type[QueryDict], None]] = None
) -> Union[List[Employee], Exception]:
    """Retrieves a list of employees from the database, optionally filtering based on a search term.

    Args:
        search (Optional[Union[Type[QueryDict], None]]): An optional search term for filtering the employees.
            The search term is applied to various fields including first name, last name, URN, lead ID,
            and the title of the current position.

    Returns:
        Union[List[Employee], Exception]: A list of `Employee` objects matching the search criteria if provided,
            otherwise all employees. If an error occurs, it raises an exception.

    Raises:
        Exception: If an error occurs during the retrieval of employees, the exception is logged and re-raised.
    """
    try:
        queryset = Employee.objects.all()
        if search:
            queryset = queryset.filter(
                Q(first_name__icontains=search)
                | Q(last_name__icontains=search)
                | Q(urn__icontains=search)
                | Q(lead_id__icontains=search)
                | Q(raw_json__currentPositions__0__title__icontains=search)
            )
        return queryset.order_by("-updated_at")
    except Exception as e:
        logger.error(f"Error getting employees list: {str(e)}")
        raise e
