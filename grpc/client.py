import grpc
import users_pb2
import users_pb2_grpc
try:
    channel = grpc.insecure_channel('localhost:50050')
    stub = users_pb2_grpc.UserStub(channel)
    response = stub.GetUser(users_pb2.Empty())
    print(response)
except Exception as e: 
    print(e)
