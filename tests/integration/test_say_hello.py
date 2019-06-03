import hello.service as grpc_service


def test_some(grpc_client):
    response = grpc_client.SayHello(
        grpc_service.HelloRequest(name='doc')
    )

    assert response.message == 'What\'s up, doc?'
