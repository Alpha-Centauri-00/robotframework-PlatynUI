import typing, clr, abc
from System import UIntPtr, ValueTuple_2, ReadOnlySpan_1, Span_1, Array_1, IComparable_1, IComparable, ISpanParsable_1, ISpanFormattable, IUtf8SpanParsable_1, IUtf8SpanFormattable, IEquatable_1, IFormattable, IFormatProvider
from System.Collections.Generic import IEqualityComparer_1, IComparer_1

class BitOperations(abc.ABC):
    # Skipped Crc32C due to it being static, abstract and generic.

    Crc32C : Crc32C_MethodGroup
    class Crc32C_MethodGroup:
        def __call__(self, crc: int, data: int) -> int:...
        # Method Crc32C(crc : UInt32, data : UInt16) was skipped since it collides with above method
        # Method Crc32C(crc : UInt32, data : UInt32) was skipped since it collides with above method
        # Method Crc32C(crc : UInt32, data : UInt64) was skipped since it collides with above method

    # Skipped IsPow2 due to it being static, abstract and generic.

    IsPow2 : IsPow2_MethodGroup
    class IsPow2_MethodGroup:
        @typing.overload
        def __call__(self, value: int) -> bool:...
        # Method IsPow2(value : UInt32) was skipped since it collides with above method
        # Method IsPow2(value : Int64) was skipped since it collides with above method
        # Method IsPow2(value : UInt64) was skipped since it collides with above method
        # Method IsPow2(value : IntPtr) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> bool:...

    # Skipped LeadingZeroCount due to it being static, abstract and generic.

    LeadingZeroCount : LeadingZeroCount_MethodGroup
    class LeadingZeroCount_MethodGroup:
        @typing.overload
        def __call__(self, value: int) -> int:...
        # Method LeadingZeroCount(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> int:...

    # Skipped Log2 due to it being static, abstract and generic.

    Log2 : Log2_MethodGroup
    class Log2_MethodGroup:
        @typing.overload
        def __call__(self, value: int) -> int:...
        # Method Log2(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> int:...

    # Skipped PopCount due to it being static, abstract and generic.

    PopCount : PopCount_MethodGroup
    class PopCount_MethodGroup:
        @typing.overload
        def __call__(self, value: int) -> int:...
        # Method PopCount(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> int:...

    # Skipped RotateLeft due to it being static, abstract and generic.

    RotateLeft : RotateLeft_MethodGroup
    class RotateLeft_MethodGroup:
        @typing.overload
        def __call__(self, value: int, offset: int) -> int:...
        # Method RotateLeft(value : UInt64, offset : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr, offset: int) -> UIntPtr:...

    # Skipped RotateRight due to it being static, abstract and generic.

    RotateRight : RotateRight_MethodGroup
    class RotateRight_MethodGroup:
        @typing.overload
        def __call__(self, value: int, offset: int) -> int:...
        # Method RotateRight(value : UInt64, offset : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr, offset: int) -> UIntPtr:...

    # Skipped RoundUpToPowerOf2 due to it being static, abstract and generic.

    RoundUpToPowerOf2 : RoundUpToPowerOf2_MethodGroup
    class RoundUpToPowerOf2_MethodGroup:
        @typing.overload
        def __call__(self, value: int) -> int:...
        # Method RoundUpToPowerOf2(value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> UIntPtr:...

    # Skipped TrailingZeroCount due to it being static, abstract and generic.

    TrailingZeroCount : TrailingZeroCount_MethodGroup
    class TrailingZeroCount_MethodGroup:
        @typing.overload
        def __call__(self, value: int) -> int:...
        # Method TrailingZeroCount(value : UInt32) was skipped since it collides with above method
        # Method TrailingZeroCount(value : Int64) was skipped since it collides with above method
        # Method TrailingZeroCount(value : UInt64) was skipped since it collides with above method
        # Method TrailingZeroCount(value : IntPtr) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> int:...



class IAdditionOperators_GenericClasses(abc.ABCMeta):
    Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TSelf = typing.TypeVar('Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TSelf')
    Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TOther = typing.TypeVar('Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TOther')
    Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TResult = typing.TypeVar('Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TSelf], typing.Type[Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TOther], typing.Type[Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TResult]]) -> typing.Type[IAdditionOperators_3[Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TSelf, Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TOther, Generic_IAdditionOperators_GenericClasses_IAdditionOperators_3_TResult]]: ...

IAdditionOperators : IAdditionOperators_GenericClasses

IAdditionOperators_3_TSelf = typing.TypeVar('IAdditionOperators_3_TSelf')
IAdditionOperators_3_TOther = typing.TypeVar('IAdditionOperators_3_TOther')
IAdditionOperators_3_TResult = typing.TypeVar('IAdditionOperators_3_TResult')
class IAdditionOperators_3(typing.Generic[IAdditionOperators_3_TSelf, IAdditionOperators_3_TOther, IAdditionOperators_3_TResult], typing.Protocol):
    @abc.abstractmethod
    def __add__(self, left: IAdditionOperators_3_TSelf, right: typing.Optional[IAdditionOperators_3_TOther]) -> typing.Optional[IAdditionOperators_3_TResult]: ...
    # Operator not supported op_CheckedAddition(left: TSelf, right: TOther)


class IAdditiveIdentity_GenericClasses(abc.ABCMeta):
    Generic_IAdditiveIdentity_GenericClasses_IAdditiveIdentity_2_TSelf = typing.TypeVar('Generic_IAdditiveIdentity_GenericClasses_IAdditiveIdentity_2_TSelf')
    Generic_IAdditiveIdentity_GenericClasses_IAdditiveIdentity_2_TResult = typing.TypeVar('Generic_IAdditiveIdentity_GenericClasses_IAdditiveIdentity_2_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IAdditiveIdentity_GenericClasses_IAdditiveIdentity_2_TSelf], typing.Type[Generic_IAdditiveIdentity_GenericClasses_IAdditiveIdentity_2_TResult]]) -> typing.Type[IAdditiveIdentity_2[Generic_IAdditiveIdentity_GenericClasses_IAdditiveIdentity_2_TSelf, Generic_IAdditiveIdentity_GenericClasses_IAdditiveIdentity_2_TResult]]: ...

IAdditiveIdentity : IAdditiveIdentity_GenericClasses

IAdditiveIdentity_2_TSelf = typing.TypeVar('IAdditiveIdentity_2_TSelf')
IAdditiveIdentity_2_TResult = typing.TypeVar('IAdditiveIdentity_2_TResult')
class IAdditiveIdentity_2(typing.Generic[IAdditiveIdentity_2_TSelf, IAdditiveIdentity_2_TResult], typing.Protocol):
    @classmethod
    @property
    def AdditiveIdentity(cls) -> typing.Optional[IAdditiveIdentity_2_TResult]: ...


class IBinaryFloatingPointIeee754_GenericClasses(abc.ABCMeta):
    Generic_IBinaryFloatingPointIeee754_GenericClasses_IBinaryFloatingPointIeee754_1_TSelf = typing.TypeVar('Generic_IBinaryFloatingPointIeee754_GenericClasses_IBinaryFloatingPointIeee754_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IBinaryFloatingPointIeee754_GenericClasses_IBinaryFloatingPointIeee754_1_TSelf]) -> typing.Type[IBinaryFloatingPointIeee754_1[Generic_IBinaryFloatingPointIeee754_GenericClasses_IBinaryFloatingPointIeee754_1_TSelf]]: ...

IBinaryFloatingPointIeee754 : IBinaryFloatingPointIeee754_GenericClasses

IBinaryFloatingPointIeee754_1_TSelf = typing.TypeVar('IBinaryFloatingPointIeee754_1_TSelf')
class IBinaryFloatingPointIeee754_1(typing.Generic[IBinaryFloatingPointIeee754_1_TSelf], IFloatingPointIeee754_1[IBinaryFloatingPointIeee754_1_TSelf], IBinaryNumber_1[IBinaryFloatingPointIeee754_1_TSelf], typing.Protocol):
    pass


class IBinaryInteger_GenericClasses(abc.ABCMeta):
    Generic_IBinaryInteger_GenericClasses_IBinaryInteger_1_TSelf = typing.TypeVar('Generic_IBinaryInteger_GenericClasses_IBinaryInteger_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IBinaryInteger_GenericClasses_IBinaryInteger_1_TSelf]) -> typing.Type[IBinaryInteger_1[Generic_IBinaryInteger_GenericClasses_IBinaryInteger_1_TSelf]]: ...

IBinaryInteger : IBinaryInteger_GenericClasses

IBinaryInteger_1_TSelf = typing.TypeVar('IBinaryInteger_1_TSelf')
class IBinaryInteger_1(typing.Generic[IBinaryInteger_1_TSelf], IBinaryNumber_1[IBinaryInteger_1_TSelf], IShiftOperators_3[IBinaryInteger_1_TSelf, int, IBinaryInteger_1_TSelf], typing.Protocol):
    @staticmethod
    def DivRem(left: IBinaryInteger_1_TSelf, right: IBinaryInteger_1_TSelf) -> ValueTuple_2[IBinaryInteger_1_TSelf, IBinaryInteger_1_TSelf]: ...
    @abc.abstractmethod
    def GetByteCount(self) -> int: ...
    @abc.abstractmethod
    def GetShortestBitLength(self) -> int: ...
    @staticmethod
    def LeadingZeroCount(value: IBinaryInteger_1_TSelf) -> IBinaryInteger_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def PopCount(value: IBinaryInteger_1_TSelf) -> IBinaryInteger_1_TSelf: ...
    @staticmethod
    def RotateLeft(value: IBinaryInteger_1_TSelf, rotateAmount: int) -> IBinaryInteger_1_TSelf: ...
    @staticmethod
    def RotateRight(value: IBinaryInteger_1_TSelf, rotateAmount: int) -> IBinaryInteger_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def TrailingZeroCount(value: IBinaryInteger_1_TSelf) -> IBinaryInteger_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def TryReadBigEndian(source: ReadOnlySpan_1[int], isUnsigned: bool, value: clr.Reference[IBinaryInteger_1_TSelf]) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def TryReadLittleEndian(source: ReadOnlySpan_1[int], isUnsigned: bool, value: clr.Reference[IBinaryInteger_1_TSelf]) -> bool: ...
    @abc.abstractmethod
    def TryWriteBigEndian(self, destination: Span_1[int], bytesWritten: clr.Reference[int]) -> bool: ...
    @abc.abstractmethod
    def TryWriteLittleEndian(self, destination: Span_1[int], bytesWritten: clr.Reference[int]) -> bool: ...
    # Skipped ReadBigEndian due to it being static, abstract and generic.

    ReadBigEndian : ReadBigEndian_MethodGroup[IBinaryInteger_1_TSelf]
    ReadBigEndian_MethodGroup_IBinaryInteger_1_TSelf = typing.TypeVar('ReadBigEndian_MethodGroup_IBinaryInteger_1_TSelf')
    class ReadBigEndian_MethodGroup(typing.Generic[ReadBigEndian_MethodGroup_IBinaryInteger_1_TSelf]):
        ReadBigEndian_MethodGroup_IBinaryInteger_1_TSelf = IBinaryInteger_1.ReadBigEndian_MethodGroup_IBinaryInteger_1_TSelf
        @typing.overload
        def __call__(self, source: Array_1[int], isUnsigned: bool) -> ReadBigEndian_MethodGroup_IBinaryInteger_1_TSelf:...
        @typing.overload
        def __call__(self, source: ReadOnlySpan_1[int], isUnsigned: bool) -> ReadBigEndian_MethodGroup_IBinaryInteger_1_TSelf:...
        @typing.overload
        def __call__(self, source: Array_1[int], startIndex: int, isUnsigned: bool) -> ReadBigEndian_MethodGroup_IBinaryInteger_1_TSelf:...

    # Skipped ReadLittleEndian due to it being static, abstract and generic.

    ReadLittleEndian : ReadLittleEndian_MethodGroup[IBinaryInteger_1_TSelf]
    ReadLittleEndian_MethodGroup_IBinaryInteger_1_TSelf = typing.TypeVar('ReadLittleEndian_MethodGroup_IBinaryInteger_1_TSelf')
    class ReadLittleEndian_MethodGroup(typing.Generic[ReadLittleEndian_MethodGroup_IBinaryInteger_1_TSelf]):
        ReadLittleEndian_MethodGroup_IBinaryInteger_1_TSelf = IBinaryInteger_1.ReadLittleEndian_MethodGroup_IBinaryInteger_1_TSelf
        @typing.overload
        def __call__(self, source: Array_1[int], isUnsigned: bool) -> ReadLittleEndian_MethodGroup_IBinaryInteger_1_TSelf:...
        @typing.overload
        def __call__(self, source: ReadOnlySpan_1[int], isUnsigned: bool) -> ReadLittleEndian_MethodGroup_IBinaryInteger_1_TSelf:...
        @typing.overload
        def __call__(self, source: Array_1[int], startIndex: int, isUnsigned: bool) -> ReadLittleEndian_MethodGroup_IBinaryInteger_1_TSelf:...

    # Skipped WriteBigEndian due to it being static, abstract and generic.

    WriteBigEndian : WriteBigEndian_MethodGroup[IBinaryInteger_1_TSelf]
    WriteBigEndian_MethodGroup_IBinaryInteger_1_TSelf = typing.TypeVar('WriteBigEndian_MethodGroup_IBinaryInteger_1_TSelf')
    class WriteBigEndian_MethodGroup(typing.Generic[WriteBigEndian_MethodGroup_IBinaryInteger_1_TSelf]):
        WriteBigEndian_MethodGroup_IBinaryInteger_1_TSelf = IBinaryInteger_1.WriteBigEndian_MethodGroup_IBinaryInteger_1_TSelf
        @typing.overload
        def __call__(self, destination: Array_1[int]) -> int:...
        @typing.overload
        def __call__(self, destination: Span_1[int]) -> int:...
        @typing.overload
        def __call__(self, destination: Array_1[int], startIndex: int) -> int:...

    # Skipped WriteLittleEndian due to it being static, abstract and generic.

    WriteLittleEndian : WriteLittleEndian_MethodGroup[IBinaryInteger_1_TSelf]
    WriteLittleEndian_MethodGroup_IBinaryInteger_1_TSelf = typing.TypeVar('WriteLittleEndian_MethodGroup_IBinaryInteger_1_TSelf')
    class WriteLittleEndian_MethodGroup(typing.Generic[WriteLittleEndian_MethodGroup_IBinaryInteger_1_TSelf]):
        WriteLittleEndian_MethodGroup_IBinaryInteger_1_TSelf = IBinaryInteger_1.WriteLittleEndian_MethodGroup_IBinaryInteger_1_TSelf
        @typing.overload
        def __call__(self, destination: Array_1[int]) -> int:...
        @typing.overload
        def __call__(self, destination: Span_1[int]) -> int:...
        @typing.overload
        def __call__(self, destination: Array_1[int], startIndex: int) -> int:...



class IBinaryNumber_GenericClasses(abc.ABCMeta):
    Generic_IBinaryNumber_GenericClasses_IBinaryNumber_1_TSelf = typing.TypeVar('Generic_IBinaryNumber_GenericClasses_IBinaryNumber_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IBinaryNumber_GenericClasses_IBinaryNumber_1_TSelf]) -> typing.Type[IBinaryNumber_1[Generic_IBinaryNumber_GenericClasses_IBinaryNumber_1_TSelf]]: ...

IBinaryNumber : IBinaryNumber_GenericClasses

IBinaryNumber_1_TSelf = typing.TypeVar('IBinaryNumber_1_TSelf')
class IBinaryNumber_1(typing.Generic[IBinaryNumber_1_TSelf], INumber_1[IBinaryNumber_1_TSelf], IBitwiseOperators_3[IBinaryNumber_1_TSelf, IBinaryNumber_1_TSelf, IBinaryNumber_1_TSelf], typing.Protocol):
    @classmethod
    @property
    def AllBitsSet(cls) -> IBinaryNumber_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def IsPow2(value: IBinaryNumber_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def Log2(value: IBinaryNumber_1_TSelf) -> IBinaryNumber_1_TSelf: ...


class IBitwiseOperators_GenericClasses(abc.ABCMeta):
    Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TSelf = typing.TypeVar('Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TSelf')
    Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TOther = typing.TypeVar('Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TOther')
    Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TResult = typing.TypeVar('Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TSelf], typing.Type[Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TOther], typing.Type[Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TResult]]) -> typing.Type[IBitwiseOperators_3[Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TSelf, Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TOther, Generic_IBitwiseOperators_GenericClasses_IBitwiseOperators_3_TResult]]: ...

IBitwiseOperators : IBitwiseOperators_GenericClasses

IBitwiseOperators_3_TSelf = typing.TypeVar('IBitwiseOperators_3_TSelf')
IBitwiseOperators_3_TOther = typing.TypeVar('IBitwiseOperators_3_TOther')
IBitwiseOperators_3_TResult = typing.TypeVar('IBitwiseOperators_3_TResult')
class IBitwiseOperators_3(typing.Generic[IBitwiseOperators_3_TSelf, IBitwiseOperators_3_TOther, IBitwiseOperators_3_TResult], typing.Protocol):
    @abc.abstractmethod
    def __and__(self, left: IBitwiseOperators_3_TSelf, right: typing.Optional[IBitwiseOperators_3_TOther]) -> typing.Optional[IBitwiseOperators_3_TResult]: ...
    @abc.abstractmethod
    def __or__(self, left: IBitwiseOperators_3_TSelf, right: typing.Optional[IBitwiseOperators_3_TOther]) -> typing.Optional[IBitwiseOperators_3_TResult]: ...
    @abc.abstractmethod
    def __xor__(self, left: IBitwiseOperators_3_TSelf, right: typing.Optional[IBitwiseOperators_3_TOther]) -> typing.Optional[IBitwiseOperators_3_TResult]: ...
    @abc.abstractmethod
    def __invert__(self, value: IBitwiseOperators_3_TSelf) -> typing.Optional[IBitwiseOperators_3_TResult]: ...


class IComparisonOperators_GenericClasses(abc.ABCMeta):
    Generic_IComparisonOperators_GenericClasses_IComparisonOperators_3_TSelf = typing.TypeVar('Generic_IComparisonOperators_GenericClasses_IComparisonOperators_3_TSelf')
    Generic_IComparisonOperators_GenericClasses_IComparisonOperators_3_TOther = typing.TypeVar('Generic_IComparisonOperators_GenericClasses_IComparisonOperators_3_TOther')
    Generic_IComparisonOperators_GenericClasses_IComparisonOperators_3_TResult = typing.TypeVar('Generic_IComparisonOperators_GenericClasses_IComparisonOperators_3_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IComparisonOperators_GenericClasses_IComparisonOperators_3_TSelf], typing.Type[Generic_IComparisonOperators_GenericClasses_IComparisonOperators_3_TOther], typing.Type[Generic_IComparisonOperators_GenericClasses_IComparisonOperators_3_TResult]]) -> typing.Type[IComparisonOperators_3[Generic_IComparisonOperators_GenericClasses_IComparisonOperators_3_TSelf, Generic_IComparisonOperators_GenericClasses_IComparisonOperators_3_TOther, Generic_IComparisonOperators_GenericClasses_IComparisonOperators_3_TResult]]: ...

IComparisonOperators : IComparisonOperators_GenericClasses

IComparisonOperators_3_TSelf = typing.TypeVar('IComparisonOperators_3_TSelf')
IComparisonOperators_3_TOther = typing.TypeVar('IComparisonOperators_3_TOther')
IComparisonOperators_3_TResult = typing.TypeVar('IComparisonOperators_3_TResult')
class IComparisonOperators_3(typing.Generic[IComparisonOperators_3_TSelf, IComparisonOperators_3_TOther, IComparisonOperators_3_TResult], IEqualityOperators_3[IComparisonOperators_3_TSelf, IComparisonOperators_3_TOther, IComparisonOperators_3_TResult], typing.Protocol):
    @abc.abstractmethod
    def __gt__(self, left: IComparisonOperators_3_TSelf, right: typing.Optional[IComparisonOperators_3_TOther]) -> typing.Optional[IComparisonOperators_3_TResult]: ...
    @abc.abstractmethod
    def __ge__(self, left: IComparisonOperators_3_TSelf, right: typing.Optional[IComparisonOperators_3_TOther]) -> typing.Optional[IComparisonOperators_3_TResult]: ...
    @abc.abstractmethod
    def __lt__(self, left: IComparisonOperators_3_TSelf, right: typing.Optional[IComparisonOperators_3_TOther]) -> typing.Optional[IComparisonOperators_3_TResult]: ...
    @abc.abstractmethod
    def __le__(self, left: IComparisonOperators_3_TSelf, right: typing.Optional[IComparisonOperators_3_TOther]) -> typing.Optional[IComparisonOperators_3_TResult]: ...


class IDecrementOperators_GenericClasses(abc.ABCMeta):
    Generic_IDecrementOperators_GenericClasses_IDecrementOperators_1_TSelf = typing.TypeVar('Generic_IDecrementOperators_GenericClasses_IDecrementOperators_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IDecrementOperators_GenericClasses_IDecrementOperators_1_TSelf]) -> typing.Type[IDecrementOperators_1[Generic_IDecrementOperators_GenericClasses_IDecrementOperators_1_TSelf]]: ...

IDecrementOperators : IDecrementOperators_GenericClasses

IDecrementOperators_1_TSelf = typing.TypeVar('IDecrementOperators_1_TSelf')
class IDecrementOperators_1(typing.Generic[IDecrementOperators_1_TSelf], typing.Protocol):
    # Operator not supported op_CheckedDecrement(value: TSelf)
    # Operator not supported op_Decrement(value: TSelf)
    pass


class IDivisionOperators_GenericClasses(abc.ABCMeta):
    Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TSelf = typing.TypeVar('Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TSelf')
    Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TOther = typing.TypeVar('Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TOther')
    Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TResult = typing.TypeVar('Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TSelf], typing.Type[Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TOther], typing.Type[Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TResult]]) -> typing.Type[IDivisionOperators_3[Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TSelf, Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TOther, Generic_IDivisionOperators_GenericClasses_IDivisionOperators_3_TResult]]: ...

IDivisionOperators : IDivisionOperators_GenericClasses

IDivisionOperators_3_TSelf = typing.TypeVar('IDivisionOperators_3_TSelf')
IDivisionOperators_3_TOther = typing.TypeVar('IDivisionOperators_3_TOther')
IDivisionOperators_3_TResult = typing.TypeVar('IDivisionOperators_3_TResult')
class IDivisionOperators_3(typing.Generic[IDivisionOperators_3_TSelf, IDivisionOperators_3_TOther, IDivisionOperators_3_TResult], typing.Protocol):
    # Operator not supported op_CheckedDivision(left: TSelf, right: TOther)
    @abc.abstractmethod
    def __truediv__(self, left: IDivisionOperators_3_TSelf, right: typing.Optional[IDivisionOperators_3_TOther]) -> typing.Optional[IDivisionOperators_3_TResult]: ...


class IEqualityOperators_GenericClasses(abc.ABCMeta):
    Generic_IEqualityOperators_GenericClasses_IEqualityOperators_3_TSelf = typing.TypeVar('Generic_IEqualityOperators_GenericClasses_IEqualityOperators_3_TSelf')
    Generic_IEqualityOperators_GenericClasses_IEqualityOperators_3_TOther = typing.TypeVar('Generic_IEqualityOperators_GenericClasses_IEqualityOperators_3_TOther')
    Generic_IEqualityOperators_GenericClasses_IEqualityOperators_3_TResult = typing.TypeVar('Generic_IEqualityOperators_GenericClasses_IEqualityOperators_3_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IEqualityOperators_GenericClasses_IEqualityOperators_3_TSelf], typing.Type[Generic_IEqualityOperators_GenericClasses_IEqualityOperators_3_TOther], typing.Type[Generic_IEqualityOperators_GenericClasses_IEqualityOperators_3_TResult]]) -> typing.Type[IEqualityOperators_3[Generic_IEqualityOperators_GenericClasses_IEqualityOperators_3_TSelf, Generic_IEqualityOperators_GenericClasses_IEqualityOperators_3_TOther, Generic_IEqualityOperators_GenericClasses_IEqualityOperators_3_TResult]]: ...

IEqualityOperators : IEqualityOperators_GenericClasses

IEqualityOperators_3_TSelf = typing.TypeVar('IEqualityOperators_3_TSelf')
IEqualityOperators_3_TOther = typing.TypeVar('IEqualityOperators_3_TOther')
IEqualityOperators_3_TResult = typing.TypeVar('IEqualityOperators_3_TResult')
class IEqualityOperators_3(typing.Generic[IEqualityOperators_3_TSelf, IEqualityOperators_3_TOther, IEqualityOperators_3_TResult], typing.Protocol):
    @abc.abstractmethod
    def __eq__(self, left: typing.Optional[IEqualityOperators_3_TSelf], right: typing.Optional[IEqualityOperators_3_TOther]) -> typing.Optional[IEqualityOperators_3_TResult]: ...
    @abc.abstractmethod
    def __ne__(self, left: typing.Optional[IEqualityOperators_3_TSelf], right: typing.Optional[IEqualityOperators_3_TOther]) -> typing.Optional[IEqualityOperators_3_TResult]: ...


class IExponentialFunctions_GenericClasses(abc.ABCMeta):
    Generic_IExponentialFunctions_GenericClasses_IExponentialFunctions_1_TSelf = typing.TypeVar('Generic_IExponentialFunctions_GenericClasses_IExponentialFunctions_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IExponentialFunctions_GenericClasses_IExponentialFunctions_1_TSelf]) -> typing.Type[IExponentialFunctions_1[Generic_IExponentialFunctions_GenericClasses_IExponentialFunctions_1_TSelf]]: ...

IExponentialFunctions : IExponentialFunctions_GenericClasses

IExponentialFunctions_1_TSelf = typing.TypeVar('IExponentialFunctions_1_TSelf')
class IExponentialFunctions_1(typing.Generic[IExponentialFunctions_1_TSelf], IFloatingPointConstants_1[IExponentialFunctions_1_TSelf], typing.Protocol):
    @staticmethod
    @abc.abstractmethod
    def Exp(x: IExponentialFunctions_1_TSelf) -> IExponentialFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Exp10(x: IExponentialFunctions_1_TSelf) -> IExponentialFunctions_1_TSelf: ...
    @staticmethod
    def Exp10M1(x: IExponentialFunctions_1_TSelf) -> IExponentialFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Exp2(x: IExponentialFunctions_1_TSelf) -> IExponentialFunctions_1_TSelf: ...
    @staticmethod
    def Exp2M1(x: IExponentialFunctions_1_TSelf) -> IExponentialFunctions_1_TSelf: ...
    @staticmethod
    def ExpM1(x: IExponentialFunctions_1_TSelf) -> IExponentialFunctions_1_TSelf: ...


class IFloatingPoint_GenericClasses(abc.ABCMeta):
    Generic_IFloatingPoint_GenericClasses_IFloatingPoint_1_TSelf = typing.TypeVar('Generic_IFloatingPoint_GenericClasses_IFloatingPoint_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IFloatingPoint_GenericClasses_IFloatingPoint_1_TSelf]) -> typing.Type[IFloatingPoint_1[Generic_IFloatingPoint_GenericClasses_IFloatingPoint_1_TSelf]]: ...

IFloatingPoint : IFloatingPoint_GenericClasses

IFloatingPoint_1_TSelf = typing.TypeVar('IFloatingPoint_1_TSelf')
class IFloatingPoint_1(typing.Generic[IFloatingPoint_1_TSelf], ISignedNumber_1[IFloatingPoint_1_TSelf], INumber_1[IFloatingPoint_1_TSelf], IFloatingPointConstants_1[IFloatingPoint_1_TSelf], typing.Protocol):
    @staticmethod
    def Ceiling(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @staticmethod
    def Floor(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @abc.abstractmethod
    def GetExponentByteCount(self) -> int: ...
    @abc.abstractmethod
    def GetExponentShortestBitLength(self) -> int: ...
    @abc.abstractmethod
    def GetSignificandBitLength(self) -> int: ...
    @abc.abstractmethod
    def GetSignificandByteCount(self) -> int: ...
    @staticmethod
    def Truncate(x: IFloatingPoint_1_TSelf) -> IFloatingPoint_1_TSelf: ...
    @abc.abstractmethod
    def TryWriteExponentBigEndian(self, destination: Span_1[int], bytesWritten: clr.Reference[int]) -> bool: ...
    @abc.abstractmethod
    def TryWriteExponentLittleEndian(self, destination: Span_1[int], bytesWritten: clr.Reference[int]) -> bool: ...
    @abc.abstractmethod
    def TryWriteSignificandBigEndian(self, destination: Span_1[int], bytesWritten: clr.Reference[int]) -> bool: ...
    @abc.abstractmethod
    def TryWriteSignificandLittleEndian(self, destination: Span_1[int], bytesWritten: clr.Reference[int]) -> bool: ...
    # Skipped WriteExponentBigEndian due to it being static, abstract and generic.

    WriteExponentBigEndian : WriteExponentBigEndian_MethodGroup[IFloatingPoint_1_TSelf]
    WriteExponentBigEndian_MethodGroup_IFloatingPoint_1_TSelf = typing.TypeVar('WriteExponentBigEndian_MethodGroup_IFloatingPoint_1_TSelf')
    class WriteExponentBigEndian_MethodGroup(typing.Generic[WriteExponentBigEndian_MethodGroup_IFloatingPoint_1_TSelf]):
        WriteExponentBigEndian_MethodGroup_IFloatingPoint_1_TSelf = IFloatingPoint_1.WriteExponentBigEndian_MethodGroup_IFloatingPoint_1_TSelf
        @typing.overload
        def __call__(self, destination: Array_1[int]) -> int:...
        @typing.overload
        def __call__(self, destination: Span_1[int]) -> int:...
        @typing.overload
        def __call__(self, destination: Array_1[int], startIndex: int) -> int:...

    # Skipped WriteExponentLittleEndian due to it being static, abstract and generic.

    WriteExponentLittleEndian : WriteExponentLittleEndian_MethodGroup[IFloatingPoint_1_TSelf]
    WriteExponentLittleEndian_MethodGroup_IFloatingPoint_1_TSelf = typing.TypeVar('WriteExponentLittleEndian_MethodGroup_IFloatingPoint_1_TSelf')
    class WriteExponentLittleEndian_MethodGroup(typing.Generic[WriteExponentLittleEndian_MethodGroup_IFloatingPoint_1_TSelf]):
        WriteExponentLittleEndian_MethodGroup_IFloatingPoint_1_TSelf = IFloatingPoint_1.WriteExponentLittleEndian_MethodGroup_IFloatingPoint_1_TSelf
        @typing.overload
        def __call__(self, destination: Array_1[int]) -> int:...
        @typing.overload
        def __call__(self, destination: Span_1[int]) -> int:...
        @typing.overload
        def __call__(self, destination: Array_1[int], startIndex: int) -> int:...

    # Skipped WriteSignificandBigEndian due to it being static, abstract and generic.

    WriteSignificandBigEndian : WriteSignificandBigEndian_MethodGroup[IFloatingPoint_1_TSelf]
    WriteSignificandBigEndian_MethodGroup_IFloatingPoint_1_TSelf = typing.TypeVar('WriteSignificandBigEndian_MethodGroup_IFloatingPoint_1_TSelf')
    class WriteSignificandBigEndian_MethodGroup(typing.Generic[WriteSignificandBigEndian_MethodGroup_IFloatingPoint_1_TSelf]):
        WriteSignificandBigEndian_MethodGroup_IFloatingPoint_1_TSelf = IFloatingPoint_1.WriteSignificandBigEndian_MethodGroup_IFloatingPoint_1_TSelf
        @typing.overload
        def __call__(self, destination: Array_1[int]) -> int:...
        @typing.overload
        def __call__(self, destination: Span_1[int]) -> int:...
        @typing.overload
        def __call__(self, destination: Array_1[int], startIndex: int) -> int:...

    # Skipped WriteSignificandLittleEndian due to it being static, abstract and generic.

    WriteSignificandLittleEndian : WriteSignificandLittleEndian_MethodGroup[IFloatingPoint_1_TSelf]
    WriteSignificandLittleEndian_MethodGroup_IFloatingPoint_1_TSelf = typing.TypeVar('WriteSignificandLittleEndian_MethodGroup_IFloatingPoint_1_TSelf')
    class WriteSignificandLittleEndian_MethodGroup(typing.Generic[WriteSignificandLittleEndian_MethodGroup_IFloatingPoint_1_TSelf]):
        WriteSignificandLittleEndian_MethodGroup_IFloatingPoint_1_TSelf = IFloatingPoint_1.WriteSignificandLittleEndian_MethodGroup_IFloatingPoint_1_TSelf
        @typing.overload
        def __call__(self, destination: Array_1[int]) -> int:...
        @typing.overload
        def __call__(self, destination: Span_1[int]) -> int:...
        @typing.overload
        def __call__(self, destination: Array_1[int], startIndex: int) -> int:...



class IFloatingPointConstants_GenericClasses(abc.ABCMeta):
    Generic_IFloatingPointConstants_GenericClasses_IFloatingPointConstants_1_TSelf = typing.TypeVar('Generic_IFloatingPointConstants_GenericClasses_IFloatingPointConstants_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IFloatingPointConstants_GenericClasses_IFloatingPointConstants_1_TSelf]) -> typing.Type[IFloatingPointConstants_1[Generic_IFloatingPointConstants_GenericClasses_IFloatingPointConstants_1_TSelf]]: ...

IFloatingPointConstants : IFloatingPointConstants_GenericClasses

IFloatingPointConstants_1_TSelf = typing.TypeVar('IFloatingPointConstants_1_TSelf')
class IFloatingPointConstants_1(typing.Generic[IFloatingPointConstants_1_TSelf], INumberBase_1[IFloatingPointConstants_1_TSelf], typing.Protocol):
    @classmethod
    @property
    def E(cls) -> IFloatingPointConstants_1_TSelf: ...
    @classmethod
    @property
    def Pi(cls) -> IFloatingPointConstants_1_TSelf: ...
    @classmethod
    @property
    def Tau(cls) -> IFloatingPointConstants_1_TSelf: ...


class IFloatingPointIeee754_GenericClasses(abc.ABCMeta):
    Generic_IFloatingPointIeee754_GenericClasses_IFloatingPointIeee754_1_TSelf = typing.TypeVar('Generic_IFloatingPointIeee754_GenericClasses_IFloatingPointIeee754_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IFloatingPointIeee754_GenericClasses_IFloatingPointIeee754_1_TSelf]) -> typing.Type[IFloatingPointIeee754_1[Generic_IFloatingPointIeee754_GenericClasses_IFloatingPointIeee754_1_TSelf]]: ...

IFloatingPointIeee754 : IFloatingPointIeee754_GenericClasses

IFloatingPointIeee754_1_TSelf = typing.TypeVar('IFloatingPointIeee754_1_TSelf')
class IFloatingPointIeee754_1(typing.Generic[IFloatingPointIeee754_1_TSelf], ITrigonometricFunctions_1[IFloatingPointIeee754_1_TSelf], IRootFunctions_1[IFloatingPointIeee754_1_TSelf], ILogarithmicFunctions_1[IFloatingPointIeee754_1_TSelf], IHyperbolicFunctions_1[IFloatingPointIeee754_1_TSelf], IFloatingPoint_1[IFloatingPointIeee754_1_TSelf], IExponentialFunctions_1[IFloatingPointIeee754_1_TSelf], IPowerFunctions_1[IFloatingPointIeee754_1_TSelf], typing.Protocol):
    @classmethod
    @property
    def Epsilon(cls) -> IFloatingPointIeee754_1_TSelf: ...
    @classmethod
    @property
    def NaN(cls) -> IFloatingPointIeee754_1_TSelf: ...
    @classmethod
    @property
    def NegativeInfinity(cls) -> IFloatingPointIeee754_1_TSelf: ...
    @classmethod
    @property
    def NegativeZero(cls) -> IFloatingPointIeee754_1_TSelf: ...
    @classmethod
    @property
    def PositiveInfinity(cls) -> IFloatingPointIeee754_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Atan2(y: IFloatingPointIeee754_1_TSelf, x: IFloatingPointIeee754_1_TSelf) -> IFloatingPointIeee754_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Atan2Pi(y: IFloatingPointIeee754_1_TSelf, x: IFloatingPointIeee754_1_TSelf) -> IFloatingPointIeee754_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def BitDecrement(x: IFloatingPointIeee754_1_TSelf) -> IFloatingPointIeee754_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def BitIncrement(x: IFloatingPointIeee754_1_TSelf) -> IFloatingPointIeee754_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def FusedMultiplyAdd(left: IFloatingPointIeee754_1_TSelf, right: IFloatingPointIeee754_1_TSelf, addend: IFloatingPointIeee754_1_TSelf) -> IFloatingPointIeee754_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Ieee754Remainder(left: IFloatingPointIeee754_1_TSelf, right: IFloatingPointIeee754_1_TSelf) -> IFloatingPointIeee754_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def ILogB(x: IFloatingPointIeee754_1_TSelf) -> int: ...
    @staticmethod
    def Lerp(value1: IFloatingPointIeee754_1_TSelf, value2: IFloatingPointIeee754_1_TSelf, amount: IFloatingPointIeee754_1_TSelf) -> IFloatingPointIeee754_1_TSelf: ...
    @staticmethod
    def ReciprocalEstimate(x: IFloatingPointIeee754_1_TSelf) -> IFloatingPointIeee754_1_TSelf: ...
    @staticmethod
    def ReciprocalSqrtEstimate(x: IFloatingPointIeee754_1_TSelf) -> IFloatingPointIeee754_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def ScaleB(x: IFloatingPointIeee754_1_TSelf, n: int) -> IFloatingPointIeee754_1_TSelf: ...


class IHyperbolicFunctions_GenericClasses(abc.ABCMeta):
    Generic_IHyperbolicFunctions_GenericClasses_IHyperbolicFunctions_1_TSelf = typing.TypeVar('Generic_IHyperbolicFunctions_GenericClasses_IHyperbolicFunctions_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IHyperbolicFunctions_GenericClasses_IHyperbolicFunctions_1_TSelf]) -> typing.Type[IHyperbolicFunctions_1[Generic_IHyperbolicFunctions_GenericClasses_IHyperbolicFunctions_1_TSelf]]: ...

IHyperbolicFunctions : IHyperbolicFunctions_GenericClasses

IHyperbolicFunctions_1_TSelf = typing.TypeVar('IHyperbolicFunctions_1_TSelf')
class IHyperbolicFunctions_1(typing.Generic[IHyperbolicFunctions_1_TSelf], IFloatingPointConstants_1[IHyperbolicFunctions_1_TSelf], typing.Protocol):
    @staticmethod
    @abc.abstractmethod
    def Acosh(x: IHyperbolicFunctions_1_TSelf) -> IHyperbolicFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Asinh(x: IHyperbolicFunctions_1_TSelf) -> IHyperbolicFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Atanh(x: IHyperbolicFunctions_1_TSelf) -> IHyperbolicFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Cosh(x: IHyperbolicFunctions_1_TSelf) -> IHyperbolicFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Sinh(x: IHyperbolicFunctions_1_TSelf) -> IHyperbolicFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Tanh(x: IHyperbolicFunctions_1_TSelf) -> IHyperbolicFunctions_1_TSelf: ...


class IIncrementOperators_GenericClasses(abc.ABCMeta):
    Generic_IIncrementOperators_GenericClasses_IIncrementOperators_1_TSelf = typing.TypeVar('Generic_IIncrementOperators_GenericClasses_IIncrementOperators_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IIncrementOperators_GenericClasses_IIncrementOperators_1_TSelf]) -> typing.Type[IIncrementOperators_1[Generic_IIncrementOperators_GenericClasses_IIncrementOperators_1_TSelf]]: ...

IIncrementOperators : IIncrementOperators_GenericClasses

IIncrementOperators_1_TSelf = typing.TypeVar('IIncrementOperators_1_TSelf')
class IIncrementOperators_1(typing.Generic[IIncrementOperators_1_TSelf], typing.Protocol):
    # Operator not supported op_CheckedIncrement(value: TSelf)
    # Operator not supported op_Increment(value: TSelf)
    pass


class ILogarithmicFunctions_GenericClasses(abc.ABCMeta):
    Generic_ILogarithmicFunctions_GenericClasses_ILogarithmicFunctions_1_TSelf = typing.TypeVar('Generic_ILogarithmicFunctions_GenericClasses_ILogarithmicFunctions_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_ILogarithmicFunctions_GenericClasses_ILogarithmicFunctions_1_TSelf]) -> typing.Type[ILogarithmicFunctions_1[Generic_ILogarithmicFunctions_GenericClasses_ILogarithmicFunctions_1_TSelf]]: ...

ILogarithmicFunctions : ILogarithmicFunctions_GenericClasses

ILogarithmicFunctions_1_TSelf = typing.TypeVar('ILogarithmicFunctions_1_TSelf')
class ILogarithmicFunctions_1(typing.Generic[ILogarithmicFunctions_1_TSelf], IFloatingPointConstants_1[ILogarithmicFunctions_1_TSelf], typing.Protocol):
    @staticmethod
    @abc.abstractmethod
    def Log10(x: ILogarithmicFunctions_1_TSelf) -> ILogarithmicFunctions_1_TSelf: ...
    @staticmethod
    def Log10P1(x: ILogarithmicFunctions_1_TSelf) -> ILogarithmicFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Log2(x: ILogarithmicFunctions_1_TSelf) -> ILogarithmicFunctions_1_TSelf: ...
    @staticmethod
    def Log2P1(x: ILogarithmicFunctions_1_TSelf) -> ILogarithmicFunctions_1_TSelf: ...
    @staticmethod
    def LogP1(x: ILogarithmicFunctions_1_TSelf) -> ILogarithmicFunctions_1_TSelf: ...


class IMinMaxValue_GenericClasses(abc.ABCMeta):
    Generic_IMinMaxValue_GenericClasses_IMinMaxValue_1_TSelf = typing.TypeVar('Generic_IMinMaxValue_GenericClasses_IMinMaxValue_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IMinMaxValue_GenericClasses_IMinMaxValue_1_TSelf]) -> typing.Type[IMinMaxValue_1[Generic_IMinMaxValue_GenericClasses_IMinMaxValue_1_TSelf]]: ...

IMinMaxValue : IMinMaxValue_GenericClasses

IMinMaxValue_1_TSelf = typing.TypeVar('IMinMaxValue_1_TSelf')
class IMinMaxValue_1(typing.Generic[IMinMaxValue_1_TSelf], typing.Protocol):
    @classmethod
    @property
    def MaxValue(cls) -> IMinMaxValue_1_TSelf: ...
    @classmethod
    @property
    def MinValue(cls) -> IMinMaxValue_1_TSelf: ...


class IModulusOperators_GenericClasses(abc.ABCMeta):
    Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TSelf = typing.TypeVar('Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TSelf')
    Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TOther = typing.TypeVar('Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TOther')
    Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TResult = typing.TypeVar('Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TSelf], typing.Type[Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TOther], typing.Type[Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TResult]]) -> typing.Type[IModulusOperators_3[Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TSelf, Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TOther, Generic_IModulusOperators_GenericClasses_IModulusOperators_3_TResult]]: ...

IModulusOperators : IModulusOperators_GenericClasses

IModulusOperators_3_TSelf = typing.TypeVar('IModulusOperators_3_TSelf')
IModulusOperators_3_TOther = typing.TypeVar('IModulusOperators_3_TOther')
IModulusOperators_3_TResult = typing.TypeVar('IModulusOperators_3_TResult')
class IModulusOperators_3(typing.Generic[IModulusOperators_3_TSelf, IModulusOperators_3_TOther, IModulusOperators_3_TResult], typing.Protocol):
    @abc.abstractmethod
    def __mod__(self, left: IModulusOperators_3_TSelf, right: typing.Optional[IModulusOperators_3_TOther]) -> typing.Optional[IModulusOperators_3_TResult]: ...


class IMultiplicativeIdentity_GenericClasses(abc.ABCMeta):
    Generic_IMultiplicativeIdentity_GenericClasses_IMultiplicativeIdentity_2_TSelf = typing.TypeVar('Generic_IMultiplicativeIdentity_GenericClasses_IMultiplicativeIdentity_2_TSelf')
    Generic_IMultiplicativeIdentity_GenericClasses_IMultiplicativeIdentity_2_TResult = typing.TypeVar('Generic_IMultiplicativeIdentity_GenericClasses_IMultiplicativeIdentity_2_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IMultiplicativeIdentity_GenericClasses_IMultiplicativeIdentity_2_TSelf], typing.Type[Generic_IMultiplicativeIdentity_GenericClasses_IMultiplicativeIdentity_2_TResult]]) -> typing.Type[IMultiplicativeIdentity_2[Generic_IMultiplicativeIdentity_GenericClasses_IMultiplicativeIdentity_2_TSelf, Generic_IMultiplicativeIdentity_GenericClasses_IMultiplicativeIdentity_2_TResult]]: ...

IMultiplicativeIdentity : IMultiplicativeIdentity_GenericClasses

IMultiplicativeIdentity_2_TSelf = typing.TypeVar('IMultiplicativeIdentity_2_TSelf')
IMultiplicativeIdentity_2_TResult = typing.TypeVar('IMultiplicativeIdentity_2_TResult')
class IMultiplicativeIdentity_2(typing.Generic[IMultiplicativeIdentity_2_TSelf, IMultiplicativeIdentity_2_TResult], typing.Protocol):
    @classmethod
    @property
    def MultiplicativeIdentity(cls) -> typing.Optional[IMultiplicativeIdentity_2_TResult]: ...


class IMultiplyOperators_GenericClasses(abc.ABCMeta):
    Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TSelf = typing.TypeVar('Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TSelf')
    Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TOther = typing.TypeVar('Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TOther')
    Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TResult = typing.TypeVar('Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TSelf], typing.Type[Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TOther], typing.Type[Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TResult]]) -> typing.Type[IMultiplyOperators_3[Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TSelf, Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TOther, Generic_IMultiplyOperators_GenericClasses_IMultiplyOperators_3_TResult]]: ...

IMultiplyOperators : IMultiplyOperators_GenericClasses

IMultiplyOperators_3_TSelf = typing.TypeVar('IMultiplyOperators_3_TSelf')
IMultiplyOperators_3_TOther = typing.TypeVar('IMultiplyOperators_3_TOther')
IMultiplyOperators_3_TResult = typing.TypeVar('IMultiplyOperators_3_TResult')
class IMultiplyOperators_3(typing.Generic[IMultiplyOperators_3_TSelf, IMultiplyOperators_3_TOther, IMultiplyOperators_3_TResult], typing.Protocol):
    # Operator not supported op_CheckedMultiply(left: TSelf, right: TOther)
    @abc.abstractmethod
    def __mul__(self, left: IMultiplyOperators_3_TSelf, right: typing.Optional[IMultiplyOperators_3_TOther]) -> typing.Optional[IMultiplyOperators_3_TResult]: ...


class INumber_GenericClasses(abc.ABCMeta):
    Generic_INumber_GenericClasses_INumber_1_TSelf = typing.TypeVar('Generic_INumber_GenericClasses_INumber_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_INumber_GenericClasses_INumber_1_TSelf]) -> typing.Type[INumber_1[Generic_INumber_GenericClasses_INumber_1_TSelf]]: ...

INumber : INumber_GenericClasses

INumber_1_TSelf = typing.TypeVar('INumber_1_TSelf')
class INumber_1(typing.Generic[INumber_1_TSelf], INumberBase_1[INumber_1_TSelf], IComparisonOperators_3[INumber_1_TSelf, INumber_1_TSelf, bool], IModulusOperators_3[INumber_1_TSelf, INumber_1_TSelf, INumber_1_TSelf], IComparable_1[INumber_1_TSelf], IComparable_0, typing.Protocol):
    @staticmethod
    def Clamp(value: INumber_1_TSelf, min: INumber_1_TSelf, max: INumber_1_TSelf) -> INumber_1_TSelf: ...
    @staticmethod
    def CopySign(value: INumber_1_TSelf, sign: INumber_1_TSelf) -> INumber_1_TSelf: ...
    @staticmethod
    def Max(x: INumber_1_TSelf, y: INumber_1_TSelf) -> INumber_1_TSelf: ...
    @staticmethod
    def MaxNumber(x: INumber_1_TSelf, y: INumber_1_TSelf) -> INumber_1_TSelf: ...
    @staticmethod
    def Min(x: INumber_1_TSelf, y: INumber_1_TSelf) -> INumber_1_TSelf: ...
    @staticmethod
    def MinNumber(x: INumber_1_TSelf, y: INumber_1_TSelf) -> INumber_1_TSelf: ...
    @staticmethod
    def Sign(value: INumber_1_TSelf) -> int: ...


class INumberBase_GenericClasses(abc.ABCMeta):
    Generic_INumberBase_GenericClasses_INumberBase_1_TSelf = typing.TypeVar('Generic_INumberBase_GenericClasses_INumberBase_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_INumberBase_GenericClasses_INumberBase_1_TSelf]) -> typing.Type[INumberBase_1[Generic_INumberBase_GenericClasses_INumberBase_1_TSelf]]: ...

INumberBase : INumberBase_GenericClasses

INumberBase_1_TSelf = typing.TypeVar('INumberBase_1_TSelf')
class INumberBase_1(typing.Generic[INumberBase_1_TSelf], ISpanParsable_1[INumberBase_1_TSelf], ISpanFormattable, IUtf8SpanParsable_1[INumberBase_1_TSelf], IUtf8SpanFormattable, IUnaryNegationOperators_2[INumberBase_1_TSelf, INumberBase_1_TSelf], IUnaryPlusOperators_2[INumberBase_1_TSelf, INumberBase_1_TSelf], ISubtractionOperators_3[INumberBase_1_TSelf, INumberBase_1_TSelf, INumberBase_1_TSelf], IMultiplyOperators_3[INumberBase_1_TSelf, INumberBase_1_TSelf, INumberBase_1_TSelf], IMultiplicativeIdentity_2[INumberBase_1_TSelf, INumberBase_1_TSelf], IIncrementOperators_1[INumberBase_1_TSelf], IEqualityOperators_3[INumberBase_1_TSelf, INumberBase_1_TSelf, bool], IEquatable_1[INumberBase_1_TSelf], IDivisionOperators_3[INumberBase_1_TSelf, INumberBase_1_TSelf, INumberBase_1_TSelf], IDecrementOperators_1[INumberBase_1_TSelf], IAdditiveIdentity_2[INumberBase_1_TSelf, INumberBase_1_TSelf], IAdditionOperators_3[INumberBase_1_TSelf, INumberBase_1_TSelf, INumberBase_1_TSelf], typing.Protocol):
    @classmethod
    @property
    def One(cls) -> INumberBase_1_TSelf: ...
    @classmethod
    @property
    def Radix(cls) -> int: ...
    @classmethod
    @property
    def Zero(cls) -> INumberBase_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Abs(value: INumberBase_1_TSelf) -> INumberBase_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def IsCanonical(value: INumberBase_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsComplexNumber(value: INumberBase_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsEvenInteger(value: INumberBase_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsFinite(value: INumberBase_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsImaginaryNumber(value: INumberBase_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsInfinity(value: INumberBase_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsInteger(value: INumberBase_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsNaN(value: INumberBase_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsNegative(value: INumberBase_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsNegativeInfinity(value: INumberBase_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsNormal(value: INumberBase_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsOddInteger(value: INumberBase_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsPositive(value: INumberBase_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsPositiveInfinity(value: INumberBase_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsRealNumber(value: INumberBase_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsSubnormal(value: INumberBase_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def IsZero(value: INumberBase_1_TSelf) -> bool: ...
    @staticmethod
    @abc.abstractmethod
    def MaxMagnitude(x: INumberBase_1_TSelf, y: INumberBase_1_TSelf) -> INumberBase_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def MaxMagnitudeNumber(x: INumberBase_1_TSelf, y: INumberBase_1_TSelf) -> INumberBase_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def MinMagnitude(x: INumberBase_1_TSelf, y: INumberBase_1_TSelf) -> INumberBase_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def MinMagnitudeNumber(x: INumberBase_1_TSelf, y: INumberBase_1_TSelf) -> INumberBase_1_TSelf: ...
    # Skipped CreateChecked due to it being static, abstract and generic.

    CreateChecked : CreateChecked_MethodGroup[INumberBase_1_TSelf]
    CreateChecked_MethodGroup_INumberBase_1_TSelf = typing.TypeVar('CreateChecked_MethodGroup_INumberBase_1_TSelf')
    class CreateChecked_MethodGroup(typing.Generic[CreateChecked_MethodGroup_INumberBase_1_TSelf]):
        CreateChecked_MethodGroup_INumberBase_1_TSelf = INumberBase_1.CreateChecked_MethodGroup_INumberBase_1_TSelf
        def __getitem__(self, t:typing.Type[CreateChecked_1_T1]) -> CreateChecked_1[CreateChecked_MethodGroup_INumberBase_1_TSelf, CreateChecked_1_T1]: ...

        CreateChecked_1_INumberBase_1_TSelf = typing.TypeVar('CreateChecked_1_INumberBase_1_TSelf')
        CreateChecked_1_T1 = typing.TypeVar('CreateChecked_1_T1')
        class CreateChecked_1(typing.Generic[CreateChecked_1_INumberBase_1_TSelf, CreateChecked_1_T1]):
            CreateChecked_1_INumberBase_1_TSelf = INumberBase_1.CreateChecked_MethodGroup.CreateChecked_1_INumberBase_1_TSelf
            CreateChecked_1_TOther = INumberBase_1.CreateChecked_MethodGroup.CreateChecked_1_T1
            def __call__(self, value: CreateChecked_1_TOther) -> CreateChecked_1_INumberBase_1_TSelf:...


    # Skipped CreateSaturating due to it being static, abstract and generic.

    CreateSaturating : CreateSaturating_MethodGroup[INumberBase_1_TSelf]
    CreateSaturating_MethodGroup_INumberBase_1_TSelf = typing.TypeVar('CreateSaturating_MethodGroup_INumberBase_1_TSelf')
    class CreateSaturating_MethodGroup(typing.Generic[CreateSaturating_MethodGroup_INumberBase_1_TSelf]):
        CreateSaturating_MethodGroup_INumberBase_1_TSelf = INumberBase_1.CreateSaturating_MethodGroup_INumberBase_1_TSelf
        def __getitem__(self, t:typing.Type[CreateSaturating_1_T1]) -> CreateSaturating_1[CreateSaturating_MethodGroup_INumberBase_1_TSelf, CreateSaturating_1_T1]: ...

        CreateSaturating_1_INumberBase_1_TSelf = typing.TypeVar('CreateSaturating_1_INumberBase_1_TSelf')
        CreateSaturating_1_T1 = typing.TypeVar('CreateSaturating_1_T1')
        class CreateSaturating_1(typing.Generic[CreateSaturating_1_INumberBase_1_TSelf, CreateSaturating_1_T1]):
            CreateSaturating_1_INumberBase_1_TSelf = INumberBase_1.CreateSaturating_MethodGroup.CreateSaturating_1_INumberBase_1_TSelf
            CreateSaturating_1_TOther = INumberBase_1.CreateSaturating_MethodGroup.CreateSaturating_1_T1
            def __call__(self, value: CreateSaturating_1_TOther) -> CreateSaturating_1_INumberBase_1_TSelf:...


    # Skipped CreateTruncating due to it being static, abstract and generic.

    CreateTruncating : CreateTruncating_MethodGroup[INumberBase_1_TSelf]
    CreateTruncating_MethodGroup_INumberBase_1_TSelf = typing.TypeVar('CreateTruncating_MethodGroup_INumberBase_1_TSelf')
    class CreateTruncating_MethodGroup(typing.Generic[CreateTruncating_MethodGroup_INumberBase_1_TSelf]):
        CreateTruncating_MethodGroup_INumberBase_1_TSelf = INumberBase_1.CreateTruncating_MethodGroup_INumberBase_1_TSelf
        def __getitem__(self, t:typing.Type[CreateTruncating_1_T1]) -> CreateTruncating_1[CreateTruncating_MethodGroup_INumberBase_1_TSelf, CreateTruncating_1_T1]: ...

        CreateTruncating_1_INumberBase_1_TSelf = typing.TypeVar('CreateTruncating_1_INumberBase_1_TSelf')
        CreateTruncating_1_T1 = typing.TypeVar('CreateTruncating_1_T1')
        class CreateTruncating_1(typing.Generic[CreateTruncating_1_INumberBase_1_TSelf, CreateTruncating_1_T1]):
            CreateTruncating_1_INumberBase_1_TSelf = INumberBase_1.CreateTruncating_MethodGroup.CreateTruncating_1_INumberBase_1_TSelf
            CreateTruncating_1_TOther = INumberBase_1.CreateTruncating_MethodGroup.CreateTruncating_1_T1
            def __call__(self, value: CreateTruncating_1_TOther) -> CreateTruncating_1_INumberBase_1_TSelf:...




class IPowerFunctions_GenericClasses(abc.ABCMeta):
    Generic_IPowerFunctions_GenericClasses_IPowerFunctions_1_TSelf = typing.TypeVar('Generic_IPowerFunctions_GenericClasses_IPowerFunctions_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IPowerFunctions_GenericClasses_IPowerFunctions_1_TSelf]) -> typing.Type[IPowerFunctions_1[Generic_IPowerFunctions_GenericClasses_IPowerFunctions_1_TSelf]]: ...

IPowerFunctions : IPowerFunctions_GenericClasses

IPowerFunctions_1_TSelf = typing.TypeVar('IPowerFunctions_1_TSelf')
class IPowerFunctions_1(typing.Generic[IPowerFunctions_1_TSelf], INumberBase_1[IPowerFunctions_1_TSelf], typing.Protocol):
    @staticmethod
    @abc.abstractmethod
    def Pow(x: IPowerFunctions_1_TSelf, y: IPowerFunctions_1_TSelf) -> IPowerFunctions_1_TSelf: ...


class IRootFunctions_GenericClasses(abc.ABCMeta):
    Generic_IRootFunctions_GenericClasses_IRootFunctions_1_TSelf = typing.TypeVar('Generic_IRootFunctions_GenericClasses_IRootFunctions_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IRootFunctions_GenericClasses_IRootFunctions_1_TSelf]) -> typing.Type[IRootFunctions_1[Generic_IRootFunctions_GenericClasses_IRootFunctions_1_TSelf]]: ...

IRootFunctions : IRootFunctions_GenericClasses

IRootFunctions_1_TSelf = typing.TypeVar('IRootFunctions_1_TSelf')
class IRootFunctions_1(typing.Generic[IRootFunctions_1_TSelf], IFloatingPointConstants_1[IRootFunctions_1_TSelf], typing.Protocol):
    @staticmethod
    @abc.abstractmethod
    def Cbrt(x: IRootFunctions_1_TSelf) -> IRootFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Hypot(x: IRootFunctions_1_TSelf, y: IRootFunctions_1_TSelf) -> IRootFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def RootN(x: IRootFunctions_1_TSelf, n: int) -> IRootFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Sqrt(x: IRootFunctions_1_TSelf) -> IRootFunctions_1_TSelf: ...


class IShiftOperators_GenericClasses(abc.ABCMeta):
    Generic_IShiftOperators_GenericClasses_IShiftOperators_3_TSelf = typing.TypeVar('Generic_IShiftOperators_GenericClasses_IShiftOperators_3_TSelf')
    Generic_IShiftOperators_GenericClasses_IShiftOperators_3_TOther = typing.TypeVar('Generic_IShiftOperators_GenericClasses_IShiftOperators_3_TOther')
    Generic_IShiftOperators_GenericClasses_IShiftOperators_3_TResult = typing.TypeVar('Generic_IShiftOperators_GenericClasses_IShiftOperators_3_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IShiftOperators_GenericClasses_IShiftOperators_3_TSelf], typing.Type[Generic_IShiftOperators_GenericClasses_IShiftOperators_3_TOther], typing.Type[Generic_IShiftOperators_GenericClasses_IShiftOperators_3_TResult]]) -> typing.Type[IShiftOperators_3[Generic_IShiftOperators_GenericClasses_IShiftOperators_3_TSelf, Generic_IShiftOperators_GenericClasses_IShiftOperators_3_TOther, Generic_IShiftOperators_GenericClasses_IShiftOperators_3_TResult]]: ...

IShiftOperators : IShiftOperators_GenericClasses

IShiftOperators_3_TSelf = typing.TypeVar('IShiftOperators_3_TSelf')
IShiftOperators_3_TOther = typing.TypeVar('IShiftOperators_3_TOther')
IShiftOperators_3_TResult = typing.TypeVar('IShiftOperators_3_TResult')
class IShiftOperators_3(typing.Generic[IShiftOperators_3_TSelf, IShiftOperators_3_TOther, IShiftOperators_3_TResult], typing.Protocol):
    @abc.abstractmethod
    def __lshift__(self, value: IShiftOperators_3_TSelf, shiftAmount: typing.Optional[IShiftOperators_3_TOther]) -> typing.Optional[IShiftOperators_3_TResult]: ...
    @abc.abstractmethod
    def __rshift__(self, value: IShiftOperators_3_TSelf, shiftAmount: typing.Optional[IShiftOperators_3_TOther]) -> typing.Optional[IShiftOperators_3_TResult]: ...
    # Operator not supported op_UnsignedRightShift(value: TSelf, shiftAmount: TOther)


class ISignedNumber_GenericClasses(abc.ABCMeta):
    Generic_ISignedNumber_GenericClasses_ISignedNumber_1_TSelf = typing.TypeVar('Generic_ISignedNumber_GenericClasses_ISignedNumber_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_ISignedNumber_GenericClasses_ISignedNumber_1_TSelf]) -> typing.Type[ISignedNumber_1[Generic_ISignedNumber_GenericClasses_ISignedNumber_1_TSelf]]: ...

ISignedNumber : ISignedNumber_GenericClasses

ISignedNumber_1_TSelf = typing.TypeVar('ISignedNumber_1_TSelf')
class ISignedNumber_1(typing.Generic[ISignedNumber_1_TSelf], INumberBase_1[ISignedNumber_1_TSelf], typing.Protocol):
    @classmethod
    @property
    def NegativeOne(cls) -> ISignedNumber_1_TSelf: ...


class ISubtractionOperators_GenericClasses(abc.ABCMeta):
    Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TSelf = typing.TypeVar('Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TSelf')
    Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TOther = typing.TypeVar('Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TOther')
    Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TResult = typing.TypeVar('Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TSelf], typing.Type[Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TOther], typing.Type[Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TResult]]) -> typing.Type[ISubtractionOperators_3[Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TSelf, Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TOther, Generic_ISubtractionOperators_GenericClasses_ISubtractionOperators_3_TResult]]: ...

ISubtractionOperators : ISubtractionOperators_GenericClasses

ISubtractionOperators_3_TSelf = typing.TypeVar('ISubtractionOperators_3_TSelf')
ISubtractionOperators_3_TOther = typing.TypeVar('ISubtractionOperators_3_TOther')
ISubtractionOperators_3_TResult = typing.TypeVar('ISubtractionOperators_3_TResult')
class ISubtractionOperators_3(typing.Generic[ISubtractionOperators_3_TSelf, ISubtractionOperators_3_TOther, ISubtractionOperators_3_TResult], typing.Protocol):
    # Operator not supported op_CheckedSubtraction(left: TSelf, right: TOther)
    @abc.abstractmethod
    def __sub__(self, left: ISubtractionOperators_3_TSelf, right: typing.Optional[ISubtractionOperators_3_TOther]) -> typing.Optional[ISubtractionOperators_3_TResult]: ...


class ITrigonometricFunctions_GenericClasses(abc.ABCMeta):
    Generic_ITrigonometricFunctions_GenericClasses_ITrigonometricFunctions_1_TSelf = typing.TypeVar('Generic_ITrigonometricFunctions_GenericClasses_ITrigonometricFunctions_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_ITrigonometricFunctions_GenericClasses_ITrigonometricFunctions_1_TSelf]) -> typing.Type[ITrigonometricFunctions_1[Generic_ITrigonometricFunctions_GenericClasses_ITrigonometricFunctions_1_TSelf]]: ...

ITrigonometricFunctions : ITrigonometricFunctions_GenericClasses

ITrigonometricFunctions_1_TSelf = typing.TypeVar('ITrigonometricFunctions_1_TSelf')
class ITrigonometricFunctions_1(typing.Generic[ITrigonometricFunctions_1_TSelf], IFloatingPointConstants_1[ITrigonometricFunctions_1_TSelf], typing.Protocol):
    @staticmethod
    @abc.abstractmethod
    def Acos(x: ITrigonometricFunctions_1_TSelf) -> ITrigonometricFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def AcosPi(x: ITrigonometricFunctions_1_TSelf) -> ITrigonometricFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Asin(x: ITrigonometricFunctions_1_TSelf) -> ITrigonometricFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def AsinPi(x: ITrigonometricFunctions_1_TSelf) -> ITrigonometricFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Atan(x: ITrigonometricFunctions_1_TSelf) -> ITrigonometricFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def AtanPi(x: ITrigonometricFunctions_1_TSelf) -> ITrigonometricFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Cos(x: ITrigonometricFunctions_1_TSelf) -> ITrigonometricFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def CosPi(x: ITrigonometricFunctions_1_TSelf) -> ITrigonometricFunctions_1_TSelf: ...
    @staticmethod
    def DegreesToRadians(degrees: ITrigonometricFunctions_1_TSelf) -> ITrigonometricFunctions_1_TSelf: ...
    @staticmethod
    def RadiansToDegrees(radians: ITrigonometricFunctions_1_TSelf) -> ITrigonometricFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Sin(x: ITrigonometricFunctions_1_TSelf) -> ITrigonometricFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def SinCos(x: ITrigonometricFunctions_1_TSelf) -> ValueTuple_2[ITrigonometricFunctions_1_TSelf, ITrigonometricFunctions_1_TSelf]: ...
    @staticmethod
    @abc.abstractmethod
    def SinCosPi(x: ITrigonometricFunctions_1_TSelf) -> ValueTuple_2[ITrigonometricFunctions_1_TSelf, ITrigonometricFunctions_1_TSelf]: ...
    @staticmethod
    @abc.abstractmethod
    def SinPi(x: ITrigonometricFunctions_1_TSelf) -> ITrigonometricFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def Tan(x: ITrigonometricFunctions_1_TSelf) -> ITrigonometricFunctions_1_TSelf: ...
    @staticmethod
    @abc.abstractmethod
    def TanPi(x: ITrigonometricFunctions_1_TSelf) -> ITrigonometricFunctions_1_TSelf: ...


class IUnaryNegationOperators_GenericClasses(abc.ABCMeta):
    Generic_IUnaryNegationOperators_GenericClasses_IUnaryNegationOperators_2_TSelf = typing.TypeVar('Generic_IUnaryNegationOperators_GenericClasses_IUnaryNegationOperators_2_TSelf')
    Generic_IUnaryNegationOperators_GenericClasses_IUnaryNegationOperators_2_TResult = typing.TypeVar('Generic_IUnaryNegationOperators_GenericClasses_IUnaryNegationOperators_2_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IUnaryNegationOperators_GenericClasses_IUnaryNegationOperators_2_TSelf], typing.Type[Generic_IUnaryNegationOperators_GenericClasses_IUnaryNegationOperators_2_TResult]]) -> typing.Type[IUnaryNegationOperators_2[Generic_IUnaryNegationOperators_GenericClasses_IUnaryNegationOperators_2_TSelf, Generic_IUnaryNegationOperators_GenericClasses_IUnaryNegationOperators_2_TResult]]: ...

IUnaryNegationOperators : IUnaryNegationOperators_GenericClasses

IUnaryNegationOperators_2_TSelf = typing.TypeVar('IUnaryNegationOperators_2_TSelf')
IUnaryNegationOperators_2_TResult = typing.TypeVar('IUnaryNegationOperators_2_TResult')
class IUnaryNegationOperators_2(typing.Generic[IUnaryNegationOperators_2_TSelf, IUnaryNegationOperators_2_TResult], typing.Protocol):
    # Operator not supported op_CheckedUnaryNegation(value: TSelf)
    @abc.abstractmethod
    def __neg__(self, value: IUnaryNegationOperators_2_TSelf) -> typing.Optional[IUnaryNegationOperators_2_TResult]: ...


class IUnaryPlusOperators_GenericClasses(abc.ABCMeta):
    Generic_IUnaryPlusOperators_GenericClasses_IUnaryPlusOperators_2_TSelf = typing.TypeVar('Generic_IUnaryPlusOperators_GenericClasses_IUnaryPlusOperators_2_TSelf')
    Generic_IUnaryPlusOperators_GenericClasses_IUnaryPlusOperators_2_TResult = typing.TypeVar('Generic_IUnaryPlusOperators_GenericClasses_IUnaryPlusOperators_2_TResult')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IUnaryPlusOperators_GenericClasses_IUnaryPlusOperators_2_TSelf], typing.Type[Generic_IUnaryPlusOperators_GenericClasses_IUnaryPlusOperators_2_TResult]]) -> typing.Type[IUnaryPlusOperators_2[Generic_IUnaryPlusOperators_GenericClasses_IUnaryPlusOperators_2_TSelf, Generic_IUnaryPlusOperators_GenericClasses_IUnaryPlusOperators_2_TResult]]: ...

IUnaryPlusOperators : IUnaryPlusOperators_GenericClasses

IUnaryPlusOperators_2_TSelf = typing.TypeVar('IUnaryPlusOperators_2_TSelf')
IUnaryPlusOperators_2_TResult = typing.TypeVar('IUnaryPlusOperators_2_TResult')
class IUnaryPlusOperators_2(typing.Generic[IUnaryPlusOperators_2_TSelf, IUnaryPlusOperators_2_TResult], typing.Protocol):
    @abc.abstractmethod
    def __pos__(self, value: IUnaryPlusOperators_2_TSelf) -> typing.Optional[IUnaryPlusOperators_2_TResult]: ...


class IUnsignedNumber_GenericClasses(abc.ABCMeta):
    Generic_IUnsignedNumber_GenericClasses_IUnsignedNumber_1_TSelf = typing.TypeVar('Generic_IUnsignedNumber_GenericClasses_IUnsignedNumber_1_TSelf')
    def __getitem__(self, types : typing.Type[Generic_IUnsignedNumber_GenericClasses_IUnsignedNumber_1_TSelf]) -> typing.Type[IUnsignedNumber_1[Generic_IUnsignedNumber_GenericClasses_IUnsignedNumber_1_TSelf]]: ...

IUnsignedNumber : IUnsignedNumber_GenericClasses

IUnsignedNumber_1_TSelf = typing.TypeVar('IUnsignedNumber_1_TSelf')
class IUnsignedNumber_1(typing.Generic[IUnsignedNumber_1_TSelf], INumberBase_1[IUnsignedNumber_1_TSelf], typing.Protocol):
    pass


class Matrix3x2(IEquatable_1[Matrix3x2]):
    def __init__(self, m11: float, m12: float, m21: float, m22: float, m31: float, m32: float) -> None: ...
    M11 : float
    M12 : float
    M21 : float
    M22 : float
    M31 : float
    M32 : float
    @classmethod
    @property
    def Identity(cls) -> Matrix3x2: ...
    @property
    def IsIdentity(self) -> bool: ...
    @property
    def Item(self) -> float: ...
    @Item.setter
    def Item(self, value: float) -> float: ...
    @property
    def Translation(self) -> Vector2: ...
    @Translation.setter
    def Translation(self, value: Vector2) -> Vector2: ...
    @staticmethod
    def Add(value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2: ...
    def GetDeterminant(self) -> float: ...
    def GetHashCode(self) -> int: ...
    @staticmethod
    def Invert(matrix: Matrix3x2, result: clr.Reference[Matrix3x2]) -> bool: ...
    @staticmethod
    def Lerp(matrix1: Matrix3x2, matrix2: Matrix3x2, amount: float) -> Matrix3x2: ...
    @staticmethod
    def Negate(value: Matrix3x2) -> Matrix3x2: ...
    def __add__(self, value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2: ...
    def __eq__(self, value1: Matrix3x2, value2: Matrix3x2) -> bool: ...
    def __ne__(self, value1: Matrix3x2, value2: Matrix3x2) -> bool: ...
    @typing.overload
    def __mul__(self, value1: Matrix3x2, value2: float) -> Matrix3x2: ...
    @typing.overload
    def __mul__(self, value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2: ...
    def __sub__(self, value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2: ...
    def __neg__(self, value: Matrix3x2) -> Matrix3x2: ...
    @staticmethod
    def Subtract(value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2: ...
    def ToString(self) -> str: ...
    # Skipped CreateRotation due to it being static, abstract and generic.

    CreateRotation : CreateRotation_MethodGroup
    class CreateRotation_MethodGroup:
        @typing.overload
        def __call__(self, radians: float) -> Matrix3x2:...
        @typing.overload
        def __call__(self, radians: float, centerPoint: Vector2) -> Matrix3x2:...

    # Skipped CreateScale due to it being static, abstract and generic.

    CreateScale : CreateScale_MethodGroup
    class CreateScale_MethodGroup:
        @typing.overload
        def __call__(self, scale: float) -> Matrix3x2:...
        @typing.overload
        def __call__(self, scales: Vector2) -> Matrix3x2:...
        @typing.overload
        def __call__(self, xScale: float, yScale: float) -> Matrix3x2:...
        @typing.overload
        def __call__(self, scale: float, centerPoint: Vector2) -> Matrix3x2:...
        @typing.overload
        def __call__(self, scales: Vector2, centerPoint: Vector2) -> Matrix3x2:...
        @typing.overload
        def __call__(self, xScale: float, yScale: float, centerPoint: Vector2) -> Matrix3x2:...

    # Skipped CreateSkew due to it being static, abstract and generic.

    CreateSkew : CreateSkew_MethodGroup
    class CreateSkew_MethodGroup:
        @typing.overload
        def __call__(self, radiansX: float, radiansY: float) -> Matrix3x2:...
        @typing.overload
        def __call__(self, radiansX: float, radiansY: float, centerPoint: Vector2) -> Matrix3x2:...

    # Skipped CreateTranslation due to it being static, abstract and generic.

    CreateTranslation : CreateTranslation_MethodGroup
    class CreateTranslation_MethodGroup:
        @typing.overload
        def __call__(self, position: Vector2) -> Matrix3x2:...
        @typing.overload
        def __call__(self, xPosition: float, yPosition: float) -> Matrix3x2:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: Matrix3x2) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Optional[typing.Any]) -> bool:...

    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        @typing.overload
        def __call__(self, value1: Matrix3x2, value2: float) -> Matrix3x2:...
        @typing.overload
        def __call__(self, value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2:...



class Matrix4x4(IEquatable_1[Matrix4x4]):
    @typing.overload
    def __init__(self, m11: float, m12: float, m13: float, m14: float, m21: float, m22: float, m23: float, m24: float, m31: float, m32: float, m33: float, m34: float, m41: float, m42: float, m43: float, m44: float) -> None: ...
    @typing.overload
    def __init__(self, value: Matrix3x2) -> None: ...
    M11 : float
    M12 : float
    M13 : float
    M14 : float
    M21 : float
    M22 : float
    M23 : float
    M24 : float
    M31 : float
    M32 : float
    M33 : float
    M34 : float
    M41 : float
    M42 : float
    M43 : float
    M44 : float
    @classmethod
    @property
    def Identity(cls) -> Matrix4x4: ...
    @property
    def IsIdentity(self) -> bool: ...
    @property
    def Item(self) -> float: ...
    @Item.setter
    def Item(self, value: float) -> float: ...
    @property
    def Translation(self) -> Vector3: ...
    @Translation.setter
    def Translation(self, value: Vector3) -> Vector3: ...
    @staticmethod
    def Add(value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4: ...
    @staticmethod
    def CreateBillboard(objectPosition: Vector3, cameraPosition: Vector3, cameraUpVector: Vector3, cameraForwardVector: Vector3) -> Matrix4x4: ...
    @staticmethod
    def CreateConstrainedBillboard(objectPosition: Vector3, cameraPosition: Vector3, rotateAxis: Vector3, cameraForwardVector: Vector3, objectForwardVector: Vector3) -> Matrix4x4: ...
    @staticmethod
    def CreateFromAxisAngle(axis: Vector3, angle: float) -> Matrix4x4: ...
    @staticmethod
    def CreateFromQuaternion(quaternion: Quaternion) -> Matrix4x4: ...
    @staticmethod
    def CreateFromYawPitchRoll(yaw: float, pitch: float, roll: float) -> Matrix4x4: ...
    @staticmethod
    def CreateLookAt(cameraPosition: Vector3, cameraTarget: Vector3, cameraUpVector: Vector3) -> Matrix4x4: ...
    @staticmethod
    def CreateLookAtLeftHanded(cameraPosition: Vector3, cameraTarget: Vector3, cameraUpVector: Vector3) -> Matrix4x4: ...
    @staticmethod
    def CreateLookTo(cameraPosition: Vector3, cameraDirection: Vector3, cameraUpVector: Vector3) -> Matrix4x4: ...
    @staticmethod
    def CreateLookToLeftHanded(cameraPosition: Vector3, cameraDirection: Vector3, cameraUpVector: Vector3) -> Matrix4x4: ...
    @staticmethod
    def CreateOrthographic(width: float, height: float, zNearPlane: float, zFarPlane: float) -> Matrix4x4: ...
    @staticmethod
    def CreateOrthographicLeftHanded(width: float, height: float, zNearPlane: float, zFarPlane: float) -> Matrix4x4: ...
    @staticmethod
    def CreateOrthographicOffCenter(left: float, right: float, bottom: float, top: float, zNearPlane: float, zFarPlane: float) -> Matrix4x4: ...
    @staticmethod
    def CreateOrthographicOffCenterLeftHanded(left: float, right: float, bottom: float, top: float, zNearPlane: float, zFarPlane: float) -> Matrix4x4: ...
    @staticmethod
    def CreatePerspective(width: float, height: float, nearPlaneDistance: float, farPlaneDistance: float) -> Matrix4x4: ...
    @staticmethod
    def CreatePerspectiveFieldOfView(fieldOfView: float, aspectRatio: float, nearPlaneDistance: float, farPlaneDistance: float) -> Matrix4x4: ...
    @staticmethod
    def CreatePerspectiveFieldOfViewLeftHanded(fieldOfView: float, aspectRatio: float, nearPlaneDistance: float, farPlaneDistance: float) -> Matrix4x4: ...
    @staticmethod
    def CreatePerspectiveLeftHanded(width: float, height: float, nearPlaneDistance: float, farPlaneDistance: float) -> Matrix4x4: ...
    @staticmethod
    def CreatePerspectiveOffCenter(left: float, right: float, bottom: float, top: float, nearPlaneDistance: float, farPlaneDistance: float) -> Matrix4x4: ...
    @staticmethod
    def CreatePerspectiveOffCenterLeftHanded(left: float, right: float, bottom: float, top: float, nearPlaneDistance: float, farPlaneDistance: float) -> Matrix4x4: ...
    @staticmethod
    def CreateReflection(value: Plane) -> Matrix4x4: ...
    @staticmethod
    def CreateShadow(lightDirection: Vector3, plane: Plane) -> Matrix4x4: ...
    @staticmethod
    def CreateViewport(x: float, y: float, width: float, height: float, minDepth: float, maxDepth: float) -> Matrix4x4: ...
    @staticmethod
    def CreateViewportLeftHanded(x: float, y: float, width: float, height: float, minDepth: float, maxDepth: float) -> Matrix4x4: ...
    @staticmethod
    def CreateWorld(position: Vector3, forward: Vector3, up: Vector3) -> Matrix4x4: ...
    @staticmethod
    def Decompose(matrix: Matrix4x4, scale: clr.Reference[Vector3], rotation: clr.Reference[Quaternion], translation: clr.Reference[Vector3]) -> bool: ...
    def GetDeterminant(self) -> float: ...
    def GetHashCode(self) -> int: ...
    @staticmethod
    def Invert(matrix: Matrix4x4, result: clr.Reference[Matrix4x4]) -> bool: ...
    @staticmethod
    def Lerp(matrix1: Matrix4x4, matrix2: Matrix4x4, amount: float) -> Matrix4x4: ...
    @staticmethod
    def Negate(value: Matrix4x4) -> Matrix4x4: ...
    def __add__(self, value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4: ...
    def __eq__(self, value1: Matrix4x4, value2: Matrix4x4) -> bool: ...
    def __ne__(self, value1: Matrix4x4, value2: Matrix4x4) -> bool: ...
    @typing.overload
    def __mul__(self, value1: Matrix4x4, value2: float) -> Matrix4x4: ...
    @typing.overload
    def __mul__(self, value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4: ...
    def __sub__(self, value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4: ...
    def __neg__(self, value: Matrix4x4) -> Matrix4x4: ...
    @staticmethod
    def Subtract(value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4: ...
    def ToString(self) -> str: ...
    @staticmethod
    def Transform(value: Matrix4x4, rotation: Quaternion) -> Matrix4x4: ...
    @staticmethod
    def Transpose(matrix: Matrix4x4) -> Matrix4x4: ...
    # Skipped CreateRotationX due to it being static, abstract and generic.

    CreateRotationX : CreateRotationX_MethodGroup
    class CreateRotationX_MethodGroup:
        @typing.overload
        def __call__(self, radians: float) -> Matrix4x4:...
        @typing.overload
        def __call__(self, radians: float, centerPoint: Vector3) -> Matrix4x4:...

    # Skipped CreateRotationY due to it being static, abstract and generic.

    CreateRotationY : CreateRotationY_MethodGroup
    class CreateRotationY_MethodGroup:
        @typing.overload
        def __call__(self, radians: float) -> Matrix4x4:...
        @typing.overload
        def __call__(self, radians: float, centerPoint: Vector3) -> Matrix4x4:...

    # Skipped CreateRotationZ due to it being static, abstract and generic.

    CreateRotationZ : CreateRotationZ_MethodGroup
    class CreateRotationZ_MethodGroup:
        @typing.overload
        def __call__(self, radians: float) -> Matrix4x4:...
        @typing.overload
        def __call__(self, radians: float, centerPoint: Vector3) -> Matrix4x4:...

    # Skipped CreateScale due to it being static, abstract and generic.

    CreateScale : CreateScale_MethodGroup
    class CreateScale_MethodGroup:
        @typing.overload
        def __call__(self, scale: float) -> Matrix4x4:...
        @typing.overload
        def __call__(self, scales: Vector3) -> Matrix4x4:...
        @typing.overload
        def __call__(self, scale: float, centerPoint: Vector3) -> Matrix4x4:...
        @typing.overload
        def __call__(self, scales: Vector3, centerPoint: Vector3) -> Matrix4x4:...
        @typing.overload
        def __call__(self, xScale: float, yScale: float, zScale: float) -> Matrix4x4:...
        @typing.overload
        def __call__(self, xScale: float, yScale: float, zScale: float, centerPoint: Vector3) -> Matrix4x4:...

    # Skipped CreateTranslation due to it being static, abstract and generic.

    CreateTranslation : CreateTranslation_MethodGroup
    class CreateTranslation_MethodGroup:
        @typing.overload
        def __call__(self, position: Vector3) -> Matrix4x4:...
        @typing.overload
        def __call__(self, xPosition: float, yPosition: float, zPosition: float) -> Matrix4x4:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: Matrix4x4) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Optional[typing.Any]) -> bool:...

    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        @typing.overload
        def __call__(self, value1: Matrix4x4, value2: float) -> Matrix4x4:...
        @typing.overload
        def __call__(self, value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4:...



class Plane(IEquatable_1[Plane]):
    @typing.overload
    def __init__(self, normal: Vector3, d: float) -> None: ...
    @typing.overload
    def __init__(self, value: Vector4) -> None: ...
    @typing.overload
    def __init__(self, x: float, y: float, z: float, d: float) -> None: ...
    D : float
    Normal : Vector3
    @staticmethod
    def CreateFromVertices(point1: Vector3, point2: Vector3, point3: Vector3) -> Plane: ...
    @staticmethod
    def Dot(plane: Plane, value: Vector4) -> float: ...
    @staticmethod
    def DotCoordinate(plane: Plane, value: Vector3) -> float: ...
    @staticmethod
    def DotNormal(plane: Plane, value: Vector3) -> float: ...
    def GetHashCode(self) -> int: ...
    @staticmethod
    def Normalize(value: Plane) -> Plane: ...
    def __eq__(self, value1: Plane, value2: Plane) -> bool: ...
    def __ne__(self, value1: Plane, value2: Plane) -> bool: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: Plane) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Optional[typing.Any]) -> bool:...

    # Skipped Transform due to it being static, abstract and generic.

    Transform : Transform_MethodGroup
    class Transform_MethodGroup:
        @typing.overload
        def __call__(self, plane: Plane, matrix: Matrix4x4) -> Plane:...
        @typing.overload
        def __call__(self, plane: Plane, rotation: Quaternion) -> Plane:...



class Quaternion(IEquatable_1[Quaternion]):
    @typing.overload
    def __init__(self, vectorPart: Vector3, scalarPart: float) -> None: ...
    @typing.overload
    def __init__(self, x: float, y: float, z: float, w: float) -> None: ...
    W : float
    X : float
    Y : float
    Z : float
    @classmethod
    @property
    def Identity(cls) -> Quaternion: ...
    @property
    def IsIdentity(self) -> bool: ...
    @property
    def Item(self) -> float: ...
    @Item.setter
    def Item(self, value: float) -> float: ...
    @classmethod
    @property
    def Zero(cls) -> Quaternion: ...
    @staticmethod
    def Add(value1: Quaternion, value2: Quaternion) -> Quaternion: ...
    @staticmethod
    def Concatenate(value1: Quaternion, value2: Quaternion) -> Quaternion: ...
    @staticmethod
    def Conjugate(value: Quaternion) -> Quaternion: ...
    @staticmethod
    def CreateFromAxisAngle(axis: Vector3, angle: float) -> Quaternion: ...
    @staticmethod
    def CreateFromRotationMatrix(matrix: Matrix4x4) -> Quaternion: ...
    @staticmethod
    def CreateFromYawPitchRoll(yaw: float, pitch: float, roll: float) -> Quaternion: ...
    @staticmethod
    def Divide(value1: Quaternion, value2: Quaternion) -> Quaternion: ...
    @staticmethod
    def Dot(quaternion1: Quaternion, quaternion2: Quaternion) -> float: ...
    def GetHashCode(self) -> int: ...
    @staticmethod
    def Inverse(value: Quaternion) -> Quaternion: ...
    def Length(self) -> float: ...
    def LengthSquared(self) -> float: ...
    @staticmethod
    def Lerp(quaternion1: Quaternion, quaternion2: Quaternion, amount: float) -> Quaternion: ...
    @staticmethod
    def Negate(value: Quaternion) -> Quaternion: ...
    @staticmethod
    def Normalize(value: Quaternion) -> Quaternion: ...
    def __add__(self, value1: Quaternion, value2: Quaternion) -> Quaternion: ...
    def __truediv__(self, value1: Quaternion, value2: Quaternion) -> Quaternion: ...
    def __eq__(self, value1: Quaternion, value2: Quaternion) -> bool: ...
    def __ne__(self, value1: Quaternion, value2: Quaternion) -> bool: ...
    @typing.overload
    def __mul__(self, value1: Quaternion, value2: float) -> Quaternion: ...
    @typing.overload
    def __mul__(self, value1: Quaternion, value2: Quaternion) -> Quaternion: ...
    def __sub__(self, value1: Quaternion, value2: Quaternion) -> Quaternion: ...
    def __neg__(self, value: Quaternion) -> Quaternion: ...
    @staticmethod
    def Slerp(quaternion1: Quaternion, quaternion2: Quaternion, amount: float) -> Quaternion: ...
    @staticmethod
    def Subtract(value1: Quaternion, value2: Quaternion) -> Quaternion: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: Quaternion) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Optional[typing.Any]) -> bool:...

    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        @typing.overload
        def __call__(self, value1: Quaternion, value2: float) -> Quaternion:...
        @typing.overload
        def __call__(self, value1: Quaternion, value2: Quaternion) -> Quaternion:...



class TotalOrderIeee754Comparer_GenericClasses(abc.ABCMeta):
    Generic_TotalOrderIeee754Comparer_GenericClasses_TotalOrderIeee754Comparer_1_T = typing.TypeVar('Generic_TotalOrderIeee754Comparer_GenericClasses_TotalOrderIeee754Comparer_1_T')
    def __getitem__(self, types : typing.Type[Generic_TotalOrderIeee754Comparer_GenericClasses_TotalOrderIeee754Comparer_1_T]) -> typing.Type[TotalOrderIeee754Comparer_1[Generic_TotalOrderIeee754Comparer_GenericClasses_TotalOrderIeee754Comparer_1_T]]: ...

TotalOrderIeee754Comparer : TotalOrderIeee754Comparer_GenericClasses

TotalOrderIeee754Comparer_1_T = typing.TypeVar('TotalOrderIeee754Comparer_1_T')
class TotalOrderIeee754Comparer_1(typing.Generic[TotalOrderIeee754Comparer_1_T], IEquatable_1[TotalOrderIeee754Comparer_1[TotalOrderIeee754Comparer_1_T]], IEqualityComparer_1[TotalOrderIeee754Comparer_1_T], IComparer_1[TotalOrderIeee754Comparer_1_T]):
    def Compare(self, x: typing.Optional[TotalOrderIeee754Comparer_1_T], y: typing.Optional[TotalOrderIeee754Comparer_1_T]) -> int: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[TotalOrderIeee754Comparer_1_T]
    Equals_MethodGroup_TotalOrderIeee754Comparer_1_T = typing.TypeVar('Equals_MethodGroup_TotalOrderIeee754Comparer_1_T')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_TotalOrderIeee754Comparer_1_T]):
        Equals_MethodGroup_TotalOrderIeee754Comparer_1_T = TotalOrderIeee754Comparer_1.Equals_MethodGroup_TotalOrderIeee754Comparer_1_T
        @typing.overload
        def __call__(self, other: TotalOrderIeee754Comparer_1[Equals_MethodGroup_TotalOrderIeee754Comparer_1_T]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Optional[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, x: typing.Optional[Equals_MethodGroup_TotalOrderIeee754Comparer_1_T], y: typing.Optional[Equals_MethodGroup_TotalOrderIeee754Comparer_1_T]) -> bool:...

    # Skipped GetHashCode due to it being static, abstract and generic.

    GetHashCode : GetHashCode_MethodGroup[TotalOrderIeee754Comparer_1_T]
    GetHashCode_MethodGroup_TotalOrderIeee754Comparer_1_T = typing.TypeVar('GetHashCode_MethodGroup_TotalOrderIeee754Comparer_1_T')
    class GetHashCode_MethodGroup(typing.Generic[GetHashCode_MethodGroup_TotalOrderIeee754Comparer_1_T]):
        GetHashCode_MethodGroup_TotalOrderIeee754Comparer_1_T = TotalOrderIeee754Comparer_1.GetHashCode_MethodGroup_TotalOrderIeee754Comparer_1_T
        @typing.overload
        def __call__(self) -> int:...
        @typing.overload
        def __call__(self, obj: GetHashCode_MethodGroup_TotalOrderIeee754Comparer_1_T) -> int:...



class Vector_GenericClasses(abc.ABCMeta):
    Generic_Vector_GenericClasses_Vector_1_T = typing.TypeVar('Generic_Vector_GenericClasses_Vector_1_T')
    def __getitem__(self, types : typing.Type[Generic_Vector_GenericClasses_Vector_1_T]) -> typing.Type[Vector_1[Generic_Vector_GenericClasses_Vector_1_T]]: ...

class Vector(Vector_0, metaclass =Vector_GenericClasses): ...

class Vector_0(abc.ABC):
    @classmethod
    @property
    def IsHardwareAccelerated(cls) -> bool: ...
    @staticmethod
    def ConvertToInt32(value: Vector_1[float]) -> Vector_1[int]: ...
    @staticmethod
    def ConvertToInt64(value: Vector_1[float]) -> Vector_1[int]: ...
    @staticmethod
    def ConvertToUInt32(value: Vector_1[float]) -> Vector_1[int]: ...
    @staticmethod
    def ConvertToUInt64(value: Vector_1[float]) -> Vector_1[int]: ...
    # Skipped Abs due to it being static, abstract and generic.

    Abs : Abs_MethodGroup
    class Abs_MethodGroup:
        def __getitem__(self, t:typing.Type[Abs_1_T1]) -> Abs_1[Abs_1_T1]: ...

        Abs_1_T1 = typing.TypeVar('Abs_1_T1')
        class Abs_1(typing.Generic[Abs_1_T1]):
            Abs_1_T = Vector_0.Abs_MethodGroup.Abs_1_T1
            def __call__(self, value: Vector_1[Abs_1_T]) -> Vector_1[Abs_1_T]:...


    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        def __getitem__(self, t:typing.Type[Add_1_T1]) -> Add_1[Add_1_T1]: ...

        Add_1_T1 = typing.TypeVar('Add_1_T1')
        class Add_1(typing.Generic[Add_1_T1]):
            Add_1_T = Vector_0.Add_MethodGroup.Add_1_T1
            def __call__(self, left: Vector_1[Add_1_T], right: Vector_1[Add_1_T]) -> Vector_1[Add_1_T]:...


    # Skipped AndNot due to it being static, abstract and generic.

    AndNot : AndNot_MethodGroup
    class AndNot_MethodGroup:
        def __getitem__(self, t:typing.Type[AndNot_1_T1]) -> AndNot_1[AndNot_1_T1]: ...

        AndNot_1_T1 = typing.TypeVar('AndNot_1_T1')
        class AndNot_1(typing.Generic[AndNot_1_T1]):
            AndNot_1_T = Vector_0.AndNot_MethodGroup.AndNot_1_T1
            def __call__(self, left: Vector_1[AndNot_1_T], right: Vector_1[AndNot_1_T]) -> Vector_1[AndNot_1_T]:...


    # Skipped As due to it being static, abstract and generic.

    As : As_MethodGroup
    class As_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[As_2_T1], typing.Type[As_2_T2]]) -> As_2[As_2_T1, As_2_T2]: ...

        As_2_T1 = typing.TypeVar('As_2_T1')
        As_2_T2 = typing.TypeVar('As_2_T2')
        class As_2(typing.Generic[As_2_T1, As_2_T2]):
            As_2_TFrom = Vector_0.As_MethodGroup.As_2_T1
            As_2_TTo = Vector_0.As_MethodGroup.As_2_T2
            def __call__(self, vector: Vector_1[As_2_TFrom]) -> Vector_1[As_2_TTo]:...


    # Skipped AsVectorByte due to it being static, abstract and generic.

    AsVectorByte : AsVectorByte_MethodGroup
    class AsVectorByte_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVectorByte_1_T1]) -> AsVectorByte_1[AsVectorByte_1_T1]: ...

        AsVectorByte_1_T1 = typing.TypeVar('AsVectorByte_1_T1')
        class AsVectorByte_1(typing.Generic[AsVectorByte_1_T1]):
            AsVectorByte_1_T = Vector_0.AsVectorByte_MethodGroup.AsVectorByte_1_T1
            def __call__(self, value: Vector_1[AsVectorByte_1_T]) -> Vector_1[int]:...


    # Skipped AsVectorDouble due to it being static, abstract and generic.

    AsVectorDouble : AsVectorDouble_MethodGroup
    class AsVectorDouble_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVectorDouble_1_T1]) -> AsVectorDouble_1[AsVectorDouble_1_T1]: ...

        AsVectorDouble_1_T1 = typing.TypeVar('AsVectorDouble_1_T1')
        class AsVectorDouble_1(typing.Generic[AsVectorDouble_1_T1]):
            AsVectorDouble_1_T = Vector_0.AsVectorDouble_MethodGroup.AsVectorDouble_1_T1
            def __call__(self, value: Vector_1[AsVectorDouble_1_T]) -> Vector_1[float]:...


    # Skipped AsVectorInt16 due to it being static, abstract and generic.

    AsVectorInt16 : AsVectorInt16_MethodGroup
    class AsVectorInt16_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVectorInt16_1_T1]) -> AsVectorInt16_1[AsVectorInt16_1_T1]: ...

        AsVectorInt16_1_T1 = typing.TypeVar('AsVectorInt16_1_T1')
        class AsVectorInt16_1(typing.Generic[AsVectorInt16_1_T1]):
            AsVectorInt16_1_T = Vector_0.AsVectorInt16_MethodGroup.AsVectorInt16_1_T1
            def __call__(self, value: Vector_1[AsVectorInt16_1_T]) -> Vector_1[int]:...


    # Skipped AsVectorInt32 due to it being static, abstract and generic.

    AsVectorInt32 : AsVectorInt32_MethodGroup
    class AsVectorInt32_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVectorInt32_1_T1]) -> AsVectorInt32_1[AsVectorInt32_1_T1]: ...

        AsVectorInt32_1_T1 = typing.TypeVar('AsVectorInt32_1_T1')
        class AsVectorInt32_1(typing.Generic[AsVectorInt32_1_T1]):
            AsVectorInt32_1_T = Vector_0.AsVectorInt32_MethodGroup.AsVectorInt32_1_T1
            def __call__(self, value: Vector_1[AsVectorInt32_1_T]) -> Vector_1[int]:...


    # Skipped AsVectorInt64 due to it being static, abstract and generic.

    AsVectorInt64 : AsVectorInt64_MethodGroup
    class AsVectorInt64_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVectorInt64_1_T1]) -> AsVectorInt64_1[AsVectorInt64_1_T1]: ...

        AsVectorInt64_1_T1 = typing.TypeVar('AsVectorInt64_1_T1')
        class AsVectorInt64_1(typing.Generic[AsVectorInt64_1_T1]):
            AsVectorInt64_1_T = Vector_0.AsVectorInt64_MethodGroup.AsVectorInt64_1_T1
            def __call__(self, value: Vector_1[AsVectorInt64_1_T]) -> Vector_1[int]:...


    # Skipped AsVectorNInt due to it being static, abstract and generic.

    AsVectorNInt : AsVectorNInt_MethodGroup
    class AsVectorNInt_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVectorNInt_1_T1]) -> AsVectorNInt_1[AsVectorNInt_1_T1]: ...

        AsVectorNInt_1_T1 = typing.TypeVar('AsVectorNInt_1_T1')
        class AsVectorNInt_1(typing.Generic[AsVectorNInt_1_T1]):
            AsVectorNInt_1_T = Vector_0.AsVectorNInt_MethodGroup.AsVectorNInt_1_T1
            def __call__(self, value: Vector_1[AsVectorNInt_1_T]) -> Vector_1[int]:...


    # Skipped AsVectorNUInt due to it being static, abstract and generic.

    AsVectorNUInt : AsVectorNUInt_MethodGroup
    class AsVectorNUInt_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVectorNUInt_1_T1]) -> AsVectorNUInt_1[AsVectorNUInt_1_T1]: ...

        AsVectorNUInt_1_T1 = typing.TypeVar('AsVectorNUInt_1_T1')
        class AsVectorNUInt_1(typing.Generic[AsVectorNUInt_1_T1]):
            AsVectorNUInt_1_T = Vector_0.AsVectorNUInt_MethodGroup.AsVectorNUInt_1_T1
            def __call__(self, value: Vector_1[AsVectorNUInt_1_T]) -> Vector_1[UIntPtr]:...


    # Skipped AsVectorSByte due to it being static, abstract and generic.

    AsVectorSByte : AsVectorSByte_MethodGroup
    class AsVectorSByte_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVectorSByte_1_T1]) -> AsVectorSByte_1[AsVectorSByte_1_T1]: ...

        AsVectorSByte_1_T1 = typing.TypeVar('AsVectorSByte_1_T1')
        class AsVectorSByte_1(typing.Generic[AsVectorSByte_1_T1]):
            AsVectorSByte_1_T = Vector_0.AsVectorSByte_MethodGroup.AsVectorSByte_1_T1
            def __call__(self, value: Vector_1[AsVectorSByte_1_T]) -> Vector_1[int]:...


    # Skipped AsVectorSingle due to it being static, abstract and generic.

    AsVectorSingle : AsVectorSingle_MethodGroup
    class AsVectorSingle_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVectorSingle_1_T1]) -> AsVectorSingle_1[AsVectorSingle_1_T1]: ...

        AsVectorSingle_1_T1 = typing.TypeVar('AsVectorSingle_1_T1')
        class AsVectorSingle_1(typing.Generic[AsVectorSingle_1_T1]):
            AsVectorSingle_1_T = Vector_0.AsVectorSingle_MethodGroup.AsVectorSingle_1_T1
            def __call__(self, value: Vector_1[AsVectorSingle_1_T]) -> Vector_1[float]:...


    # Skipped AsVectorUInt16 due to it being static, abstract and generic.

    AsVectorUInt16 : AsVectorUInt16_MethodGroup
    class AsVectorUInt16_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVectorUInt16_1_T1]) -> AsVectorUInt16_1[AsVectorUInt16_1_T1]: ...

        AsVectorUInt16_1_T1 = typing.TypeVar('AsVectorUInt16_1_T1')
        class AsVectorUInt16_1(typing.Generic[AsVectorUInt16_1_T1]):
            AsVectorUInt16_1_T = Vector_0.AsVectorUInt16_MethodGroup.AsVectorUInt16_1_T1
            def __call__(self, value: Vector_1[AsVectorUInt16_1_T]) -> Vector_1[int]:...


    # Skipped AsVectorUInt32 due to it being static, abstract and generic.

    AsVectorUInt32 : AsVectorUInt32_MethodGroup
    class AsVectorUInt32_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVectorUInt32_1_T1]) -> AsVectorUInt32_1[AsVectorUInt32_1_T1]: ...

        AsVectorUInt32_1_T1 = typing.TypeVar('AsVectorUInt32_1_T1')
        class AsVectorUInt32_1(typing.Generic[AsVectorUInt32_1_T1]):
            AsVectorUInt32_1_T = Vector_0.AsVectorUInt32_MethodGroup.AsVectorUInt32_1_T1
            def __call__(self, value: Vector_1[AsVectorUInt32_1_T]) -> Vector_1[int]:...


    # Skipped AsVectorUInt64 due to it being static, abstract and generic.

    AsVectorUInt64 : AsVectorUInt64_MethodGroup
    class AsVectorUInt64_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVectorUInt64_1_T1]) -> AsVectorUInt64_1[AsVectorUInt64_1_T1]: ...

        AsVectorUInt64_1_T1 = typing.TypeVar('AsVectorUInt64_1_T1')
        class AsVectorUInt64_1(typing.Generic[AsVectorUInt64_1_T1]):
            AsVectorUInt64_1_T = Vector_0.AsVectorUInt64_MethodGroup.AsVectorUInt64_1_T1
            def __call__(self, value: Vector_1[AsVectorUInt64_1_T]) -> Vector_1[int]:...


    # Skipped BitwiseAnd due to it being static, abstract and generic.

    BitwiseAnd : BitwiseAnd_MethodGroup
    class BitwiseAnd_MethodGroup:
        def __getitem__(self, t:typing.Type[BitwiseAnd_1_T1]) -> BitwiseAnd_1[BitwiseAnd_1_T1]: ...

        BitwiseAnd_1_T1 = typing.TypeVar('BitwiseAnd_1_T1')
        class BitwiseAnd_1(typing.Generic[BitwiseAnd_1_T1]):
            BitwiseAnd_1_T = Vector_0.BitwiseAnd_MethodGroup.BitwiseAnd_1_T1
            def __call__(self, left: Vector_1[BitwiseAnd_1_T], right: Vector_1[BitwiseAnd_1_T]) -> Vector_1[BitwiseAnd_1_T]:...


    # Skipped BitwiseOr due to it being static, abstract and generic.

    BitwiseOr : BitwiseOr_MethodGroup
    class BitwiseOr_MethodGroup:
        def __getitem__(self, t:typing.Type[BitwiseOr_1_T1]) -> BitwiseOr_1[BitwiseOr_1_T1]: ...

        BitwiseOr_1_T1 = typing.TypeVar('BitwiseOr_1_T1')
        class BitwiseOr_1(typing.Generic[BitwiseOr_1_T1]):
            BitwiseOr_1_T = Vector_0.BitwiseOr_MethodGroup.BitwiseOr_1_T1
            def __call__(self, left: Vector_1[BitwiseOr_1_T], right: Vector_1[BitwiseOr_1_T]) -> Vector_1[BitwiseOr_1_T]:...


    # Skipped Ceiling due to it being static, abstract and generic.

    Ceiling : Ceiling_MethodGroup
    class Ceiling_MethodGroup:
        def __call__(self, value: Vector_1[float]) -> Vector_1[float]:...
        # Method Ceiling(value : Vector`1) was skipped since it collides with above method

    # Skipped ConditionalSelect due to it being static, abstract and generic.

    ConditionalSelect : ConditionalSelect_MethodGroup
    class ConditionalSelect_MethodGroup:
        def __getitem__(self, t:typing.Type[ConditionalSelect_1_T1]) -> ConditionalSelect_1[ConditionalSelect_1_T1]: ...

        ConditionalSelect_1_T1 = typing.TypeVar('ConditionalSelect_1_T1')
        class ConditionalSelect_1(typing.Generic[ConditionalSelect_1_T1]):
            ConditionalSelect_1_T = Vector_0.ConditionalSelect_MethodGroup.ConditionalSelect_1_T1
            def __call__(self, condition: Vector_1[ConditionalSelect_1_T], left: Vector_1[ConditionalSelect_1_T], right: Vector_1[ConditionalSelect_1_T]) -> Vector_1[ConditionalSelect_1_T]:...

        def __call__(self, condition: Vector_1[int], left: Vector_1[float], right: Vector_1[float]) -> Vector_1[float]:...
        # Method ConditionalSelect(condition : Vector`1, left : Vector`1, right : Vector`1) was skipped since it collides with above method

    # Skipped ConvertToDouble due to it being static, abstract and generic.

    ConvertToDouble : ConvertToDouble_MethodGroup
    class ConvertToDouble_MethodGroup:
        def __call__(self, value: Vector_1[int]) -> Vector_1[float]:...
        # Method ConvertToDouble(value : Vector`1) was skipped since it collides with above method

    # Skipped ConvertToSingle due to it being static, abstract and generic.

    ConvertToSingle : ConvertToSingle_MethodGroup
    class ConvertToSingle_MethodGroup:
        def __call__(self, value: Vector_1[int]) -> Vector_1[float]:...
        # Method ConvertToSingle(value : Vector`1) was skipped since it collides with above method

    # Skipped Divide due to it being static, abstract and generic.

    Divide : Divide_MethodGroup
    class Divide_MethodGroup:
        def __getitem__(self, t:typing.Type[Divide_1_T1]) -> Divide_1[Divide_1_T1]: ...

        Divide_1_T1 = typing.TypeVar('Divide_1_T1')
        class Divide_1(typing.Generic[Divide_1_T1]):
            Divide_1_T = Vector_0.Divide_MethodGroup.Divide_1_T1
            @typing.overload
            def __call__(self, left: Vector_1[Divide_1_T], right: Vector_1[Divide_1_T]) -> Vector_1[Divide_1_T]:...
            @typing.overload
            def __call__(self, left: Vector_1[Divide_1_T], right: typing.Optional[Divide_1_T]) -> Vector_1[Divide_1_T]:...


    # Skipped Dot due to it being static, abstract and generic.

    Dot : Dot_MethodGroup
    class Dot_MethodGroup:
        def __getitem__(self, t:typing.Type[Dot_1_T1]) -> Dot_1[Dot_1_T1]: ...

        Dot_1_T1 = typing.TypeVar('Dot_1_T1')
        class Dot_1(typing.Generic[Dot_1_T1]):
            Dot_1_T = Vector_0.Dot_MethodGroup.Dot_1_T1
            def __call__(self, left: Vector_1[Dot_1_T], right: Vector_1[Dot_1_T]) -> Dot_1_T:...


    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        def __getitem__(self, t:typing.Type[Equals_1_T1]) -> Equals_1[Equals_1_T1]: ...

        Equals_1_T1 = typing.TypeVar('Equals_1_T1')
        class Equals_1(typing.Generic[Equals_1_T1]):
            Equals_1_T = Vector_0.Equals_MethodGroup.Equals_1_T1
            def __call__(self, left: Vector_1[Equals_1_T], right: Vector_1[Equals_1_T]) -> Vector_1[Equals_1_T]:...

        def __call__(self, left: Vector_1[float], right: Vector_1[float]) -> Vector_1[int]:...
        # Method Equals(left : Vector`1, right : Vector`1) was skipped since it collides with above method
        # Method Equals(left : Vector`1, right : Vector`1) was skipped since it collides with above method
        # Method Equals(left : Vector`1, right : Vector`1) was skipped since it collides with above method

    # Skipped EqualsAll due to it being static, abstract and generic.

    EqualsAll : EqualsAll_MethodGroup
    class EqualsAll_MethodGroup:
        def __getitem__(self, t:typing.Type[EqualsAll_1_T1]) -> EqualsAll_1[EqualsAll_1_T1]: ...

        EqualsAll_1_T1 = typing.TypeVar('EqualsAll_1_T1')
        class EqualsAll_1(typing.Generic[EqualsAll_1_T1]):
            EqualsAll_1_T = Vector_0.EqualsAll_MethodGroup.EqualsAll_1_T1
            def __call__(self, left: Vector_1[EqualsAll_1_T], right: Vector_1[EqualsAll_1_T]) -> bool:...


    # Skipped EqualsAny due to it being static, abstract and generic.

    EqualsAny : EqualsAny_MethodGroup
    class EqualsAny_MethodGroup:
        def __getitem__(self, t:typing.Type[EqualsAny_1_T1]) -> EqualsAny_1[EqualsAny_1_T1]: ...

        EqualsAny_1_T1 = typing.TypeVar('EqualsAny_1_T1')
        class EqualsAny_1(typing.Generic[EqualsAny_1_T1]):
            EqualsAny_1_T = Vector_0.EqualsAny_MethodGroup.EqualsAny_1_T1
            def __call__(self, left: Vector_1[EqualsAny_1_T], right: Vector_1[EqualsAny_1_T]) -> bool:...


    # Skipped Floor due to it being static, abstract and generic.

    Floor : Floor_MethodGroup
    class Floor_MethodGroup:
        def __call__(self, value: Vector_1[float]) -> Vector_1[float]:...
        # Method Floor(value : Vector`1) was skipped since it collides with above method

    # Skipped GetElement due to it being static, abstract and generic.

    GetElement : GetElement_MethodGroup
    class GetElement_MethodGroup:
        def __getitem__(self, t:typing.Type[GetElement_1_T1]) -> GetElement_1[GetElement_1_T1]: ...

        GetElement_1_T1 = typing.TypeVar('GetElement_1_T1')
        class GetElement_1(typing.Generic[GetElement_1_T1]):
            GetElement_1_T = Vector_0.GetElement_MethodGroup.GetElement_1_T1
            def __call__(self, vector: Vector_1[GetElement_1_T], index: int) -> GetElement_1_T:...


    # Skipped GreaterThan due to it being static, abstract and generic.

    GreaterThan : GreaterThan_MethodGroup
    class GreaterThan_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThan_1_T1]) -> GreaterThan_1[GreaterThan_1_T1]: ...

        GreaterThan_1_T1 = typing.TypeVar('GreaterThan_1_T1')
        class GreaterThan_1(typing.Generic[GreaterThan_1_T1]):
            GreaterThan_1_T = Vector_0.GreaterThan_MethodGroup.GreaterThan_1_T1
            def __call__(self, left: Vector_1[GreaterThan_1_T], right: Vector_1[GreaterThan_1_T]) -> Vector_1[GreaterThan_1_T]:...

        def __call__(self, left: Vector_1[float], right: Vector_1[float]) -> Vector_1[int]:...
        # Method GreaterThan(left : Vector`1, right : Vector`1) was skipped since it collides with above method
        # Method GreaterThan(left : Vector`1, right : Vector`1) was skipped since it collides with above method
        # Method GreaterThan(left : Vector`1, right : Vector`1) was skipped since it collides with above method

    # Skipped GreaterThanAll due to it being static, abstract and generic.

    GreaterThanAll : GreaterThanAll_MethodGroup
    class GreaterThanAll_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanAll_1_T1]) -> GreaterThanAll_1[GreaterThanAll_1_T1]: ...

        GreaterThanAll_1_T1 = typing.TypeVar('GreaterThanAll_1_T1')
        class GreaterThanAll_1(typing.Generic[GreaterThanAll_1_T1]):
            GreaterThanAll_1_T = Vector_0.GreaterThanAll_MethodGroup.GreaterThanAll_1_T1
            def __call__(self, left: Vector_1[GreaterThanAll_1_T], right: Vector_1[GreaterThanAll_1_T]) -> bool:...


    # Skipped GreaterThanAny due to it being static, abstract and generic.

    GreaterThanAny : GreaterThanAny_MethodGroup
    class GreaterThanAny_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanAny_1_T1]) -> GreaterThanAny_1[GreaterThanAny_1_T1]: ...

        GreaterThanAny_1_T1 = typing.TypeVar('GreaterThanAny_1_T1')
        class GreaterThanAny_1(typing.Generic[GreaterThanAny_1_T1]):
            GreaterThanAny_1_T = Vector_0.GreaterThanAny_MethodGroup.GreaterThanAny_1_T1
            def __call__(self, left: Vector_1[GreaterThanAny_1_T], right: Vector_1[GreaterThanAny_1_T]) -> bool:...


    # Skipped GreaterThanOrEqual due to it being static, abstract and generic.

    GreaterThanOrEqual : GreaterThanOrEqual_MethodGroup
    class GreaterThanOrEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanOrEqual_1_T1]) -> GreaterThanOrEqual_1[GreaterThanOrEqual_1_T1]: ...

        GreaterThanOrEqual_1_T1 = typing.TypeVar('GreaterThanOrEqual_1_T1')
        class GreaterThanOrEqual_1(typing.Generic[GreaterThanOrEqual_1_T1]):
            GreaterThanOrEqual_1_T = Vector_0.GreaterThanOrEqual_MethodGroup.GreaterThanOrEqual_1_T1
            def __call__(self, left: Vector_1[GreaterThanOrEqual_1_T], right: Vector_1[GreaterThanOrEqual_1_T]) -> Vector_1[GreaterThanOrEqual_1_T]:...

        def __call__(self, left: Vector_1[float], right: Vector_1[float]) -> Vector_1[int]:...
        # Method GreaterThanOrEqual(left : Vector`1, right : Vector`1) was skipped since it collides with above method
        # Method GreaterThanOrEqual(left : Vector`1, right : Vector`1) was skipped since it collides with above method
        # Method GreaterThanOrEqual(left : Vector`1, right : Vector`1) was skipped since it collides with above method

    # Skipped GreaterThanOrEqualAll due to it being static, abstract and generic.

    GreaterThanOrEqualAll : GreaterThanOrEqualAll_MethodGroup
    class GreaterThanOrEqualAll_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanOrEqualAll_1_T1]) -> GreaterThanOrEqualAll_1[GreaterThanOrEqualAll_1_T1]: ...

        GreaterThanOrEqualAll_1_T1 = typing.TypeVar('GreaterThanOrEqualAll_1_T1')
        class GreaterThanOrEqualAll_1(typing.Generic[GreaterThanOrEqualAll_1_T1]):
            GreaterThanOrEqualAll_1_T = Vector_0.GreaterThanOrEqualAll_MethodGroup.GreaterThanOrEqualAll_1_T1
            def __call__(self, left: Vector_1[GreaterThanOrEqualAll_1_T], right: Vector_1[GreaterThanOrEqualAll_1_T]) -> bool:...


    # Skipped GreaterThanOrEqualAny due to it being static, abstract and generic.

    GreaterThanOrEqualAny : GreaterThanOrEqualAny_MethodGroup
    class GreaterThanOrEqualAny_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanOrEqualAny_1_T1]) -> GreaterThanOrEqualAny_1[GreaterThanOrEqualAny_1_T1]: ...

        GreaterThanOrEqualAny_1_T1 = typing.TypeVar('GreaterThanOrEqualAny_1_T1')
        class GreaterThanOrEqualAny_1(typing.Generic[GreaterThanOrEqualAny_1_T1]):
            GreaterThanOrEqualAny_1_T = Vector_0.GreaterThanOrEqualAny_MethodGroup.GreaterThanOrEqualAny_1_T1
            def __call__(self, left: Vector_1[GreaterThanOrEqualAny_1_T], right: Vector_1[GreaterThanOrEqualAny_1_T]) -> bool:...


    # Skipped LessThan due to it being static, abstract and generic.

    LessThan : LessThan_MethodGroup
    class LessThan_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThan_1_T1]) -> LessThan_1[LessThan_1_T1]: ...

        LessThan_1_T1 = typing.TypeVar('LessThan_1_T1')
        class LessThan_1(typing.Generic[LessThan_1_T1]):
            LessThan_1_T = Vector_0.LessThan_MethodGroup.LessThan_1_T1
            def __call__(self, left: Vector_1[LessThan_1_T], right: Vector_1[LessThan_1_T]) -> Vector_1[LessThan_1_T]:...

        def __call__(self, left: Vector_1[float], right: Vector_1[float]) -> Vector_1[int]:...
        # Method LessThan(left : Vector`1, right : Vector`1) was skipped since it collides with above method
        # Method LessThan(left : Vector`1, right : Vector`1) was skipped since it collides with above method
        # Method LessThan(left : Vector`1, right : Vector`1) was skipped since it collides with above method

    # Skipped LessThanAll due to it being static, abstract and generic.

    LessThanAll : LessThanAll_MethodGroup
    class LessThanAll_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanAll_1_T1]) -> LessThanAll_1[LessThanAll_1_T1]: ...

        LessThanAll_1_T1 = typing.TypeVar('LessThanAll_1_T1')
        class LessThanAll_1(typing.Generic[LessThanAll_1_T1]):
            LessThanAll_1_T = Vector_0.LessThanAll_MethodGroup.LessThanAll_1_T1
            def __call__(self, left: Vector_1[LessThanAll_1_T], right: Vector_1[LessThanAll_1_T]) -> bool:...


    # Skipped LessThanAny due to it being static, abstract and generic.

    LessThanAny : LessThanAny_MethodGroup
    class LessThanAny_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanAny_1_T1]) -> LessThanAny_1[LessThanAny_1_T1]: ...

        LessThanAny_1_T1 = typing.TypeVar('LessThanAny_1_T1')
        class LessThanAny_1(typing.Generic[LessThanAny_1_T1]):
            LessThanAny_1_T = Vector_0.LessThanAny_MethodGroup.LessThanAny_1_T1
            def __call__(self, left: Vector_1[LessThanAny_1_T], right: Vector_1[LessThanAny_1_T]) -> bool:...


    # Skipped LessThanOrEqual due to it being static, abstract and generic.

    LessThanOrEqual : LessThanOrEqual_MethodGroup
    class LessThanOrEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanOrEqual_1_T1]) -> LessThanOrEqual_1[LessThanOrEqual_1_T1]: ...

        LessThanOrEqual_1_T1 = typing.TypeVar('LessThanOrEqual_1_T1')
        class LessThanOrEqual_1(typing.Generic[LessThanOrEqual_1_T1]):
            LessThanOrEqual_1_T = Vector_0.LessThanOrEqual_MethodGroup.LessThanOrEqual_1_T1
            def __call__(self, left: Vector_1[LessThanOrEqual_1_T], right: Vector_1[LessThanOrEqual_1_T]) -> Vector_1[LessThanOrEqual_1_T]:...

        def __call__(self, left: Vector_1[float], right: Vector_1[float]) -> Vector_1[int]:...
        # Method LessThanOrEqual(left : Vector`1, right : Vector`1) was skipped since it collides with above method
        # Method LessThanOrEqual(left : Vector`1, right : Vector`1) was skipped since it collides with above method
        # Method LessThanOrEqual(left : Vector`1, right : Vector`1) was skipped since it collides with above method

    # Skipped LessThanOrEqualAll due to it being static, abstract and generic.

    LessThanOrEqualAll : LessThanOrEqualAll_MethodGroup
    class LessThanOrEqualAll_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanOrEqualAll_1_T1]) -> LessThanOrEqualAll_1[LessThanOrEqualAll_1_T1]: ...

        LessThanOrEqualAll_1_T1 = typing.TypeVar('LessThanOrEqualAll_1_T1')
        class LessThanOrEqualAll_1(typing.Generic[LessThanOrEqualAll_1_T1]):
            LessThanOrEqualAll_1_T = Vector_0.LessThanOrEqualAll_MethodGroup.LessThanOrEqualAll_1_T1
            def __call__(self, left: Vector_1[LessThanOrEqualAll_1_T], right: Vector_1[LessThanOrEqualAll_1_T]) -> bool:...


    # Skipped LessThanOrEqualAny due to it being static, abstract and generic.

    LessThanOrEqualAny : LessThanOrEqualAny_MethodGroup
    class LessThanOrEqualAny_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanOrEqualAny_1_T1]) -> LessThanOrEqualAny_1[LessThanOrEqualAny_1_T1]: ...

        LessThanOrEqualAny_1_T1 = typing.TypeVar('LessThanOrEqualAny_1_T1')
        class LessThanOrEqualAny_1(typing.Generic[LessThanOrEqualAny_1_T1]):
            LessThanOrEqualAny_1_T = Vector_0.LessThanOrEqualAny_MethodGroup.LessThanOrEqualAny_1_T1
            def __call__(self, left: Vector_1[LessThanOrEqualAny_1_T], right: Vector_1[LessThanOrEqualAny_1_T]) -> bool:...


    # Skipped Load due to it being static, abstract and generic.

    Load : Load_MethodGroup
    class Load_MethodGroup:
        def __getitem__(self, t:typing.Type[Load_1_T1]) -> Load_1[Load_1_T1]: ...

        Load_1_T1 = typing.TypeVar('Load_1_T1')
        class Load_1(typing.Generic[Load_1_T1]):
            Load_1_T = Vector_0.Load_MethodGroup.Load_1_T1
            def __call__(self, source: clr.Reference[Load_1_T]) -> Vector_1[Load_1_T]:...


    # Skipped LoadAligned due to it being static, abstract and generic.

    LoadAligned : LoadAligned_MethodGroup
    class LoadAligned_MethodGroup:
        def __getitem__(self, t:typing.Type[LoadAligned_1_T1]) -> LoadAligned_1[LoadAligned_1_T1]: ...

        LoadAligned_1_T1 = typing.TypeVar('LoadAligned_1_T1')
        class LoadAligned_1(typing.Generic[LoadAligned_1_T1]):
            LoadAligned_1_T = Vector_0.LoadAligned_MethodGroup.LoadAligned_1_T1
            def __call__(self, source: clr.Reference[LoadAligned_1_T]) -> Vector_1[LoadAligned_1_T]:...


    # Skipped LoadAlignedNonTemporal due to it being static, abstract and generic.

    LoadAlignedNonTemporal : LoadAlignedNonTemporal_MethodGroup
    class LoadAlignedNonTemporal_MethodGroup:
        def __getitem__(self, t:typing.Type[LoadAlignedNonTemporal_1_T1]) -> LoadAlignedNonTemporal_1[LoadAlignedNonTemporal_1_T1]: ...

        LoadAlignedNonTemporal_1_T1 = typing.TypeVar('LoadAlignedNonTemporal_1_T1')
        class LoadAlignedNonTemporal_1(typing.Generic[LoadAlignedNonTemporal_1_T1]):
            LoadAlignedNonTemporal_1_T = Vector_0.LoadAlignedNonTemporal_MethodGroup.LoadAlignedNonTemporal_1_T1
            def __call__(self, source: clr.Reference[LoadAlignedNonTemporal_1_T]) -> Vector_1[LoadAlignedNonTemporal_1_T]:...


    # Skipped LoadUnsafe due to it being static, abstract and generic.

    LoadUnsafe : LoadUnsafe_MethodGroup
    class LoadUnsafe_MethodGroup:
        def __getitem__(self, t:typing.Type[LoadUnsafe_1_T1]) -> LoadUnsafe_1[LoadUnsafe_1_T1]: ...

        LoadUnsafe_1_T1 = typing.TypeVar('LoadUnsafe_1_T1')
        class LoadUnsafe_1(typing.Generic[LoadUnsafe_1_T1]):
            LoadUnsafe_1_T = Vector_0.LoadUnsafe_MethodGroup.LoadUnsafe_1_T1
            @typing.overload
            def __call__(self, source: typing.Optional[clr.Reference[LoadUnsafe_1_T]]) -> Vector_1[LoadUnsafe_1_T]:...
            @typing.overload
            def __call__(self, source: typing.Optional[clr.Reference[LoadUnsafe_1_T]], elementOffset: UIntPtr) -> Vector_1[LoadUnsafe_1_T]:...


    # Skipped Max due to it being static, abstract and generic.

    Max : Max_MethodGroup
    class Max_MethodGroup:
        def __getitem__(self, t:typing.Type[Max_1_T1]) -> Max_1[Max_1_T1]: ...

        Max_1_T1 = typing.TypeVar('Max_1_T1')
        class Max_1(typing.Generic[Max_1_T1]):
            Max_1_T = Vector_0.Max_MethodGroup.Max_1_T1
            def __call__(self, left: Vector_1[Max_1_T], right: Vector_1[Max_1_T]) -> Vector_1[Max_1_T]:...


    # Skipped Min due to it being static, abstract and generic.

    Min : Min_MethodGroup
    class Min_MethodGroup:
        def __getitem__(self, t:typing.Type[Min_1_T1]) -> Min_1[Min_1_T1]: ...

        Min_1_T1 = typing.TypeVar('Min_1_T1')
        class Min_1(typing.Generic[Min_1_T1]):
            Min_1_T = Vector_0.Min_MethodGroup.Min_1_T1
            def __call__(self, left: Vector_1[Min_1_T], right: Vector_1[Min_1_T]) -> Vector_1[Min_1_T]:...


    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        def __getitem__(self, t:typing.Type[Multiply_1_T1]) -> Multiply_1[Multiply_1_T1]: ...

        Multiply_1_T1 = typing.TypeVar('Multiply_1_T1')
        class Multiply_1(typing.Generic[Multiply_1_T1]):
            Multiply_1_T = Vector_0.Multiply_MethodGroup.Multiply_1_T1
            @typing.overload
            def __call__(self, left: Vector_1[Multiply_1_T], right: Vector_1[Multiply_1_T]) -> Vector_1[Multiply_1_T]:...
            @typing.overload
            def __call__(self, left: Vector_1[Multiply_1_T], right: typing.Optional[Multiply_1_T]) -> Vector_1[Multiply_1_T]:...
            @typing.overload
            def __call__(self, left: typing.Optional[Multiply_1_T], right: Vector_1[Multiply_1_T]) -> Vector_1[Multiply_1_T]:...


    # Skipped Narrow due to it being static, abstract and generic.

    Narrow : Narrow_MethodGroup
    class Narrow_MethodGroup:
        def __call__(self, low: Vector_1[float], high: Vector_1[float]) -> Vector_1[float]:...
        # Method Narrow(low : Vector`1, high : Vector`1) was skipped since it collides with above method
        # Method Narrow(low : Vector`1, high : Vector`1) was skipped since it collides with above method
        # Method Narrow(low : Vector`1, high : Vector`1) was skipped since it collides with above method
        # Method Narrow(low : Vector`1, high : Vector`1) was skipped since it collides with above method
        # Method Narrow(low : Vector`1, high : Vector`1) was skipped since it collides with above method
        # Method Narrow(low : Vector`1, high : Vector`1) was skipped since it collides with above method

    # Skipped Negate due to it being static, abstract and generic.

    Negate : Negate_MethodGroup
    class Negate_MethodGroup:
        def __getitem__(self, t:typing.Type[Negate_1_T1]) -> Negate_1[Negate_1_T1]: ...

        Negate_1_T1 = typing.TypeVar('Negate_1_T1')
        class Negate_1(typing.Generic[Negate_1_T1]):
            Negate_1_T = Vector_0.Negate_MethodGroup.Negate_1_T1
            def __call__(self, value: Vector_1[Negate_1_T]) -> Vector_1[Negate_1_T]:...


    # Skipped OnesComplement due to it being static, abstract and generic.

    OnesComplement : OnesComplement_MethodGroup
    class OnesComplement_MethodGroup:
        def __getitem__(self, t:typing.Type[OnesComplement_1_T1]) -> OnesComplement_1[OnesComplement_1_T1]: ...

        OnesComplement_1_T1 = typing.TypeVar('OnesComplement_1_T1')
        class OnesComplement_1(typing.Generic[OnesComplement_1_T1]):
            OnesComplement_1_T = Vector_0.OnesComplement_MethodGroup.OnesComplement_1_T1
            def __call__(self, value: Vector_1[OnesComplement_1_T]) -> Vector_1[OnesComplement_1_T]:...


    # Skipped ShiftLeft due to it being static, abstract and generic.

    ShiftLeft : ShiftLeft_MethodGroup
    class ShiftLeft_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector_1[int], shiftCount: int) -> Vector_1[int]:...
        # Method ShiftLeft(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector_1[UIntPtr], shiftCount: int) -> Vector_1[UIntPtr]:...

    # Skipped ShiftRightArithmetic due to it being static, abstract and generic.

    ShiftRightArithmetic : ShiftRightArithmetic_MethodGroup
    class ShiftRightArithmetic_MethodGroup:
        def __call__(self, value: Vector_1[int], shiftCount: int) -> Vector_1[int]:...
        # Method ShiftRightArithmetic(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method

    # Skipped ShiftRightLogical due to it being static, abstract and generic.

    ShiftRightLogical : ShiftRightLogical_MethodGroup
    class ShiftRightLogical_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector_1[int], shiftCount: int) -> Vector_1[int]:...
        # Method ShiftRightLogical(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector`1, shiftCount : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector_1[UIntPtr], shiftCount: int) -> Vector_1[UIntPtr]:...

    # Skipped SquareRoot due to it being static, abstract and generic.

    SquareRoot : SquareRoot_MethodGroup
    class SquareRoot_MethodGroup:
        def __getitem__(self, t:typing.Type[SquareRoot_1_T1]) -> SquareRoot_1[SquareRoot_1_T1]: ...

        SquareRoot_1_T1 = typing.TypeVar('SquareRoot_1_T1')
        class SquareRoot_1(typing.Generic[SquareRoot_1_T1]):
            SquareRoot_1_T = Vector_0.SquareRoot_MethodGroup.SquareRoot_1_T1
            def __call__(self, value: Vector_1[SquareRoot_1_T]) -> Vector_1[SquareRoot_1_T]:...


    # Skipped Store due to it being static, abstract and generic.

    Store : Store_MethodGroup
    class Store_MethodGroup:
        def __getitem__(self, t:typing.Type[Store_1_T1]) -> Store_1[Store_1_T1]: ...

        Store_1_T1 = typing.TypeVar('Store_1_T1')
        class Store_1(typing.Generic[Store_1_T1]):
            Store_1_T = Vector_0.Store_MethodGroup.Store_1_T1
            def __call__(self, source: Vector_1[Store_1_T], destination: clr.Reference[Store_1_T]) -> None:...


    # Skipped StoreAligned due to it being static, abstract and generic.

    StoreAligned : StoreAligned_MethodGroup
    class StoreAligned_MethodGroup:
        def __getitem__(self, t:typing.Type[StoreAligned_1_T1]) -> StoreAligned_1[StoreAligned_1_T1]: ...

        StoreAligned_1_T1 = typing.TypeVar('StoreAligned_1_T1')
        class StoreAligned_1(typing.Generic[StoreAligned_1_T1]):
            StoreAligned_1_T = Vector_0.StoreAligned_MethodGroup.StoreAligned_1_T1
            def __call__(self, source: Vector_1[StoreAligned_1_T], destination: clr.Reference[StoreAligned_1_T]) -> None:...


    # Skipped StoreAlignedNonTemporal due to it being static, abstract and generic.

    StoreAlignedNonTemporal : StoreAlignedNonTemporal_MethodGroup
    class StoreAlignedNonTemporal_MethodGroup:
        def __getitem__(self, t:typing.Type[StoreAlignedNonTemporal_1_T1]) -> StoreAlignedNonTemporal_1[StoreAlignedNonTemporal_1_T1]: ...

        StoreAlignedNonTemporal_1_T1 = typing.TypeVar('StoreAlignedNonTemporal_1_T1')
        class StoreAlignedNonTemporal_1(typing.Generic[StoreAlignedNonTemporal_1_T1]):
            StoreAlignedNonTemporal_1_T = Vector_0.StoreAlignedNonTemporal_MethodGroup.StoreAlignedNonTemporal_1_T1
            def __call__(self, source: Vector_1[StoreAlignedNonTemporal_1_T], destination: clr.Reference[StoreAlignedNonTemporal_1_T]) -> None:...


    # Skipped StoreUnsafe due to it being static, abstract and generic.

    StoreUnsafe : StoreUnsafe_MethodGroup
    class StoreUnsafe_MethodGroup:
        def __getitem__(self, t:typing.Type[StoreUnsafe_1_T1]) -> StoreUnsafe_1[StoreUnsafe_1_T1]: ...

        StoreUnsafe_1_T1 = typing.TypeVar('StoreUnsafe_1_T1')
        class StoreUnsafe_1(typing.Generic[StoreUnsafe_1_T1]):
            StoreUnsafe_1_T = Vector_0.StoreUnsafe_MethodGroup.StoreUnsafe_1_T1
            @typing.overload
            def __call__(self, source: Vector_1[StoreUnsafe_1_T], destination: typing.Optional[clr.Reference[StoreUnsafe_1_T]]) -> None:...
            @typing.overload
            def __call__(self, source: Vector_1[StoreUnsafe_1_T], destination: typing.Optional[clr.Reference[StoreUnsafe_1_T]], elementOffset: UIntPtr) -> None:...


    # Skipped Subtract due to it being static, abstract and generic.

    Subtract : Subtract_MethodGroup
    class Subtract_MethodGroup:
        def __getitem__(self, t:typing.Type[Subtract_1_T1]) -> Subtract_1[Subtract_1_T1]: ...

        Subtract_1_T1 = typing.TypeVar('Subtract_1_T1')
        class Subtract_1(typing.Generic[Subtract_1_T1]):
            Subtract_1_T = Vector_0.Subtract_MethodGroup.Subtract_1_T1
            def __call__(self, left: Vector_1[Subtract_1_T], right: Vector_1[Subtract_1_T]) -> Vector_1[Subtract_1_T]:...


    # Skipped Sum due to it being static, abstract and generic.

    Sum : Sum_MethodGroup
    class Sum_MethodGroup:
        def __getitem__(self, t:typing.Type[Sum_1_T1]) -> Sum_1[Sum_1_T1]: ...

        Sum_1_T1 = typing.TypeVar('Sum_1_T1')
        class Sum_1(typing.Generic[Sum_1_T1]):
            Sum_1_T = Vector_0.Sum_MethodGroup.Sum_1_T1
            def __call__(self, value: Vector_1[Sum_1_T]) -> Sum_1_T:...


    # Skipped ToScalar due to it being static, abstract and generic.

    ToScalar : ToScalar_MethodGroup
    class ToScalar_MethodGroup:
        def __getitem__(self, t:typing.Type[ToScalar_1_T1]) -> ToScalar_1[ToScalar_1_T1]: ...

        ToScalar_1_T1 = typing.TypeVar('ToScalar_1_T1')
        class ToScalar_1(typing.Generic[ToScalar_1_T1]):
            ToScalar_1_T = Vector_0.ToScalar_MethodGroup.ToScalar_1_T1
            def __call__(self, vector: Vector_1[ToScalar_1_T]) -> ToScalar_1_T:...


    # Skipped Widen due to it being static, abstract and generic.

    Widen : Widen_MethodGroup
    class Widen_MethodGroup:
        def __call__(self, source: Vector_1[float], low: clr.Reference[Vector_1[float]], high: clr.Reference[Vector_1[float]]) -> None:...
        # Method Widen(source : Vector`1, low : Vector`1&, high : Vector`1&) was skipped since it collides with above method
        # Method Widen(source : Vector`1, low : Vector`1&, high : Vector`1&) was skipped since it collides with above method
        # Method Widen(source : Vector`1, low : Vector`1&, high : Vector`1&) was skipped since it collides with above method
        # Method Widen(source : Vector`1, low : Vector`1&, high : Vector`1&) was skipped since it collides with above method
        # Method Widen(source : Vector`1, low : Vector`1&, high : Vector`1&) was skipped since it collides with above method
        # Method Widen(source : Vector`1, low : Vector`1&, high : Vector`1&) was skipped since it collides with above method

    # Skipped WidenLower due to it being static, abstract and generic.

    WidenLower : WidenLower_MethodGroup
    class WidenLower_MethodGroup:
        def __call__(self, source: Vector_1[float]) -> Vector_1[float]:...
        # Method WidenLower(source : Vector`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector`1) was skipped since it collides with above method

    # Skipped WidenUpper due to it being static, abstract and generic.

    WidenUpper : WidenUpper_MethodGroup
    class WidenUpper_MethodGroup:
        def __call__(self, source: Vector_1[float]) -> Vector_1[float]:...
        # Method WidenUpper(source : Vector`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector`1) was skipped since it collides with above method

    # Skipped WithElement due to it being static, abstract and generic.

    WithElement : WithElement_MethodGroup
    class WithElement_MethodGroup:
        def __getitem__(self, t:typing.Type[WithElement_1_T1]) -> WithElement_1[WithElement_1_T1]: ...

        WithElement_1_T1 = typing.TypeVar('WithElement_1_T1')
        class WithElement_1(typing.Generic[WithElement_1_T1]):
            WithElement_1_T = Vector_0.WithElement_MethodGroup.WithElement_1_T1
            def __call__(self, vector: Vector_1[WithElement_1_T], index: int, value: typing.Optional[WithElement_1_T]) -> Vector_1[WithElement_1_T]:...


    # Skipped Xor due to it being static, abstract and generic.

    Xor : Xor_MethodGroup
    class Xor_MethodGroup:
        def __getitem__(self, t:typing.Type[Xor_1_T1]) -> Xor_1[Xor_1_T1]: ...

        Xor_1_T1 = typing.TypeVar('Xor_1_T1')
        class Xor_1(typing.Generic[Xor_1_T1]):
            Xor_1_T = Vector_0.Xor_MethodGroup.Xor_1_T1
            def __call__(self, left: Vector_1[Xor_1_T], right: Vector_1[Xor_1_T]) -> Vector_1[Xor_1_T]:...




Vector_1_T = typing.TypeVar('Vector_1_T')
class Vector_1(typing.Generic[Vector_1_T], IFormattable, IEquatable_1[Vector_1[Vector_1_T]]):
    @typing.overload
    def __init__(self, value: Vector_1_T) -> None: ...
    @typing.overload
    def __init__(self, values: Array_1[Vector_1_T]) -> None: ...
    @typing.overload
    def __init__(self, values: ReadOnlySpan_1[Vector_1_T]) -> None: ...
    @typing.overload
    def __init__(self, values: ReadOnlySpan_1[int]) -> None: ...
    @typing.overload
    def __init__(self, values: Span_1[Vector_1_T]) -> None: ...
    @typing.overload
    def __init__(self, values: Array_1[Vector_1_T], index: int) -> None: ...
    @classmethod
    @property
    def AllBitsSet(cls) -> Vector_1[Vector_1_T]: ...
    @classmethod
    @property
    def Count(cls) -> int: ...
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @property
    def Item(self) -> typing.Optional[Vector_1_T]: ...
    @classmethod
    @property
    def One(cls) -> Vector_1[Vector_1_T]: ...
    @classmethod
    @property
    def Zero(cls) -> Vector_1[Vector_1_T]: ...
    def GetHashCode(self) -> int: ...
    def __add__(self, left: Vector_1[Vector_1_T], right: Vector_1[Vector_1_T]) -> Vector_1[Vector_1_T]: ...
    def __and__(self, left: Vector_1[Vector_1_T], right: Vector_1[Vector_1_T]) -> Vector_1[Vector_1_T]: ...
    def __or__(self, left: Vector_1[Vector_1_T], right: Vector_1[Vector_1_T]) -> Vector_1[Vector_1_T]: ...
    @typing.overload
    def __truediv__(self, left: Vector_1[Vector_1_T], right: Vector_1[Vector_1_T]) -> Vector_1[Vector_1_T]: ...
    @typing.overload
    def __truediv__(self, left: Vector_1[Vector_1_T], right: typing.Optional[Vector_1_T]) -> Vector_1[Vector_1_T]: ...
    def __eq__(self, left: Vector_1[Vector_1_T], right: Vector_1[Vector_1_T]) -> bool: ...
    def __xor__(self, left: Vector_1[Vector_1_T], right: Vector_1[Vector_1_T]) -> Vector_1[Vector_1_T]: ...
    # Operator not supported op_Explicit(value: Vector`1)
    # Operator not supported op_Explicit(value: Vector`1)
    # Operator not supported op_Explicit(value: Vector`1)
    # Operator not supported op_Explicit(value: Vector`1)
    # Operator not supported op_Explicit(value: Vector`1)
    # Operator not supported op_Explicit(value: Vector`1)
    # Operator not supported op_Explicit(value: Vector`1)
    # Operator not supported op_Explicit(value: Vector`1)
    # Operator not supported op_Explicit(value: Vector`1)
    # Operator not supported op_Explicit(value: Vector`1)
    # Operator not supported op_Explicit(value: Vector`1)
    # Operator not supported op_Explicit(value: Vector`1)
    def __ne__(self, left: Vector_1[Vector_1_T], right: Vector_1[Vector_1_T]) -> bool: ...
    def __lshift__(self, value: Vector_1[Vector_1_T], shiftCount: int) -> Vector_1[Vector_1_T]: ...
    @typing.overload
    def __mul__(self, left: Vector_1[Vector_1_T], right: Vector_1[Vector_1_T]) -> Vector_1[Vector_1_T]: ...
    @typing.overload
    def __mul__(self, value: Vector_1[Vector_1_T], factor: typing.Optional[Vector_1_T]) -> Vector_1[Vector_1_T]: ...
    @typing.overload
    def __mul__(self, factor: typing.Optional[Vector_1_T], value: Vector_1[Vector_1_T]) -> Vector_1[Vector_1_T]: ...
    def __invert__(self, value: Vector_1[Vector_1_T]) -> Vector_1[Vector_1_T]: ...
    def __rshift__(self, value: Vector_1[Vector_1_T], shiftCount: int) -> Vector_1[Vector_1_T]: ...
    def __sub__(self, left: Vector_1[Vector_1_T], right: Vector_1[Vector_1_T]) -> Vector_1[Vector_1_T]: ...
    def __neg__(self, value: Vector_1[Vector_1_T]) -> Vector_1[Vector_1_T]: ...
    def __pos__(self, value: Vector_1[Vector_1_T]) -> Vector_1[Vector_1_T]: ...
    # Operator not supported op_UnsignedRightShift(value: Vector`1, shiftCount: Int32)
    # Skipped CopyTo due to it being static, abstract and generic.

    CopyTo : CopyTo_MethodGroup[Vector_1_T]
    CopyTo_MethodGroup_Vector_1_T = typing.TypeVar('CopyTo_MethodGroup_Vector_1_T')
    class CopyTo_MethodGroup(typing.Generic[CopyTo_MethodGroup_Vector_1_T]):
        CopyTo_MethodGroup_Vector_1_T = Vector_1.CopyTo_MethodGroup_Vector_1_T
        @typing.overload
        def __call__(self, destination: Array_1[CopyTo_MethodGroup_Vector_1_T]) -> None:...
        @typing.overload
        def __call__(self, destination: Span_1[int]) -> None:...
        @typing.overload
        def __call__(self, destination: Span_1[CopyTo_MethodGroup_Vector_1_T]) -> None:...
        @typing.overload
        def __call__(self, destination: Array_1[CopyTo_MethodGroup_Vector_1_T], startIndex: int) -> None:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[Vector_1_T]
    Equals_MethodGroup_Vector_1_T = typing.TypeVar('Equals_MethodGroup_Vector_1_T')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_Vector_1_T]):
        Equals_MethodGroup_Vector_1_T = Vector_1.Equals_MethodGroup_Vector_1_T
        @typing.overload
        def __call__(self, other: Vector_1[Equals_MethodGroup_Vector_1_T]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Optional[typing.Any]) -> bool:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup[Vector_1_T]
    ToString_MethodGroup_Vector_1_T = typing.TypeVar('ToString_MethodGroup_Vector_1_T')
    class ToString_MethodGroup(typing.Generic[ToString_MethodGroup_Vector_1_T]):
        ToString_MethodGroup_Vector_1_T = Vector_1.ToString_MethodGroup_Vector_1_T
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: typing.Optional[str]) -> str:...
        @typing.overload
        def __call__(self, format: typing.Optional[str], formatProvider: typing.Optional[IFormatProvider]) -> str:...

    # Skipped TryCopyTo due to it being static, abstract and generic.

    TryCopyTo : TryCopyTo_MethodGroup[Vector_1_T]
    TryCopyTo_MethodGroup_Vector_1_T = typing.TypeVar('TryCopyTo_MethodGroup_Vector_1_T')
    class TryCopyTo_MethodGroup(typing.Generic[TryCopyTo_MethodGroup_Vector_1_T]):
        TryCopyTo_MethodGroup_Vector_1_T = Vector_1.TryCopyTo_MethodGroup_Vector_1_T
        @typing.overload
        def __call__(self, destination: Span_1[int]) -> bool:...
        @typing.overload
        def __call__(self, destination: Span_1[TryCopyTo_MethodGroup_Vector_1_T]) -> bool:...



class Vector2(IFormattable, IEquatable_1[Vector2]):
    @typing.overload
    def __init__(self, value: float) -> None: ...
    @typing.overload
    def __init__(self, values: ReadOnlySpan_1[float]) -> None: ...
    @typing.overload
    def __init__(self, x: float, y: float) -> None: ...
    X : float
    Y : float
    @property
    def Item(self) -> float: ...
    @Item.setter
    def Item(self, value: float) -> float: ...
    @classmethod
    @property
    def One(cls) -> Vector2: ...
    @classmethod
    @property
    def UnitX(cls) -> Vector2: ...
    @classmethod
    @property
    def UnitY(cls) -> Vector2: ...
    @classmethod
    @property
    def Zero(cls) -> Vector2: ...
    @staticmethod
    def Abs(value: Vector2) -> Vector2: ...
    @staticmethod
    def Add(left: Vector2, right: Vector2) -> Vector2: ...
    @staticmethod
    def Clamp(value1: Vector2, min: Vector2, max: Vector2) -> Vector2: ...
    @staticmethod
    def Distance(value1: Vector2, value2: Vector2) -> float: ...
    @staticmethod
    def DistanceSquared(value1: Vector2, value2: Vector2) -> float: ...
    @staticmethod
    def Dot(value1: Vector2, value2: Vector2) -> float: ...
    def GetHashCode(self) -> int: ...
    def Length(self) -> float: ...
    def LengthSquared(self) -> float: ...
    @staticmethod
    def Lerp(value1: Vector2, value2: Vector2, amount: float) -> Vector2: ...
    @staticmethod
    def Max(value1: Vector2, value2: Vector2) -> Vector2: ...
    @staticmethod
    def Min(value1: Vector2, value2: Vector2) -> Vector2: ...
    @staticmethod
    def Negate(value: Vector2) -> Vector2: ...
    @staticmethod
    def Normalize(value: Vector2) -> Vector2: ...
    def __add__(self, left: Vector2, right: Vector2) -> Vector2: ...
    @typing.overload
    def __truediv__(self, value1: Vector2, value2: float) -> Vector2: ...
    @typing.overload
    def __truediv__(self, left: Vector2, right: Vector2) -> Vector2: ...
    def __eq__(self, left: Vector2, right: Vector2) -> bool: ...
    def __ne__(self, left: Vector2, right: Vector2) -> bool: ...
    @typing.overload
    def __mul__(self, left: float, right: Vector2) -> Vector2: ...
    @typing.overload
    def __mul__(self, left: Vector2, right: float) -> Vector2: ...
    @typing.overload
    def __mul__(self, left: Vector2, right: Vector2) -> Vector2: ...
    def __sub__(self, left: Vector2, right: Vector2) -> Vector2: ...
    def __neg__(self, value: Vector2) -> Vector2: ...
    @staticmethod
    def Reflect(vector: Vector2, normal: Vector2) -> Vector2: ...
    @staticmethod
    def SquareRoot(value: Vector2) -> Vector2: ...
    @staticmethod
    def Subtract(left: Vector2, right: Vector2) -> Vector2: ...
    def TryCopyTo(self, destination: Span_1[float]) -> bool: ...
    # Skipped CopyTo due to it being static, abstract and generic.

    CopyTo : CopyTo_MethodGroup
    class CopyTo_MethodGroup:
        @typing.overload
        def __call__(self, array: Array_1[float]) -> None:...
        @typing.overload
        def __call__(self, destination: Span_1[float]) -> None:...
        @typing.overload
        def __call__(self, array: Array_1[float], index: int) -> None:...

    # Skipped Divide due to it being static, abstract and generic.

    Divide : Divide_MethodGroup
    class Divide_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector2, divisor: float) -> Vector2:...
        @typing.overload
        def __call__(self, left: Vector2, right: Vector2) -> Vector2:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: Vector2) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Optional[typing.Any]) -> bool:...

    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        @typing.overload
        def __call__(self, left: float, right: Vector2) -> Vector2:...
        @typing.overload
        def __call__(self, left: Vector2, right: float) -> Vector2:...
        @typing.overload
        def __call__(self, left: Vector2, right: Vector2) -> Vector2:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: typing.Optional[str]) -> str:...
        @typing.overload
        def __call__(self, format: typing.Optional[str], formatProvider: typing.Optional[IFormatProvider]) -> str:...

    # Skipped Transform due to it being static, abstract and generic.

    Transform : Transform_MethodGroup
    class Transform_MethodGroup:
        @typing.overload
        def __call__(self, position: Vector2, matrix: Matrix3x2) -> Vector2:...
        @typing.overload
        def __call__(self, position: Vector2, matrix: Matrix4x4) -> Vector2:...
        @typing.overload
        def __call__(self, value: Vector2, rotation: Quaternion) -> Vector2:...

    # Skipped TransformNormal due to it being static, abstract and generic.

    TransformNormal : TransformNormal_MethodGroup
    class TransformNormal_MethodGroup:
        @typing.overload
        def __call__(self, normal: Vector2, matrix: Matrix3x2) -> Vector2:...
        @typing.overload
        def __call__(self, normal: Vector2, matrix: Matrix4x4) -> Vector2:...



class Vector3(IFormattable, IEquatable_1[Vector3]):
    @typing.overload
    def __init__(self, value: float) -> None: ...
    @typing.overload
    def __init__(self, value: Vector2, z: float) -> None: ...
    @typing.overload
    def __init__(self, values: ReadOnlySpan_1[float]) -> None: ...
    @typing.overload
    def __init__(self, x: float, y: float, z: float) -> None: ...
    X : float
    Y : float
    Z : float
    @property
    def Item(self) -> float: ...
    @Item.setter
    def Item(self, value: float) -> float: ...
    @classmethod
    @property
    def One(cls) -> Vector3: ...
    @classmethod
    @property
    def UnitX(cls) -> Vector3: ...
    @classmethod
    @property
    def UnitY(cls) -> Vector3: ...
    @classmethod
    @property
    def UnitZ(cls) -> Vector3: ...
    @classmethod
    @property
    def Zero(cls) -> Vector3: ...
    @staticmethod
    def Abs(value: Vector3) -> Vector3: ...
    @staticmethod
    def Add(left: Vector3, right: Vector3) -> Vector3: ...
    @staticmethod
    def Clamp(value1: Vector3, min: Vector3, max: Vector3) -> Vector3: ...
    @staticmethod
    def Cross(vector1: Vector3, vector2: Vector3) -> Vector3: ...
    @staticmethod
    def Distance(value1: Vector3, value2: Vector3) -> float: ...
    @staticmethod
    def DistanceSquared(value1: Vector3, value2: Vector3) -> float: ...
    @staticmethod
    def Dot(vector1: Vector3, vector2: Vector3) -> float: ...
    def GetHashCode(self) -> int: ...
    def Length(self) -> float: ...
    def LengthSquared(self) -> float: ...
    @staticmethod
    def Lerp(value1: Vector3, value2: Vector3, amount: float) -> Vector3: ...
    @staticmethod
    def Max(value1: Vector3, value2: Vector3) -> Vector3: ...
    @staticmethod
    def Min(value1: Vector3, value2: Vector3) -> Vector3: ...
    @staticmethod
    def Negate(value: Vector3) -> Vector3: ...
    @staticmethod
    def Normalize(value: Vector3) -> Vector3: ...
    def __add__(self, left: Vector3, right: Vector3) -> Vector3: ...
    @typing.overload
    def __truediv__(self, value1: Vector3, value2: float) -> Vector3: ...
    @typing.overload
    def __truediv__(self, left: Vector3, right: Vector3) -> Vector3: ...
    def __eq__(self, left: Vector3, right: Vector3) -> bool: ...
    def __ne__(self, left: Vector3, right: Vector3) -> bool: ...
    @typing.overload
    def __mul__(self, left: float, right: Vector3) -> Vector3: ...
    @typing.overload
    def __mul__(self, left: Vector3, right: float) -> Vector3: ...
    @typing.overload
    def __mul__(self, left: Vector3, right: Vector3) -> Vector3: ...
    def __sub__(self, left: Vector3, right: Vector3) -> Vector3: ...
    def __neg__(self, value: Vector3) -> Vector3: ...
    @staticmethod
    def Reflect(vector: Vector3, normal: Vector3) -> Vector3: ...
    @staticmethod
    def SquareRoot(value: Vector3) -> Vector3: ...
    @staticmethod
    def Subtract(left: Vector3, right: Vector3) -> Vector3: ...
    @staticmethod
    def TransformNormal(normal: Vector3, matrix: Matrix4x4) -> Vector3: ...
    def TryCopyTo(self, destination: Span_1[float]) -> bool: ...
    # Skipped CopyTo due to it being static, abstract and generic.

    CopyTo : CopyTo_MethodGroup
    class CopyTo_MethodGroup:
        @typing.overload
        def __call__(self, array: Array_1[float]) -> None:...
        @typing.overload
        def __call__(self, destination: Span_1[float]) -> None:...
        @typing.overload
        def __call__(self, array: Array_1[float], index: int) -> None:...

    # Skipped Divide due to it being static, abstract and generic.

    Divide : Divide_MethodGroup
    class Divide_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector3, divisor: float) -> Vector3:...
        @typing.overload
        def __call__(self, left: Vector3, right: Vector3) -> Vector3:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: Vector3) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Optional[typing.Any]) -> bool:...

    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        @typing.overload
        def __call__(self, left: float, right: Vector3) -> Vector3:...
        @typing.overload
        def __call__(self, left: Vector3, right: float) -> Vector3:...
        @typing.overload
        def __call__(self, left: Vector3, right: Vector3) -> Vector3:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: typing.Optional[str]) -> str:...
        @typing.overload
        def __call__(self, format: typing.Optional[str], formatProvider: typing.Optional[IFormatProvider]) -> str:...

    # Skipped Transform due to it being static, abstract and generic.

    Transform : Transform_MethodGroup
    class Transform_MethodGroup:
        @typing.overload
        def __call__(self, position: Vector3, matrix: Matrix4x4) -> Vector3:...
        @typing.overload
        def __call__(self, value: Vector3, rotation: Quaternion) -> Vector3:...



class Vector4(IFormattable, IEquatable_1[Vector4]):
    @typing.overload
    def __init__(self, value: float) -> None: ...
    @typing.overload
    def __init__(self, value: Vector3, w: float) -> None: ...
    @typing.overload
    def __init__(self, value: Vector2, z: float, w: float) -> None: ...
    @typing.overload
    def __init__(self, values: ReadOnlySpan_1[float]) -> None: ...
    @typing.overload
    def __init__(self, x: float, y: float, z: float, w: float) -> None: ...
    W : float
    X : float
    Y : float
    Z : float
    @property
    def Item(self) -> float: ...
    @Item.setter
    def Item(self, value: float) -> float: ...
    @classmethod
    @property
    def One(cls) -> Vector4: ...
    @classmethod
    @property
    def UnitW(cls) -> Vector4: ...
    @classmethod
    @property
    def UnitX(cls) -> Vector4: ...
    @classmethod
    @property
    def UnitY(cls) -> Vector4: ...
    @classmethod
    @property
    def UnitZ(cls) -> Vector4: ...
    @classmethod
    @property
    def Zero(cls) -> Vector4: ...
    @staticmethod
    def Abs(value: Vector4) -> Vector4: ...
    @staticmethod
    def Add(left: Vector4, right: Vector4) -> Vector4: ...
    @staticmethod
    def Clamp(value1: Vector4, min: Vector4, max: Vector4) -> Vector4: ...
    @staticmethod
    def Distance(value1: Vector4, value2: Vector4) -> float: ...
    @staticmethod
    def DistanceSquared(value1: Vector4, value2: Vector4) -> float: ...
    @staticmethod
    def Dot(vector1: Vector4, vector2: Vector4) -> float: ...
    def GetHashCode(self) -> int: ...
    def Length(self) -> float: ...
    def LengthSquared(self) -> float: ...
    @staticmethod
    def Lerp(value1: Vector4, value2: Vector4, amount: float) -> Vector4: ...
    @staticmethod
    def Max(value1: Vector4, value2: Vector4) -> Vector4: ...
    @staticmethod
    def Min(value1: Vector4, value2: Vector4) -> Vector4: ...
    @staticmethod
    def Negate(value: Vector4) -> Vector4: ...
    @staticmethod
    def Normalize(vector: Vector4) -> Vector4: ...
    def __add__(self, left: Vector4, right: Vector4) -> Vector4: ...
    @typing.overload
    def __truediv__(self, value1: Vector4, value2: float) -> Vector4: ...
    @typing.overload
    def __truediv__(self, left: Vector4, right: Vector4) -> Vector4: ...
    def __eq__(self, left: Vector4, right: Vector4) -> bool: ...
    def __ne__(self, left: Vector4, right: Vector4) -> bool: ...
    @typing.overload
    def __mul__(self, left: float, right: Vector4) -> Vector4: ...
    @typing.overload
    def __mul__(self, left: Vector4, right: float) -> Vector4: ...
    @typing.overload
    def __mul__(self, left: Vector4, right: Vector4) -> Vector4: ...
    def __sub__(self, left: Vector4, right: Vector4) -> Vector4: ...
    def __neg__(self, value: Vector4) -> Vector4: ...
    @staticmethod
    def SquareRoot(value: Vector4) -> Vector4: ...
    @staticmethod
    def Subtract(left: Vector4, right: Vector4) -> Vector4: ...
    def TryCopyTo(self, destination: Span_1[float]) -> bool: ...
    # Skipped CopyTo due to it being static, abstract and generic.

    CopyTo : CopyTo_MethodGroup
    class CopyTo_MethodGroup:
        @typing.overload
        def __call__(self, array: Array_1[float]) -> None:...
        @typing.overload
        def __call__(self, destination: Span_1[float]) -> None:...
        @typing.overload
        def __call__(self, array: Array_1[float], index: int) -> None:...

    # Skipped Divide due to it being static, abstract and generic.

    Divide : Divide_MethodGroup
    class Divide_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector4, divisor: float) -> Vector4:...
        @typing.overload
        def __call__(self, left: Vector4, right: Vector4) -> Vector4:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: Vector4) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Optional[typing.Any]) -> bool:...

    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        @typing.overload
        def __call__(self, left: float, right: Vector4) -> Vector4:...
        @typing.overload
        def __call__(self, left: Vector4, right: float) -> Vector4:...
        @typing.overload
        def __call__(self, left: Vector4, right: Vector4) -> Vector4:...

    # Skipped ToString due to it being static, abstract and generic.

    ToString : ToString_MethodGroup
    class ToString_MethodGroup:
        @typing.overload
        def __call__(self) -> str:...
        @typing.overload
        def __call__(self, format: typing.Optional[str]) -> str:...
        @typing.overload
        def __call__(self, format: typing.Optional[str], formatProvider: typing.Optional[IFormatProvider]) -> str:...

    # Skipped Transform due to it being static, abstract and generic.

    Transform : Transform_MethodGroup
    class Transform_MethodGroup:
        @typing.overload
        def __call__(self, position: Vector2, matrix: Matrix4x4) -> Vector4:...
        @typing.overload
        def __call__(self, position: Vector3, matrix: Matrix4x4) -> Vector4:...
        @typing.overload
        def __call__(self, value: Vector2, rotation: Quaternion) -> Vector4:...
        @typing.overload
        def __call__(self, value: Vector3, rotation: Quaternion) -> Vector4:...
        @typing.overload
        def __call__(self, value: Vector4, rotation: Quaternion) -> Vector4:...
        @typing.overload
        def __call__(self, vector: Vector4, matrix: Matrix4x4) -> Vector4:...


