from rest_framework.pagination import PageNumberPagination


class TaskPagination(PageNumberPagination):
    page_size = 2  # Number of items to include in each page
    page_size_query_param = 'page_size'  # Custom query parameter to override page_size
    max_page_size = 100