# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: backup_protocol.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x62\x61\x63kup_protocol.proto\x12\x0f\x62\x61\x63kup_protocol\".\n\rServerMessage\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"H\n\x12ServerListResponse\x12\x32\n\nserverList\x18\x01 \x03(\x0b\x32\x1e.backup_protocol.ServerMessage\";\n\x0cWriteRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x0c\n\x04uuid\x18\x03 \x01(\t\"W\n\rWriteResponse\x12\'\n\x06status\x18\x01 \x01(\x0e\x32\x17.backup_protocol.Status\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\"!\n\x11ReadDeleteRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\">\n\x07\x41llData\x12\x33\n\x0creadResponse\x18\x01 \x03(\x0b\x32\x1d.backup_protocol.ReadResponse\"g\n\x0cReadResponse\x12\'\n\x06status\x18\x01 \x01(\x0e\x32\x17.backup_protocol.Status\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\"E\n\x08Response\x12)\n\x08response\x18\x01 \x01(\x0e\x32\x17.backup_protocol.Status\x12\x0e\n\x06reason\x18\x02 \x01(\t\"0\n\nFileDetail\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"9\n\x08\x46ileList\x12-\n\x08\x66ileList\x18\x01 \x03(\x0b\x32\x1b.backup_protocol.FileDetail\"\x1b\n\x0bRequestType\x12\x0c\n\x04type\x18\x01 \x01(\t*\x1f\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\x32\xb1\x02\n\x07Replica\x12I\n\x04Read\x12\".backup_protocol.ReadDeleteRequest\x1a\x1d.backup_protocol.ReadResponse\x12\x46\n\x05Write\x12\x1d.backup_protocol.WriteRequest\x1a\x1e.backup_protocol.WriteResponse\x12G\n\x06\x44\x65lete\x12\".backup_protocol.ReadDeleteRequest\x1a\x19.backup_protocol.Response\x12J\n\nGetAllData\x12\".backup_protocol.ReadDeleteRequest\x1a\x18.backup_protocol.AllData2\xb5\x01\n\x0eRegistryServer\x12Q\n\x0fRegisterReplica\x12\x1e.backup_protocol.ServerMessage\x1a\x1e.backup_protocol.ServerMessage\x12P\n\x0bGetReplicas\x12\x1c.backup_protocol.RequestType\x1a#.backup_protocol.ServerListResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'backup_protocol_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STATUS._serialized_start=727
  _STATUS._serialized_end=758
  _SERVERMESSAGE._serialized_start=42
  _SERVERMESSAGE._serialized_end=88
  _SERVERLISTRESPONSE._serialized_start=90
  _SERVERLISTRESPONSE._serialized_end=162
  _WRITEREQUEST._serialized_start=164
  _WRITEREQUEST._serialized_end=223
  _WRITERESPONSE._serialized_start=225
  _WRITERESPONSE._serialized_end=312
  _READDELETEREQUEST._serialized_start=314
  _READDELETEREQUEST._serialized_end=347
  _ALLDATA._serialized_start=349
  _ALLDATA._serialized_end=411
  _READRESPONSE._serialized_start=413
  _READRESPONSE._serialized_end=516
  _RESPONSE._serialized_start=518
  _RESPONSE._serialized_end=587
  _FILEDETAIL._serialized_start=589
  _FILEDETAIL._serialized_end=637
  _FILELIST._serialized_start=639
  _FILELIST._serialized_end=696
  _REQUESTTYPE._serialized_start=698
  _REQUESTTYPE._serialized_end=725
  _REPLICA._serialized_start=761
  _REPLICA._serialized_end=1066
  _REGISTRYSERVER._serialized_start=1069
  _REGISTRYSERVER._serialized_end=1250
# @@protoc_insertion_point(module_scope)
