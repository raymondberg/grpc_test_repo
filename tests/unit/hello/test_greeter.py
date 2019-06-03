from hello.service import HelloRequest

from hello.greeter import Greeter

def test_greeter_responds_to_SayHello():
    request = HelloRequest(name='doc')

    response = Greeter().SayHello(request, {})

    assert response.message == 'What\'s up, doc?'
