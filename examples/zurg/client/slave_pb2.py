# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='slave.proto',
  package='zurg',
  serialized_pb='\n\x0bslave.proto\x12\x04zurg\"X\n\x15GetFileContentRequest\x12\x11\n\tfile_name\x18\x01 \x02(\t\x12\x19\n\x08max_size\x18\x02 \x01(\x05:\x07\x31\x30\x34\x38\x35\x37\x36\x12\x11\n\x06offset\x18\x03 \x01(\x03:\x01\x30\"P\n\x16GetFileContentResponse\x12\x12\n\nerror_code\x18\x01 \x02(\x05\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\x12\x11\n\tfile_size\x18\x03 \x01(\x03\"\xda\x01\n\x11RunCommandRequest\x12\x0f\n\x07\x63ommand\x18\x01 \x02(\t\x12\x11\n\x03\x63wd\x18\x02 \x01(\t:\x04/tmp\x12\x0c\n\x04\x61rgs\x18\x03 \x03(\t\x12\x0c\n\x04\x65nvs\x18\x04 \x03(\t\x12\x18\n\tenvs_only\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\nmax_stdout\x18\x06 \x01(\x05:\x07\x31\x30\x34\x38\x35\x37\x36\x12\x1b\n\nmax_stderr\x18\x07 \x01(\x05:\x07\x31\x30\x34\x38\x35\x37\x36\x12\x13\n\x07timeout\x18\x08 \x01(\x05:\x02\x36\x30\x12\x1c\n\rmax_memory_mb\x18\t \x01(\x05:\x05\x33\x32\x37\x36\x38\"\xa3\x02\n\x12RunCommandResponse\x12\x12\n\nerror_code\x18\x01 \x02(\x05\x12\x0b\n\x03pid\x18\x02 \x01(\x05\x12\x0e\n\x06status\x18\x03 \x01(\x05\x12\x12\n\nstd_output\x18\x04 \x01(\x0c\x12\x11\n\tstd_error\x18\x05 \x01(\x0c\x12\x15\n\rstart_time_us\x18\x10 \x01(\x03\x12\x16\n\x0e\x66inish_time_us\x18\x11 \x01(\x03\x12\x11\n\tuser_time\x18\x12 \x01(\x02\x12\x13\n\x0bsystem_time\x18\x13 \x01(\x02\x12\x18\n\x10memory_maxrss_kb\x18\x14 \x01(\x03\x12\x16\n\x0b\x65xit_status\x18\x1e \x01(\x05:\x01\x30\x12\x13\n\x08signaled\x18\x1f \x01(\x05:\x01\x30\x12\x17\n\x08\x63oredump\x18  \x01(\x08:\x05\x66\x61lse\"\xc4\x01\n\x15\x41\x64\x64\x41pplicationRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x12\n\nexecutable\x18\x02 \x02(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x03(\t\x12\x0c\n\x04\x65nvs\x18\x04 \x03(\t\x12\x18\n\tenvs_only\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x1d\n\x0fredirect_stdout\x18\x06 \x01(\x08:\x04true\x12\x1d\n\x0fredirect_stderr\x18\x07 \x01(\x08:\x04true\x12\x15\n\x03\x63wd\x18\x08 \x01(\t:\x08/var/tmp\"\x18\n\x16\x41\x64\x64\x41pplicationResponse\"\'\n\x17StartApplicationRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\"\x1a\n\x18StartApplicationResponse\"&\n\x16StopApplicationRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\"\x19\n\x17StopApplicationResponse\"%\n\x15GetApplicationRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\"\x18\n\x16GetApplicationResponse\"\x19\n\x17ListApplicationsRequest\"w\n\x18ListApplicationsResponse\x12\x46\n\x0c\x61pplications\x18\x02 \x03(\x0b\x32\x30.zurg.ListApplicationsResponse.ApplicationStatus\x1a\x13\n\x11\x41pplicationStatus\")\n\x19RemoveApplicationsRequest\x12\x0c\n\x04name\x18\x01 \x03(\t\"\x1c\n\x1aRemoveApplicationsResponse2\x85\x05\n\x0cSlaveService\x12K\n\x0egetFileContent\x12\x1b.zurg.GetFileContentRequest\x1a\x1c.zurg.GetFileContentResponse\x12?\n\nrunCommand\x12\x17.zurg.RunCommandRequest\x1a\x18.zurg.RunCommandResponse\x12K\n\x0e\x61\x64\x64\x41pplication\x12\x1b.zurg.AddApplicationRequest\x1a\x1c.zurg.AddApplicationResponse\x12Q\n\x10startApplication\x12\x1d.zurg.StartApplicationRequest\x1a\x1e.zurg.StartApplicationResponse\x12N\n\x0fstopApplication\x12\x1c.zurg.StopApplicationRequest\x1a\x1d.zurg.StopApplicationResponse\x12K\n\x0egetApplication\x12\x1b.zurg.GetApplicationRequest\x1a\x1c.zurg.GetApplicationResponse\x12Q\n\x10listApplications\x12\x1d.zurg.ListApplicationsRequest\x1a\x1e.zurg.ListApplicationsResponse\x12W\n\x12removeApplications\x12\x1f.zurg.RemoveApplicationsRequest\x1a .zurg.RemoveApplicationsResponseB4\n\x1d\x63om.chenshuo.muduo.zurg.protoB\nSlaveProto\x80\x01\x01\x88\x01\x01\x90\x01\x01')




_GETFILECONTENTREQUEST = descriptor.Descriptor(
  name='GetFileContentRequest',
  full_name='zurg.GetFileContentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='file_name', full_name='zurg.GetFileContentRequest.file_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_size', full_name='zurg.GetFileContentRequest.max_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1048576,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='offset', full_name='zurg.GetFileContentRequest.offset', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=21,
  serialized_end=109,
)


_GETFILECONTENTRESPONSE = descriptor.Descriptor(
  name='GetFileContentResponse',
  full_name='zurg.GetFileContentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='error_code', full_name='zurg.GetFileContentResponse.error_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='content', full_name='zurg.GetFileContentResponse.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='file_size', full_name='zurg.GetFileContentResponse.file_size', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=111,
  serialized_end=191,
)


_RUNCOMMANDREQUEST = descriptor.Descriptor(
  name='RunCommandRequest',
  full_name='zurg.RunCommandRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='command', full_name='zurg.RunCommandRequest.command', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cwd', full_name='zurg.RunCommandRequest.cwd', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("/tmp", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='args', full_name='zurg.RunCommandRequest.args', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='envs', full_name='zurg.RunCommandRequest.envs', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='envs_only', full_name='zurg.RunCommandRequest.envs_only', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_stdout', full_name='zurg.RunCommandRequest.max_stdout', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1048576,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_stderr', full_name='zurg.RunCommandRequest.max_stderr', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1048576,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timeout', full_name='zurg.RunCommandRequest.timeout', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=60,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_memory_mb', full_name='zurg.RunCommandRequest.max_memory_mb', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=32768,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=194,
  serialized_end=412,
)


_RUNCOMMANDRESPONSE = descriptor.Descriptor(
  name='RunCommandResponse',
  full_name='zurg.RunCommandResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='error_code', full_name='zurg.RunCommandResponse.error_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pid', full_name='zurg.RunCommandResponse.pid', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='status', full_name='zurg.RunCommandResponse.status', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='std_output', full_name='zurg.RunCommandResponse.std_output', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='std_error', full_name='zurg.RunCommandResponse.std_error', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='start_time_us', full_name='zurg.RunCommandResponse.start_time_us', index=5,
      number=16, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='finish_time_us', full_name='zurg.RunCommandResponse.finish_time_us', index=6,
      number=17, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_time', full_name='zurg.RunCommandResponse.user_time', index=7,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='system_time', full_name='zurg.RunCommandResponse.system_time', index=8,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='memory_maxrss_kb', full_name='zurg.RunCommandResponse.memory_maxrss_kb', index=9,
      number=20, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='exit_status', full_name='zurg.RunCommandResponse.exit_status', index=10,
      number=30, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='signaled', full_name='zurg.RunCommandResponse.signaled', index=11,
      number=31, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='coredump', full_name='zurg.RunCommandResponse.coredump', index=12,
      number=32, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=415,
  serialized_end=706,
)


_ADDAPPLICATIONREQUEST = descriptor.Descriptor(
  name='AddApplicationRequest',
  full_name='zurg.AddApplicationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='zurg.AddApplicationRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='executable', full_name='zurg.AddApplicationRequest.executable', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='args', full_name='zurg.AddApplicationRequest.args', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='envs', full_name='zurg.AddApplicationRequest.envs', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='envs_only', full_name='zurg.AddApplicationRequest.envs_only', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='redirect_stdout', full_name='zurg.AddApplicationRequest.redirect_stdout', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='redirect_stderr', full_name='zurg.AddApplicationRequest.redirect_stderr', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cwd', full_name='zurg.AddApplicationRequest.cwd', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("/var/tmp", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=709,
  serialized_end=905,
)


_ADDAPPLICATIONRESPONSE = descriptor.Descriptor(
  name='AddApplicationResponse',
  full_name='zurg.AddApplicationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=907,
  serialized_end=931,
)


_STARTAPPLICATIONREQUEST = descriptor.Descriptor(
  name='StartApplicationRequest',
  full_name='zurg.StartApplicationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='zurg.StartApplicationRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=933,
  serialized_end=972,
)


_STARTAPPLICATIONRESPONSE = descriptor.Descriptor(
  name='StartApplicationResponse',
  full_name='zurg.StartApplicationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=974,
  serialized_end=1000,
)


_STOPAPPLICATIONREQUEST = descriptor.Descriptor(
  name='StopApplicationRequest',
  full_name='zurg.StopApplicationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='zurg.StopApplicationRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1002,
  serialized_end=1040,
)


_STOPAPPLICATIONRESPONSE = descriptor.Descriptor(
  name='StopApplicationResponse',
  full_name='zurg.StopApplicationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1042,
  serialized_end=1067,
)


_GETAPPLICATIONREQUEST = descriptor.Descriptor(
  name='GetApplicationRequest',
  full_name='zurg.GetApplicationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='zurg.GetApplicationRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1069,
  serialized_end=1106,
)


_GETAPPLICATIONRESPONSE = descriptor.Descriptor(
  name='GetApplicationResponse',
  full_name='zurg.GetApplicationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1108,
  serialized_end=1132,
)


_LISTAPPLICATIONSREQUEST = descriptor.Descriptor(
  name='ListApplicationsRequest',
  full_name='zurg.ListApplicationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1134,
  serialized_end=1159,
)


_LISTAPPLICATIONSRESPONSE_APPLICATIONSTATUS = descriptor.Descriptor(
  name='ApplicationStatus',
  full_name='zurg.ListApplicationsResponse.ApplicationStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1261,
  serialized_end=1280,
)

_LISTAPPLICATIONSRESPONSE = descriptor.Descriptor(
  name='ListApplicationsResponse',
  full_name='zurg.ListApplicationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='applications', full_name='zurg.ListApplicationsResponse.applications', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_LISTAPPLICATIONSRESPONSE_APPLICATIONSTATUS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1161,
  serialized_end=1280,
)


_REMOVEAPPLICATIONSREQUEST = descriptor.Descriptor(
  name='RemoveApplicationsRequest',
  full_name='zurg.RemoveApplicationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='zurg.RemoveApplicationsRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1282,
  serialized_end=1323,
)


_REMOVEAPPLICATIONSRESPONSE = descriptor.Descriptor(
  name='RemoveApplicationsResponse',
  full_name='zurg.RemoveApplicationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1325,
  serialized_end=1353,
)

_LISTAPPLICATIONSRESPONSE_APPLICATIONSTATUS.containing_type = _LISTAPPLICATIONSRESPONSE;
_LISTAPPLICATIONSRESPONSE.fields_by_name['applications'].message_type = _LISTAPPLICATIONSRESPONSE_APPLICATIONSTATUS
DESCRIPTOR.message_types_by_name['GetFileContentRequest'] = _GETFILECONTENTREQUEST
DESCRIPTOR.message_types_by_name['GetFileContentResponse'] = _GETFILECONTENTRESPONSE
DESCRIPTOR.message_types_by_name['RunCommandRequest'] = _RUNCOMMANDREQUEST
DESCRIPTOR.message_types_by_name['RunCommandResponse'] = _RUNCOMMANDRESPONSE
DESCRIPTOR.message_types_by_name['AddApplicationRequest'] = _ADDAPPLICATIONREQUEST
DESCRIPTOR.message_types_by_name['AddApplicationResponse'] = _ADDAPPLICATIONRESPONSE
DESCRIPTOR.message_types_by_name['StartApplicationRequest'] = _STARTAPPLICATIONREQUEST
DESCRIPTOR.message_types_by_name['StartApplicationResponse'] = _STARTAPPLICATIONRESPONSE
DESCRIPTOR.message_types_by_name['StopApplicationRequest'] = _STOPAPPLICATIONREQUEST
DESCRIPTOR.message_types_by_name['StopApplicationResponse'] = _STOPAPPLICATIONRESPONSE
DESCRIPTOR.message_types_by_name['GetApplicationRequest'] = _GETAPPLICATIONREQUEST
DESCRIPTOR.message_types_by_name['GetApplicationResponse'] = _GETAPPLICATIONRESPONSE
DESCRIPTOR.message_types_by_name['ListApplicationsRequest'] = _LISTAPPLICATIONSREQUEST
DESCRIPTOR.message_types_by_name['ListApplicationsResponse'] = _LISTAPPLICATIONSRESPONSE
DESCRIPTOR.message_types_by_name['RemoveApplicationsRequest'] = _REMOVEAPPLICATIONSREQUEST
DESCRIPTOR.message_types_by_name['RemoveApplicationsResponse'] = _REMOVEAPPLICATIONSRESPONSE

class GetFileContentRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETFILECONTENTREQUEST
  
  # @@protoc_insertion_point(class_scope:zurg.GetFileContentRequest)

class GetFileContentResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETFILECONTENTRESPONSE
  
  # @@protoc_insertion_point(class_scope:zurg.GetFileContentResponse)

class RunCommandRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNCOMMANDREQUEST
  
  # @@protoc_insertion_point(class_scope:zurg.RunCommandRequest)

class RunCommandResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNCOMMANDRESPONSE
  
  # @@protoc_insertion_point(class_scope:zurg.RunCommandResponse)

class AddApplicationRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ADDAPPLICATIONREQUEST
  
  # @@protoc_insertion_point(class_scope:zurg.AddApplicationRequest)

class AddApplicationResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ADDAPPLICATIONRESPONSE
  
  # @@protoc_insertion_point(class_scope:zurg.AddApplicationResponse)

class StartApplicationRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STARTAPPLICATIONREQUEST
  
  # @@protoc_insertion_point(class_scope:zurg.StartApplicationRequest)

class StartApplicationResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STARTAPPLICATIONRESPONSE
  
  # @@protoc_insertion_point(class_scope:zurg.StartApplicationResponse)

class StopApplicationRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STOPAPPLICATIONREQUEST
  
  # @@protoc_insertion_point(class_scope:zurg.StopApplicationRequest)

class StopApplicationResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STOPAPPLICATIONRESPONSE
  
  # @@protoc_insertion_point(class_scope:zurg.StopApplicationResponse)

class GetApplicationRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETAPPLICATIONREQUEST
  
  # @@protoc_insertion_point(class_scope:zurg.GetApplicationRequest)

class GetApplicationResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETAPPLICATIONRESPONSE
  
  # @@protoc_insertion_point(class_scope:zurg.GetApplicationResponse)

class ListApplicationsRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LISTAPPLICATIONSREQUEST
  
  # @@protoc_insertion_point(class_scope:zurg.ListApplicationsRequest)

class ListApplicationsResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class ApplicationStatus(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _LISTAPPLICATIONSRESPONSE_APPLICATIONSTATUS
    
    # @@protoc_insertion_point(class_scope:zurg.ListApplicationsResponse.ApplicationStatus)
  DESCRIPTOR = _LISTAPPLICATIONSRESPONSE
  
  # @@protoc_insertion_point(class_scope:zurg.ListApplicationsResponse)

class RemoveApplicationsRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REMOVEAPPLICATIONSREQUEST
  
  # @@protoc_insertion_point(class_scope:zurg.RemoveApplicationsRequest)

class RemoveApplicationsResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REMOVEAPPLICATIONSRESPONSE
  
  # @@protoc_insertion_point(class_scope:zurg.RemoveApplicationsResponse)


_SLAVESERVICE = descriptor.ServiceDescriptor(
  name='SlaveService',
  full_name='zurg.SlaveService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1356,
  serialized_end=2001,
  methods=[
  descriptor.MethodDescriptor(
    name='getFileContent',
    full_name='zurg.SlaveService.getFileContent',
    index=0,
    containing_service=None,
    input_type=_GETFILECONTENTREQUEST,
    output_type=_GETFILECONTENTRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='runCommand',
    full_name='zurg.SlaveService.runCommand',
    index=1,
    containing_service=None,
    input_type=_RUNCOMMANDREQUEST,
    output_type=_RUNCOMMANDRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='addApplication',
    full_name='zurg.SlaveService.addApplication',
    index=2,
    containing_service=None,
    input_type=_ADDAPPLICATIONREQUEST,
    output_type=_ADDAPPLICATIONRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='startApplication',
    full_name='zurg.SlaveService.startApplication',
    index=3,
    containing_service=None,
    input_type=_STARTAPPLICATIONREQUEST,
    output_type=_STARTAPPLICATIONRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='stopApplication',
    full_name='zurg.SlaveService.stopApplication',
    index=4,
    containing_service=None,
    input_type=_STOPAPPLICATIONREQUEST,
    output_type=_STOPAPPLICATIONRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='getApplication',
    full_name='zurg.SlaveService.getApplication',
    index=5,
    containing_service=None,
    input_type=_GETAPPLICATIONREQUEST,
    output_type=_GETAPPLICATIONRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='listApplications',
    full_name='zurg.SlaveService.listApplications',
    index=6,
    containing_service=None,
    input_type=_LISTAPPLICATIONSREQUEST,
    output_type=_LISTAPPLICATIONSRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='removeApplications',
    full_name='zurg.SlaveService.removeApplications',
    index=7,
    containing_service=None,
    input_type=_REMOVEAPPLICATIONSREQUEST,
    output_type=_REMOVEAPPLICATIONSRESPONSE,
    options=None,
  ),
])

class SlaveService(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _SLAVESERVICE
class SlaveService_Stub(SlaveService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _SLAVESERVICE

# @@protoc_insertion_point(module_scope)
