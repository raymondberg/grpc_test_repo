import hello.service as grpc_service

class Greeter(grpc_service.GreeterServicer):
    def SayHello(self, request, context):
        return grpc_service.HelloReply(message="What's up, {}?".format(request.name))
