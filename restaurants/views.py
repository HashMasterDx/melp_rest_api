from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RestaurantSerializer
from .models import Restaurant
import math


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.AllowAny]


def haversine_distance(lat1, lon1, lat2, lon2):
    """Calcula la distancia Haversine entre dos puntos (en metros)."""
    R = 6371000  # Radio de la Tierra en metros
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) * math.sin(delta_phi / 2) + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2) * math.sin(delta_lambda / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


class RestaurantStatisticsView(APIView):
    def get(self, request):
        latitude = float(request.query_params.get('latitude'))
        longitude = float(request.query_params.get('longitude'))
        radius = float(request.query_params.get('radius', 1000))

        restaurants_within_radius = []

        for restaurant in Restaurant.objects.all():
            distance = haversine_distance(latitude, longitude, restaurant.lat, restaurant.lng)
            if distance <= radius:
                restaurants_within_radius.append(restaurant)

        count = len(restaurants_within_radius)
        ratings = [r.rating for r in restaurants_within_radius]

        avg_rating = sum(ratings) / count if count > 0 else 0
        std_dev_rating = 0  # Calcular la desviación estándar manualmente

        if count > 1:
            variance = sum((x - avg_rating) ** 2 for x in ratings) / (count - 1)
            std_dev_rating = math.sqrt(variance)

        return Response({
            'count': count,
            'avg_rating': round(avg_rating, 2),
            'std_dev_rating': round(std_dev_rating, 2)
        })