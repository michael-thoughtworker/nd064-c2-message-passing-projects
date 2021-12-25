import grpc
import location_pb2
import location_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.OrderServiceStub(channel)

# Update this with desired payload
location = location_pb2.LocationMessage(
    id=100,
    person_id=67,
    longitude="12.3"
    latitude='18.5',
    creation_time="2021-12-25"
)


response = stub.Create(location)