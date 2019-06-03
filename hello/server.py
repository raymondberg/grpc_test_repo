from concurrent import futures
import time

import grpc

from .greeter import Greeter

import hello.service as grpc_service

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_service.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:5000')
    server.start()
    while True:
        time.sleep(6)


if __name__ == '__main__':
    run_server()
