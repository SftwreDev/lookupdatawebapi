from typing import Any

from ninja import Field, Schema
from ninja.errors import HttpError
from ninja.pagination import PaginationBase


class CustomPagination(PaginationBase):
    class Input(Schema):
        page: int = Field(1, ge=1)
        page_size: int = Field(10, ge=10)

    class Output(Schema):
        total_items_count: int
        total_pages_count: int
        page_size: int | None
        page: int
        previous_page: str | None
        next_page: str | None

    def __init__(self, page_size: int = 10, **kwargs):
        self.page_size = page_size
        super().__init__(**kwargs)

    def paginate_queryset(self, queryset, pagination: Input, request) -> Any:
        try:
            offset = (pagination.page - 1) * self.page_size
            total_items_count = self._items_count(queryset)
            next_page, previous_page = None, None
            self.page_size = pagination.page_size
            if pagination.page > 1:
                previous_page = request.build_absolute_uri(
                    request.path + "?page=" + str(pagination.page - 1)
                )
            if offset + self.page_size < total_items_count:
                next_page = request.build_absolute_uri(
                    request.path + "?page=" + str(pagination.page + 1)
                )
            return {
                "total_items_count": total_items_count,
                "total_pages_count": (total_items_count + self.page_size - 1)
                // self.page_size,
                "page_size": self.page_size,
                "page": pagination.page,
                "previous_page": previous_page,
                "next_page": next_page,
                "items": queryset[offset : offset + self.page_size],
            }
        except Exception as e:
            raise HttpError(400, str(e))


class Error(Schema):
    message: str
