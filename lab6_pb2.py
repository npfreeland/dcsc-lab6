# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lab6.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nlab6.proto\x12\tlab6Proto\"\"\n\naddRequest\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\t\n\x01\x62\x18\x02 \x01(\x05\"\x15\n\x08\x61\x64\x64Reply\x12\t\n\x01\x63\x18\x01 \x01(\x05\"\x1e\n\x0frawimageRequest\x12\x0b\n\x03img\x18\x01 \x01(\x0c\"+\n\nimageReply\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\")\n\x11\x64otproductRequest\x12\t\n\x01\x61\x18\x01 \x03(\x01\x12\t\n\x01\x62\x18\x02 \x03(\x01\"\x1c\n\x0f\x64otproductReply\x12\t\n\x01\x63\x18\x01 \x01(\x01\"\x1f\n\x10jsonimageRequest\x12\x0b\n\x03img\x18\x01 \x01(\t2\x95\x02\n\x08Lab6grpc\x12\x35\n\x05\x64oAdd\x12\x15.lab6Proto.addRequest\x1a\x13.lab6Proto.addReply\"\x00\x12J\n\x0c\x64oDotproduct\x12\x1c.lab6Proto.dotproductRequest\x1a\x1a.lab6Proto.dotproductReply\"\x00\x12\x41\n\ndoRawimage\x12\x1a.lab6Proto.rawimageRequest\x1a\x15.lab6Proto.imageReply\"\x00\x12\x43\n\x0b\x64oJsonimage\x12\x1b.lab6Proto.jsonimageRequest\x1a\x15.lab6Proto.imageReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'lab6_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDREQUEST._serialized_start=25
  _ADDREQUEST._serialized_end=59
  _ADDREPLY._serialized_start=61
  _ADDREPLY._serialized_end=82
  _RAWIMAGEREQUEST._serialized_start=84
  _RAWIMAGEREQUEST._serialized_end=114
  _IMAGEREPLY._serialized_start=116
  _IMAGEREPLY._serialized_end=159
  _DOTPRODUCTREQUEST._serialized_start=161
  _DOTPRODUCTREQUEST._serialized_end=202
  _DOTPRODUCTREPLY._serialized_start=204
  _DOTPRODUCTREPLY._serialized_end=232
  _JSONIMAGEREQUEST._serialized_start=234
  _JSONIMAGEREQUEST._serialized_end=265
  _LAB6GRPC._serialized_start=268
  _LAB6GRPC._serialized_end=545
# @@protoc_insertion_point(module_scope)
