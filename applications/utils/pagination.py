from rest_framework.pagination import PageNumberPagination, BasePagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'size'
    max_page_size = 10000


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'size'
    max_page_size = 30




