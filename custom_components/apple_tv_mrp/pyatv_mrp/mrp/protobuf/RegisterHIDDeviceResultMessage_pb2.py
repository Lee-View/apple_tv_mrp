# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/RegisterHIDDeviceResultMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import ProtocolMessage_pb2 as pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/RegisterHIDDeviceResultMessage.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n7pyatv/mrp/protobuf/RegisterHIDDeviceResultMessage.proto\x1a(pyatv/mrp/protobuf/ProtocolMessage.proto\"M\n\x1eRegisterHIDDeviceResultMessage\x12\x11\n\terrorCode\x18\x01 \x01(\x05\x12\x18\n\x10\x64\x65viceIdentifier\x18\x02 \x01(\x05:Y\n\x1eregisterHIDDeviceResultMessage\x12\x10.ProtocolMessage\x18\x0c \x01(\x0b\x32\x1f.RegisterHIDDeviceResultMessage')
  ,
  dependencies=[pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,])


REGISTERHIDDEVICERESULTMESSAGE_FIELD_NUMBER = 12
registerHIDDeviceResultMessage = _descriptor.FieldDescriptor(
  name='registerHIDDeviceResultMessage', full_name='registerHIDDeviceResultMessage', index=0,
  number=12, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)


_REGISTERHIDDEVICERESULTMESSAGE = _descriptor.Descriptor(
  name='RegisterHIDDeviceResultMessage',
  full_name='RegisterHIDDeviceResultMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='errorCode', full_name='RegisterHIDDeviceResultMessage.errorCode', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceIdentifier', full_name='RegisterHIDDeviceResultMessage.deviceIdentifier', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=178,
)

DESCRIPTOR.message_types_by_name['RegisterHIDDeviceResultMessage'] = _REGISTERHIDDEVICERESULTMESSAGE
DESCRIPTOR.extensions_by_name['registerHIDDeviceResultMessage'] = registerHIDDeviceResultMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterHIDDeviceResultMessage = _reflection.GeneratedProtocolMessageType('RegisterHIDDeviceResultMessage', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERHIDDEVICERESULTMESSAGE,
  __module__ = 'pyatv.mrp.protobuf.RegisterHIDDeviceResultMessage_pb2'
  # @@protoc_insertion_point(class_scope:RegisterHIDDeviceResultMessage)
  ))
_sym_db.RegisterMessage(RegisterHIDDeviceResultMessage)

registerHIDDeviceResultMessage.message_type = _REGISTERHIDDEVICERESULTMESSAGE
pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(registerHIDDeviceResultMessage)

# @@protoc_insertion_point(module_scope)
