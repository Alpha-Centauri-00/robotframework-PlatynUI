# This file was generated by PythonNetStubGenerator
# mypy: ignore-errors
import typing, clr, abc
from System.Runtime.InteropServices import GCHandle
from System import Span_1, Exception, MulticastDelegate, IAsyncResult, RuntimeMethodHandle, AsyncCallback, Attribute
from  import 
from System.Reflection import MethodInfo

class ObjectiveCMarshal(abc.ABC):
    @staticmethod
    def CreateReferenceTrackingHandle(obj: typing.Any, taggedMemory: clr.Reference[Span_1[int]]) -> GCHandle: ...
    @staticmethod
    def Initialize(beginEndCallback: , isReferencedCallback: , trackedObjectEnteredFinalization: , unhandledExceptionPropagationHandler: ObjectiveCMarshal.UnhandledExceptionPropagationHandler) -> None: ...
    @staticmethod
    def SetMessageSendCallback(msgSendFunction: ObjectiveCMarshal.MessageSendFunction, func: int) -> None: ...
    @staticmethod
    def SetMessageSendPendingException(exception: typing.Optional[Exception]) -> None: ...

    class MessageSendFunction(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        MsgSend : ObjectiveCMarshal.MessageSendFunction # 0
        MsgSendFpret : ObjectiveCMarshal.MessageSendFunction # 1
        MsgSendStret : ObjectiveCMarshal.MessageSendFunction # 2
        MsgSendSuper : ObjectiveCMarshal.MessageSendFunction # 3
        MsgSendSuperStret : ObjectiveCMarshal.MessageSendFunction # 4


    class UnhandledExceptionPropagationHandler(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Optional[typing.Any]: ...
        def BeginInvoke(self, exception: Exception, lastMethod: RuntimeMethodHandle, context: clr.Reference[int], callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, context: clr.Reference[int], result: IAsyncResult) -> : ...
        def Invoke(self, exception: Exception, lastMethod: RuntimeMethodHandle, context: clr.Reference[int]) -> : ...



class ObjectiveCTrackedTypeAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...

