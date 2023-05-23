# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import backend_pb2 as backend__pb2


class WsProtoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createGameEvent = channel.unary_unary(
                '/WsProto/createGameEvent',
                request_serializer=backend__pb2.Post.SerializeToString,
                response_deserializer=backend__pb2.GameResponce.FromString,
                )
        self.editGameEvent = channel.unary_unary(
                '/WsProto/editGameEvent',
                request_serializer=backend__pb2.UpdatePost.SerializeToString,
                response_deserializer=backend__pb2.GameResponce.FromString,
                )
        self.createMoveEvent = channel.unary_unary(
                '/WsProto/createMoveEvent',
                request_serializer=backend__pb2.MovePost.SerializeToString,
                response_deserializer=backend__pb2.CheckerMoveResponce.FromString,
                )


class WsProtoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def createGameEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def editGameEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createMoveEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WsProtoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createGameEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.createGameEvent,
                    request_deserializer=backend__pb2.Post.FromString,
                    response_serializer=backend__pb2.GameResponce.SerializeToString,
            ),
            'editGameEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.editGameEvent,
                    request_deserializer=backend__pb2.UpdatePost.FromString,
                    response_serializer=backend__pb2.GameResponce.SerializeToString,
            ),
            'createMoveEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.createMoveEvent,
                    request_deserializer=backend__pb2.MovePost.FromString,
                    response_serializer=backend__pb2.CheckerMoveResponce.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'WsProto', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WsProto(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def createGameEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/WsProto/createGameEvent',
            backend__pb2.Post.SerializeToString,
            backend__pb2.GameResponce.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def editGameEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/WsProto/editGameEvent',
            backend__pb2.UpdatePost.SerializeToString,
            backend__pb2.GameResponce.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createMoveEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/WsProto/createMoveEvent',
            backend__pb2.MovePost.SerializeToString,
            backend__pb2.CheckerMoveResponce.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)