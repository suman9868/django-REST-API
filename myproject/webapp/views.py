# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeesSerializer

class employeesList(APIView):
	def get(self, request):
		e = employees.objects.all()
		serializer = employeesSerializer(e, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		#data = {'firstname': request.data.get('firstname'),'lastname': request.data.get('lastname'),'emp_id': request.data.get('emp_id')}
		data = JSONParser().parse(request)
		serializer = employeesSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def delete(self, request, format=None):
		e = employees.objects.all()
		e.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class employeesDetail(APIView):
	"""
	def get_object(self,pk):
		try:
			return employees.objects.get(pk=pk)
		except employees.DoesNotExist:
			raise Http404
	"""
	def get(self, request, pk, format=None):
		#e = self.get_object(pk)
		try:
			e = employees.objects.get(pk=pk)
			e = employeesSerializer(e)
			return Response(e.data)
		except employees.DoesNotExist:
			raise Http404
	
	def put(self, request, pk, format=None):
		e = employees.objects.get(pk=pk)
		serializer = employeesSerializer(e, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

	def delete(self, request, pk, format=None):
		e = employees.objects.get(pk=pk)
		e.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
