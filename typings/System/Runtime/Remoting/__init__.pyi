import typing
from System import MarshalByRefObject

class ObjectHandle(MarshalByRefObject):
    def __init__(self, o: typing.Optional[typing.Any]) -> None: ...
    def Unwrap(self) -> typing.Optional[typing.Any]: ...

