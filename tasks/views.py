from rest_framework import viewsets
from .models import Task
from .paginations import TaskPagination
from .serializers import TaskSerializers, TaskSerializersDetails
from .filters import TaskFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework import authentication, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from like.models import Like

# class Tasks(ListCreateAPIView):
#     queryset= Task.objects.all()
#     serializer_class= TaskSerializers
    # filter_backends = [filters.BaseFilterBackend]
    # filterset_fields = ['start', 'end', 'vehicle']

class Tasks(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = TaskPagination

    # filter_backends = [filters.BaseFilterBackend]
    # filterset_class = TaskFilter

    def get(self, request, format=None) -> Response:
        queryset = Task.objects.all()
        # filtered = self.filterset_class(request.GET, queryset=queryset).qs
        paginator = TaskPagination()
        paginated = paginator.paginate_queryset(queryset, request)
        serialized = TaskSerializers(queryset, many=True, context={'request': request})
        return Response({
            'count': paginator.page.paginator.count,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'results': serialized.data
        })

    def post(self, request, format=None) -> Response:
        # Deserialize the request data using your serializer
        serialized = TaskSerializers(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.data, status=status.HTTP_400_BAD_REQUEST)


# class TaskDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers

# from rest_framework import viewsets, status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from .models import Task
# from .serializers import TaskSerializersDetails

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializersDetails
    permission_classes = [IsAuthenticated]
    pagination_class = TaskPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = TaskFilter

    def get_serializer_class(self):
        if self.action == "list":
            return TaskSerializers
        return super(TaskViewSet, self).get_serializer_class()

    def get_queryset(self):
        search = self.request.query_params.get('search', None)
        if search:
            return Task.objects.filter(description__contains=search)
        return super(TaskViewSet, self).get_queryset()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True,)
            result = self.get_paginated_response(serializer.data)

        else:
            serializer = self.get_serializer(queryset, many=True,)
            result = serializer

        return Response(result.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            obj = self.get_object()
        except Task.DoesNotExist:
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
        serialized = self.get_serializer(obj)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, permission_classes=[IsAuthenticated], methods=['patch'])
    def like(self, request, *args, **kwargs):
        print('check')
        task_id = request.data.get('task_id')
        print(task_id)
        task = Task.objects.filter(id=task_id).first()
        if not task:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="task Not found!")
        message = Like.objects.like(user=request.user, instance=task)
        return Response(status=status.HTTP_200_OK, data=message)
