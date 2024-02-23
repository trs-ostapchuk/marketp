from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Seller, Customer
from .serializers import SellerSerializer, CustomerSerializer
from rest_framework.authtoken.models import Token


class SellerRegistration(APIView):
    def post(self, request):
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerRegistration(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellerLogin(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            seller = Seller.objects.get(email=email, password=password)
            token, _ = Token.objects.get_or_create(user=seller)
            serializer = SellerSerializer(seller)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)
        except Seller.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class CustomerLogin(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            customer = Customer.objects.get(email=email, password=password)
            token, _ = Token.objects.get_or_create(user=customer)
            serializer = CustomerSerializer(customer)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class SellerList(APIView):
    def get(self, request):
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many=True)
        return Response(serializer.data)


class CustomerList(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
