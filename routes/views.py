from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Route, Stop
from .serializers import RouteSerializer, StopSerializer

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    @action(detail=True, methods=['get', 'post'])
    def stops(self, request, pk=None):
        route = self.get_object()

        if request.method == 'GET':
            stops = route.stops.all().order_by('order')
            serializer = StopSerializer(stops, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            # For bulk update, you can accept a list of stops
            stops_data = request.data
            if not isinstance(stops_data, list):
                return Response({"error": "Expected a list of stops"}, status=status.HTTP_400_BAD_REQUEST)

            # Remove existing stops and add new ones (simplest approach)
            route.stops.all().delete()
            for stop_data in stops_data:
                Stop.objects.create(route=route, **stop_data)

            return Response({"status": "Stops updated"}, status=status.HTTP_200_OK)