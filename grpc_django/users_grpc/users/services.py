import grpc
from . import users_pb2
from . import users_pb2_grpc

class UsersServicer(users_pb2_grpc.UserServicer):

    def GetUser(self, request, context):
        return users_pb2.UserInfo(
            name="rodrigo",
            last_name="urcino",
            email="francisco@miflink.com",
            age="25",
            phone="7411196882"
        )


def grpc_user(server):
    users_pb2_grpc.add_UserServicer_to_server(UsersServicer(), server)
    
