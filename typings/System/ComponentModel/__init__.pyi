import typing
from System import Attribute, Exception
from System.Runtime.InteropServices import ExternalException
from System.Collections import IDictionary
from System.Reflection import MethodBase
from System.Runtime.Serialization import SerializationInfo, StreamingContext

class DefaultValueAttribute(Attribute):
    # Constructor .ctor(value : Int16) was skipped since it collides with above method
    # Constructor .ctor(value : Int32) was skipped since it collides with above method
    # Constructor .ctor(value : Int64) was skipped since it collides with above method
    # Constructor .ctor(value : Single) was skipped since it collides with above method
    # Constructor .ctor(value : Double) was skipped since it collides with above method
    # Constructor .ctor(value : Boolean) was skipped since it collides with above method
    # Constructor .ctor(value : String) was skipped since it collides with above method
    # Constructor .ctor(value : SByte) was skipped since it collides with above method
    # Constructor .ctor(value : UInt16) was skipped since it collides with above method
    # Constructor .ctor(value : UInt32) was skipped since it collides with above method
    # Constructor .ctor(value : UInt64) was skipped since it collides with above method
    @typing.overload
    def __init__(self, type: typing.Type[typing.Any], value: typing.Optional[str]) -> None: ...
    @typing.overload
    def __init__(self, value: str) -> None: ...
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: typing.Optional[typing.Any]) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def Value(self) -> typing.Optional[typing.Any]: ...
    def Equals(self, obj: typing.Optional[typing.Any]) -> bool: ...
    def GetHashCode(self) -> int: ...


class EditorBrowsableAttribute(Attribute):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, state: EditorBrowsableState) -> None: ...
    @property
    def State(self) -> EditorBrowsableState: ...
    @property
    def TypeId(self) -> typing.Any: ...
    def Equals(self, obj: typing.Optional[typing.Any]) -> bool: ...
    def GetHashCode(self) -> int: ...


class EditorBrowsableState(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Always : EditorBrowsableState # 0
    Never : EditorBrowsableState # 1
    Advanced : EditorBrowsableState # 2


class Win32Exception(ExternalException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, error: int) -> None: ...
    @typing.overload
    def __init__(self, error: int, message: typing.Optional[str]) -> None: ...
    @typing.overload
    def __init__(self, message: typing.Optional[str]) -> None: ...
    @typing.overload
    def __init__(self, message: typing.Optional[str], innerException: typing.Optional[Exception]) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def ErrorCode(self) -> int: ...
    @property
    def HelpLink(self) -> typing.Optional[str]: ...
    @HelpLink.setter
    def HelpLink(self, value: typing.Optional[str]) -> typing.Optional[str]: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> typing.Optional[Exception]: ...
    @property
    def Message(self) -> str: ...
    @property
    def NativeErrorCode(self) -> int: ...
    @property
    def Source(self) -> typing.Optional[str]: ...
    @Source.setter
    def Source(self, value: typing.Optional[str]) -> typing.Optional[str]: ...
    @property
    def StackTrace(self) -> typing.Optional[str]: ...
    @property
    def TargetSite(self) -> typing.Optional[MethodBase]: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def ToString(self) -> str: ...

