from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Company
from .serializers import CompanySerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET'])
def testapi(request):
    api_urls = {
        'List': '/company-list/',
        'Detail View': '/company-detail/<str:pk>',
        'Create': '/company-create/',
        'Delete': '/company-delete/<str:pk>',
        'Update': '/company-update/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def companyList(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def companyDetail(request, pk):
    company = Company.objects.get(id = pk)
    serializer = CompanySerializer(company, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def companyCreate(request):
    serializer = CompanySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def companyUpdate(request, pk):
    company = Company.objects.get(id = pk)
    serializer = CompanySerializer(instance=company, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def companyDelete(request, pk):
    company = Company.objects.get(id = pk).delete()
    return JsonResponse({'message': '{} Company were deleted successfully!'.format(company[0])}, status=status.HTTP_204_NO_CONTENT)

def view_company(request):
    companies = Company.objects.all()
    return render(request, 'company/list-company.html', {'companies': companies})

@csrf_exempt
def companyApi(request, id=0):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_serializer = CompanySerializer(companies, many=True)
        return JsonResponse(companies_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CompanySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Fail to add!", safe=False)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        company = Company.objects.get(id = data['id'])
        serializer = CompanySerializer(instance=company, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Update successfully!", safe=False)
        return JsonResponse("Fail to update!", safe=False)
    elif request.method == "DELETE":
        company = Company.objects.get(id = id)
        company.delete()
        return JsonResponse("Delete successfully!", safe=False)

