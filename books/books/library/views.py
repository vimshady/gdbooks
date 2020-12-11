from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Book, Request

@api_view(['GET', 'POST', 'DELETE'])
def request_view(request, pk=None):
	if request.method == 'POST':

		try:
			validate_email(request.data['email'])
		except ValidationError:
			return Response({"message": "Provide a valid email", "data": {}})
		try:
			book = Book.objects.get(title=request.data['title'])
		except:
			return Response({"message": "Title doest not exist in our list of titles in the database", "data": {}})

		if book.is_available():
			print('bok', book.is_available)
			r = Request.objects.create(book=book, email=request.data['email'])
			return Response({"message": "Request made!", "data": {
				'id': book.id,
				'available': book.is_available(),
				'title': book.title,
				'timestamp': book.request.timestamp
				}})
		else:
			return Response({"message": "Could not request. See existing request", "data": {
				'id': book.id,
				'available': book.is_available(),
				'title': book.title,
				'timestamp': book.request.timestamp
				}})
	if request.method == 'DELETE':
		try:
			r = Request.objects.get(pk=pk)
		except:
			return Response({"message": "Could not find your request", "data": {}})
		r.delete()
		return Response({"message": "Request deleted. Book now available", "data": {}})
	print('GET request')
	if request.method == 'GET':
		if pk:
			try:
				r = Request.objects.get(pk=pk)
			except:
				return Response({"message": "Could not find your request", "data": {}})

			return Response({"message": "GET", "data":{
					'id': r.book.id,
					'available': r.book.is_available(),
					'title': r.book.title,
					'timestamp': r.timestamp
					}})
		else:
			data = []
			for r in Request.objects.all():
				data.append({
					'id': r.book.id,
					'available': r.book.is_available(),
					'title': r.book.title,
					'timestamp': r.timestamp
					})

	return Response({"message": "GET", "data":data})