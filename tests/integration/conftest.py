import os
import signal
import subprocess
import time

import grpc
import pytest

import hello.service as grpc_service


@pytest.fixture(scope="session", autouse=True)
def grpc_server():
	process = subprocess.Popen(
		['python', '-m', 'hello.server'],
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
	)

	yield process

	process.kill()
	output, error = process.communicate(timeout=1)
	assert not error 


@pytest.fixture
def grpc_client():
	with grpc.insecure_channel('localhost:5000') as channel:
		stub = grpc_service.GreeterStub(channel)
		yield stub
