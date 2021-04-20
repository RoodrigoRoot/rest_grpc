import users_pb2
import users_pb2_grpc
import grpc
from concurrent import futures


class UsersServicer(users_pb2_grpc.UserServicer):

    def GetUser(self, request, context):
        return users_pb2.UserInfo(
            name="Rodrigo",
            last_name="Urcino",
            email="francisco@miflink.com",
            age="25",
            phone="7411196882"
        )
         



class Server:

    @staticmethod
    def run():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        users_pb2_grpc.add_UserServicer_to_server(
            UsersServicer(), server
        )
        server.add_insecure_port('[::]:50050')
        server.start()
        print("running on port 50050")
        server.wait_for_termination()

Server.run()