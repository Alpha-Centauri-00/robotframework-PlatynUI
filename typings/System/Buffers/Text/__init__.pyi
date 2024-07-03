import typing, clr, abc
from System.Buffers import OperationStatus, StandardFormat
from System import ReadOnlySpan_1, Span_1, Decimal, DateTimeOffset, DateTime, Guid, TimeSpan

class Base64(abc.ABC):
    @staticmethod
    def DecodeFromUtf8(utf8: ReadOnlySpan_1[int], bytes: Span_1[int], bytesConsumed: clr.Reference[int], bytesWritten: clr.Reference[int], isFinalBlock: bool = ...) -> OperationStatus: ...
    @staticmethod
    def DecodeFromUtf8InPlace(buffer: Span_1[int], bytesWritten: clr.Reference[int]) -> OperationStatus: ...
    @staticmethod
    def EncodeToUtf8(bytes: ReadOnlySpan_1[int], utf8: Span_1[int], bytesConsumed: clr.Reference[int], bytesWritten: clr.Reference[int], isFinalBlock: bool = ...) -> OperationStatus: ...
    @staticmethod
    def EncodeToUtf8InPlace(buffer: Span_1[int], dataLength: int, bytesWritten: clr.Reference[int]) -> OperationStatus: ...
    @staticmethod
    def GetMaxDecodedFromUtf8Length(length: int) -> int: ...
    @staticmethod
    def GetMaxEncodedToUtf8Length(length: int) -> int: ...
    # Skipped IsValid due to it being static, abstract and generic.

    IsValid : IsValid_MethodGroup
    class IsValid_MethodGroup:
        @typing.overload
        def __call__(self, base64Text: ReadOnlySpan_1[str]) -> bool:...
        @typing.overload
        def __call__(self, base64TextUtf8: ReadOnlySpan_1[int]) -> bool:...
        @typing.overload
        def __call__(self, base64TextUtf8: ReadOnlySpan_1[int], decodedLength: clr.Reference[int]) -> bool:...
        @typing.overload
        def __call__(self, base64Text: ReadOnlySpan_1[str], decodedLength: clr.Reference[int]) -> bool:...



class Utf8Formatter(abc.ABC):
    # Skipped TryFormat due to it being static, abstract and generic.

    TryFormat : TryFormat_MethodGroup
    class TryFormat_MethodGroup:
        @typing.overload
        def __call__(self, value: float, destination: Span_1[int], bytesWritten: clr.Reference[int], format: StandardFormat = ...) -> bool:...
        # Method TryFormat(value : Single, destination : Span`1, bytesWritten : Int32&, format : StandardFormat) was skipped since it collides with above method
        # Method TryFormat(value : Byte, destination : Span`1, bytesWritten : Int32&, format : StandardFormat) was skipped since it collides with above method
        # Method TryFormat(value : SByte, destination : Span`1, bytesWritten : Int32&, format : StandardFormat) was skipped since it collides with above method
        # Method TryFormat(value : UInt16, destination : Span`1, bytesWritten : Int32&, format : StandardFormat) was skipped since it collides with above method
        # Method TryFormat(value : Int16, destination : Span`1, bytesWritten : Int32&, format : StandardFormat) was skipped since it collides with above method
        # Method TryFormat(value : UInt32, destination : Span`1, bytesWritten : Int32&, format : StandardFormat) was skipped since it collides with above method
        # Method TryFormat(value : Int32, destination : Span`1, bytesWritten : Int32&, format : StandardFormat) was skipped since it collides with above method
        # Method TryFormat(value : UInt64, destination : Span`1, bytesWritten : Int32&, format : StandardFormat) was skipped since it collides with above method
        # Method TryFormat(value : Int64, destination : Span`1, bytesWritten : Int32&, format : StandardFormat) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Decimal, destination: Span_1[int], bytesWritten: clr.Reference[int], format: StandardFormat = ...) -> bool:...
        # Method TryFormat(value : Boolean, destination : Span`1, bytesWritten : Int32&, format : StandardFormat) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: DateTimeOffset, destination: Span_1[int], bytesWritten: clr.Reference[int], format: StandardFormat = ...) -> bool:...
        @typing.overload
        def __call__(self, value: DateTime, destination: Span_1[int], bytesWritten: clr.Reference[int], format: StandardFormat = ...) -> bool:...
        @typing.overload
        def __call__(self, value: Guid, destination: Span_1[int], bytesWritten: clr.Reference[int], format: StandardFormat = ...) -> bool:...
        @typing.overload
        def __call__(self, value: TimeSpan, destination: Span_1[int], bytesWritten: clr.Reference[int], format: StandardFormat = ...) -> bool:...



class Utf8Parser(abc.ABC):
    # Skipped TryParse due to it being static, abstract and generic.

    TryParse : TryParse_MethodGroup
    class TryParse_MethodGroup:
        @typing.overload
        def __call__(self, source: ReadOnlySpan_1[int], value: clr.Reference[float], bytesConsumed: clr.Reference[int], standardFormat: str = ...) -> bool:...
        # Method TryParse(source : ReadOnlySpan`1, value : Double&, bytesConsumed : Int32&, standardFormat : Char) was skipped since it collides with above method
        # Method TryParse(source : ReadOnlySpan`1, value : SByte&, bytesConsumed : Int32&, standardFormat : Char) was skipped since it collides with above method
        # Method TryParse(source : ReadOnlySpan`1, value : Int16&, bytesConsumed : Int32&, standardFormat : Char) was skipped since it collides with above method
        # Method TryParse(source : ReadOnlySpan`1, value : Int32&, bytesConsumed : Int32&, standardFormat : Char) was skipped since it collides with above method
        # Method TryParse(source : ReadOnlySpan`1, value : Int64&, bytesConsumed : Int32&, standardFormat : Char) was skipped since it collides with above method
        # Method TryParse(source : ReadOnlySpan`1, value : Byte&, bytesConsumed : Int32&, standardFormat : Char) was skipped since it collides with above method
        # Method TryParse(source : ReadOnlySpan`1, value : UInt16&, bytesConsumed : Int32&, standardFormat : Char) was skipped since it collides with above method
        # Method TryParse(source : ReadOnlySpan`1, value : UInt32&, bytesConsumed : Int32&, standardFormat : Char) was skipped since it collides with above method
        # Method TryParse(source : ReadOnlySpan`1, value : UInt64&, bytesConsumed : Int32&, standardFormat : Char) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: ReadOnlySpan_1[int], value: clr.Reference[Decimal], bytesConsumed: clr.Reference[int], standardFormat: str = ...) -> bool:...
        # Method TryParse(source : ReadOnlySpan`1, value : Boolean&, bytesConsumed : Int32&, standardFormat : Char) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: ReadOnlySpan_1[int], value: clr.Reference[DateTime], bytesConsumed: clr.Reference[int], standardFormat: str = ...) -> bool:...
        @typing.overload
        def __call__(self, source: ReadOnlySpan_1[int], value: clr.Reference[DateTimeOffset], bytesConsumed: clr.Reference[int], standardFormat: str = ...) -> bool:...
        @typing.overload
        def __call__(self, source: ReadOnlySpan_1[int], value: clr.Reference[Guid], bytesConsumed: clr.Reference[int], standardFormat: str = ...) -> bool:...
        @typing.overload
        def __call__(self, source: ReadOnlySpan_1[int], value: clr.Reference[TimeSpan], bytesConsumed: clr.Reference[int], standardFormat: str = ...) -> bool:...


