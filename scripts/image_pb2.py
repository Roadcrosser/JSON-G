# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schemas/image.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13schemas/image.proto\x12\x05jsong\"\xbc\x03\n\x05Image\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x12\x14\n\x0ctransparency\x18\x03 \x01(\x08\x12\x1f\n\x04size\x18\x04 \x01(\x0b\x32\x11.jsong.Image.Size\x12\"\n\x06layers\x18\x05 \x03(\x0b\x32\x12.jsong.Image.Layer\x1a%\n\x04Size\x12\r\n\x05width\x18\x01 \x01(\x03\x12\x0e\n\x06height\x18\x02 \x01(\x03\x1a@\n\x05\x43olor\x12\x0b\n\x03red\x18\x01 \x01(\x05\x12\r\n\x05green\x18\x02 \x01(\x05\x12\x0c\n\x04\x62lue\x18\x03 \x01(\x05\x12\r\n\x05\x61lpha\x18\x04 \x01(\x05\x1a \n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x03\x12\t\n\x01y\x18\x02 \x01(\x03\x1aS\n\x05Pixel\x12\'\n\x08position\x18\x01 \x01(\x0b\x32\x15.jsong.Image.Position\x12!\n\x05\x63olor\x18\x02 \x01(\x0b\x32\x12.jsong.Image.Color\x1aV\n\x05Layer\x12)\n\rdefault_color\x18\x01 \x01(\x0b\x32\x12.jsong.Image.Color\x12\"\n\x06pixels\x18\x02 \x03(\x0b\x32\x12.jsong.Image.Pixelb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'schemas.image_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _IMAGE._serialized_start=31
  _IMAGE._serialized_end=475
  _IMAGE_SIZE._serialized_start=165
  _IMAGE_SIZE._serialized_end=202
  _IMAGE_COLOR._serialized_start=204
  _IMAGE_COLOR._serialized_end=268
  _IMAGE_POSITION._serialized_start=270
  _IMAGE_POSITION._serialized_end=302
  _IMAGE_PIXEL._serialized_start=304
  _IMAGE_PIXEL._serialized_end=387
  _IMAGE_LAYER._serialized_start=389
  _IMAGE_LAYER._serialized_end=475
# @@protoc_insertion_point(module_scope)