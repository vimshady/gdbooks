from rest_framework import serializers

from .models import Request

class BookRequestListSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer to define the Book API representation.
    """

    class Meta:
        model = Request
        fields = ('id',)

    def get_queryset(self):
        queryset = self.queryset.filter()

        request_id = self.request.query_params.get('id', None)
        if request_id is not None:
            queryset = queryset.get(id=request_id)

        return queryset

class BookRequestCreateSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer to define the Book API representation.
    """

    class Meta:
        model = Request
        fields = ('id',)

    def create(self, validated_data):
        print('yoaa')
        print(self.context, validated_data)
        # print(validated_data)
        # need_id = self.context['request'].data.get('title')  
        # book_title = request_id = self.request.query_params.get('title', None)
        # print(book_title)
        # obj = Request.objects.create(**validated_data, book_title=book_title)
        pass
        # return obj


# POST /request

# - email (string): Requesting user's email address
# - title (string): Desired book title

# Response

# - id (int): ID of the book
# - available (boolean): return whether a specific book is available (a book is available if it has not been requested by anyone)
# - title (string): Title of the book
# - timestamp (string): ISO-8601 formatted date/time the book was requested



# Retrieve request endpoint
# Allows users to retrieve/see an existing request by using an id, or a list of all existing requests if id is omitted.

# Request

# GET /request/ -or- GET /request/<id>

# Response

# If id isn't set, return all existing requests. Otherwise, return the specified request data.



# Delete request endpoint
# Allows a user to remove an existing request, making that book available.

# Request

# DELETE /request/<id>

# Response

# Empty response body
