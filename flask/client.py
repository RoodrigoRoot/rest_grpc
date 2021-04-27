import users_pb2
import users_pb2_grpc
import grpc

try:
    channel = grpc.insecure_channel("localhost:50051")
    stub = users_pb2_grpc.UserStub(channel)
    response = stub.GetUser(users_pb2.Empty())
    print(response)
except grpc.RpcError as e:
    print(e)