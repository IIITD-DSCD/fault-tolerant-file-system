# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import backup_protocol_pb2 as backup__protocol__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ReplicaStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Read = channel.unary_unary(
                '/backup_protocol.Replica/Read',
                request_serializer=backup__protocol__pb2.ReadDeleteRequest.SerializeToString,
                response_deserializer=backup__protocol__pb2.ReadResponse.FromString,
                )
        self.Write = channel.unary_unary(
                '/backup_protocol.Replica/Write',
                request_serializer=backup__protocol__pb2.WriteRequest.SerializeToString,
                response_deserializer=backup__protocol__pb2.WriteResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/backup_protocol.Replica/Delete',
                request_serializer=backup__protocol__pb2.ReadDeleteRequest.SerializeToString,
                response_deserializer=backup__protocol__pb2.Response.FromString,
                )
        self.HandleWrite = channel.unary_unary(
                '/backup_protocol.Replica/HandleWrite',
                request_serializer=backup__protocol__pb2.WriteRequest.SerializeToString,
                response_deserializer=backup__protocol__pb2.WriteResponse.FromString,
                )


class ReplicaServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HandleWrite(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReplicaServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=backup__protocol__pb2.ReadDeleteRequest.FromString,
                    response_serializer=backup__protocol__pb2.ReadResponse.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=backup__protocol__pb2.WriteRequest.FromString,
                    response_serializer=backup__protocol__pb2.WriteResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=backup__protocol__pb2.ReadDeleteRequest.FromString,
                    response_serializer=backup__protocol__pb2.Response.SerializeToString,
            ),
            'HandleWrite': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleWrite,
                    request_deserializer=backup__protocol__pb2.WriteRequest.FromString,
                    response_serializer=backup__protocol__pb2.WriteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'backup_protocol.Replica', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Replica(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/backup_protocol.Replica/Read',
            backup__protocol__pb2.ReadDeleteRequest.SerializeToString,
            backup__protocol__pb2.ReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/backup_protocol.Replica/Write',
            backup__protocol__pb2.WriteRequest.SerializeToString,
            backup__protocol__pb2.WriteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/backup_protocol.Replica/Delete',
            backup__protocol__pb2.ReadDeleteRequest.SerializeToString,
            backup__protocol__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HandleWrite(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/backup_protocol.Replica/HandleWrite',
            backup__protocol__pb2.WriteRequest.SerializeToString,
            backup__protocol__pb2.WriteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class RegistryServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterReplica = channel.unary_unary(
                '/backup_protocol.RegistryServer/RegisterReplica',
                request_serializer=backup__protocol__pb2.ServerMessage.SerializeToString,
                response_deserializer=backup__protocol__pb2.ServerMessage.FromString,
                )
        self.NotifyPrimary = channel.unary_unary(
                '/backup_protocol.RegistryServer/NotifyPrimary',
                request_serializer=backup__protocol__pb2.ServerMessage.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetReplicas = channel.unary_unary(
                '/backup_protocol.RegistryServer/GetReplicas',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=backup__protocol__pb2.ServerListResponse.FromString,
                )


class RegistryServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterReplica(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NotifyPrimary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetReplicas(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RegistryServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterReplica': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterReplica,
                    request_deserializer=backup__protocol__pb2.ServerMessage.FromString,
                    response_serializer=backup__protocol__pb2.ServerMessage.SerializeToString,
            ),
            'NotifyPrimary': grpc.unary_unary_rpc_method_handler(
                    servicer.NotifyPrimary,
                    request_deserializer=backup__protocol__pb2.ServerMessage.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetReplicas': grpc.unary_unary_rpc_method_handler(
                    servicer.GetReplicas,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=backup__protocol__pb2.ServerListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'backup_protocol.RegistryServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RegistryServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterReplica(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/backup_protocol.RegistryServer/RegisterReplica',
            backup__protocol__pb2.ServerMessage.SerializeToString,
            backup__protocol__pb2.ServerMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NotifyPrimary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/backup_protocol.RegistryServer/NotifyPrimary',
            backup__protocol__pb2.ServerMessage.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetReplicas(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/backup_protocol.RegistryServer/GetReplicas',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            backup__protocol__pb2.ServerListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
