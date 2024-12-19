from django.shortcuts import render
from rest_framework import generics
from .models import menu, booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import viewsets, permissions


# Create your views here.


def index(request):
    return render(request, 'index_start.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
