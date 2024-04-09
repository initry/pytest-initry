from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

import responses_pb2 as _responses_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class Test(_message.Message):
    __slots__ = ("nodeid", "location", "uuid", "test_run_uuid", "description")
    NODEID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    TEST_RUN_UUID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    nodeid: str
    location: str
    uuid: str
    test_run_uuid: str
    description: str
    def __init__(
        self,
        nodeid: _Optional[str] = ...,
        location: _Optional[str] = ...,
        uuid: _Optional[str] = ...,
        test_run_uuid: _Optional[str] = ...,
        description: _Optional[str] = ...,
    ) -> None: ...

class CreateTestsRequest(_message.Message):
    __slots__ = ("tests",)
    TESTS_FIELD_NUMBER: _ClassVar[int]
    tests: _containers.RepeatedCompositeFieldContainer[Test]
    def __init__(
        self, tests: _Optional[_Iterable[_Union[Test, _Mapping]]] = ...
    ) -> None: ...
