import grpc

import hello.service as grpc_service

def guide_greet(stub):
    response = stub.SayHello(
        grpc_service.HelloRequest(name="Peter")
    )
    print(response.message)


with grpc.insecure_channel('localhost:5000') as channel:
    stub = grpc_service.GreeterStub(channel)
    guide_greet(stub)
