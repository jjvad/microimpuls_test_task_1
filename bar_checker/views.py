from rest_framework import generics
from rest_framework.response import Response
from .models import PressureRecord
from .serializers import PressureRecordSerializer
from django.utils import timezone
from datetime import timedelta
from django.db.models import Avg


class PressureRecordCreateView(generics.CreateAPIView):
    serializer_class = PressureRecordSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LastRecordView(generics.RetrieveAPIView):
    serializer_class = PressureRecordSerializer

    def get_object(self):
        return PressureRecord.objects.filter(user=self.request.user).latest('timestamp')


class StatsView(generics.GenericAPIView):
    def get(self, request, period):
        user = request.user
        now = timezone.now()

        if period == 'day':
            start = now - timedelta(days=1)
        elif period == 'month':
            start = now - timedelta(days=30)
        else:
            return Response({"error": "Invalid period"}, status=400)

        stats = PressureRecord.objects.filter(
            user=user,
            timestamp__gte=start
        ).aggregate(
            avg_systolic=Avg('systolic'),
            avg_diastolic=Avg('diastolic')
        )

        return Response(stats)