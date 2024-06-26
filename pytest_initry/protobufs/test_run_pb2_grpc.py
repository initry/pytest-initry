# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import responses_pb2 as responses__pb2
import test_run_pb2 as test__run__pb2


class TestRunServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateTestRun = channel.unary_unary(
                '/TestRunService/CreateTestRun',
                request_serializer=test__run__pb2.CreateTestRunRequest.SerializeToString,
                response_deserializer=responses__pb2.StatusOk.FromString,
                )
        self.StopTestRun = channel.unary_unary(
                '/TestRunService/StopTestRun',
                request_serializer=test__run__pb2.StopTestRunRequest.SerializeToString,
                response_deserializer=responses__pb2.StatusOk.FromString,
                )


class TestRunServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateTestRun(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopTestRun(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TestRunServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateTestRun': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTestRun,
                    request_deserializer=test__run__pb2.CreateTestRunRequest.FromString,
                    response_serializer=responses__pb2.StatusOk.SerializeToString,
            ),
            'StopTestRun': grpc.unary_unary_rpc_method_handler(
                    servicer.StopTestRun,
                    request_deserializer=test__run__pb2.StopTestRunRequest.FromString,
                    response_serializer=responses__pb2.StatusOk.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TestRunService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TestRunService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateTestRun(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TestRunService/CreateTestRun',
            test__run__pb2.CreateTestRunRequest.SerializeToString,
            responses__pb2.StatusOk.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopTestRun(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TestRunService/StopTestRun',
            test__run__pb2.StopTestRunRequest.SerializeToString,
            responses__pb2.StatusOk.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
