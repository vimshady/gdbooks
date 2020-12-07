from .serializers import BookRequestListSerializer, BookRequestCreateSerializer
from .models import Book, Request
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.response import Response


class BookRequestList(APIView):
    """
    API endpoint that lists requests or lets you add one
    """
    queryset = Request.objects.all()
    serializer_class = BookRequestListSerializer

    def get_object(self, pk):
        try:
        	return Request.objects.get(pk=pk)
        except Request.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
    	if pk:
    		request = self.get_object(pk)
    		serializer = BookRequestListSerializer(request)
    		return Response(serializer.data)
    	requests = Request.objects.all()
    	serializer = BookRequestListSerializer(requests, many=True)
    	return Response(serializer.data)

    def delete(self, request, pk, format=None):
    	print('deleting')
    	request = self.get_object(pk)
    	request.delete()
    	return Response(status=status.HTTP_204_NO_CONTENT)

class BookRequestCreate(viewsets.ModelViewSet):
    """
    API endpoint that lists requests or lets you add one
    """
    queryset = Request.objects.all()
    serializer_class = BookRequestListSerializer

    def get_serializer_context(self):
        context = super(BookRequestCreate, self).get_serializer_context()
        context["email"] = request.data.get("email")
        context["title"] = request.data.get("title")
        return context

    def get_object(self, pk):
        try:
        	return Request.objects.get(pk=pk)
        except Request.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        print('request.data', request.data)
        serializer = BookRequestCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)