import time
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc
from  app.udaconnect.services import LocationService


class LocationServicer(location_pb2_grpc.LocationServiceServicer):

    def Create(self, request, context):
        print("Received a message!")

        request_value = {
            "id": request.id,
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude,
            "creation_time": request.creation_time
        }
        print(request_value)
        LocationService.create(request_value)

        return location_pb2.LocationMessage(**request_value)