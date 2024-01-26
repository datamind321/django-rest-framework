from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class MyPagination(PageNumberPagination):
    page_size=5
    page_query_param='p'
    page_size_query_param='records'   # user-define page params per page records
    max_page_size = 7
    last_page_strings = 'end'

class MyLimitPagination(LimitOffsetPagination):
    default_limit=5
    max_limit=7
    limit_query_param='lim'
    offset_query_param='off'


class MyCursorPagination(CursorPagination):
    page_size=5
    cursor_query_param='cur'
    ordering = 'name'

