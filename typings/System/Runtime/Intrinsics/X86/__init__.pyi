import typing, clr, abc
from System.Runtime.Intrinsics import Vector128_1, Vector256_1, Vector512_1
from System import ValueTuple_4, ValueTuple_2, UIntPtr

class Aes(Sse2):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def Decrypt(value: Vector128_1[int], roundKey: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def DecryptLast(value: Vector128_1[int], roundKey: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def Encrypt(value: Vector128_1[int], roundKey: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def EncryptLast(value: Vector128_1[int], roundKey: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def InverseMixColumns(value: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def KeygenAssist(value: Vector128_1[int], control: int) -> Vector128_1[int]: ...

    class X64(Sse2.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...



class Avx(Sse42):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def BroadcastScalarToVector128(source: clr.Reference[float]) -> Vector128_1[float]: ...
    @staticmethod
    def ConvertToVector128Int32(value: Vector256_1[float]) -> Vector128_1[int]: ...
    @staticmethod
    def ConvertToVector128Int32WithTruncation(value: Vector256_1[float]) -> Vector128_1[int]: ...
    @staticmethod
    def ConvertToVector128Single(value: Vector256_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def ConvertToVector256Int32(value: Vector256_1[float]) -> Vector256_1[int]: ...
    @staticmethod
    def ConvertToVector256Int32WithTruncation(value: Vector256_1[float]) -> Vector256_1[int]: ...
    @staticmethod
    def ConvertToVector256Single(value: Vector256_1[int]) -> Vector256_1[float]: ...
    @staticmethod
    def DotProduct(left: Vector256_1[float], right: Vector256_1[float], control: int) -> Vector256_1[float]: ...
    @staticmethod
    def DuplicateOddIndexed(value: Vector256_1[float]) -> Vector256_1[float]: ...
    @staticmethod
    def Reciprocal(value: Vector256_1[float]) -> Vector256_1[float]: ...
    @staticmethod
    def ReciprocalSqrt(value: Vector256_1[float]) -> Vector256_1[float]: ...
    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method Add(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped AddSubtract due to it being static, abstract and generic.

    AddSubtract : AddSubtract_MethodGroup
    class AddSubtract_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method AddSubtract(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped And due to it being static, abstract and generic.

    And : And_MethodGroup
    class And_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method And(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped AndNot due to it being static, abstract and generic.

    AndNot : AndNot_MethodGroup
    class AndNot_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method AndNot(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped Blend due to it being static, abstract and generic.

    Blend : Blend_MethodGroup
    class Blend_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float], control: int) -> Vector256_1[float]:...
        # Method Blend(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method

    # Skipped BlendVariable due to it being static, abstract and generic.

    BlendVariable : BlendVariable_MethodGroup
    class BlendVariable_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float], mask: Vector256_1[float]) -> Vector256_1[float]:...
        # Method BlendVariable(left : Vector256`1, right : Vector256`1, mask : Vector256`1) was skipped since it collides with above method

    # Skipped BroadcastScalarToVector256 due to it being static, abstract and generic.

    BroadcastScalarToVector256 : BroadcastScalarToVector256_MethodGroup
    class BroadcastScalarToVector256_MethodGroup:
        def __call__(self, source: clr.Reference[float]) -> Vector256_1[float]:...
        # Method BroadcastScalarToVector256(source : Double*) was skipped since it collides with above method

    # Skipped BroadcastVector128ToVector256 due to it being static, abstract and generic.

    BroadcastVector128ToVector256 : BroadcastVector128ToVector256_MethodGroup
    class BroadcastVector128ToVector256_MethodGroup:
        def __call__(self, address: clr.Reference[float]) -> Vector256_1[float]:...
        # Method BroadcastVector128ToVector256(address : Double*) was skipped since it collides with above method

    # Skipped Ceiling due to it being static, abstract and generic.

    Ceiling : Ceiling_MethodGroup
    class Ceiling_MethodGroup:
        def __call__(self, value: Vector256_1[float]) -> Vector256_1[float]:...
        # Method Ceiling(value : Vector256`1) was skipped since it collides with above method

    # Skipped Compare due to it being static, abstract and generic.

    Compare : Compare_MethodGroup
    class Compare_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float], mode: FloatComparisonMode) -> Vector128_1[float]:...
        @typing.overload
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float], mode: FloatComparisonMode) -> Vector256_1[float]:...
        # Method Compare(left : Vector128`1, right : Vector128`1, mode : FloatComparisonMode) was skipped since it collides with above method
        # Method Compare(left : Vector256`1, right : Vector256`1, mode : FloatComparisonMode) was skipped since it collides with above method

    # Skipped CompareEqual due to it being static, abstract and generic.

    CompareEqual : CompareEqual_MethodGroup
    class CompareEqual_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method CompareEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped CompareGreaterThan due to it being static, abstract and generic.

    CompareGreaterThan : CompareGreaterThan_MethodGroup
    class CompareGreaterThan_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method CompareGreaterThan(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped CompareGreaterThanOrEqual due to it being static, abstract and generic.

    CompareGreaterThanOrEqual : CompareGreaterThanOrEqual_MethodGroup
    class CompareGreaterThanOrEqual_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method CompareGreaterThanOrEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped CompareLessThan due to it being static, abstract and generic.

    CompareLessThan : CompareLessThan_MethodGroup
    class CompareLessThan_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method CompareLessThan(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped CompareLessThanOrEqual due to it being static, abstract and generic.

    CompareLessThanOrEqual : CompareLessThanOrEqual_MethodGroup
    class CompareLessThanOrEqual_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method CompareLessThanOrEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped CompareNotEqual due to it being static, abstract and generic.

    CompareNotEqual : CompareNotEqual_MethodGroup
    class CompareNotEqual_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method CompareNotEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped CompareNotGreaterThan due to it being static, abstract and generic.

    CompareNotGreaterThan : CompareNotGreaterThan_MethodGroup
    class CompareNotGreaterThan_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method CompareNotGreaterThan(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped CompareNotGreaterThanOrEqual due to it being static, abstract and generic.

    CompareNotGreaterThanOrEqual : CompareNotGreaterThanOrEqual_MethodGroup
    class CompareNotGreaterThanOrEqual_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method CompareNotGreaterThanOrEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped CompareNotLessThan due to it being static, abstract and generic.

    CompareNotLessThan : CompareNotLessThan_MethodGroup
    class CompareNotLessThan_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method CompareNotLessThan(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped CompareNotLessThanOrEqual due to it being static, abstract and generic.

    CompareNotLessThanOrEqual : CompareNotLessThanOrEqual_MethodGroup
    class CompareNotLessThanOrEqual_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method CompareNotLessThanOrEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped CompareOrdered due to it being static, abstract and generic.

    CompareOrdered : CompareOrdered_MethodGroup
    class CompareOrdered_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method CompareOrdered(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped CompareScalar due to it being static, abstract and generic.

    CompareScalar : CompareScalar_MethodGroup
    class CompareScalar_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float], mode: FloatComparisonMode) -> Vector128_1[float]:...
        # Method CompareScalar(left : Vector128`1, right : Vector128`1, mode : FloatComparisonMode) was skipped since it collides with above method

    # Skipped CompareUnordered due to it being static, abstract and generic.

    CompareUnordered : CompareUnordered_MethodGroup
    class CompareUnordered_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method CompareUnordered(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped ConvertToVector256Double due to it being static, abstract and generic.

    ConvertToVector256Double : ConvertToVector256Double_MethodGroup
    class ConvertToVector256Double_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector256_1[float]:...
        # Method ConvertToVector256Double(value : Vector128`1) was skipped since it collides with above method

    # Skipped Divide due to it being static, abstract and generic.

    Divide : Divide_MethodGroup
    class Divide_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method Divide(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped DuplicateEvenIndexed due to it being static, abstract and generic.

    DuplicateEvenIndexed : DuplicateEvenIndexed_MethodGroup
    class DuplicateEvenIndexed_MethodGroup:
        def __call__(self, value: Vector256_1[float]) -> Vector256_1[float]:...
        # Method DuplicateEvenIndexed(value : Vector256`1) was skipped since it collides with above method

    # Skipped ExtractVector128 due to it being static, abstract and generic.

    ExtractVector128 : ExtractVector128_MethodGroup
    class ExtractVector128_MethodGroup:
        def __call__(self, value: Vector256_1[float], index: int) -> Vector128_1[float]:...
        # Method ExtractVector128(value : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector256`1, index : Byte) was skipped since it collides with above method

    # Skipped Floor due to it being static, abstract and generic.

    Floor : Floor_MethodGroup
    class Floor_MethodGroup:
        def __call__(self, value: Vector256_1[float]) -> Vector256_1[float]:...
        # Method Floor(value : Vector256`1) was skipped since it collides with above method

    # Skipped HorizontalAdd due to it being static, abstract and generic.

    HorizontalAdd : HorizontalAdd_MethodGroup
    class HorizontalAdd_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method HorizontalAdd(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped HorizontalSubtract due to it being static, abstract and generic.

    HorizontalSubtract : HorizontalSubtract_MethodGroup
    class HorizontalSubtract_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method HorizontalSubtract(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped InsertVector128 due to it being static, abstract and generic.

    InsertVector128 : InsertVector128_MethodGroup
    class InsertVector128_MethodGroup:
        def __call__(self, value: Vector256_1[float], data: Vector128_1[float], index: int) -> Vector256_1[float]:...
        # Method InsertVector128(value : Vector256`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector256`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector256`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector256`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector256`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector256`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector256`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector256`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector256`1, data : Vector128`1, index : Byte) was skipped since it collides with above method

    # Skipped LoadAlignedVector256 due to it being static, abstract and generic.

    LoadAlignedVector256 : LoadAlignedVector256_MethodGroup
    class LoadAlignedVector256_MethodGroup:
        def __call__(self, address: clr.Reference[float]) -> Vector256_1[float]:...
        # Method LoadAlignedVector256(address : Double*) was skipped since it collides with above method
        # Method LoadAlignedVector256(address : SByte*) was skipped since it collides with above method
        # Method LoadAlignedVector256(address : Byte*) was skipped since it collides with above method
        # Method LoadAlignedVector256(address : Int16*) was skipped since it collides with above method
        # Method LoadAlignedVector256(address : UInt16*) was skipped since it collides with above method
        # Method LoadAlignedVector256(address : Int32*) was skipped since it collides with above method
        # Method LoadAlignedVector256(address : UInt32*) was skipped since it collides with above method
        # Method LoadAlignedVector256(address : Int64*) was skipped since it collides with above method
        # Method LoadAlignedVector256(address : UInt64*) was skipped since it collides with above method

    # Skipped LoadDquVector256 due to it being static, abstract and generic.

    LoadDquVector256 : LoadDquVector256_MethodGroup
    class LoadDquVector256_MethodGroup:
        def __call__(self, address: clr.Reference[int]) -> Vector256_1[int]:...
        # Method LoadDquVector256(address : Byte*) was skipped since it collides with above method
        # Method LoadDquVector256(address : Int16*) was skipped since it collides with above method
        # Method LoadDquVector256(address : UInt16*) was skipped since it collides with above method
        # Method LoadDquVector256(address : Int32*) was skipped since it collides with above method
        # Method LoadDquVector256(address : UInt32*) was skipped since it collides with above method
        # Method LoadDquVector256(address : Int64*) was skipped since it collides with above method
        # Method LoadDquVector256(address : UInt64*) was skipped since it collides with above method

    # Skipped LoadVector256 due to it being static, abstract and generic.

    LoadVector256 : LoadVector256_MethodGroup
    class LoadVector256_MethodGroup:
        def __call__(self, address: clr.Reference[float]) -> Vector256_1[float]:...
        # Method LoadVector256(address : Double*) was skipped since it collides with above method
        # Method LoadVector256(address : SByte*) was skipped since it collides with above method
        # Method LoadVector256(address : Byte*) was skipped since it collides with above method
        # Method LoadVector256(address : Int16*) was skipped since it collides with above method
        # Method LoadVector256(address : UInt16*) was skipped since it collides with above method
        # Method LoadVector256(address : Int32*) was skipped since it collides with above method
        # Method LoadVector256(address : UInt32*) was skipped since it collides with above method
        # Method LoadVector256(address : Int64*) was skipped since it collides with above method
        # Method LoadVector256(address : UInt64*) was skipped since it collides with above method

    # Skipped MaskLoad due to it being static, abstract and generic.

    MaskLoad : MaskLoad_MethodGroup
    class MaskLoad_MethodGroup:
        @typing.overload
        def __call__(self, address: clr.Reference[float], mask: Vector128_1[float]) -> Vector128_1[float]:...
        # Method MaskLoad(address : Double*, mask : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, address: clr.Reference[float], mask: Vector256_1[float]) -> Vector256_1[float]:...
        # Method MaskLoad(address : Double*, mask : Vector256`1) was skipped since it collides with above method

    # Skipped MaskStore due to it being static, abstract and generic.

    MaskStore : MaskStore_MethodGroup
    class MaskStore_MethodGroup:
        @typing.overload
        def __call__(self, address: clr.Reference[float], mask: Vector128_1[float], source: Vector128_1[float]) -> None:...
        # Method MaskStore(address : Double*, mask : Vector128`1, source : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, address: clr.Reference[float], mask: Vector256_1[float], source: Vector256_1[float]) -> None:...
        # Method MaskStore(address : Double*, mask : Vector256`1, source : Vector256`1) was skipped since it collides with above method

    # Skipped Max due to it being static, abstract and generic.

    Max : Max_MethodGroup
    class Max_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method Max(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped Min due to it being static, abstract and generic.

    Min : Min_MethodGroup
    class Min_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method Min(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped MoveMask due to it being static, abstract and generic.

    MoveMask : MoveMask_MethodGroup
    class MoveMask_MethodGroup:
        def __call__(self, value: Vector256_1[float]) -> int:...
        # Method MoveMask(value : Vector256`1) was skipped since it collides with above method

    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method Multiply(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped Or due to it being static, abstract and generic.

    Or : Or_MethodGroup
    class Or_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method Or(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped Permute due to it being static, abstract and generic.

    Permute : Permute_MethodGroup
    class Permute_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float], control: int) -> Vector128_1[float]:...
        # Method Permute(value : Vector128`1, control : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector256_1[float], control: int) -> Vector256_1[float]:...
        # Method Permute(value : Vector256`1, control : Byte) was skipped since it collides with above method

    # Skipped Permute2x128 due to it being static, abstract and generic.

    Permute2x128 : Permute2x128_MethodGroup
    class Permute2x128_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float], control: int) -> Vector256_1[float]:...
        # Method Permute2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
        # Method Permute2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
        # Method Permute2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
        # Method Permute2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
        # Method Permute2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
        # Method Permute2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
        # Method Permute2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
        # Method Permute2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
        # Method Permute2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method

    # Skipped PermuteVar due to it being static, abstract and generic.

    PermuteVar : PermuteVar_MethodGroup
    class PermuteVar_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], control: Vector128_1[int]) -> Vector128_1[float]:...
        # Method PermuteVar(left : Vector128`1, control : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector256_1[float], control: Vector256_1[int]) -> Vector256_1[float]:...
        # Method PermuteVar(left : Vector256`1, control : Vector256`1) was skipped since it collides with above method

    # Skipped RoundCurrentDirection due to it being static, abstract and generic.

    RoundCurrentDirection : RoundCurrentDirection_MethodGroup
    class RoundCurrentDirection_MethodGroup:
        def __call__(self, value: Vector256_1[float]) -> Vector256_1[float]:...
        # Method RoundCurrentDirection(value : Vector256`1) was skipped since it collides with above method

    # Skipped RoundToNearestInteger due to it being static, abstract and generic.

    RoundToNearestInteger : RoundToNearestInteger_MethodGroup
    class RoundToNearestInteger_MethodGroup:
        def __call__(self, value: Vector256_1[float]) -> Vector256_1[float]:...
        # Method RoundToNearestInteger(value : Vector256`1) was skipped since it collides with above method

    # Skipped RoundToNegativeInfinity due to it being static, abstract and generic.

    RoundToNegativeInfinity : RoundToNegativeInfinity_MethodGroup
    class RoundToNegativeInfinity_MethodGroup:
        def __call__(self, value: Vector256_1[float]) -> Vector256_1[float]:...
        # Method RoundToNegativeInfinity(value : Vector256`1) was skipped since it collides with above method

    # Skipped RoundToPositiveInfinity due to it being static, abstract and generic.

    RoundToPositiveInfinity : RoundToPositiveInfinity_MethodGroup
    class RoundToPositiveInfinity_MethodGroup:
        def __call__(self, value: Vector256_1[float]) -> Vector256_1[float]:...
        # Method RoundToPositiveInfinity(value : Vector256`1) was skipped since it collides with above method

    # Skipped RoundToZero due to it being static, abstract and generic.

    RoundToZero : RoundToZero_MethodGroup
    class RoundToZero_MethodGroup:
        def __call__(self, value: Vector256_1[float]) -> Vector256_1[float]:...
        # Method RoundToZero(value : Vector256`1) was skipped since it collides with above method

    # Skipped Shuffle due to it being static, abstract and generic.

    Shuffle : Shuffle_MethodGroup
    class Shuffle_MethodGroup:
        def __call__(self, value: Vector256_1[float], right: Vector256_1[float], control: int) -> Vector256_1[float]:...
        # Method Shuffle(value : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method

    # Skipped Sqrt due to it being static, abstract and generic.

    Sqrt : Sqrt_MethodGroup
    class Sqrt_MethodGroup:
        def __call__(self, value: Vector256_1[float]) -> Vector256_1[float]:...
        # Method Sqrt(value : Vector256`1) was skipped since it collides with above method

    # Skipped Store due to it being static, abstract and generic.

    Store : Store_MethodGroup
    class Store_MethodGroup:
        def __call__(self, address: clr.Reference[float], source: Vector256_1[float]) -> None:...
        # Method Store(address : Double*, source : Vector256`1) was skipped since it collides with above method
        # Method Store(address : SByte*, source : Vector256`1) was skipped since it collides with above method
        # Method Store(address : Byte*, source : Vector256`1) was skipped since it collides with above method
        # Method Store(address : Int16*, source : Vector256`1) was skipped since it collides with above method
        # Method Store(address : UInt16*, source : Vector256`1) was skipped since it collides with above method
        # Method Store(address : Int32*, source : Vector256`1) was skipped since it collides with above method
        # Method Store(address : UInt32*, source : Vector256`1) was skipped since it collides with above method
        # Method Store(address : Int64*, source : Vector256`1) was skipped since it collides with above method
        # Method Store(address : UInt64*, source : Vector256`1) was skipped since it collides with above method

    # Skipped StoreAligned due to it being static, abstract and generic.

    StoreAligned : StoreAligned_MethodGroup
    class StoreAligned_MethodGroup:
        def __call__(self, address: clr.Reference[float], source: Vector256_1[float]) -> None:...
        # Method StoreAligned(address : Double*, source : Vector256`1) was skipped since it collides with above method
        # Method StoreAligned(address : SByte*, source : Vector256`1) was skipped since it collides with above method
        # Method StoreAligned(address : Byte*, source : Vector256`1) was skipped since it collides with above method
        # Method StoreAligned(address : Int16*, source : Vector256`1) was skipped since it collides with above method
        # Method StoreAligned(address : UInt16*, source : Vector256`1) was skipped since it collides with above method
        # Method StoreAligned(address : Int32*, source : Vector256`1) was skipped since it collides with above method
        # Method StoreAligned(address : UInt32*, source : Vector256`1) was skipped since it collides with above method
        # Method StoreAligned(address : Int64*, source : Vector256`1) was skipped since it collides with above method
        # Method StoreAligned(address : UInt64*, source : Vector256`1) was skipped since it collides with above method

    # Skipped StoreAlignedNonTemporal due to it being static, abstract and generic.

    StoreAlignedNonTemporal : StoreAlignedNonTemporal_MethodGroup
    class StoreAlignedNonTemporal_MethodGroup:
        def __call__(self, address: clr.Reference[float], source: Vector256_1[float]) -> None:...
        # Method StoreAlignedNonTemporal(address : Double*, source : Vector256`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : SByte*, source : Vector256`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : Byte*, source : Vector256`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : Int16*, source : Vector256`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : UInt16*, source : Vector256`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : Int32*, source : Vector256`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : UInt32*, source : Vector256`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : Int64*, source : Vector256`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : UInt64*, source : Vector256`1) was skipped since it collides with above method

    # Skipped Subtract due to it being static, abstract and generic.

    Subtract : Subtract_MethodGroup
    class Subtract_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method Subtract(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped TestC due to it being static, abstract and generic.

    TestC : TestC_MethodGroup
    class TestC_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> bool:...
        # Method TestC(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> bool:...
        # Method TestC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped TestNotZAndNotC due to it being static, abstract and generic.

    TestNotZAndNotC : TestNotZAndNotC_MethodGroup
    class TestNotZAndNotC_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> bool:...
        # Method TestNotZAndNotC(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> bool:...
        # Method TestNotZAndNotC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestNotZAndNotC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestNotZAndNotC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestNotZAndNotC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestNotZAndNotC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestNotZAndNotC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestNotZAndNotC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestNotZAndNotC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestNotZAndNotC(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped TestZ due to it being static, abstract and generic.

    TestZ : TestZ_MethodGroup
    class TestZ_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> bool:...
        # Method TestZ(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> bool:...
        # Method TestZ(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestZ(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestZ(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestZ(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestZ(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestZ(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestZ(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestZ(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method TestZ(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped UnpackHigh due to it being static, abstract and generic.

    UnpackHigh : UnpackHigh_MethodGroup
    class UnpackHigh_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method UnpackHigh(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped UnpackLow due to it being static, abstract and generic.

    UnpackLow : UnpackLow_MethodGroup
    class UnpackLow_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method UnpackLow(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped Xor due to it being static, abstract and generic.

    Xor : Xor_MethodGroup
    class Xor_MethodGroup:
        def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
        # Method Xor(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method


    class X64(Sse42.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...



class Avx2(Avx):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def ConvertToInt32(value: Vector256_1[int]) -> int: ...
    @staticmethod
    def ConvertToUInt32(value: Vector256_1[int]) -> int: ...
    @staticmethod
    def HorizontalAddSaturate(left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]: ...
    @staticmethod
    def HorizontalSubtractSaturate(left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]: ...
    @staticmethod
    def MultipleSumAbsoluteDifferences(left: Vector256_1[int], right: Vector256_1[int], mask: int) -> Vector256_1[int]: ...
    @staticmethod
    def MultiplyHighRoundScale(left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]: ...
    @staticmethod
    def SumAbsoluteDifferences(left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]: ...
    # Skipped Abs due to it being static, abstract and generic.

    Abs : Abs_MethodGroup
    class Abs_MethodGroup:
        def __call__(self, value: Vector256_1[int]) -> Vector256_1[int]:...
        # Method Abs(value : Vector256`1) was skipped since it collides with above method
        # Method Abs(value : Vector256`1) was skipped since it collides with above method

    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method Add(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Add(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Add(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Add(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Add(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Add(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Add(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped AddSaturate due to it being static, abstract and generic.

    AddSaturate : AddSaturate_MethodGroup
    class AddSaturate_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method AddSaturate(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped AlignRight due to it being static, abstract and generic.

    AlignRight : AlignRight_MethodGroup
    class AlignRight_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int], mask: int) -> Vector256_1[int]:...
        # Method AlignRight(left : Vector256`1, right : Vector256`1, mask : Byte) was skipped since it collides with above method
        # Method AlignRight(left : Vector256`1, right : Vector256`1, mask : Byte) was skipped since it collides with above method
        # Method AlignRight(left : Vector256`1, right : Vector256`1, mask : Byte) was skipped since it collides with above method
        # Method AlignRight(left : Vector256`1, right : Vector256`1, mask : Byte) was skipped since it collides with above method
        # Method AlignRight(left : Vector256`1, right : Vector256`1, mask : Byte) was skipped since it collides with above method
        # Method AlignRight(left : Vector256`1, right : Vector256`1, mask : Byte) was skipped since it collides with above method
        # Method AlignRight(left : Vector256`1, right : Vector256`1, mask : Byte) was skipped since it collides with above method

    # Skipped And due to it being static, abstract and generic.

    And : And_MethodGroup
    class And_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method And(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method And(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method And(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method And(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method And(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method And(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method And(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped AndNot due to it being static, abstract and generic.

    AndNot : AndNot_MethodGroup
    class AndNot_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method AndNot(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method AndNot(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method AndNot(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method AndNot(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method AndNot(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method AndNot(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method AndNot(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped Average due to it being static, abstract and generic.

    Average : Average_MethodGroup
    class Average_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method Average(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped Blend due to it being static, abstract and generic.

    Blend : Blend_MethodGroup
    class Blend_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int], control: int) -> Vector128_1[int]:...
        # Method Blend(left : Vector128`1, right : Vector128`1, control : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int], control: int) -> Vector256_1[int]:...
        # Method Blend(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
        # Method Blend(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
        # Method Blend(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method

    # Skipped BlendVariable due to it being static, abstract and generic.

    BlendVariable : BlendVariable_MethodGroup
    class BlendVariable_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int], mask: Vector256_1[int]) -> Vector256_1[int]:...
        # Method BlendVariable(left : Vector256`1, right : Vector256`1, mask : Vector256`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector256`1, right : Vector256`1, mask : Vector256`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector256`1, right : Vector256`1, mask : Vector256`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector256`1, right : Vector256`1, mask : Vector256`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector256`1, right : Vector256`1, mask : Vector256`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector256`1, right : Vector256`1, mask : Vector256`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector256`1, right : Vector256`1, mask : Vector256`1) was skipped since it collides with above method

    # Skipped BroadcastScalarToVector128 due to it being static, abstract and generic.

    BroadcastScalarToVector128 : BroadcastScalarToVector128_MethodGroup
    class BroadcastScalarToVector128_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method BroadcastScalarToVector128(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector128(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector128(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector128(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector128(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector128(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector128(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector128(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector128(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: clr.Reference[int]) -> Vector128_1[int]:...
        # Method BroadcastScalarToVector128(source : SByte*) was skipped since it collides with above method
        # Method BroadcastScalarToVector128(source : Int16*) was skipped since it collides with above method
        # Method BroadcastScalarToVector128(source : UInt16*) was skipped since it collides with above method
        # Method BroadcastScalarToVector128(source : Int32*) was skipped since it collides with above method
        # Method BroadcastScalarToVector128(source : UInt32*) was skipped since it collides with above method
        # Method BroadcastScalarToVector128(source : Int64*) was skipped since it collides with above method
        # Method BroadcastScalarToVector128(source : UInt64*) was skipped since it collides with above method

    # Skipped BroadcastScalarToVector256 due to it being static, abstract and generic.

    BroadcastScalarToVector256 : BroadcastScalarToVector256_MethodGroup
    class BroadcastScalarToVector256_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector256_1[float]:...
        # Method BroadcastScalarToVector256(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector256(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector256(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector256(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector256(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector256(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector256(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector256(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector256(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: clr.Reference[int]) -> Vector256_1[int]:...
        # Method BroadcastScalarToVector256(source : SByte*) was skipped since it collides with above method
        # Method BroadcastScalarToVector256(source : Int16*) was skipped since it collides with above method
        # Method BroadcastScalarToVector256(source : UInt16*) was skipped since it collides with above method
        # Method BroadcastScalarToVector256(source : Int32*) was skipped since it collides with above method
        # Method BroadcastScalarToVector256(source : UInt32*) was skipped since it collides with above method
        # Method BroadcastScalarToVector256(source : Int64*) was skipped since it collides with above method
        # Method BroadcastScalarToVector256(source : UInt64*) was skipped since it collides with above method

    # Skipped BroadcastVector128ToVector256 due to it being static, abstract and generic.

    BroadcastVector128ToVector256 : BroadcastVector128ToVector256_MethodGroup
    class BroadcastVector128ToVector256_MethodGroup:
        def __call__(self, address: clr.Reference[int]) -> Vector256_1[int]:...
        # Method BroadcastVector128ToVector256(address : Byte*) was skipped since it collides with above method
        # Method BroadcastVector128ToVector256(address : Int16*) was skipped since it collides with above method
        # Method BroadcastVector128ToVector256(address : UInt16*) was skipped since it collides with above method
        # Method BroadcastVector128ToVector256(address : Int32*) was skipped since it collides with above method
        # Method BroadcastVector128ToVector256(address : UInt32*) was skipped since it collides with above method
        # Method BroadcastVector128ToVector256(address : Int64*) was skipped since it collides with above method
        # Method BroadcastVector128ToVector256(address : UInt64*) was skipped since it collides with above method

    # Skipped CompareEqual due to it being static, abstract and generic.

    CompareEqual : CompareEqual_MethodGroup
    class CompareEqual_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method CompareEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped CompareGreaterThan due to it being static, abstract and generic.

    CompareGreaterThan : CompareGreaterThan_MethodGroup
    class CompareGreaterThan_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method CompareGreaterThan(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped ConvertToVector256Int16 due to it being static, abstract and generic.

    ConvertToVector256Int16 : ConvertToVector256Int16_MethodGroup
    class ConvertToVector256Int16_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector256_1[int]:...
        # Method ConvertToVector256Int16(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, address: clr.Reference[int]) -> Vector256_1[int]:...
        # Method ConvertToVector256Int16(address : Byte*) was skipped since it collides with above method

    # Skipped ConvertToVector256Int32 due to it being static, abstract and generic.

    ConvertToVector256Int32 : ConvertToVector256Int32_MethodGroup
    class ConvertToVector256Int32_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector256_1[int]:...
        # Method ConvertToVector256Int32(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToVector256Int32(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToVector256Int32(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, address: clr.Reference[int]) -> Vector256_1[int]:...
        # Method ConvertToVector256Int32(address : Byte*) was skipped since it collides with above method
        # Method ConvertToVector256Int32(address : Int16*) was skipped since it collides with above method
        # Method ConvertToVector256Int32(address : UInt16*) was skipped since it collides with above method

    # Skipped ConvertToVector256Int64 due to it being static, abstract and generic.

    ConvertToVector256Int64 : ConvertToVector256Int64_MethodGroup
    class ConvertToVector256Int64_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector256_1[int]:...
        # Method ConvertToVector256Int64(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToVector256Int64(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToVector256Int64(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToVector256Int64(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToVector256Int64(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, address: clr.Reference[int]) -> Vector256_1[int]:...
        # Method ConvertToVector256Int64(address : Byte*) was skipped since it collides with above method
        # Method ConvertToVector256Int64(address : Int16*) was skipped since it collides with above method
        # Method ConvertToVector256Int64(address : UInt16*) was skipped since it collides with above method
        # Method ConvertToVector256Int64(address : Int32*) was skipped since it collides with above method
        # Method ConvertToVector256Int64(address : UInt32*) was skipped since it collides with above method

    # Skipped ExtractVector128 due to it being static, abstract and generic.

    ExtractVector128 : ExtractVector128_MethodGroup
    class ExtractVector128_MethodGroup:
        def __call__(self, value: Vector256_1[int], index: int) -> Vector128_1[int]:...
        # Method ExtractVector128(value : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector256`1, index : Byte) was skipped since it collides with above method

    # Skipped GatherMaskVector128 due to it being static, abstract and generic.

    GatherMaskVector128 : GatherMaskVector128_MethodGroup
    class GatherMaskVector128_MethodGroup:
        @typing.overload
        def __call__(self, source: Vector128_1[float], baseAddress: clr.Reference[float], index: Vector128_1[int], mask: Vector128_1[float], scale: int) -> Vector128_1[float]:...
        # Method GatherMaskVector128(source : Vector128`1, baseAddress : Double*, index : Vector128`1, mask : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherMaskVector128(source : Vector128`1, baseAddress : Single*, index : Vector128`1, mask : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherMaskVector128(source : Vector128`1, baseAddress : Double*, index : Vector128`1, mask : Vector128`1, scale : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, source: Vector128_1[float], baseAddress: clr.Reference[float], index: Vector256_1[int], mask: Vector128_1[float], scale: int) -> Vector128_1[float]:...
        # Method GatherMaskVector128(source : Vector128`1, baseAddress : Int32*, index : Vector128`1, mask : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherMaskVector128(source : Vector128`1, baseAddress : UInt32*, index : Vector128`1, mask : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherMaskVector128(source : Vector128`1, baseAddress : Int64*, index : Vector128`1, mask : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherMaskVector128(source : Vector128`1, baseAddress : UInt64*, index : Vector128`1, mask : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherMaskVector128(source : Vector128`1, baseAddress : Int32*, index : Vector128`1, mask : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherMaskVector128(source : Vector128`1, baseAddress : UInt32*, index : Vector128`1, mask : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherMaskVector128(source : Vector128`1, baseAddress : Int64*, index : Vector128`1, mask : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherMaskVector128(source : Vector128`1, baseAddress : UInt64*, index : Vector128`1, mask : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherMaskVector128(source : Vector128`1, baseAddress : Int32*, index : Vector256`1, mask : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherMaskVector128(source : Vector128`1, baseAddress : UInt32*, index : Vector256`1, mask : Vector128`1, scale : Byte) was skipped since it collides with above method

    # Skipped GatherMaskVector256 due to it being static, abstract and generic.

    GatherMaskVector256 : GatherMaskVector256_MethodGroup
    class GatherMaskVector256_MethodGroup:
        @typing.overload
        def __call__(self, source: Vector256_1[float], baseAddress: clr.Reference[float], index: Vector256_1[int], mask: Vector256_1[float], scale: int) -> Vector256_1[float]:...
        @typing.overload
        def __call__(self, source: Vector256_1[float], baseAddress: clr.Reference[float], index: Vector128_1[int], mask: Vector256_1[float], scale: int) -> Vector256_1[float]:...
        # Method GatherMaskVector256(source : Vector256`1, baseAddress : Double*, index : Vector256`1, mask : Vector256`1, scale : Byte) was skipped since it collides with above method
        # Method GatherMaskVector256(source : Vector256`1, baseAddress : Int32*, index : Vector256`1, mask : Vector256`1, scale : Byte) was skipped since it collides with above method
        # Method GatherMaskVector256(source : Vector256`1, baseAddress : UInt32*, index : Vector256`1, mask : Vector256`1, scale : Byte) was skipped since it collides with above method
        # Method GatherMaskVector256(source : Vector256`1, baseAddress : Int64*, index : Vector128`1, mask : Vector256`1, scale : Byte) was skipped since it collides with above method
        # Method GatherMaskVector256(source : Vector256`1, baseAddress : UInt64*, index : Vector128`1, mask : Vector256`1, scale : Byte) was skipped since it collides with above method
        # Method GatherMaskVector256(source : Vector256`1, baseAddress : Int64*, index : Vector256`1, mask : Vector256`1, scale : Byte) was skipped since it collides with above method
        # Method GatherMaskVector256(source : Vector256`1, baseAddress : UInt64*, index : Vector256`1, mask : Vector256`1, scale : Byte) was skipped since it collides with above method

    # Skipped GatherVector128 due to it being static, abstract and generic.

    GatherVector128 : GatherVector128_MethodGroup
    class GatherVector128_MethodGroup:
        @typing.overload
        def __call__(self, baseAddress: clr.Reference[float], index: Vector128_1[int], scale: int) -> Vector128_1[float]:...
        # Method GatherVector128(baseAddress : Double*, index : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherVector128(baseAddress : Single*, index : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherVector128(baseAddress : Double*, index : Vector128`1, scale : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, baseAddress: clr.Reference[float], index: Vector256_1[int], scale: int) -> Vector128_1[float]:...
        # Method GatherVector128(baseAddress : Int32*, index : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherVector128(baseAddress : UInt32*, index : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherVector128(baseAddress : Int64*, index : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherVector128(baseAddress : UInt64*, index : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherVector128(baseAddress : Int32*, index : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherVector128(baseAddress : UInt32*, index : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherVector128(baseAddress : Int64*, index : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherVector128(baseAddress : UInt64*, index : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherVector128(baseAddress : Int32*, index : Vector256`1, scale : Byte) was skipped since it collides with above method
        # Method GatherVector128(baseAddress : UInt32*, index : Vector256`1, scale : Byte) was skipped since it collides with above method

    # Skipped GatherVector256 due to it being static, abstract and generic.

    GatherVector256 : GatherVector256_MethodGroup
    class GatherVector256_MethodGroup:
        @typing.overload
        def __call__(self, baseAddress: clr.Reference[float], index: Vector256_1[int], scale: int) -> Vector256_1[float]:...
        @typing.overload
        def __call__(self, baseAddress: clr.Reference[float], index: Vector128_1[int], scale: int) -> Vector256_1[float]:...
        # Method GatherVector256(baseAddress : Double*, index : Vector256`1, scale : Byte) was skipped since it collides with above method
        # Method GatherVector256(baseAddress : Int32*, index : Vector256`1, scale : Byte) was skipped since it collides with above method
        # Method GatherVector256(baseAddress : UInt32*, index : Vector256`1, scale : Byte) was skipped since it collides with above method
        # Method GatherVector256(baseAddress : Int64*, index : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherVector256(baseAddress : UInt64*, index : Vector128`1, scale : Byte) was skipped since it collides with above method
        # Method GatherVector256(baseAddress : Int64*, index : Vector256`1, scale : Byte) was skipped since it collides with above method
        # Method GatherVector256(baseAddress : UInt64*, index : Vector256`1, scale : Byte) was skipped since it collides with above method

    # Skipped HorizontalAdd due to it being static, abstract and generic.

    HorizontalAdd : HorizontalAdd_MethodGroup
    class HorizontalAdd_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method HorizontalAdd(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped HorizontalSubtract due to it being static, abstract and generic.

    HorizontalSubtract : HorizontalSubtract_MethodGroup
    class HorizontalSubtract_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method HorizontalSubtract(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped InsertVector128 due to it being static, abstract and generic.

    InsertVector128 : InsertVector128_MethodGroup
    class InsertVector128_MethodGroup:
        def __call__(self, value: Vector256_1[int], data: Vector128_1[int], index: int) -> Vector256_1[int]:...
        # Method InsertVector128(value : Vector256`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector256`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector256`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector256`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector256`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector256`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector256`1, data : Vector128`1, index : Byte) was skipped since it collides with above method

    # Skipped LoadAlignedVector256NonTemporal due to it being static, abstract and generic.

    LoadAlignedVector256NonTemporal : LoadAlignedVector256NonTemporal_MethodGroup
    class LoadAlignedVector256NonTemporal_MethodGroup:
        def __call__(self, address: clr.Reference[int]) -> Vector256_1[int]:...
        # Method LoadAlignedVector256NonTemporal(address : Byte*) was skipped since it collides with above method
        # Method LoadAlignedVector256NonTemporal(address : Int16*) was skipped since it collides with above method
        # Method LoadAlignedVector256NonTemporal(address : UInt16*) was skipped since it collides with above method
        # Method LoadAlignedVector256NonTemporal(address : Int32*) was skipped since it collides with above method
        # Method LoadAlignedVector256NonTemporal(address : UInt32*) was skipped since it collides with above method
        # Method LoadAlignedVector256NonTemporal(address : Int64*) was skipped since it collides with above method
        # Method LoadAlignedVector256NonTemporal(address : UInt64*) was skipped since it collides with above method

    # Skipped MaskLoad due to it being static, abstract and generic.

    MaskLoad : MaskLoad_MethodGroup
    class MaskLoad_MethodGroup:
        @typing.overload
        def __call__(self, address: clr.Reference[int], mask: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MaskLoad(address : UInt32*, mask : Vector128`1) was skipped since it collides with above method
        # Method MaskLoad(address : Int64*, mask : Vector128`1) was skipped since it collides with above method
        # Method MaskLoad(address : UInt64*, mask : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, address: clr.Reference[int], mask: Vector256_1[int]) -> Vector256_1[int]:...
        # Method MaskLoad(address : UInt32*, mask : Vector256`1) was skipped since it collides with above method
        # Method MaskLoad(address : Int64*, mask : Vector256`1) was skipped since it collides with above method
        # Method MaskLoad(address : UInt64*, mask : Vector256`1) was skipped since it collides with above method

    # Skipped MaskStore due to it being static, abstract and generic.

    MaskStore : MaskStore_MethodGroup
    class MaskStore_MethodGroup:
        @typing.overload
        def __call__(self, address: clr.Reference[int], mask: Vector128_1[int], source: Vector128_1[int]) -> None:...
        # Method MaskStore(address : UInt32*, mask : Vector128`1, source : Vector128`1) was skipped since it collides with above method
        # Method MaskStore(address : Int64*, mask : Vector128`1, source : Vector128`1) was skipped since it collides with above method
        # Method MaskStore(address : UInt64*, mask : Vector128`1, source : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, address: clr.Reference[int], mask: Vector256_1[int], source: Vector256_1[int]) -> None:...
        # Method MaskStore(address : UInt32*, mask : Vector256`1, source : Vector256`1) was skipped since it collides with above method
        # Method MaskStore(address : Int64*, mask : Vector256`1, source : Vector256`1) was skipped since it collides with above method
        # Method MaskStore(address : UInt64*, mask : Vector256`1, source : Vector256`1) was skipped since it collides with above method

    # Skipped Max due to it being static, abstract and generic.

    Max : Max_MethodGroup
    class Max_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method Max(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Max(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Max(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Max(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Max(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped Min due to it being static, abstract and generic.

    Min : Min_MethodGroup
    class Min_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method Min(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Min(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Min(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Min(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Min(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped MoveMask due to it being static, abstract and generic.

    MoveMask : MoveMask_MethodGroup
    class MoveMask_MethodGroup:
        def __call__(self, value: Vector256_1[int]) -> int:...
        # Method MoveMask(value : Vector256`1) was skipped since it collides with above method

    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method Multiply(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped MultiplyAddAdjacent due to it being static, abstract and generic.

    MultiplyAddAdjacent : MultiplyAddAdjacent_MethodGroup
    class MultiplyAddAdjacent_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method MultiplyAddAdjacent(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped MultiplyHigh due to it being static, abstract and generic.

    MultiplyHigh : MultiplyHigh_MethodGroup
    class MultiplyHigh_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method MultiplyHigh(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped MultiplyLow due to it being static, abstract and generic.

    MultiplyLow : MultiplyLow_MethodGroup
    class MultiplyLow_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method MultiplyLow(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method MultiplyLow(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method MultiplyLow(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped Or due to it being static, abstract and generic.

    Or : Or_MethodGroup
    class Or_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method Or(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Or(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Or(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Or(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Or(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Or(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Or(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped PackSignedSaturate due to it being static, abstract and generic.

    PackSignedSaturate : PackSignedSaturate_MethodGroup
    class PackSignedSaturate_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method PackSignedSaturate(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped PackUnsignedSaturate due to it being static, abstract and generic.

    PackUnsignedSaturate : PackUnsignedSaturate_MethodGroup
    class PackUnsignedSaturate_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method PackUnsignedSaturate(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped Permute2x128 due to it being static, abstract and generic.

    Permute2x128 : Permute2x128_MethodGroup
    class Permute2x128_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int], control: int) -> Vector256_1[int]:...
        # Method Permute2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
        # Method Permute2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
        # Method Permute2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
        # Method Permute2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
        # Method Permute2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
        # Method Permute2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
        # Method Permute2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method

    # Skipped Permute4x64 due to it being static, abstract and generic.

    Permute4x64 : Permute4x64_MethodGroup
    class Permute4x64_MethodGroup:
        def __call__(self, value: Vector256_1[float], control: int) -> Vector256_1[float]:...
        # Method Permute4x64(value : Vector256`1, control : Byte) was skipped since it collides with above method
        # Method Permute4x64(value : Vector256`1, control : Byte) was skipped since it collides with above method

    # Skipped PermuteVar8x32 due to it being static, abstract and generic.

    PermuteVar8x32 : PermuteVar8x32_MethodGroup
    class PermuteVar8x32_MethodGroup:
        def __call__(self, left: Vector256_1[float], control: Vector256_1[int]) -> Vector256_1[float]:...
        # Method PermuteVar8x32(left : Vector256`1, control : Vector256`1) was skipped since it collides with above method
        # Method PermuteVar8x32(left : Vector256`1, control : Vector256`1) was skipped since it collides with above method

    # Skipped ShiftLeftLogical due to it being static, abstract and generic.

    ShiftLeftLogical : ShiftLeftLogical_MethodGroup
    class ShiftLeftLogical_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector256_1[int], count: int) -> Vector256_1[int]:...
        # Method ShiftLeftLogical(value : Vector256`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector256`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector256`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector256`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector256`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector256_1[int], count: Vector128_1[int]) -> Vector256_1[int]:...
        # Method ShiftLeftLogical(value : Vector256`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector256`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector256`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector256`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector256`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftLeftLogical128BitLane due to it being static, abstract and generic.

    ShiftLeftLogical128BitLane : ShiftLeftLogical128BitLane_MethodGroup
    class ShiftLeftLogical128BitLane_MethodGroup:
        def __call__(self, value: Vector256_1[int], numBytes: int) -> Vector256_1[int]:...
        # Method ShiftLeftLogical128BitLane(value : Vector256`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical128BitLane(value : Vector256`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical128BitLane(value : Vector256`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical128BitLane(value : Vector256`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical128BitLane(value : Vector256`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical128BitLane(value : Vector256`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical128BitLane(value : Vector256`1, numBytes : Byte) was skipped since it collides with above method

    # Skipped ShiftLeftLogicalVariable due to it being static, abstract and generic.

    ShiftLeftLogicalVariable : ShiftLeftLogicalVariable_MethodGroup
    class ShiftLeftLogicalVariable_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ShiftLeftLogicalVariable(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLeftLogicalVariable(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLeftLogicalVariable(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector256_1[int], count: Vector256_1[int]) -> Vector256_1[int]:...
        # Method ShiftLeftLogicalVariable(value : Vector256`1, count : Vector256`1) was skipped since it collides with above method
        # Method ShiftLeftLogicalVariable(value : Vector256`1, count : Vector256`1) was skipped since it collides with above method
        # Method ShiftLeftLogicalVariable(value : Vector256`1, count : Vector256`1) was skipped since it collides with above method

    # Skipped ShiftRightArithmetic due to it being static, abstract and generic.

    ShiftRightArithmetic : ShiftRightArithmetic_MethodGroup
    class ShiftRightArithmetic_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector256_1[int], count: int) -> Vector256_1[int]:...
        # Method ShiftRightArithmetic(value : Vector256`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector256_1[int], count: Vector128_1[int]) -> Vector256_1[int]:...
        # Method ShiftRightArithmetic(value : Vector256`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftRightArithmeticVariable due to it being static, abstract and generic.

    ShiftRightArithmeticVariable : ShiftRightArithmeticVariable_MethodGroup
    class ShiftRightArithmeticVariable_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
        @typing.overload
        def __call__(self, value: Vector256_1[int], count: Vector256_1[int]) -> Vector256_1[int]:...

    # Skipped ShiftRightLogical due to it being static, abstract and generic.

    ShiftRightLogical : ShiftRightLogical_MethodGroup
    class ShiftRightLogical_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector256_1[int], count: int) -> Vector256_1[int]:...
        # Method ShiftRightLogical(value : Vector256`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector256`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector256`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector256`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector256`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector256_1[int], count: Vector128_1[int]) -> Vector256_1[int]:...
        # Method ShiftRightLogical(value : Vector256`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector256`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector256`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector256`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector256`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftRightLogical128BitLane due to it being static, abstract and generic.

    ShiftRightLogical128BitLane : ShiftRightLogical128BitLane_MethodGroup
    class ShiftRightLogical128BitLane_MethodGroup:
        def __call__(self, value: Vector256_1[int], numBytes: int) -> Vector256_1[int]:...
        # Method ShiftRightLogical128BitLane(value : Vector256`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical128BitLane(value : Vector256`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical128BitLane(value : Vector256`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical128BitLane(value : Vector256`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical128BitLane(value : Vector256`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical128BitLane(value : Vector256`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical128BitLane(value : Vector256`1, numBytes : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogicalVariable due to it being static, abstract and generic.

    ShiftRightLogicalVariable : ShiftRightLogicalVariable_MethodGroup
    class ShiftRightLogicalVariable_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ShiftRightLogicalVariable(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftRightLogicalVariable(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftRightLogicalVariable(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector256_1[int], count: Vector256_1[int]) -> Vector256_1[int]:...
        # Method ShiftRightLogicalVariable(value : Vector256`1, count : Vector256`1) was skipped since it collides with above method
        # Method ShiftRightLogicalVariable(value : Vector256`1, count : Vector256`1) was skipped since it collides with above method
        # Method ShiftRightLogicalVariable(value : Vector256`1, count : Vector256`1) was skipped since it collides with above method

    # Skipped Shuffle due to it being static, abstract and generic.

    Shuffle : Shuffle_MethodGroup
    class Shuffle_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector256_1[int], control: int) -> Vector256_1[int]:...
        # Method Shuffle(value : Vector256`1, control : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector256_1[int], mask: Vector256_1[int]) -> Vector256_1[int]:...
        # Method Shuffle(value : Vector256`1, mask : Vector256`1) was skipped since it collides with above method

    # Skipped ShuffleHigh due to it being static, abstract and generic.

    ShuffleHigh : ShuffleHigh_MethodGroup
    class ShuffleHigh_MethodGroup:
        def __call__(self, value: Vector256_1[int], control: int) -> Vector256_1[int]:...
        # Method ShuffleHigh(value : Vector256`1, control : Byte) was skipped since it collides with above method

    # Skipped ShuffleLow due to it being static, abstract and generic.

    ShuffleLow : ShuffleLow_MethodGroup
    class ShuffleLow_MethodGroup:
        def __call__(self, value: Vector256_1[int], control: int) -> Vector256_1[int]:...
        # Method ShuffleLow(value : Vector256`1, control : Byte) was skipped since it collides with above method

    # Skipped Sign due to it being static, abstract and generic.

    Sign : Sign_MethodGroup
    class Sign_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method Sign(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Sign(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped Subtract due to it being static, abstract and generic.

    Subtract : Subtract_MethodGroup
    class Subtract_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method Subtract(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Subtract(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Subtract(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Subtract(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Subtract(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Subtract(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Subtract(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped SubtractSaturate due to it being static, abstract and generic.

    SubtractSaturate : SubtractSaturate_MethodGroup
    class SubtractSaturate_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method SubtractSaturate(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped UnpackHigh due to it being static, abstract and generic.

    UnpackHigh : UnpackHigh_MethodGroup
    class UnpackHigh_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method UnpackHigh(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped UnpackLow due to it being static, abstract and generic.

    UnpackLow : UnpackLow_MethodGroup
    class UnpackLow_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method UnpackLow(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped Xor due to it being static, abstract and generic.

    Xor : Xor_MethodGroup
    class Xor_MethodGroup:
        def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method Xor(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Xor(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Xor(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Xor(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Xor(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Xor(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
        # Method Xor(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method


    class X64(Avx.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...



class Avx512BW(Avx512F):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def ConvertToVector256ByteWithSaturation(value: Vector512_1[int]) -> Vector256_1[int]: ...
    @staticmethod
    def ConvertToVector256SByteWithSaturation(value: Vector512_1[int]) -> Vector256_1[int]: ...
    @staticmethod
    def MultiplyHighRoundScale(left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]: ...
    @staticmethod
    def ShiftRightArithmeticVariable(value: Vector512_1[int], count: Vector512_1[int]) -> Vector512_1[int]: ...
    @staticmethod
    def SumAbsoluteDifferences(left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]: ...
    @staticmethod
    def SumAbsoluteDifferencesInBlock32(left: Vector512_1[int], right: Vector512_1[int], control: int) -> Vector512_1[int]: ...
    # Skipped Abs due to it being static, abstract and generic.

    Abs : Abs_MethodGroup
    class Abs_MethodGroup:
        def __call__(self, value: Vector512_1[int]) -> Vector512_1[int]:...
        # Method Abs(value : Vector512`1) was skipped since it collides with above method

    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method Add(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Add(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Add(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped AddSaturate due to it being static, abstract and generic.

    AddSaturate : AddSaturate_MethodGroup
    class AddSaturate_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method AddSaturate(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped AlignRight due to it being static, abstract and generic.

    AlignRight : AlignRight_MethodGroup
    class AlignRight_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int], mask: int) -> Vector512_1[int]:...
        # Method AlignRight(left : Vector512`1, right : Vector512`1, mask : Byte) was skipped since it collides with above method

    # Skipped Average due to it being static, abstract and generic.

    Average : Average_MethodGroup
    class Average_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method Average(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped BlendVariable due to it being static, abstract and generic.

    BlendVariable : BlendVariable_MethodGroup
    class BlendVariable_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int], mask: Vector512_1[int]) -> Vector512_1[int]:...
        # Method BlendVariable(left : Vector512`1, right : Vector512`1, mask : Vector512`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector512`1, right : Vector512`1, mask : Vector512`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector512`1, right : Vector512`1, mask : Vector512`1) was skipped since it collides with above method

    # Skipped BroadcastScalarToVector512 due to it being static, abstract and generic.

    BroadcastScalarToVector512 : BroadcastScalarToVector512_MethodGroup
    class BroadcastScalarToVector512_MethodGroup:
        def __call__(self, value: Vector128_1[int]) -> Vector512_1[int]:...
        # Method BroadcastScalarToVector512(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector512(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector512(value : Vector128`1) was skipped since it collides with above method

    # Skipped CompareEqual due to it being static, abstract and generic.

    CompareEqual : CompareEqual_MethodGroup
    class CompareEqual_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method CompareEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped CompareGreaterThan due to it being static, abstract and generic.

    CompareGreaterThan : CompareGreaterThan_MethodGroup
    class CompareGreaterThan_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method CompareGreaterThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped CompareGreaterThanOrEqual due to it being static, abstract and generic.

    CompareGreaterThanOrEqual : CompareGreaterThanOrEqual_MethodGroup
    class CompareGreaterThanOrEqual_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method CompareGreaterThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped CompareLessThan due to it being static, abstract and generic.

    CompareLessThan : CompareLessThan_MethodGroup
    class CompareLessThan_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method CompareLessThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped CompareLessThanOrEqual due to it being static, abstract and generic.

    CompareLessThanOrEqual : CompareLessThanOrEqual_MethodGroup
    class CompareLessThanOrEqual_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method CompareLessThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped CompareNotEqual due to it being static, abstract and generic.

    CompareNotEqual : CompareNotEqual_MethodGroup
    class CompareNotEqual_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method CompareNotEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareNotEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareNotEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToVector256Byte due to it being static, abstract and generic.

    ConvertToVector256Byte : ConvertToVector256Byte_MethodGroup
    class ConvertToVector256Byte_MethodGroup:
        def __call__(self, value: Vector512_1[int]) -> Vector256_1[int]:...
        # Method ConvertToVector256Byte(value : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToVector256SByte due to it being static, abstract and generic.

    ConvertToVector256SByte : ConvertToVector256SByte_MethodGroup
    class ConvertToVector256SByte_MethodGroup:
        def __call__(self, value: Vector512_1[int]) -> Vector256_1[int]:...
        # Method ConvertToVector256SByte(value : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToVector512Int16 due to it being static, abstract and generic.

    ConvertToVector512Int16 : ConvertToVector512Int16_MethodGroup
    class ConvertToVector512Int16_MethodGroup:
        def __call__(self, value: Vector256_1[int]) -> Vector512_1[int]:...
        # Method ConvertToVector512Int16(value : Vector256`1) was skipped since it collides with above method

    # Skipped ConvertToVector512UInt16 due to it being static, abstract and generic.

    ConvertToVector512UInt16 : ConvertToVector512UInt16_MethodGroup
    class ConvertToVector512UInt16_MethodGroup:
        def __call__(self, value: Vector256_1[int]) -> Vector512_1[int]:...
        # Method ConvertToVector512UInt16(value : Vector256`1) was skipped since it collides with above method

    # Skipped LoadVector512 due to it being static, abstract and generic.

    LoadVector512 : LoadVector512_MethodGroup
    class LoadVector512_MethodGroup:
        def __call__(self, address: clr.Reference[int]) -> Vector512_1[int]:...
        # Method LoadVector512(address : Byte*) was skipped since it collides with above method
        # Method LoadVector512(address : Int16*) was skipped since it collides with above method
        # Method LoadVector512(address : UInt16*) was skipped since it collides with above method

    # Skipped Max due to it being static, abstract and generic.

    Max : Max_MethodGroup
    class Max_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method Max(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Max(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Max(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped Min due to it being static, abstract and generic.

    Min : Min_MethodGroup
    class Min_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method Min(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Min(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Min(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped MultiplyAddAdjacent due to it being static, abstract and generic.

    MultiplyAddAdjacent : MultiplyAddAdjacent_MethodGroup
    class MultiplyAddAdjacent_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method MultiplyAddAdjacent(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped MultiplyHigh due to it being static, abstract and generic.

    MultiplyHigh : MultiplyHigh_MethodGroup
    class MultiplyHigh_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method MultiplyHigh(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped MultiplyLow due to it being static, abstract and generic.

    MultiplyLow : MultiplyLow_MethodGroup
    class MultiplyLow_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method MultiplyLow(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped PackSignedSaturate due to it being static, abstract and generic.

    PackSignedSaturate : PackSignedSaturate_MethodGroup
    class PackSignedSaturate_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method PackSignedSaturate(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped PackUnsignedSaturate due to it being static, abstract and generic.

    PackUnsignedSaturate : PackUnsignedSaturate_MethodGroup
    class PackUnsignedSaturate_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method PackUnsignedSaturate(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped PermuteVar32x16 due to it being static, abstract and generic.

    PermuteVar32x16 : PermuteVar32x16_MethodGroup
    class PermuteVar32x16_MethodGroup:
        def __call__(self, left: Vector512_1[int], control: Vector512_1[int]) -> Vector512_1[int]:...
        # Method PermuteVar32x16(left : Vector512`1, control : Vector512`1) was skipped since it collides with above method

    # Skipped PermuteVar32x16x2 due to it being static, abstract and generic.

    PermuteVar32x16x2 : PermuteVar32x16x2_MethodGroup
    class PermuteVar32x16x2_MethodGroup:
        def __call__(self, lower: Vector512_1[int], indices: Vector512_1[int], upper: Vector512_1[int]) -> Vector512_1[int]:...
        # Method PermuteVar32x16x2(lower : Vector512`1, indices : Vector512`1, upper : Vector512`1) was skipped since it collides with above method

    # Skipped ShiftLeftLogical due to it being static, abstract and generic.

    ShiftLeftLogical : ShiftLeftLogical_MethodGroup
    class ShiftLeftLogical_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector512_1[int], count: int) -> Vector512_1[int]:...
        # Method ShiftLeftLogical(value : Vector512`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector512_1[int], count: Vector128_1[int]) -> Vector512_1[int]:...
        # Method ShiftLeftLogical(value : Vector512`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftLeftLogical128BitLane due to it being static, abstract and generic.

    ShiftLeftLogical128BitLane : ShiftLeftLogical128BitLane_MethodGroup
    class ShiftLeftLogical128BitLane_MethodGroup:
        def __call__(self, value: Vector512_1[int], numBytes: int) -> Vector512_1[int]:...
        # Method ShiftLeftLogical128BitLane(value : Vector512`1, numBytes : Byte) was skipped since it collides with above method

    # Skipped ShiftLeftLogicalVariable due to it being static, abstract and generic.

    ShiftLeftLogicalVariable : ShiftLeftLogicalVariable_MethodGroup
    class ShiftLeftLogicalVariable_MethodGroup:
        def __call__(self, value: Vector512_1[int], count: Vector512_1[int]) -> Vector512_1[int]:...
        # Method ShiftLeftLogicalVariable(value : Vector512`1, count : Vector512`1) was skipped since it collides with above method

    # Skipped ShiftRightArithmetic due to it being static, abstract and generic.

    ShiftRightArithmetic : ShiftRightArithmetic_MethodGroup
    class ShiftRightArithmetic_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector512_1[int], count: int) -> Vector512_1[int]:...
        @typing.overload
        def __call__(self, value: Vector512_1[int], count: Vector128_1[int]) -> Vector512_1[int]:...

    # Skipped ShiftRightLogical due to it being static, abstract and generic.

    ShiftRightLogical : ShiftRightLogical_MethodGroup
    class ShiftRightLogical_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector512_1[int], count: int) -> Vector512_1[int]:...
        # Method ShiftRightLogical(value : Vector512`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector512_1[int], count: Vector128_1[int]) -> Vector512_1[int]:...
        # Method ShiftRightLogical(value : Vector512`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftRightLogical128BitLane due to it being static, abstract and generic.

    ShiftRightLogical128BitLane : ShiftRightLogical128BitLane_MethodGroup
    class ShiftRightLogical128BitLane_MethodGroup:
        def __call__(self, value: Vector512_1[int], numBytes: int) -> Vector512_1[int]:...
        # Method ShiftRightLogical128BitLane(value : Vector512`1, numBytes : Byte) was skipped since it collides with above method

    # Skipped ShiftRightLogicalVariable due to it being static, abstract and generic.

    ShiftRightLogicalVariable : ShiftRightLogicalVariable_MethodGroup
    class ShiftRightLogicalVariable_MethodGroup:
        def __call__(self, value: Vector512_1[int], count: Vector512_1[int]) -> Vector512_1[int]:...
        # Method ShiftRightLogicalVariable(value : Vector512`1, count : Vector512`1) was skipped since it collides with above method

    # Skipped Shuffle due to it being static, abstract and generic.

    Shuffle : Shuffle_MethodGroup
    class Shuffle_MethodGroup:
        def __call__(self, value: Vector512_1[int], mask: Vector512_1[int]) -> Vector512_1[int]:...
        # Method Shuffle(value : Vector512`1, mask : Vector512`1) was skipped since it collides with above method

    # Skipped ShuffleHigh due to it being static, abstract and generic.

    ShuffleHigh : ShuffleHigh_MethodGroup
    class ShuffleHigh_MethodGroup:
        def __call__(self, value: Vector512_1[int], control: int) -> Vector512_1[int]:...
        # Method ShuffleHigh(value : Vector512`1, control : Byte) was skipped since it collides with above method

    # Skipped ShuffleLow due to it being static, abstract and generic.

    ShuffleLow : ShuffleLow_MethodGroup
    class ShuffleLow_MethodGroup:
        def __call__(self, value: Vector512_1[int], control: int) -> Vector512_1[int]:...
        # Method ShuffleLow(value : Vector512`1, control : Byte) was skipped since it collides with above method

    # Skipped Store due to it being static, abstract and generic.

    Store : Store_MethodGroup
    class Store_MethodGroup:
        def __call__(self, address: clr.Reference[int], source: Vector512_1[int]) -> None:...
        # Method Store(address : Byte*, source : Vector512`1) was skipped since it collides with above method
        # Method Store(address : Int16*, source : Vector512`1) was skipped since it collides with above method
        # Method Store(address : UInt16*, source : Vector512`1) was skipped since it collides with above method

    # Skipped Subtract due to it being static, abstract and generic.

    Subtract : Subtract_MethodGroup
    class Subtract_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method Subtract(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Subtract(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Subtract(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped SubtractSaturate due to it being static, abstract and generic.

    SubtractSaturate : SubtractSaturate_MethodGroup
    class SubtractSaturate_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method SubtractSaturate(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped UnpackHigh due to it being static, abstract and generic.

    UnpackHigh : UnpackHigh_MethodGroup
    class UnpackHigh_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method UnpackHigh(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped UnpackLow due to it being static, abstract and generic.

    UnpackLow : UnpackLow_MethodGroup
    class UnpackLow_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method UnpackLow(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method


    class VL(Avx512F.VL):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        # Skipped CompareGreaterThan due to it being static, abstract and generic.

        CompareGreaterThan : CompareGreaterThan_MethodGroup
        class CompareGreaterThan_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
            # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareGreaterThan(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

        # Skipped CompareGreaterThanOrEqual due to it being static, abstract and generic.

        CompareGreaterThanOrEqual : CompareGreaterThanOrEqual_MethodGroup
        class CompareGreaterThanOrEqual_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
            # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareGreaterThanOrEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
            # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareGreaterThanOrEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
            # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareGreaterThanOrEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

        # Skipped CompareLessThan due to it being static, abstract and generic.

        CompareLessThan : CompareLessThan_MethodGroup
        class CompareLessThan_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
            # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareLessThan(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
            # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareLessThan(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
            # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareLessThan(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

        # Skipped CompareLessThanOrEqual due to it being static, abstract and generic.

        CompareLessThanOrEqual : CompareLessThanOrEqual_MethodGroup
        class CompareLessThanOrEqual_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
            # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareLessThanOrEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
            # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareLessThanOrEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
            # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareLessThanOrEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

        # Skipped CompareNotEqual due to it being static, abstract and generic.

        CompareNotEqual : CompareNotEqual_MethodGroup
        class CompareNotEqual_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
            # Method CompareNotEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareNotEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
            # Method CompareNotEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareNotEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
            # Method CompareNotEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareNotEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

        # Skipped ConvertToVector128Byte due to it being static, abstract and generic.

        ConvertToVector128Byte : ConvertToVector128Byte_MethodGroup
        class ConvertToVector128Byte_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128Byte(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128Byte(value : Vector256`1) was skipped since it collides with above method

        # Skipped ConvertToVector128ByteWithSaturation due to it being static, abstract and generic.

        ConvertToVector128ByteWithSaturation : ConvertToVector128ByteWithSaturation_MethodGroup
        class ConvertToVector128ByteWithSaturation_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector128_1[int]:...

        # Skipped ConvertToVector128SByte due to it being static, abstract and generic.

        ConvertToVector128SByte : ConvertToVector128SByte_MethodGroup
        class ConvertToVector128SByte_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128SByte(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128SByte(value : Vector256`1) was skipped since it collides with above method

        # Skipped ConvertToVector128SByteWithSaturation due to it being static, abstract and generic.

        ConvertToVector128SByteWithSaturation : ConvertToVector128SByteWithSaturation_MethodGroup
        class ConvertToVector128SByteWithSaturation_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector128_1[int]:...

        # Skipped PermuteVar16x16 due to it being static, abstract and generic.

        PermuteVar16x16 : PermuteVar16x16_MethodGroup
        class PermuteVar16x16_MethodGroup:
            def __call__(self, left: Vector256_1[int], control: Vector256_1[int]) -> Vector256_1[int]:...
            # Method PermuteVar16x16(left : Vector256`1, control : Vector256`1) was skipped since it collides with above method

        # Skipped PermuteVar16x16x2 due to it being static, abstract and generic.

        PermuteVar16x16x2 : PermuteVar16x16x2_MethodGroup
        class PermuteVar16x16x2_MethodGroup:
            def __call__(self, lower: Vector256_1[int], indices: Vector256_1[int], upper: Vector256_1[int]) -> Vector256_1[int]:...
            # Method PermuteVar16x16x2(lower : Vector256`1, indices : Vector256`1, upper : Vector256`1) was skipped since it collides with above method

        # Skipped PermuteVar8x16 due to it being static, abstract and generic.

        PermuteVar8x16 : PermuteVar8x16_MethodGroup
        class PermuteVar8x16_MethodGroup:
            def __call__(self, left: Vector128_1[int], control: Vector128_1[int]) -> Vector128_1[int]:...
            # Method PermuteVar8x16(left : Vector128`1, control : Vector128`1) was skipped since it collides with above method

        # Skipped PermuteVar8x16x2 due to it being static, abstract and generic.

        PermuteVar8x16x2 : PermuteVar8x16x2_MethodGroup
        class PermuteVar8x16x2_MethodGroup:
            def __call__(self, lower: Vector128_1[int], indices: Vector128_1[int], upper: Vector128_1[int]) -> Vector128_1[int]:...
            # Method PermuteVar8x16x2(lower : Vector128`1, indices : Vector128`1, upper : Vector128`1) was skipped since it collides with above method

        # Skipped ShiftLeftLogicalVariable due to it being static, abstract and generic.

        ShiftLeftLogicalVariable : ShiftLeftLogicalVariable_MethodGroup
        class ShiftLeftLogicalVariable_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
            # Method ShiftLeftLogicalVariable(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int], count: Vector256_1[int]) -> Vector256_1[int]:...
            # Method ShiftLeftLogicalVariable(value : Vector256`1, count : Vector256`1) was skipped since it collides with above method

        # Skipped ShiftRightArithmeticVariable due to it being static, abstract and generic.

        ShiftRightArithmeticVariable : ShiftRightArithmeticVariable_MethodGroup
        class ShiftRightArithmeticVariable_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, value: Vector256_1[int], count: Vector256_1[int]) -> Vector256_1[int]:...

        # Skipped ShiftRightLogicalVariable due to it being static, abstract and generic.

        ShiftRightLogicalVariable : ShiftRightLogicalVariable_MethodGroup
        class ShiftRightLogicalVariable_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
            # Method ShiftRightLogicalVariable(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int], count: Vector256_1[int]) -> Vector256_1[int]:...
            # Method ShiftRightLogicalVariable(value : Vector256`1, count : Vector256`1) was skipped since it collides with above method

        # Skipped SumAbsoluteDifferencesInBlock32 due to it being static, abstract and generic.

        SumAbsoluteDifferencesInBlock32 : SumAbsoluteDifferencesInBlock32_MethodGroup
        class SumAbsoluteDifferencesInBlock32_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[int], right: Vector128_1[int], control: int) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, left: Vector256_1[int], right: Vector256_1[int], control: int) -> Vector256_1[int]:...



    class X64(Avx512F.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...



class Avx512CD(Avx512F):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    # Skipped DetectConflicts due to it being static, abstract and generic.

    DetectConflicts : DetectConflicts_MethodGroup
    class DetectConflicts_MethodGroup:
        def __call__(self, value: Vector512_1[int]) -> Vector512_1[int]:...
        # Method DetectConflicts(value : Vector512`1) was skipped since it collides with above method
        # Method DetectConflicts(value : Vector512`1) was skipped since it collides with above method
        # Method DetectConflicts(value : Vector512`1) was skipped since it collides with above method

    # Skipped LeadingZeroCount due to it being static, abstract and generic.

    LeadingZeroCount : LeadingZeroCount_MethodGroup
    class LeadingZeroCount_MethodGroup:
        def __call__(self, value: Vector512_1[int]) -> Vector512_1[int]:...
        # Method LeadingZeroCount(value : Vector512`1) was skipped since it collides with above method
        # Method LeadingZeroCount(value : Vector512`1) was skipped since it collides with above method
        # Method LeadingZeroCount(value : Vector512`1) was skipped since it collides with above method


    class VL(Avx512F.VL):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        # Skipped DetectConflicts due to it being static, abstract and generic.

        DetectConflicts : DetectConflicts_MethodGroup
        class DetectConflicts_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            # Method DetectConflicts(value : Vector128`1) was skipped since it collides with above method
            # Method DetectConflicts(value : Vector128`1) was skipped since it collides with above method
            # Method DetectConflicts(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector256_1[int]:...
            # Method DetectConflicts(value : Vector256`1) was skipped since it collides with above method
            # Method DetectConflicts(value : Vector256`1) was skipped since it collides with above method
            # Method DetectConflicts(value : Vector256`1) was skipped since it collides with above method

        # Skipped LeadingZeroCount due to it being static, abstract and generic.

        LeadingZeroCount : LeadingZeroCount_MethodGroup
        class LeadingZeroCount_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            # Method LeadingZeroCount(value : Vector128`1) was skipped since it collides with above method
            # Method LeadingZeroCount(value : Vector128`1) was skipped since it collides with above method
            # Method LeadingZeroCount(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector256_1[int]:...
            # Method LeadingZeroCount(value : Vector256`1) was skipped since it collides with above method
            # Method LeadingZeroCount(value : Vector256`1) was skipped since it collides with above method
            # Method LeadingZeroCount(value : Vector256`1) was skipped since it collides with above method



    class X64(Avx512F.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...



class Avx512DQ(Avx512F):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    # Skipped And due to it being static, abstract and generic.

    And : And_MethodGroup
    class And_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method And(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped AndNot due to it being static, abstract and generic.

    AndNot : AndNot_MethodGroup
    class AndNot_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method AndNot(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped BroadcastPairScalarToVector512 due to it being static, abstract and generic.

    BroadcastPairScalarToVector512 : BroadcastPairScalarToVector512_MethodGroup
    class BroadcastPairScalarToVector512_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector512_1[float]:...
        # Method BroadcastPairScalarToVector512(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastPairScalarToVector512(value : Vector128`1) was skipped since it collides with above method

    # Skipped BroadcastVector128ToVector512 due to it being static, abstract and generic.

    BroadcastVector128ToVector512 : BroadcastVector128ToVector512_MethodGroup
    class BroadcastVector128ToVector512_MethodGroup:
        def __call__(self, address: clr.Reference[float]) -> Vector512_1[float]:...
        # Method BroadcastVector128ToVector512(address : Int64*) was skipped since it collides with above method
        # Method BroadcastVector128ToVector512(address : UInt64*) was skipped since it collides with above method

    # Skipped BroadcastVector256ToVector512 due to it being static, abstract and generic.

    BroadcastVector256ToVector512 : BroadcastVector256ToVector512_MethodGroup
    class BroadcastVector256ToVector512_MethodGroup:
        def __call__(self, address: clr.Reference[float]) -> Vector512_1[float]:...
        # Method BroadcastVector256ToVector512(address : Int32*) was skipped since it collides with above method
        # Method BroadcastVector256ToVector512(address : UInt32*) was skipped since it collides with above method

    # Skipped ConvertToVector256Single due to it being static, abstract and generic.

    ConvertToVector256Single : ConvertToVector256Single_MethodGroup
    class ConvertToVector256Single_MethodGroup:
        def __call__(self, value: Vector512_1[int]) -> Vector256_1[float]:...
        # Method ConvertToVector256Single(value : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToVector512Double due to it being static, abstract and generic.

    ConvertToVector512Double : ConvertToVector512Double_MethodGroup
    class ConvertToVector512Double_MethodGroup:
        def __call__(self, value: Vector512_1[int]) -> Vector512_1[float]:...
        # Method ConvertToVector512Double(value : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToVector512Int64 due to it being static, abstract and generic.

    ConvertToVector512Int64 : ConvertToVector512Int64_MethodGroup
    class ConvertToVector512Int64_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector256_1[float]) -> Vector512_1[int]:...
        @typing.overload
        def __call__(self, value: Vector512_1[float]) -> Vector512_1[int]:...

    # Skipped ConvertToVector512Int64WithTruncation due to it being static, abstract and generic.

    ConvertToVector512Int64WithTruncation : ConvertToVector512Int64WithTruncation_MethodGroup
    class ConvertToVector512Int64WithTruncation_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector256_1[float]) -> Vector512_1[int]:...
        @typing.overload
        def __call__(self, value: Vector512_1[float]) -> Vector512_1[int]:...

    # Skipped ConvertToVector512UInt64 due to it being static, abstract and generic.

    ConvertToVector512UInt64 : ConvertToVector512UInt64_MethodGroup
    class ConvertToVector512UInt64_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector256_1[float]) -> Vector512_1[int]:...
        @typing.overload
        def __call__(self, value: Vector512_1[float]) -> Vector512_1[int]:...

    # Skipped ConvertToVector512UInt64WithTruncation due to it being static, abstract and generic.

    ConvertToVector512UInt64WithTruncation : ConvertToVector512UInt64WithTruncation_MethodGroup
    class ConvertToVector512UInt64WithTruncation_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector256_1[float]) -> Vector512_1[int]:...
        @typing.overload
        def __call__(self, value: Vector512_1[float]) -> Vector512_1[int]:...

    # Skipped ExtractVector128 due to it being static, abstract and generic.

    ExtractVector128 : ExtractVector128_MethodGroup
    class ExtractVector128_MethodGroup:
        def __call__(self, value: Vector512_1[float], index: int) -> Vector128_1[float]:...
        # Method ExtractVector128(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector512`1, index : Byte) was skipped since it collides with above method

    # Skipped ExtractVector256 due to it being static, abstract and generic.

    ExtractVector256 : ExtractVector256_MethodGroup
    class ExtractVector256_MethodGroup:
        def __call__(self, value: Vector512_1[float], index: int) -> Vector256_1[float]:...
        # Method ExtractVector256(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector256(value : Vector512`1, index : Byte) was skipped since it collides with above method

    # Skipped InsertVector128 due to it being static, abstract and generic.

    InsertVector128 : InsertVector128_MethodGroup
    class InsertVector128_MethodGroup:
        def __call__(self, value: Vector512_1[float], data: Vector128_1[float], index: int) -> Vector512_1[float]:...
        # Method InsertVector128(value : Vector512`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector512`1, data : Vector128`1, index : Byte) was skipped since it collides with above method

    # Skipped InsertVector256 due to it being static, abstract and generic.

    InsertVector256 : InsertVector256_MethodGroup
    class InsertVector256_MethodGroup:
        def __call__(self, value: Vector512_1[float], data: Vector256_1[float], index: int) -> Vector512_1[float]:...
        # Method InsertVector256(value : Vector512`1, data : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector256(value : Vector512`1, data : Vector256`1, index : Byte) was skipped since it collides with above method

    # Skipped MultiplyLow due to it being static, abstract and generic.

    MultiplyLow : MultiplyLow_MethodGroup
    class MultiplyLow_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method MultiplyLow(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped Or due to it being static, abstract and generic.

    Or : Or_MethodGroup
    class Or_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method Or(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped Range due to it being static, abstract and generic.

    Range : Range_MethodGroup
    class Range_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float], control: int) -> Vector512_1[float]:...
        # Method Range(left : Vector512`1, right : Vector512`1, control : Byte) was skipped since it collides with above method

    # Skipped RangeScalar due to it being static, abstract and generic.

    RangeScalar : RangeScalar_MethodGroup
    class RangeScalar_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float], control: int) -> Vector128_1[float]:...
        # Method RangeScalar(left : Vector128`1, right : Vector128`1, control : Byte) was skipped since it collides with above method

    # Skipped Reduce due to it being static, abstract and generic.

    Reduce : Reduce_MethodGroup
    class Reduce_MethodGroup:
        def __call__(self, value: Vector512_1[float], control: int) -> Vector512_1[float]:...
        # Method Reduce(value : Vector512`1, control : Byte) was skipped since it collides with above method

    # Skipped ReduceScalar due to it being static, abstract and generic.

    ReduceScalar : ReduceScalar_MethodGroup
    class ReduceScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float], control: int) -> Vector128_1[float]:...
        # Method ReduceScalar(value : Vector128`1, control : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float], control: int) -> Vector128_1[float]:...
        # Method ReduceScalar(upper : Vector128`1, value : Vector128`1, control : Byte) was skipped since it collides with above method

    # Skipped Xor due to it being static, abstract and generic.

    Xor : Xor_MethodGroup
    class Xor_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method Xor(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method


    class VL(Avx512F.VL):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        # Skipped BroadcastPairScalarToVector128 due to it being static, abstract and generic.

        BroadcastPairScalarToVector128 : BroadcastPairScalarToVector128_MethodGroup
        class BroadcastPairScalarToVector128_MethodGroup:
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            # Method BroadcastPairScalarToVector128(value : Vector128`1) was skipped since it collides with above method

        # Skipped BroadcastPairScalarToVector256 due to it being static, abstract and generic.

        BroadcastPairScalarToVector256 : BroadcastPairScalarToVector256_MethodGroup
        class BroadcastPairScalarToVector256_MethodGroup:
            def __call__(self, value: Vector128_1[float]) -> Vector256_1[float]:...
            # Method BroadcastPairScalarToVector256(value : Vector128`1) was skipped since it collides with above method
            # Method BroadcastPairScalarToVector256(value : Vector128`1) was skipped since it collides with above method

        # Skipped ConvertToVector128Double due to it being static, abstract and generic.

        ConvertToVector128Double : ConvertToVector128Double_MethodGroup
        class ConvertToVector128Double_MethodGroup:
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[float]:...
            # Method ConvertToVector128Double(value : Vector128`1) was skipped since it collides with above method

        # Skipped ConvertToVector128Int64 due to it being static, abstract and generic.

        ConvertToVector128Int64 : ConvertToVector128Int64_MethodGroup
        class ConvertToVector128Int64_MethodGroup:
            def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...
            # Method ConvertToVector128Int64(value : Vector128`1) was skipped since it collides with above method

        # Skipped ConvertToVector128Int64WithTruncation due to it being static, abstract and generic.

        ConvertToVector128Int64WithTruncation : ConvertToVector128Int64WithTruncation_MethodGroup
        class ConvertToVector128Int64WithTruncation_MethodGroup:
            def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...
            # Method ConvertToVector128Int64WithTruncation(value : Vector128`1) was skipped since it collides with above method

        # Skipped ConvertToVector128Single due to it being static, abstract and generic.

        ConvertToVector128Single : ConvertToVector128Single_MethodGroup
        class ConvertToVector128Single_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[float]:...
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector128_1[float]:...
            # Method ConvertToVector128Single(value : Vector128`1) was skipped since it collides with above method
            # Method ConvertToVector128Single(value : Vector256`1) was skipped since it collides with above method

        # Skipped ConvertToVector128UInt64 due to it being static, abstract and generic.

        ConvertToVector128UInt64 : ConvertToVector128UInt64_MethodGroup
        class ConvertToVector128UInt64_MethodGroup:
            def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...
            # Method ConvertToVector128UInt64(value : Vector128`1) was skipped since it collides with above method

        # Skipped ConvertToVector128UInt64WithTruncation due to it being static, abstract and generic.

        ConvertToVector128UInt64WithTruncation : ConvertToVector128UInt64WithTruncation_MethodGroup
        class ConvertToVector128UInt64WithTruncation_MethodGroup:
            def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...
            # Method ConvertToVector128UInt64WithTruncation(value : Vector128`1) was skipped since it collides with above method

        # Skipped ConvertToVector256Double due to it being static, abstract and generic.

        ConvertToVector256Double : ConvertToVector256Double_MethodGroup
        class ConvertToVector256Double_MethodGroup:
            def __call__(self, value: Vector256_1[int]) -> Vector256_1[float]:...
            # Method ConvertToVector256Double(value : Vector256`1) was skipped since it collides with above method

        # Skipped ConvertToVector256Int64 due to it being static, abstract and generic.

        ConvertToVector256Int64 : ConvertToVector256Int64_MethodGroup
        class ConvertToVector256Int64_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[float]) -> Vector256_1[int]:...
            @typing.overload
            def __call__(self, value: Vector256_1[float]) -> Vector256_1[int]:...

        # Skipped ConvertToVector256Int64WithTruncation due to it being static, abstract and generic.

        ConvertToVector256Int64WithTruncation : ConvertToVector256Int64WithTruncation_MethodGroup
        class ConvertToVector256Int64WithTruncation_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[float]) -> Vector256_1[int]:...
            @typing.overload
            def __call__(self, value: Vector256_1[float]) -> Vector256_1[int]:...

        # Skipped ConvertToVector256UInt64 due to it being static, abstract and generic.

        ConvertToVector256UInt64 : ConvertToVector256UInt64_MethodGroup
        class ConvertToVector256UInt64_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[float]) -> Vector256_1[int]:...
            @typing.overload
            def __call__(self, value: Vector256_1[float]) -> Vector256_1[int]:...

        # Skipped ConvertToVector256UInt64WithTruncation due to it being static, abstract and generic.

        ConvertToVector256UInt64WithTruncation : ConvertToVector256UInt64WithTruncation_MethodGroup
        class ConvertToVector256UInt64WithTruncation_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[float]) -> Vector256_1[int]:...
            @typing.overload
            def __call__(self, value: Vector256_1[float]) -> Vector256_1[int]:...

        # Skipped MultiplyLow due to it being static, abstract and generic.

        MultiplyLow : MultiplyLow_MethodGroup
        class MultiplyLow_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
            # Method MultiplyLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
            # Method MultiplyLow(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

        # Skipped Range due to it being static, abstract and generic.

        Range : Range_MethodGroup
        class Range_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float], control: int) -> Vector128_1[float]:...
            # Method Range(left : Vector128`1, right : Vector128`1, control : Byte) was skipped since it collides with above method
            @typing.overload
            def __call__(self, left: Vector256_1[float], right: Vector256_1[float], control: int) -> Vector256_1[float]:...
            # Method Range(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method

        # Skipped Reduce due to it being static, abstract and generic.

        Reduce : Reduce_MethodGroup
        class Reduce_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[float], control: int) -> Vector128_1[float]:...
            # Method Reduce(value : Vector128`1, control : Byte) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[float], control: int) -> Vector256_1[float]:...
            # Method Reduce(value : Vector256`1, control : Byte) was skipped since it collides with above method



    class X64(Avx512F.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...



class Avx512F(Avx2):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def ConvertScalarToVector128Double(upper: Vector128_1[float], value: int) -> Vector128_1[float]: ...
    @staticmethod
    def ConvertScalarToVector128Single(upper: Vector128_1[float], value: int) -> Vector128_1[float]: ...
    @staticmethod
    def ConvertToVector128Int16WithSaturation(value: Vector512_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def ConvertToVector128UInt16WithSaturation(value: Vector512_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def ConvertToVector256Int16WithSaturation(value: Vector512_1[int]) -> Vector256_1[int]: ...
    @staticmethod
    def ConvertToVector256Int32WithSaturation(value: Vector512_1[int]) -> Vector256_1[int]: ...
    @staticmethod
    def ConvertToVector256Int32WithTruncation(value: Vector512_1[float]) -> Vector256_1[int]: ...
    @staticmethod
    def ConvertToVector256Single(value: Vector512_1[float]) -> Vector256_1[float]: ...
    @staticmethod
    def ConvertToVector256UInt16WithSaturation(value: Vector512_1[int]) -> Vector256_1[int]: ...
    @staticmethod
    def ConvertToVector256UInt32WithSaturation(value: Vector512_1[int]) -> Vector256_1[int]: ...
    @staticmethod
    def ConvertToVector256UInt32WithTruncation(value: Vector512_1[float]) -> Vector256_1[int]: ...
    @staticmethod
    def ConvertToVector512Int32WithTruncation(value: Vector512_1[float]) -> Vector512_1[int]: ...
    @staticmethod
    def ConvertToVector512UInt32WithTruncation(value: Vector512_1[float]) -> Vector512_1[int]: ...
    @staticmethod
    def DuplicateOddIndexed(value: Vector512_1[float]) -> Vector512_1[float]: ...
    @staticmethod
    def Permute2x64(value: Vector512_1[float], control: int) -> Vector512_1[float]: ...
    @staticmethod
    def Permute4x32(value: Vector512_1[float], control: int) -> Vector512_1[float]: ...
    @staticmethod
    def PermuteVar2x64(left: Vector512_1[float], control: Vector512_1[int]) -> Vector512_1[float]: ...
    @staticmethod
    def PermuteVar4x32(left: Vector512_1[float], control: Vector512_1[int]) -> Vector512_1[float]: ...
    # Skipped Abs due to it being static, abstract and generic.

    Abs : Abs_MethodGroup
    class Abs_MethodGroup:
        def __call__(self, value: Vector512_1[int]) -> Vector512_1[int]:...
        # Method Abs(value : Vector512`1) was skipped since it collides with above method

    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method Add(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Add(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Add(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Add(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Add(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped AlignRight32 due to it being static, abstract and generic.

    AlignRight32 : AlignRight32_MethodGroup
    class AlignRight32_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int], mask: int) -> Vector512_1[int]:...
        # Method AlignRight32(left : Vector512`1, right : Vector512`1, mask : Byte) was skipped since it collides with above method

    # Skipped AlignRight64 due to it being static, abstract and generic.

    AlignRight64 : AlignRight64_MethodGroup
    class AlignRight64_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int], mask: int) -> Vector512_1[int]:...
        # Method AlignRight64(left : Vector512`1, right : Vector512`1, mask : Byte) was skipped since it collides with above method

    # Skipped And due to it being static, abstract and generic.

    And : And_MethodGroup
    class And_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method And(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method And(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method And(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method And(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method And(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method And(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method And(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped AndNot due to it being static, abstract and generic.

    AndNot : AndNot_MethodGroup
    class AndNot_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method AndNot(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method AndNot(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method AndNot(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method AndNot(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method AndNot(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method AndNot(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method AndNot(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped BlendVariable due to it being static, abstract and generic.

    BlendVariable : BlendVariable_MethodGroup
    class BlendVariable_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float], mask: Vector512_1[float]) -> Vector512_1[float]:...
        # Method BlendVariable(left : Vector512`1, right : Vector512`1, mask : Vector512`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector512`1, right : Vector512`1, mask : Vector512`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector512`1, right : Vector512`1, mask : Vector512`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector512`1, right : Vector512`1, mask : Vector512`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector512`1, right : Vector512`1, mask : Vector512`1) was skipped since it collides with above method

    # Skipped BroadcastScalarToVector512 due to it being static, abstract and generic.

    BroadcastScalarToVector512 : BroadcastScalarToVector512_MethodGroup
    class BroadcastScalarToVector512_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector512_1[float]:...
        # Method BroadcastScalarToVector512(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector512(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector512(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector512(value : Vector128`1) was skipped since it collides with above method
        # Method BroadcastScalarToVector512(value : Vector128`1) was skipped since it collides with above method

    # Skipped BroadcastVector128ToVector512 due to it being static, abstract and generic.

    BroadcastVector128ToVector512 : BroadcastVector128ToVector512_MethodGroup
    class BroadcastVector128ToVector512_MethodGroup:
        def __call__(self, address: clr.Reference[float]) -> Vector512_1[float]:...
        # Method BroadcastVector128ToVector512(address : Int32*) was skipped since it collides with above method
        # Method BroadcastVector128ToVector512(address : UInt32*) was skipped since it collides with above method

    # Skipped BroadcastVector256ToVector512 due to it being static, abstract and generic.

    BroadcastVector256ToVector512 : BroadcastVector256ToVector512_MethodGroup
    class BroadcastVector256ToVector512_MethodGroup:
        def __call__(self, address: clr.Reference[float]) -> Vector512_1[float]:...
        # Method BroadcastVector256ToVector512(address : Int64*) was skipped since it collides with above method
        # Method BroadcastVector256ToVector512(address : UInt64*) was skipped since it collides with above method

    # Skipped Compare due to it being static, abstract and generic.

    Compare : Compare_MethodGroup
    class Compare_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float], mode: FloatComparisonMode) -> Vector512_1[float]:...
        # Method Compare(left : Vector512`1, right : Vector512`1, mode : FloatComparisonMode) was skipped since it collides with above method

    # Skipped CompareEqual due to it being static, abstract and generic.

    CompareEqual : CompareEqual_MethodGroup
    class CompareEqual_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method CompareEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped CompareGreaterThan due to it being static, abstract and generic.

    CompareGreaterThan : CompareGreaterThan_MethodGroup
    class CompareGreaterThan_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method CompareGreaterThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped CompareGreaterThanOrEqual due to it being static, abstract and generic.

    CompareGreaterThanOrEqual : CompareGreaterThanOrEqual_MethodGroup
    class CompareGreaterThanOrEqual_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method CompareGreaterThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped CompareLessThan due to it being static, abstract and generic.

    CompareLessThan : CompareLessThan_MethodGroup
    class CompareLessThan_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method CompareLessThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped CompareLessThanOrEqual due to it being static, abstract and generic.

    CompareLessThanOrEqual : CompareLessThanOrEqual_MethodGroup
    class CompareLessThanOrEqual_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method CompareLessThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped CompareNotEqual due to it being static, abstract and generic.

    CompareNotEqual : CompareNotEqual_MethodGroup
    class CompareNotEqual_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method CompareNotEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareNotEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareNotEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareNotEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method CompareNotEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped CompareNotGreaterThan due to it being static, abstract and generic.

    CompareNotGreaterThan : CompareNotGreaterThan_MethodGroup
    class CompareNotGreaterThan_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method CompareNotGreaterThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped CompareNotGreaterThanOrEqual due to it being static, abstract and generic.

    CompareNotGreaterThanOrEqual : CompareNotGreaterThanOrEqual_MethodGroup
    class CompareNotGreaterThanOrEqual_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method CompareNotGreaterThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped CompareNotLessThan due to it being static, abstract and generic.

    CompareNotLessThan : CompareNotLessThan_MethodGroup
    class CompareNotLessThan_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method CompareNotLessThan(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped CompareNotLessThanOrEqual due to it being static, abstract and generic.

    CompareNotLessThanOrEqual : CompareNotLessThanOrEqual_MethodGroup
    class CompareNotLessThanOrEqual_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method CompareNotLessThanOrEqual(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped CompareOrdered due to it being static, abstract and generic.

    CompareOrdered : CompareOrdered_MethodGroup
    class CompareOrdered_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method CompareOrdered(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped CompareUnordered due to it being static, abstract and generic.

    CompareUnordered : CompareUnordered_MethodGroup
    class CompareUnordered_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method CompareUnordered(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToUInt32 due to it being static, abstract and generic.

    ConvertToUInt32 : ConvertToUInt32_MethodGroup
    class ConvertToUInt32_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> int:...
        # Method ConvertToUInt32(value : Vector128`1) was skipped since it collides with above method

    # Skipped ConvertToUInt32WithTruncation due to it being static, abstract and generic.

    ConvertToUInt32WithTruncation : ConvertToUInt32WithTruncation_MethodGroup
    class ConvertToUInt32WithTruncation_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> int:...
        # Method ConvertToUInt32WithTruncation(value : Vector128`1) was skipped since it collides with above method

    # Skipped ConvertToVector128Byte due to it being static, abstract and generic.

    ConvertToVector128Byte : ConvertToVector128Byte_MethodGroup
    class ConvertToVector128Byte_MethodGroup:
        def __call__(self, value: Vector512_1[int]) -> Vector128_1[int]:...
        # Method ConvertToVector128Byte(value : Vector512`1) was skipped since it collides with above method
        # Method ConvertToVector128Byte(value : Vector512`1) was skipped since it collides with above method
        # Method ConvertToVector128Byte(value : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToVector128ByteWithSaturation due to it being static, abstract and generic.

    ConvertToVector128ByteWithSaturation : ConvertToVector128ByteWithSaturation_MethodGroup
    class ConvertToVector128ByteWithSaturation_MethodGroup:
        def __call__(self, value: Vector512_1[int]) -> Vector128_1[int]:...
        # Method ConvertToVector128ByteWithSaturation(value : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToVector128Int16 due to it being static, abstract and generic.

    ConvertToVector128Int16 : ConvertToVector128Int16_MethodGroup
    class ConvertToVector128Int16_MethodGroup:
        def __call__(self, value: Vector512_1[int]) -> Vector128_1[int]:...
        # Method ConvertToVector128Int16(value : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToVector128SByte due to it being static, abstract and generic.

    ConvertToVector128SByte : ConvertToVector128SByte_MethodGroup
    class ConvertToVector128SByte_MethodGroup:
        def __call__(self, value: Vector512_1[int]) -> Vector128_1[int]:...
        # Method ConvertToVector128SByte(value : Vector512`1) was skipped since it collides with above method
        # Method ConvertToVector128SByte(value : Vector512`1) was skipped since it collides with above method
        # Method ConvertToVector128SByte(value : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToVector128SByteWithSaturation due to it being static, abstract and generic.

    ConvertToVector128SByteWithSaturation : ConvertToVector128SByteWithSaturation_MethodGroup
    class ConvertToVector128SByteWithSaturation_MethodGroup:
        def __call__(self, value: Vector512_1[int]) -> Vector128_1[int]:...
        # Method ConvertToVector128SByteWithSaturation(value : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToVector128UInt16 due to it being static, abstract and generic.

    ConvertToVector128UInt16 : ConvertToVector128UInt16_MethodGroup
    class ConvertToVector128UInt16_MethodGroup:
        def __call__(self, value: Vector512_1[int]) -> Vector128_1[int]:...
        # Method ConvertToVector128UInt16(value : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToVector256Int16 due to it being static, abstract and generic.

    ConvertToVector256Int16 : ConvertToVector256Int16_MethodGroup
    class ConvertToVector256Int16_MethodGroup:
        def __call__(self, value: Vector512_1[int]) -> Vector256_1[int]:...
        # Method ConvertToVector256Int16(value : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToVector256Int32 due to it being static, abstract and generic.

    ConvertToVector256Int32 : ConvertToVector256Int32_MethodGroup
    class ConvertToVector256Int32_MethodGroup:
        def __call__(self, value: Vector512_1[float]) -> Vector256_1[int]:...
        # Method ConvertToVector256Int32(value : Vector512`1) was skipped since it collides with above method
        # Method ConvertToVector256Int32(value : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToVector256UInt16 due to it being static, abstract and generic.

    ConvertToVector256UInt16 : ConvertToVector256UInt16_MethodGroup
    class ConvertToVector256UInt16_MethodGroup:
        def __call__(self, value: Vector512_1[int]) -> Vector256_1[int]:...
        # Method ConvertToVector256UInt16(value : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToVector256UInt32 due to it being static, abstract and generic.

    ConvertToVector256UInt32 : ConvertToVector256UInt32_MethodGroup
    class ConvertToVector256UInt32_MethodGroup:
        def __call__(self, value: Vector512_1[float]) -> Vector256_1[int]:...
        # Method ConvertToVector256UInt32(value : Vector512`1) was skipped since it collides with above method
        # Method ConvertToVector256UInt32(value : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToVector512Double due to it being static, abstract and generic.

    ConvertToVector512Double : ConvertToVector512Double_MethodGroup
    class ConvertToVector512Double_MethodGroup:
        def __call__(self, value: Vector256_1[float]) -> Vector512_1[float]:...
        # Method ConvertToVector512Double(value : Vector256`1) was skipped since it collides with above method
        # Method ConvertToVector512Double(value : Vector256`1) was skipped since it collides with above method

    # Skipped ConvertToVector512Int32 due to it being static, abstract and generic.

    ConvertToVector512Int32 : ConvertToVector512Int32_MethodGroup
    class ConvertToVector512Int32_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector512_1[float]) -> Vector512_1[int]:...
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector512_1[int]:...
        # Method ConvertToVector512Int32(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector256_1[int]) -> Vector512_1[int]:...
        # Method ConvertToVector512Int32(value : Vector256`1) was skipped since it collides with above method

    # Skipped ConvertToVector512Int64 due to it being static, abstract and generic.

    ConvertToVector512Int64 : ConvertToVector512Int64_MethodGroup
    class ConvertToVector512Int64_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector512_1[int]:...
        # Method ConvertToVector512Int64(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToVector512Int64(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToVector512Int64(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector256_1[int]) -> Vector512_1[int]:...
        # Method ConvertToVector512Int64(value : Vector256`1) was skipped since it collides with above method

    # Skipped ConvertToVector512Single due to it being static, abstract and generic.

    ConvertToVector512Single : ConvertToVector512Single_MethodGroup
    class ConvertToVector512Single_MethodGroup:
        def __call__(self, value: Vector512_1[int]) -> Vector512_1[float]:...
        # Method ConvertToVector512Single(value : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToVector512UInt32 due to it being static, abstract and generic.

    ConvertToVector512UInt32 : ConvertToVector512UInt32_MethodGroup
    class ConvertToVector512UInt32_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector512_1[float]) -> Vector512_1[int]:...
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector512_1[int]:...
        # Method ConvertToVector512UInt32(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector256_1[int]) -> Vector512_1[int]:...
        # Method ConvertToVector512UInt32(value : Vector256`1) was skipped since it collides with above method

    # Skipped ConvertToVector512UInt64 due to it being static, abstract and generic.

    ConvertToVector512UInt64 : ConvertToVector512UInt64_MethodGroup
    class ConvertToVector512UInt64_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector512_1[int]:...
        # Method ConvertToVector512UInt64(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToVector512UInt64(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToVector512UInt64(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector256_1[int]) -> Vector512_1[int]:...
        # Method ConvertToVector512UInt64(value : Vector256`1) was skipped since it collides with above method

    # Skipped Divide due to it being static, abstract and generic.

    Divide : Divide_MethodGroup
    class Divide_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method Divide(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped DuplicateEvenIndexed due to it being static, abstract and generic.

    DuplicateEvenIndexed : DuplicateEvenIndexed_MethodGroup
    class DuplicateEvenIndexed_MethodGroup:
        def __call__(self, value: Vector512_1[float]) -> Vector512_1[float]:...
        # Method DuplicateEvenIndexed(value : Vector512`1) was skipped since it collides with above method

    # Skipped ExtractVector128 due to it being static, abstract and generic.

    ExtractVector128 : ExtractVector128_MethodGroup
    class ExtractVector128_MethodGroup:
        def __call__(self, value: Vector512_1[float], index: int) -> Vector128_1[float]:...
        # Method ExtractVector128(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector128(value : Vector512`1, index : Byte) was skipped since it collides with above method

    # Skipped ExtractVector256 due to it being static, abstract and generic.

    ExtractVector256 : ExtractVector256_MethodGroup
    class ExtractVector256_MethodGroup:
        def __call__(self, value: Vector512_1[float], index: int) -> Vector256_1[float]:...
        # Method ExtractVector256(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector256(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector256(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector256(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector256(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector256(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector256(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector256(value : Vector512`1, index : Byte) was skipped since it collides with above method
        # Method ExtractVector256(value : Vector512`1, index : Byte) was skipped since it collides with above method

    # Skipped Fixup due to it being static, abstract and generic.

    Fixup : Fixup_MethodGroup
    class Fixup_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float], table: Vector512_1[int], control: int) -> Vector512_1[float]:...
        # Method Fixup(left : Vector512`1, right : Vector512`1, table : Vector512`1, control : Byte) was skipped since it collides with above method

    # Skipped FixupScalar due to it being static, abstract and generic.

    FixupScalar : FixupScalar_MethodGroup
    class FixupScalar_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float], table: Vector128_1[int], control: int) -> Vector128_1[float]:...
        # Method FixupScalar(left : Vector128`1, right : Vector128`1, table : Vector128`1, control : Byte) was skipped since it collides with above method

    # Skipped FusedMultiplyAdd due to it being static, abstract and generic.

    FusedMultiplyAdd : FusedMultiplyAdd_MethodGroup
    class FusedMultiplyAdd_MethodGroup:
        def __call__(self, a: Vector512_1[float], b: Vector512_1[float], c: Vector512_1[float]) -> Vector512_1[float]:...
        # Method FusedMultiplyAdd(a : Vector512`1, b : Vector512`1, c : Vector512`1) was skipped since it collides with above method

    # Skipped FusedMultiplyAddNegated due to it being static, abstract and generic.

    FusedMultiplyAddNegated : FusedMultiplyAddNegated_MethodGroup
    class FusedMultiplyAddNegated_MethodGroup:
        def __call__(self, a: Vector512_1[float], b: Vector512_1[float], c: Vector512_1[float]) -> Vector512_1[float]:...
        # Method FusedMultiplyAddNegated(a : Vector512`1, b : Vector512`1, c : Vector512`1) was skipped since it collides with above method

    # Skipped FusedMultiplyAddSubtract due to it being static, abstract and generic.

    FusedMultiplyAddSubtract : FusedMultiplyAddSubtract_MethodGroup
    class FusedMultiplyAddSubtract_MethodGroup:
        def __call__(self, a: Vector512_1[float], b: Vector512_1[float], c: Vector512_1[float]) -> Vector512_1[float]:...
        # Method FusedMultiplyAddSubtract(a : Vector512`1, b : Vector512`1, c : Vector512`1) was skipped since it collides with above method

    # Skipped FusedMultiplySubtract due to it being static, abstract and generic.

    FusedMultiplySubtract : FusedMultiplySubtract_MethodGroup
    class FusedMultiplySubtract_MethodGroup:
        def __call__(self, a: Vector512_1[float], b: Vector512_1[float], c: Vector512_1[float]) -> Vector512_1[float]:...
        # Method FusedMultiplySubtract(a : Vector512`1, b : Vector512`1, c : Vector512`1) was skipped since it collides with above method

    # Skipped FusedMultiplySubtractAdd due to it being static, abstract and generic.

    FusedMultiplySubtractAdd : FusedMultiplySubtractAdd_MethodGroup
    class FusedMultiplySubtractAdd_MethodGroup:
        def __call__(self, a: Vector512_1[float], b: Vector512_1[float], c: Vector512_1[float]) -> Vector512_1[float]:...
        # Method FusedMultiplySubtractAdd(a : Vector512`1, b : Vector512`1, c : Vector512`1) was skipped since it collides with above method

    # Skipped FusedMultiplySubtractNegated due to it being static, abstract and generic.

    FusedMultiplySubtractNegated : FusedMultiplySubtractNegated_MethodGroup
    class FusedMultiplySubtractNegated_MethodGroup:
        def __call__(self, a: Vector512_1[float], b: Vector512_1[float], c: Vector512_1[float]) -> Vector512_1[float]:...
        # Method FusedMultiplySubtractNegated(a : Vector512`1, b : Vector512`1, c : Vector512`1) was skipped since it collides with above method

    # Skipped GetExponent due to it being static, abstract and generic.

    GetExponent : GetExponent_MethodGroup
    class GetExponent_MethodGroup:
        def __call__(self, value: Vector512_1[float]) -> Vector512_1[float]:...
        # Method GetExponent(value : Vector512`1) was skipped since it collides with above method

    # Skipped GetExponentScalar due to it being static, abstract and generic.

    GetExponentScalar : GetExponentScalar_MethodGroup
    class GetExponentScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method GetExponentScalar(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method GetExponentScalar(upper : Vector128`1, value : Vector128`1) was skipped since it collides with above method

    # Skipped GetMantissa due to it being static, abstract and generic.

    GetMantissa : GetMantissa_MethodGroup
    class GetMantissa_MethodGroup:
        def __call__(self, value: Vector512_1[float], control: int) -> Vector512_1[float]:...
        # Method GetMantissa(value : Vector512`1, control : Byte) was skipped since it collides with above method

    # Skipped GetMantissaScalar due to it being static, abstract and generic.

    GetMantissaScalar : GetMantissaScalar_MethodGroup
    class GetMantissaScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float], control: int) -> Vector128_1[float]:...
        # Method GetMantissaScalar(value : Vector128`1, control : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float], control: int) -> Vector128_1[float]:...
        # Method GetMantissaScalar(upper : Vector128`1, value : Vector128`1, control : Byte) was skipped since it collides with above method

    # Skipped InsertVector128 due to it being static, abstract and generic.

    InsertVector128 : InsertVector128_MethodGroup
    class InsertVector128_MethodGroup:
        def __call__(self, value: Vector512_1[float], data: Vector128_1[float], index: int) -> Vector512_1[float]:...
        # Method InsertVector128(value : Vector512`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector512`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector512`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector512`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector512`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector512`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector512`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector512`1, data : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector128(value : Vector512`1, data : Vector128`1, index : Byte) was skipped since it collides with above method

    # Skipped InsertVector256 due to it being static, abstract and generic.

    InsertVector256 : InsertVector256_MethodGroup
    class InsertVector256_MethodGroup:
        def __call__(self, value: Vector512_1[float], data: Vector256_1[float], index: int) -> Vector512_1[float]:...
        # Method InsertVector256(value : Vector512`1, data : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector256(value : Vector512`1, data : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector256(value : Vector512`1, data : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector256(value : Vector512`1, data : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector256(value : Vector512`1, data : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector256(value : Vector512`1, data : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector256(value : Vector512`1, data : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector256(value : Vector512`1, data : Vector256`1, index : Byte) was skipped since it collides with above method
        # Method InsertVector256(value : Vector512`1, data : Vector256`1, index : Byte) was skipped since it collides with above method

    # Skipped LoadAlignedVector512 due to it being static, abstract and generic.

    LoadAlignedVector512 : LoadAlignedVector512_MethodGroup
    class LoadAlignedVector512_MethodGroup:
        def __call__(self, address: clr.Reference[float]) -> Vector512_1[float]:...
        # Method LoadAlignedVector512(address : Double*) was skipped since it collides with above method
        # Method LoadAlignedVector512(address : Byte*) was skipped since it collides with above method
        # Method LoadAlignedVector512(address : SByte*) was skipped since it collides with above method
        # Method LoadAlignedVector512(address : Int16*) was skipped since it collides with above method
        # Method LoadAlignedVector512(address : UInt16*) was skipped since it collides with above method
        # Method LoadAlignedVector512(address : Int32*) was skipped since it collides with above method
        # Method LoadAlignedVector512(address : UInt32*) was skipped since it collides with above method
        # Method LoadAlignedVector512(address : Int64*) was skipped since it collides with above method
        # Method LoadAlignedVector512(address : UInt64*) was skipped since it collides with above method

    # Skipped LoadAlignedVector512NonTemporal due to it being static, abstract and generic.

    LoadAlignedVector512NonTemporal : LoadAlignedVector512NonTemporal_MethodGroup
    class LoadAlignedVector512NonTemporal_MethodGroup:
        def __call__(self, address: clr.Reference[int]) -> Vector512_1[int]:...
        # Method LoadAlignedVector512NonTemporal(address : Byte*) was skipped since it collides with above method
        # Method LoadAlignedVector512NonTemporal(address : Int16*) was skipped since it collides with above method
        # Method LoadAlignedVector512NonTemporal(address : UInt16*) was skipped since it collides with above method
        # Method LoadAlignedVector512NonTemporal(address : Int32*) was skipped since it collides with above method
        # Method LoadAlignedVector512NonTemporal(address : UInt32*) was skipped since it collides with above method
        # Method LoadAlignedVector512NonTemporal(address : Int64*) was skipped since it collides with above method
        # Method LoadAlignedVector512NonTemporal(address : UInt64*) was skipped since it collides with above method

    # Skipped LoadVector512 due to it being static, abstract and generic.

    LoadVector512 : LoadVector512_MethodGroup
    class LoadVector512_MethodGroup:
        def __call__(self, address: clr.Reference[float]) -> Vector512_1[float]:...
        # Method LoadVector512(address : Double*) was skipped since it collides with above method
        # Method LoadVector512(address : SByte*) was skipped since it collides with above method
        # Method LoadVector512(address : Byte*) was skipped since it collides with above method
        # Method LoadVector512(address : Int16*) was skipped since it collides with above method
        # Method LoadVector512(address : UInt16*) was skipped since it collides with above method
        # Method LoadVector512(address : Int32*) was skipped since it collides with above method
        # Method LoadVector512(address : UInt32*) was skipped since it collides with above method
        # Method LoadVector512(address : Int64*) was skipped since it collides with above method
        # Method LoadVector512(address : UInt64*) was skipped since it collides with above method

    # Skipped Max due to it being static, abstract and generic.

    Max : Max_MethodGroup
    class Max_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method Max(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Max(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Max(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Max(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Max(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped Min due to it being static, abstract and generic.

    Min : Min_MethodGroup
    class Min_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method Min(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Min(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Min(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Min(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Min(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method Multiply(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Multiply(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Multiply(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped MultiplyLow due to it being static, abstract and generic.

    MultiplyLow : MultiplyLow_MethodGroup
    class MultiplyLow_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method MultiplyLow(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped Or due to it being static, abstract and generic.

    Or : Or_MethodGroup
    class Or_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method Or(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Or(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Or(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Or(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Or(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Or(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Or(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped Permute4x64 due to it being static, abstract and generic.

    Permute4x64 : Permute4x64_MethodGroup
    class Permute4x64_MethodGroup:
        def __call__(self, value: Vector512_1[float], control: int) -> Vector512_1[float]:...
        # Method Permute4x64(value : Vector512`1, control : Byte) was skipped since it collides with above method
        # Method Permute4x64(value : Vector512`1, control : Byte) was skipped since it collides with above method

    # Skipped PermuteVar16x32 due to it being static, abstract and generic.

    PermuteVar16x32 : PermuteVar16x32_MethodGroup
    class PermuteVar16x32_MethodGroup:
        def __call__(self, left: Vector512_1[float], control: Vector512_1[int]) -> Vector512_1[float]:...
        # Method PermuteVar16x32(left : Vector512`1, control : Vector512`1) was skipped since it collides with above method
        # Method PermuteVar16x32(left : Vector512`1, control : Vector512`1) was skipped since it collides with above method

    # Skipped PermuteVar16x32x2 due to it being static, abstract and generic.

    PermuteVar16x32x2 : PermuteVar16x32x2_MethodGroup
    class PermuteVar16x32x2_MethodGroup:
        def __call__(self, lower: Vector512_1[float], indices: Vector512_1[int], upper: Vector512_1[float]) -> Vector512_1[float]:...
        # Method PermuteVar16x32x2(lower : Vector512`1, indices : Vector512`1, upper : Vector512`1) was skipped since it collides with above method
        # Method PermuteVar16x32x2(lower : Vector512`1, indices : Vector512`1, upper : Vector512`1) was skipped since it collides with above method

    # Skipped PermuteVar8x64 due to it being static, abstract and generic.

    PermuteVar8x64 : PermuteVar8x64_MethodGroup
    class PermuteVar8x64_MethodGroup:
        def __call__(self, value: Vector512_1[float], control: Vector512_1[int]) -> Vector512_1[float]:...
        # Method PermuteVar8x64(value : Vector512`1, control : Vector512`1) was skipped since it collides with above method
        # Method PermuteVar8x64(value : Vector512`1, control : Vector512`1) was skipped since it collides with above method

    # Skipped PermuteVar8x64x2 due to it being static, abstract and generic.

    PermuteVar8x64x2 : PermuteVar8x64x2_MethodGroup
    class PermuteVar8x64x2_MethodGroup:
        def __call__(self, lower: Vector512_1[float], indices: Vector512_1[int], upper: Vector512_1[float]) -> Vector512_1[float]:...
        # Method PermuteVar8x64x2(lower : Vector512`1, indices : Vector512`1, upper : Vector512`1) was skipped since it collides with above method
        # Method PermuteVar8x64x2(lower : Vector512`1, indices : Vector512`1, upper : Vector512`1) was skipped since it collides with above method

    # Skipped Reciprocal14 due to it being static, abstract and generic.

    Reciprocal14 : Reciprocal14_MethodGroup
    class Reciprocal14_MethodGroup:
        def __call__(self, value: Vector512_1[float]) -> Vector512_1[float]:...
        # Method Reciprocal14(value : Vector512`1) was skipped since it collides with above method

    # Skipped Reciprocal14Scalar due to it being static, abstract and generic.

    Reciprocal14Scalar : Reciprocal14Scalar_MethodGroup
    class Reciprocal14Scalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Reciprocal14Scalar(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Reciprocal14Scalar(upper : Vector128`1, value : Vector128`1) was skipped since it collides with above method

    # Skipped ReciprocalSqrt14 due to it being static, abstract and generic.

    ReciprocalSqrt14 : ReciprocalSqrt14_MethodGroup
    class ReciprocalSqrt14_MethodGroup:
        def __call__(self, value: Vector512_1[float]) -> Vector512_1[float]:...
        # Method ReciprocalSqrt14(value : Vector512`1) was skipped since it collides with above method

    # Skipped ReciprocalSqrt14Scalar due to it being static, abstract and generic.

    ReciprocalSqrt14Scalar : ReciprocalSqrt14Scalar_MethodGroup
    class ReciprocalSqrt14Scalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method ReciprocalSqrt14Scalar(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method ReciprocalSqrt14Scalar(upper : Vector128`1, value : Vector128`1) was skipped since it collides with above method

    # Skipped RotateLeft due to it being static, abstract and generic.

    RotateLeft : RotateLeft_MethodGroup
    class RotateLeft_MethodGroup:
        def __call__(self, value: Vector512_1[int], count: int) -> Vector512_1[int]:...
        # Method RotateLeft(value : Vector512`1, count : Byte) was skipped since it collides with above method
        # Method RotateLeft(value : Vector512`1, count : Byte) was skipped since it collides with above method
        # Method RotateLeft(value : Vector512`1, count : Byte) was skipped since it collides with above method

    # Skipped RotateLeftVariable due to it being static, abstract and generic.

    RotateLeftVariable : RotateLeftVariable_MethodGroup
    class RotateLeftVariable_MethodGroup:
        def __call__(self, value: Vector512_1[int], count: Vector512_1[int]) -> Vector512_1[int]:...
        # Method RotateLeftVariable(value : Vector512`1, count : Vector512`1) was skipped since it collides with above method
        # Method RotateLeftVariable(value : Vector512`1, count : Vector512`1) was skipped since it collides with above method
        # Method RotateLeftVariable(value : Vector512`1, count : Vector512`1) was skipped since it collides with above method

    # Skipped RotateRight due to it being static, abstract and generic.

    RotateRight : RotateRight_MethodGroup
    class RotateRight_MethodGroup:
        def __call__(self, value: Vector512_1[int], count: int) -> Vector512_1[int]:...
        # Method RotateRight(value : Vector512`1, count : Byte) was skipped since it collides with above method
        # Method RotateRight(value : Vector512`1, count : Byte) was skipped since it collides with above method
        # Method RotateRight(value : Vector512`1, count : Byte) was skipped since it collides with above method

    # Skipped RotateRightVariable due to it being static, abstract and generic.

    RotateRightVariable : RotateRightVariable_MethodGroup
    class RotateRightVariable_MethodGroup:
        def __call__(self, value: Vector512_1[int], count: Vector512_1[int]) -> Vector512_1[int]:...
        # Method RotateRightVariable(value : Vector512`1, count : Vector512`1) was skipped since it collides with above method
        # Method RotateRightVariable(value : Vector512`1, count : Vector512`1) was skipped since it collides with above method
        # Method RotateRightVariable(value : Vector512`1, count : Vector512`1) was skipped since it collides with above method

    # Skipped RoundScale due to it being static, abstract and generic.

    RoundScale : RoundScale_MethodGroup
    class RoundScale_MethodGroup:
        def __call__(self, value: Vector512_1[float], control: int) -> Vector512_1[float]:...
        # Method RoundScale(value : Vector512`1, control : Byte) was skipped since it collides with above method

    # Skipped RoundScaleScalar due to it being static, abstract and generic.

    RoundScaleScalar : RoundScaleScalar_MethodGroup
    class RoundScaleScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float], control: int) -> Vector128_1[float]:...
        # Method RoundScaleScalar(value : Vector128`1, control : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float], control: int) -> Vector128_1[float]:...
        # Method RoundScaleScalar(upper : Vector128`1, value : Vector128`1, control : Byte) was skipped since it collides with above method

    # Skipped Scale due to it being static, abstract and generic.

    Scale : Scale_MethodGroup
    class Scale_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method Scale(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped ScaleScalar due to it being static, abstract and generic.

    ScaleScalar : ScaleScalar_MethodGroup
    class ScaleScalar_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method ScaleScalar(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftLeftLogical due to it being static, abstract and generic.

    ShiftLeftLogical : ShiftLeftLogical_MethodGroup
    class ShiftLeftLogical_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector512_1[int], count: int) -> Vector512_1[int]:...
        # Method ShiftLeftLogical(value : Vector512`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector512`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector512`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector512_1[int], count: Vector128_1[int]) -> Vector512_1[int]:...
        # Method ShiftLeftLogical(value : Vector512`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector512`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector512`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftLeftLogicalVariable due to it being static, abstract and generic.

    ShiftLeftLogicalVariable : ShiftLeftLogicalVariable_MethodGroup
    class ShiftLeftLogicalVariable_MethodGroup:
        def __call__(self, value: Vector512_1[int], count: Vector512_1[int]) -> Vector512_1[int]:...
        # Method ShiftLeftLogicalVariable(value : Vector512`1, count : Vector512`1) was skipped since it collides with above method
        # Method ShiftLeftLogicalVariable(value : Vector512`1, count : Vector512`1) was skipped since it collides with above method
        # Method ShiftLeftLogicalVariable(value : Vector512`1, count : Vector512`1) was skipped since it collides with above method

    # Skipped ShiftRightArithmetic due to it being static, abstract and generic.

    ShiftRightArithmetic : ShiftRightArithmetic_MethodGroup
    class ShiftRightArithmetic_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector512_1[int], count: int) -> Vector512_1[int]:...
        # Method ShiftRightArithmetic(value : Vector512`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector512_1[int], count: Vector128_1[int]) -> Vector512_1[int]:...
        # Method ShiftRightArithmetic(value : Vector512`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftRightArithmeticVariable due to it being static, abstract and generic.

    ShiftRightArithmeticVariable : ShiftRightArithmeticVariable_MethodGroup
    class ShiftRightArithmeticVariable_MethodGroup:
        def __call__(self, value: Vector512_1[int], count: Vector512_1[int]) -> Vector512_1[int]:...
        # Method ShiftRightArithmeticVariable(value : Vector512`1, count : Vector512`1) was skipped since it collides with above method

    # Skipped ShiftRightLogical due to it being static, abstract and generic.

    ShiftRightLogical : ShiftRightLogical_MethodGroup
    class ShiftRightLogical_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector512_1[int], count: int) -> Vector512_1[int]:...
        # Method ShiftRightLogical(value : Vector512`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector512`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector512`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector512_1[int], count: Vector128_1[int]) -> Vector512_1[int]:...
        # Method ShiftRightLogical(value : Vector512`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector512`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector512`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftRightLogicalVariable due to it being static, abstract and generic.

    ShiftRightLogicalVariable : ShiftRightLogicalVariable_MethodGroup
    class ShiftRightLogicalVariable_MethodGroup:
        def __call__(self, value: Vector512_1[int], count: Vector512_1[int]) -> Vector512_1[int]:...
        # Method ShiftRightLogicalVariable(value : Vector512`1, count : Vector512`1) was skipped since it collides with above method
        # Method ShiftRightLogicalVariable(value : Vector512`1, count : Vector512`1) was skipped since it collides with above method
        # Method ShiftRightLogicalVariable(value : Vector512`1, count : Vector512`1) was skipped since it collides with above method

    # Skipped Shuffle due to it being static, abstract and generic.

    Shuffle : Shuffle_MethodGroup
    class Shuffle_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector512_1[int], control: int) -> Vector512_1[int]:...
        # Method Shuffle(value : Vector512`1, control : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector512_1[float], right: Vector512_1[float], control: int) -> Vector512_1[float]:...
        # Method Shuffle(value : Vector512`1, right : Vector512`1, control : Byte) was skipped since it collides with above method

    # Skipped Shuffle4x128 due to it being static, abstract and generic.

    Shuffle4x128 : Shuffle4x128_MethodGroup
    class Shuffle4x128_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float], control: int) -> Vector512_1[float]:...
        # Method Shuffle4x128(left : Vector512`1, right : Vector512`1, control : Byte) was skipped since it collides with above method
        # Method Shuffle4x128(left : Vector512`1, right : Vector512`1, control : Byte) was skipped since it collides with above method
        # Method Shuffle4x128(left : Vector512`1, right : Vector512`1, control : Byte) was skipped since it collides with above method
        # Method Shuffle4x128(left : Vector512`1, right : Vector512`1, control : Byte) was skipped since it collides with above method
        # Method Shuffle4x128(left : Vector512`1, right : Vector512`1, control : Byte) was skipped since it collides with above method

    # Skipped Sqrt due to it being static, abstract and generic.

    Sqrt : Sqrt_MethodGroup
    class Sqrt_MethodGroup:
        def __call__(self, value: Vector512_1[float]) -> Vector512_1[float]:...
        # Method Sqrt(value : Vector512`1) was skipped since it collides with above method

    # Skipped Store due to it being static, abstract and generic.

    Store : Store_MethodGroup
    class Store_MethodGroup:
        def __call__(self, address: clr.Reference[float], source: Vector512_1[float]) -> None:...
        # Method Store(address : Double*, source : Vector512`1) was skipped since it collides with above method
        # Method Store(address : SByte*, source : Vector512`1) was skipped since it collides with above method
        # Method Store(address : Byte*, source : Vector512`1) was skipped since it collides with above method
        # Method Store(address : Int16*, source : Vector512`1) was skipped since it collides with above method
        # Method Store(address : UInt16*, source : Vector512`1) was skipped since it collides with above method
        # Method Store(address : Int32*, source : Vector512`1) was skipped since it collides with above method
        # Method Store(address : UInt32*, source : Vector512`1) was skipped since it collides with above method
        # Method Store(address : Int64*, source : Vector512`1) was skipped since it collides with above method
        # Method Store(address : UInt64*, source : Vector512`1) was skipped since it collides with above method

    # Skipped StoreAligned due to it being static, abstract and generic.

    StoreAligned : StoreAligned_MethodGroup
    class StoreAligned_MethodGroup:
        def __call__(self, address: clr.Reference[float], source: Vector512_1[float]) -> None:...
        # Method StoreAligned(address : Double*, source : Vector512`1) was skipped since it collides with above method
        # Method StoreAligned(address : Byte*, source : Vector512`1) was skipped since it collides with above method
        # Method StoreAligned(address : SByte*, source : Vector512`1) was skipped since it collides with above method
        # Method StoreAligned(address : Int16*, source : Vector512`1) was skipped since it collides with above method
        # Method StoreAligned(address : UInt16*, source : Vector512`1) was skipped since it collides with above method
        # Method StoreAligned(address : Int32*, source : Vector512`1) was skipped since it collides with above method
        # Method StoreAligned(address : UInt32*, source : Vector512`1) was skipped since it collides with above method
        # Method StoreAligned(address : Int64*, source : Vector512`1) was skipped since it collides with above method
        # Method StoreAligned(address : UInt64*, source : Vector512`1) was skipped since it collides with above method

    # Skipped StoreAlignedNonTemporal due to it being static, abstract and generic.

    StoreAlignedNonTemporal : StoreAlignedNonTemporal_MethodGroup
    class StoreAlignedNonTemporal_MethodGroup:
        def __call__(self, address: clr.Reference[float], source: Vector512_1[float]) -> None:...
        # Method StoreAlignedNonTemporal(address : Double*, source : Vector512`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : SByte*, source : Vector512`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : Byte*, source : Vector512`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : Int16*, source : Vector512`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : UInt16*, source : Vector512`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : Int32*, source : Vector512`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : UInt32*, source : Vector512`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : Int64*, source : Vector512`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : UInt64*, source : Vector512`1) was skipped since it collides with above method

    # Skipped Subtract due to it being static, abstract and generic.

    Subtract : Subtract_MethodGroup
    class Subtract_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method Subtract(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Subtract(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Subtract(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Subtract(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Subtract(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped TernaryLogic due to it being static, abstract and generic.

    TernaryLogic : TernaryLogic_MethodGroup
    class TernaryLogic_MethodGroup:
        def __call__(self, a: Vector512_1[float], b: Vector512_1[float], c: Vector512_1[float], control: int) -> Vector512_1[float]:...
        # Method TernaryLogic(a : Vector512`1, b : Vector512`1, c : Vector512`1, control : Byte) was skipped since it collides with above method
        # Method TernaryLogic(a : Vector512`1, b : Vector512`1, c : Vector512`1, control : Byte) was skipped since it collides with above method
        # Method TernaryLogic(a : Vector512`1, b : Vector512`1, c : Vector512`1, control : Byte) was skipped since it collides with above method
        # Method TernaryLogic(a : Vector512`1, b : Vector512`1, c : Vector512`1, control : Byte) was skipped since it collides with above method
        # Method TernaryLogic(a : Vector512`1, b : Vector512`1, c : Vector512`1, control : Byte) was skipped since it collides with above method
        # Method TernaryLogic(a : Vector512`1, b : Vector512`1, c : Vector512`1, control : Byte) was skipped since it collides with above method
        # Method TernaryLogic(a : Vector512`1, b : Vector512`1, c : Vector512`1, control : Byte) was skipped since it collides with above method
        # Method TernaryLogic(a : Vector512`1, b : Vector512`1, c : Vector512`1, control : Byte) was skipped since it collides with above method
        # Method TernaryLogic(a : Vector512`1, b : Vector512`1, c : Vector512`1, control : Byte) was skipped since it collides with above method

    # Skipped UnpackHigh due to it being static, abstract and generic.

    UnpackHigh : UnpackHigh_MethodGroup
    class UnpackHigh_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method UnpackHigh(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped UnpackLow due to it being static, abstract and generic.

    UnpackLow : UnpackLow_MethodGroup
    class UnpackLow_MethodGroup:
        def __call__(self, left: Vector512_1[float], right: Vector512_1[float]) -> Vector512_1[float]:...
        # Method UnpackLow(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method

    # Skipped Xor due to it being static, abstract and generic.

    Xor : Xor_MethodGroup
    class Xor_MethodGroup:
        def __call__(self, left: Vector512_1[int], right: Vector512_1[int]) -> Vector512_1[int]:...
        # Method Xor(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Xor(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Xor(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Xor(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Xor(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Xor(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method
        # Method Xor(left : Vector512`1, right : Vector512`1) was skipped since it collides with above method


    class VL(abc.ABC):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        @staticmethod
        def ConvertToVector128Double(value: Vector128_1[int]) -> Vector128_1[float]: ...
        @staticmethod
        def ConvertToVector128Single(value: Vector128_1[int]) -> Vector128_1[float]: ...
        @staticmethod
        def ConvertToVector256Double(value: Vector128_1[int]) -> Vector256_1[float]: ...
        @staticmethod
        def ConvertToVector256Single(value: Vector256_1[int]) -> Vector256_1[float]: ...
        @staticmethod
        def ConvertToVector256UInt32(value: Vector256_1[float]) -> Vector256_1[int]: ...
        @staticmethod
        def ConvertToVector256UInt32WithTruncation(value: Vector256_1[float]) -> Vector256_1[int]: ...
        # Skipped Abs due to it being static, abstract and generic.

        Abs : Abs_MethodGroup
        class Abs_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector256_1[int]:...

        # Skipped AlignRight32 due to it being static, abstract and generic.

        AlignRight32 : AlignRight32_MethodGroup
        class AlignRight32_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[int], right: Vector128_1[int], mask: int) -> Vector128_1[int]:...
            # Method AlignRight32(left : Vector128`1, right : Vector128`1, mask : Byte) was skipped since it collides with above method
            @typing.overload
            def __call__(self, left: Vector256_1[int], right: Vector256_1[int], mask: int) -> Vector256_1[int]:...
            # Method AlignRight32(left : Vector256`1, right : Vector256`1, mask : Byte) was skipped since it collides with above method

        # Skipped AlignRight64 due to it being static, abstract and generic.

        AlignRight64 : AlignRight64_MethodGroup
        class AlignRight64_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[int], right: Vector128_1[int], mask: int) -> Vector128_1[int]:...
            # Method AlignRight64(left : Vector128`1, right : Vector128`1, mask : Byte) was skipped since it collides with above method
            @typing.overload
            def __call__(self, left: Vector256_1[int], right: Vector256_1[int], mask: int) -> Vector256_1[int]:...
            # Method AlignRight64(left : Vector256`1, right : Vector256`1, mask : Byte) was skipped since it collides with above method

        # Skipped CompareGreaterThan due to it being static, abstract and generic.

        CompareGreaterThan : CompareGreaterThan_MethodGroup
        class CompareGreaterThan_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
            # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareGreaterThan(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

        # Skipped CompareGreaterThanOrEqual due to it being static, abstract and generic.

        CompareGreaterThanOrEqual : CompareGreaterThanOrEqual_MethodGroup
        class CompareGreaterThanOrEqual_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
            # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareGreaterThanOrEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
            # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareGreaterThanOrEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
            # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareGreaterThanOrEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

        # Skipped CompareLessThan due to it being static, abstract and generic.

        CompareLessThan : CompareLessThan_MethodGroup
        class CompareLessThan_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
            # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareLessThan(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
            # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareLessThan(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
            # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareLessThan(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

        # Skipped CompareLessThanOrEqual due to it being static, abstract and generic.

        CompareLessThanOrEqual : CompareLessThanOrEqual_MethodGroup
        class CompareLessThanOrEqual_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
            # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareLessThanOrEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
            # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareLessThanOrEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
            # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareLessThanOrEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

        # Skipped CompareNotEqual due to it being static, abstract and generic.

        CompareNotEqual : CompareNotEqual_MethodGroup
        class CompareNotEqual_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
            # Method CompareNotEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareNotEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
            # Method CompareNotEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareNotEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method
            # Method CompareNotEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            # Method CompareNotEqual(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

        # Skipped ConvertToVector128Byte due to it being static, abstract and generic.

        ConvertToVector128Byte : ConvertToVector128Byte_MethodGroup
        class ConvertToVector128Byte_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128Byte(value : Vector128`1) was skipped since it collides with above method
            # Method ConvertToVector128Byte(value : Vector128`1) was skipped since it collides with above method
            # Method ConvertToVector128Byte(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128Byte(value : Vector256`1) was skipped since it collides with above method
            # Method ConvertToVector128Byte(value : Vector256`1) was skipped since it collides with above method
            # Method ConvertToVector128Byte(value : Vector256`1) was skipped since it collides with above method

        # Skipped ConvertToVector128ByteWithSaturation due to it being static, abstract and generic.

        ConvertToVector128ByteWithSaturation : ConvertToVector128ByteWithSaturation_MethodGroup
        class ConvertToVector128ByteWithSaturation_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128ByteWithSaturation(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128ByteWithSaturation(value : Vector256`1) was skipped since it collides with above method

        # Skipped ConvertToVector128Int16 due to it being static, abstract and generic.

        ConvertToVector128Int16 : ConvertToVector128Int16_MethodGroup
        class ConvertToVector128Int16_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128Int16(value : Vector128`1) was skipped since it collides with above method
            # Method ConvertToVector128Int16(value : Vector128`1) was skipped since it collides with above method
            # Method ConvertToVector128Int16(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128Int16(value : Vector256`1) was skipped since it collides with above method
            # Method ConvertToVector128Int16(value : Vector256`1) was skipped since it collides with above method
            # Method ConvertToVector128Int16(value : Vector256`1) was skipped since it collides with above method

        # Skipped ConvertToVector128Int16WithSaturation due to it being static, abstract and generic.

        ConvertToVector128Int16WithSaturation : ConvertToVector128Int16WithSaturation_MethodGroup
        class ConvertToVector128Int16WithSaturation_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128Int16WithSaturation(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128Int16WithSaturation(value : Vector256`1) was skipped since it collides with above method

        # Skipped ConvertToVector128Int32 due to it being static, abstract and generic.

        ConvertToVector128Int32 : ConvertToVector128Int32_MethodGroup
        class ConvertToVector128Int32_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128Int32(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128Int32(value : Vector256`1) was skipped since it collides with above method

        # Skipped ConvertToVector128Int32WithSaturation due to it being static, abstract and generic.

        ConvertToVector128Int32WithSaturation : ConvertToVector128Int32WithSaturation_MethodGroup
        class ConvertToVector128Int32WithSaturation_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector128_1[int]:...

        # Skipped ConvertToVector128SByte due to it being static, abstract and generic.

        ConvertToVector128SByte : ConvertToVector128SByte_MethodGroup
        class ConvertToVector128SByte_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128SByte(value : Vector128`1) was skipped since it collides with above method
            # Method ConvertToVector128SByte(value : Vector128`1) was skipped since it collides with above method
            # Method ConvertToVector128SByte(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128SByte(value : Vector256`1) was skipped since it collides with above method
            # Method ConvertToVector128SByte(value : Vector256`1) was skipped since it collides with above method
            # Method ConvertToVector128SByte(value : Vector256`1) was skipped since it collides with above method

        # Skipped ConvertToVector128SByteWithSaturation due to it being static, abstract and generic.

        ConvertToVector128SByteWithSaturation : ConvertToVector128SByteWithSaturation_MethodGroup
        class ConvertToVector128SByteWithSaturation_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128SByteWithSaturation(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128SByteWithSaturation(value : Vector256`1) was skipped since it collides with above method

        # Skipped ConvertToVector128UInt16 due to it being static, abstract and generic.

        ConvertToVector128UInt16 : ConvertToVector128UInt16_MethodGroup
        class ConvertToVector128UInt16_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128UInt16(value : Vector128`1) was skipped since it collides with above method
            # Method ConvertToVector128UInt16(value : Vector128`1) was skipped since it collides with above method
            # Method ConvertToVector128UInt16(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128UInt16(value : Vector256`1) was skipped since it collides with above method
            # Method ConvertToVector128UInt16(value : Vector256`1) was skipped since it collides with above method
            # Method ConvertToVector128UInt16(value : Vector256`1) was skipped since it collides with above method

        # Skipped ConvertToVector128UInt16WithSaturation due to it being static, abstract and generic.

        ConvertToVector128UInt16WithSaturation : ConvertToVector128UInt16WithSaturation_MethodGroup
        class ConvertToVector128UInt16WithSaturation_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128UInt16WithSaturation(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector128_1[int]:...
            # Method ConvertToVector128UInt16WithSaturation(value : Vector256`1) was skipped since it collides with above method

        # Skipped ConvertToVector128UInt32 due to it being static, abstract and generic.

        ConvertToVector128UInt32 : ConvertToVector128UInt32_MethodGroup
        class ConvertToVector128UInt32_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...
            # Method ConvertToVector128UInt32(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[float]) -> Vector128_1[int]:...
            # Method ConvertToVector128UInt32(value : Vector128`1) was skipped since it collides with above method
            # Method ConvertToVector128UInt32(value : Vector128`1) was skipped since it collides with above method
            # Method ConvertToVector128UInt32(value : Vector256`1) was skipped since it collides with above method
            # Method ConvertToVector128UInt32(value : Vector256`1) was skipped since it collides with above method

        # Skipped ConvertToVector128UInt32WithSaturation due to it being static, abstract and generic.

        ConvertToVector128UInt32WithSaturation : ConvertToVector128UInt32WithSaturation_MethodGroup
        class ConvertToVector128UInt32WithSaturation_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, value: Vector256_1[int]) -> Vector128_1[int]:...

        # Skipped ConvertToVector128UInt32WithTruncation due to it being static, abstract and generic.

        ConvertToVector128UInt32WithTruncation : ConvertToVector128UInt32WithTruncation_MethodGroup
        class ConvertToVector128UInt32WithTruncation_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...
            # Method ConvertToVector128UInt32WithTruncation(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[float]) -> Vector128_1[int]:...

        # Skipped Fixup due to it being static, abstract and generic.

        Fixup : Fixup_MethodGroup
        class Fixup_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float], table: Vector128_1[int], control: int) -> Vector128_1[float]:...
            # Method Fixup(left : Vector128`1, right : Vector128`1, table : Vector128`1, control : Byte) was skipped since it collides with above method
            @typing.overload
            def __call__(self, left: Vector256_1[float], right: Vector256_1[float], table: Vector256_1[int], control: int) -> Vector256_1[float]:...
            # Method Fixup(left : Vector256`1, right : Vector256`1, table : Vector256`1, control : Byte) was skipped since it collides with above method

        # Skipped GetExponent due to it being static, abstract and generic.

        GetExponent : GetExponent_MethodGroup
        class GetExponent_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
            # Method GetExponent(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[float]) -> Vector256_1[float]:...
            # Method GetExponent(value : Vector256`1) was skipped since it collides with above method

        # Skipped GetMantissa due to it being static, abstract and generic.

        GetMantissa : GetMantissa_MethodGroup
        class GetMantissa_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[float], control: int) -> Vector128_1[float]:...
            # Method GetMantissa(value : Vector128`1, control : Byte) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[float], control: int) -> Vector256_1[float]:...
            # Method GetMantissa(value : Vector256`1, control : Byte) was skipped since it collides with above method

        # Skipped Max due to it being static, abstract and generic.

        Max : Max_MethodGroup
        class Max_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
            # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
            # Method Max(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

        # Skipped Min due to it being static, abstract and generic.

        Min : Min_MethodGroup
        class Min_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
            # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
            # Method Min(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

        # Skipped PermuteVar2x64x2 due to it being static, abstract and generic.

        PermuteVar2x64x2 : PermuteVar2x64x2_MethodGroup
        class PermuteVar2x64x2_MethodGroup:
            def __call__(self, lower: Vector128_1[float], indices: Vector128_1[int], upper: Vector128_1[float]) -> Vector128_1[float]:...
            # Method PermuteVar2x64x2(lower : Vector128`1, indices : Vector128`1, upper : Vector128`1) was skipped since it collides with above method
            # Method PermuteVar2x64x2(lower : Vector128`1, indices : Vector128`1, upper : Vector128`1) was skipped since it collides with above method

        # Skipped PermuteVar4x32x2 due to it being static, abstract and generic.

        PermuteVar4x32x2 : PermuteVar4x32x2_MethodGroup
        class PermuteVar4x32x2_MethodGroup:
            def __call__(self, lower: Vector128_1[float], indices: Vector128_1[int], upper: Vector128_1[float]) -> Vector128_1[float]:...
            # Method PermuteVar4x32x2(lower : Vector128`1, indices : Vector128`1, upper : Vector128`1) was skipped since it collides with above method
            # Method PermuteVar4x32x2(lower : Vector128`1, indices : Vector128`1, upper : Vector128`1) was skipped since it collides with above method

        # Skipped PermuteVar4x64 due to it being static, abstract and generic.

        PermuteVar4x64 : PermuteVar4x64_MethodGroup
        class PermuteVar4x64_MethodGroup:
            def __call__(self, value: Vector256_1[float], control: Vector256_1[int]) -> Vector256_1[float]:...
            # Method PermuteVar4x64(value : Vector256`1, control : Vector256`1) was skipped since it collides with above method
            # Method PermuteVar4x64(value : Vector256`1, control : Vector256`1) was skipped since it collides with above method

        # Skipped PermuteVar4x64x2 due to it being static, abstract and generic.

        PermuteVar4x64x2 : PermuteVar4x64x2_MethodGroup
        class PermuteVar4x64x2_MethodGroup:
            def __call__(self, lower: Vector256_1[float], indices: Vector256_1[int], upper: Vector256_1[float]) -> Vector256_1[float]:...
            # Method PermuteVar4x64x2(lower : Vector256`1, indices : Vector256`1, upper : Vector256`1) was skipped since it collides with above method
            # Method PermuteVar4x64x2(lower : Vector256`1, indices : Vector256`1, upper : Vector256`1) was skipped since it collides with above method

        # Skipped PermuteVar8x32x2 due to it being static, abstract and generic.

        PermuteVar8x32x2 : PermuteVar8x32x2_MethodGroup
        class PermuteVar8x32x2_MethodGroup:
            def __call__(self, lower: Vector256_1[float], indices: Vector256_1[int], upper: Vector256_1[float]) -> Vector256_1[float]:...
            # Method PermuteVar8x32x2(lower : Vector256`1, indices : Vector256`1, upper : Vector256`1) was skipped since it collides with above method
            # Method PermuteVar8x32x2(lower : Vector256`1, indices : Vector256`1, upper : Vector256`1) was skipped since it collides with above method

        # Skipped Reciprocal14 due to it being static, abstract and generic.

        Reciprocal14 : Reciprocal14_MethodGroup
        class Reciprocal14_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
            # Method Reciprocal14(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[float]) -> Vector256_1[float]:...
            # Method Reciprocal14(value : Vector256`1) was skipped since it collides with above method

        # Skipped ReciprocalSqrt14 due to it being static, abstract and generic.

        ReciprocalSqrt14 : ReciprocalSqrt14_MethodGroup
        class ReciprocalSqrt14_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
            # Method ReciprocalSqrt14(value : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[float]) -> Vector256_1[float]:...
            # Method ReciprocalSqrt14(value : Vector256`1) was skipped since it collides with above method

        # Skipped RotateLeft due to it being static, abstract and generic.

        RotateLeft : RotateLeft_MethodGroup
        class RotateLeft_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int], count: int) -> Vector128_1[int]:...
            # Method RotateLeft(value : Vector128`1, count : Byte) was skipped since it collides with above method
            # Method RotateLeft(value : Vector128`1, count : Byte) was skipped since it collides with above method
            # Method RotateLeft(value : Vector128`1, count : Byte) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int], count: int) -> Vector256_1[int]:...
            # Method RotateLeft(value : Vector256`1, count : Byte) was skipped since it collides with above method
            # Method RotateLeft(value : Vector256`1, count : Byte) was skipped since it collides with above method
            # Method RotateLeft(value : Vector256`1, count : Byte) was skipped since it collides with above method

        # Skipped RotateLeftVariable due to it being static, abstract and generic.

        RotateLeftVariable : RotateLeftVariable_MethodGroup
        class RotateLeftVariable_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
            # Method RotateLeftVariable(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
            # Method RotateLeftVariable(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
            # Method RotateLeftVariable(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int], count: Vector256_1[int]) -> Vector256_1[int]:...
            # Method RotateLeftVariable(value : Vector256`1, count : Vector256`1) was skipped since it collides with above method
            # Method RotateLeftVariable(value : Vector256`1, count : Vector256`1) was skipped since it collides with above method
            # Method RotateLeftVariable(value : Vector256`1, count : Vector256`1) was skipped since it collides with above method

        # Skipped RotateRight due to it being static, abstract and generic.

        RotateRight : RotateRight_MethodGroup
        class RotateRight_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int], count: int) -> Vector128_1[int]:...
            # Method RotateRight(value : Vector128`1, count : Byte) was skipped since it collides with above method
            # Method RotateRight(value : Vector128`1, count : Byte) was skipped since it collides with above method
            # Method RotateRight(value : Vector128`1, count : Byte) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int], count: int) -> Vector256_1[int]:...
            # Method RotateRight(value : Vector256`1, count : Byte) was skipped since it collides with above method
            # Method RotateRight(value : Vector256`1, count : Byte) was skipped since it collides with above method
            # Method RotateRight(value : Vector256`1, count : Byte) was skipped since it collides with above method

        # Skipped RotateRightVariable due to it being static, abstract and generic.

        RotateRightVariable : RotateRightVariable_MethodGroup
        class RotateRightVariable_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
            # Method RotateRightVariable(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
            # Method RotateRightVariable(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
            # Method RotateRightVariable(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[int], count: Vector256_1[int]) -> Vector256_1[int]:...
            # Method RotateRightVariable(value : Vector256`1, count : Vector256`1) was skipped since it collides with above method
            # Method RotateRightVariable(value : Vector256`1, count : Vector256`1) was skipped since it collides with above method
            # Method RotateRightVariable(value : Vector256`1, count : Vector256`1) was skipped since it collides with above method

        # Skipped RoundScale due to it being static, abstract and generic.

        RoundScale : RoundScale_MethodGroup
        class RoundScale_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[float], control: int) -> Vector128_1[float]:...
            # Method RoundScale(value : Vector128`1, control : Byte) was skipped since it collides with above method
            @typing.overload
            def __call__(self, value: Vector256_1[float], control: int) -> Vector256_1[float]:...
            # Method RoundScale(value : Vector256`1, control : Byte) was skipped since it collides with above method

        # Skipped Scale due to it being static, abstract and generic.

        Scale : Scale_MethodGroup
        class Scale_MethodGroup:
            @typing.overload
            def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
            # Method Scale(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
            @typing.overload
            def __call__(self, left: Vector256_1[float], right: Vector256_1[float]) -> Vector256_1[float]:...
            # Method Scale(left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

        # Skipped ShiftRightArithmetic due to it being static, abstract and generic.

        ShiftRightArithmetic : ShiftRightArithmetic_MethodGroup
        class ShiftRightArithmetic_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int], count: int) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, value: Vector256_1[int], count: int) -> Vector256_1[int]:...
            @typing.overload
            def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, value: Vector256_1[int], count: Vector128_1[int]) -> Vector256_1[int]:...

        # Skipped ShiftRightArithmeticVariable due to it being static, abstract and generic.

        ShiftRightArithmeticVariable : ShiftRightArithmeticVariable_MethodGroup
        class ShiftRightArithmeticVariable_MethodGroup:
            @typing.overload
            def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
            @typing.overload
            def __call__(self, value: Vector256_1[int], count: Vector256_1[int]) -> Vector256_1[int]:...

        # Skipped Shuffle2x128 due to it being static, abstract and generic.

        Shuffle2x128 : Shuffle2x128_MethodGroup
        class Shuffle2x128_MethodGroup:
            def __call__(self, left: Vector256_1[float], right: Vector256_1[float], control: int) -> Vector256_1[float]:...
            # Method Shuffle2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
            # Method Shuffle2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
            # Method Shuffle2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
            # Method Shuffle2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method
            # Method Shuffle2x128(left : Vector256`1, right : Vector256`1, control : Byte) was skipped since it collides with above method

        # Skipped TernaryLogic due to it being static, abstract and generic.

        TernaryLogic : TernaryLogic_MethodGroup
        class TernaryLogic_MethodGroup:
            @typing.overload
            def __call__(self, a: Vector128_1[float], b: Vector128_1[float], c: Vector128_1[float], control: int) -> Vector128_1[float]:...
            # Method TernaryLogic(a : Vector128`1, b : Vector128`1, c : Vector128`1, control : Byte) was skipped since it collides with above method
            @typing.overload
            def __call__(self, a: Vector256_1[float], b: Vector256_1[float], c: Vector256_1[float], control: int) -> Vector256_1[float]:...
            # Method TernaryLogic(a : Vector256`1, b : Vector256`1, c : Vector256`1, control : Byte) was skipped since it collides with above method
            # Method TernaryLogic(a : Vector128`1, b : Vector128`1, c : Vector128`1, control : Byte) was skipped since it collides with above method
            # Method TernaryLogic(a : Vector128`1, b : Vector128`1, c : Vector128`1, control : Byte) was skipped since it collides with above method
            # Method TernaryLogic(a : Vector128`1, b : Vector128`1, c : Vector128`1, control : Byte) was skipped since it collides with above method
            # Method TernaryLogic(a : Vector128`1, b : Vector128`1, c : Vector128`1, control : Byte) was skipped since it collides with above method
            # Method TernaryLogic(a : Vector128`1, b : Vector128`1, c : Vector128`1, control : Byte) was skipped since it collides with above method
            # Method TernaryLogic(a : Vector128`1, b : Vector128`1, c : Vector128`1, control : Byte) was skipped since it collides with above method
            # Method TernaryLogic(a : Vector128`1, b : Vector128`1, c : Vector128`1, control : Byte) was skipped since it collides with above method
            # Method TernaryLogic(a : Vector128`1, b : Vector128`1, c : Vector128`1, control : Byte) was skipped since it collides with above method
            # Method TernaryLogic(a : Vector256`1, b : Vector256`1, c : Vector256`1, control : Byte) was skipped since it collides with above method
            # Method TernaryLogic(a : Vector256`1, b : Vector256`1, c : Vector256`1, control : Byte) was skipped since it collides with above method
            # Method TernaryLogic(a : Vector256`1, b : Vector256`1, c : Vector256`1, control : Byte) was skipped since it collides with above method
            # Method TernaryLogic(a : Vector256`1, b : Vector256`1, c : Vector256`1, control : Byte) was skipped since it collides with above method
            # Method TernaryLogic(a : Vector256`1, b : Vector256`1, c : Vector256`1, control : Byte) was skipped since it collides with above method
            # Method TernaryLogic(a : Vector256`1, b : Vector256`1, c : Vector256`1, control : Byte) was skipped since it collides with above method
            # Method TernaryLogic(a : Vector256`1, b : Vector256`1, c : Vector256`1, control : Byte) was skipped since it collides with above method
            # Method TernaryLogic(a : Vector256`1, b : Vector256`1, c : Vector256`1, control : Byte) was skipped since it collides with above method



    class X64(Avx2.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        @staticmethod
        def ConvertScalarToVector128Double(upper: Vector128_1[float], value: int) -> Vector128_1[float]: ...
        @staticmethod
        def ConvertScalarToVector128Single(upper: Vector128_1[float], value: int) -> Vector128_1[float]: ...
        # Skipped ConvertToUInt64 due to it being static, abstract and generic.

        ConvertToUInt64 : ConvertToUInt64_MethodGroup
        class ConvertToUInt64_MethodGroup:
            def __call__(self, value: Vector128_1[float]) -> int:...
            # Method ConvertToUInt64(value : Vector128`1) was skipped since it collides with above method

        # Skipped ConvertToUInt64WithTruncation due to it being static, abstract and generic.

        ConvertToUInt64WithTruncation : ConvertToUInt64WithTruncation_MethodGroup
        class ConvertToUInt64WithTruncation_MethodGroup:
            def __call__(self, value: Vector128_1[float]) -> int:...
            # Method ConvertToUInt64WithTruncation(value : Vector128`1) was skipped since it collides with above method




class Avx512Vbmi(Avx512BW):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    # Skipped PermuteVar64x8 due to it being static, abstract and generic.

    PermuteVar64x8 : PermuteVar64x8_MethodGroup
    class PermuteVar64x8_MethodGroup:
        def __call__(self, left: Vector512_1[int], control: Vector512_1[int]) -> Vector512_1[int]:...
        # Method PermuteVar64x8(left : Vector512`1, control : Vector512`1) was skipped since it collides with above method

    # Skipped PermuteVar64x8x2 due to it being static, abstract and generic.

    PermuteVar64x8x2 : PermuteVar64x8x2_MethodGroup
    class PermuteVar64x8x2_MethodGroup:
        def __call__(self, lower: Vector512_1[int], indices: Vector512_1[int], upper: Vector512_1[int]) -> Vector512_1[int]:...
        # Method PermuteVar64x8x2(lower : Vector512`1, indices : Vector512`1, upper : Vector512`1) was skipped since it collides with above method


    class VL(Avx512BW.VL):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        # Skipped PermuteVar16x8 due to it being static, abstract and generic.

        PermuteVar16x8 : PermuteVar16x8_MethodGroup
        class PermuteVar16x8_MethodGroup:
            def __call__(self, left: Vector128_1[int], control: Vector128_1[int]) -> Vector128_1[int]:...
            # Method PermuteVar16x8(left : Vector128`1, control : Vector128`1) was skipped since it collides with above method

        # Skipped PermuteVar16x8x2 due to it being static, abstract and generic.

        PermuteVar16x8x2 : PermuteVar16x8x2_MethodGroup
        class PermuteVar16x8x2_MethodGroup:
            def __call__(self, lower: Vector128_1[int], indices: Vector128_1[int], upper: Vector128_1[int]) -> Vector128_1[int]:...
            # Method PermuteVar16x8x2(lower : Vector128`1, indices : Vector128`1, upper : Vector128`1) was skipped since it collides with above method

        # Skipped PermuteVar32x8 due to it being static, abstract and generic.

        PermuteVar32x8 : PermuteVar32x8_MethodGroup
        class PermuteVar32x8_MethodGroup:
            def __call__(self, left: Vector256_1[int], control: Vector256_1[int]) -> Vector256_1[int]:...
            # Method PermuteVar32x8(left : Vector256`1, control : Vector256`1) was skipped since it collides with above method

        # Skipped PermuteVar32x8x2 due to it being static, abstract and generic.

        PermuteVar32x8x2 : PermuteVar32x8x2_MethodGroup
        class PermuteVar32x8x2_MethodGroup:
            def __call__(self, lower: Vector256_1[int], indices: Vector256_1[int], upper: Vector256_1[int]) -> Vector256_1[int]:...
            # Method PermuteVar32x8x2(lower : Vector256`1, indices : Vector256`1, upper : Vector256`1) was skipped since it collides with above method



    class X64(Avx512BW.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...



class AvxVnni(Avx2):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    # Skipped MultiplyWideningAndAdd due to it being static, abstract and generic.

    MultiplyWideningAndAdd : MultiplyWideningAndAdd_MethodGroup
    class MultiplyWideningAndAdd_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyWideningAndAdd(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, addend: Vector256_1[int], left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method MultiplyWideningAndAdd(addend : Vector256`1, left : Vector256`1, right : Vector256`1) was skipped since it collides with above method

    # Skipped MultiplyWideningAndAddSaturate due to it being static, abstract and generic.

    MultiplyWideningAndAddSaturate : MultiplyWideningAndAddSaturate_MethodGroup
    class MultiplyWideningAndAddSaturate_MethodGroup:
        @typing.overload
        def __call__(self, addend: Vector128_1[int], left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyWideningAndAddSaturate(addend : Vector128`1, left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, addend: Vector256_1[int], left: Vector256_1[int], right: Vector256_1[int]) -> Vector256_1[int]:...
        # Method MultiplyWideningAndAddSaturate(addend : Vector256`1, left : Vector256`1, right : Vector256`1) was skipped since it collides with above method


    class X64(Avx2.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...



class Bmi1(X86Base):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def AndNot(left: int, right: int) -> int: ...
    @staticmethod
    def ExtractLowestSetBit(value: int) -> int: ...
    @staticmethod
    def GetMaskUpToLowestSetBit(value: int) -> int: ...
    @staticmethod
    def ResetLowestSetBit(value: int) -> int: ...
    @staticmethod
    def TrailingZeroCount(value: int) -> int: ...
    # Skipped BitFieldExtract due to it being static, abstract and generic.

    BitFieldExtract : BitFieldExtract_MethodGroup
    class BitFieldExtract_MethodGroup:
        @typing.overload
        def __call__(self, value: int, control: int) -> int:...
        @typing.overload
        def __call__(self, value: int, start: int, length: int) -> int:...


    class X64(X86Base.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        @staticmethod
        def AndNot(left: int, right: int) -> int: ...
        @staticmethod
        def ExtractLowestSetBit(value: int) -> int: ...
        @staticmethod
        def GetMaskUpToLowestSetBit(value: int) -> int: ...
        @staticmethod
        def ResetLowestSetBit(value: int) -> int: ...
        @staticmethod
        def TrailingZeroCount(value: int) -> int: ...
        # Skipped BitFieldExtract due to it being static, abstract and generic.

        BitFieldExtract : BitFieldExtract_MethodGroup
        class BitFieldExtract_MethodGroup:
            @typing.overload
            def __call__(self, value: int, control: int) -> int:...
            @typing.overload
            def __call__(self, value: int, start: int, length: int) -> int:...




class Bmi2(X86Base):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def ParallelBitDeposit(value: int, mask: int) -> int: ...
    @staticmethod
    def ParallelBitExtract(value: int, mask: int) -> int: ...
    @staticmethod
    def ZeroHighBits(value: int, index: int) -> int: ...
    # Skipped MultiplyNoFlags due to it being static, abstract and generic.

    MultiplyNoFlags : MultiplyNoFlags_MethodGroup
    class MultiplyNoFlags_MethodGroup:
        @typing.overload
        def __call__(self, left: int, right: int) -> int:...
        @typing.overload
        def __call__(self, left: int, right: int, low: clr.Reference[int]) -> int:...


    class X64(X86Base.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        @staticmethod
        def ParallelBitDeposit(value: int, mask: int) -> int: ...
        @staticmethod
        def ParallelBitExtract(value: int, mask: int) -> int: ...
        @staticmethod
        def ZeroHighBits(value: int, index: int) -> int: ...
        # Skipped MultiplyNoFlags due to it being static, abstract and generic.

        MultiplyNoFlags : MultiplyNoFlags_MethodGroup
        class MultiplyNoFlags_MethodGroup:
            @typing.overload
            def __call__(self, left: int, right: int) -> int:...
            @typing.overload
            def __call__(self, left: int, right: int, low: clr.Reference[int]) -> int:...




class FloatComparisonMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    OrderedEqualNonSignaling : FloatComparisonMode # 0
    OrderedLessThanSignaling : FloatComparisonMode # 1
    OrderedLessThanOrEqualSignaling : FloatComparisonMode # 2
    UnorderedNonSignaling : FloatComparisonMode # 3
    UnorderedNotEqualNonSignaling : FloatComparisonMode # 4
    UnorderedNotLessThanSignaling : FloatComparisonMode # 5
    UnorderedNotLessThanOrEqualSignaling : FloatComparisonMode # 6
    OrderedNonSignaling : FloatComparisonMode # 7
    UnorderedEqualNonSignaling : FloatComparisonMode # 8
    UnorderedNotGreaterThanOrEqualSignaling : FloatComparisonMode # 9
    UnorderedNotGreaterThanSignaling : FloatComparisonMode # 10
    OrderedFalseNonSignaling : FloatComparisonMode # 11
    OrderedNotEqualNonSignaling : FloatComparisonMode # 12
    OrderedGreaterThanOrEqualSignaling : FloatComparisonMode # 13
    OrderedGreaterThanSignaling : FloatComparisonMode # 14
    UnorderedTrueNonSignaling : FloatComparisonMode # 15
    OrderedEqualSignaling : FloatComparisonMode # 16
    OrderedLessThanNonSignaling : FloatComparisonMode # 17
    OrderedLessThanOrEqualNonSignaling : FloatComparisonMode # 18
    UnorderedSignaling : FloatComparisonMode # 19
    UnorderedNotEqualSignaling : FloatComparisonMode # 20
    UnorderedNotLessThanNonSignaling : FloatComparisonMode # 21
    UnorderedNotLessThanOrEqualNonSignaling : FloatComparisonMode # 22
    OrderedSignaling : FloatComparisonMode # 23
    UnorderedEqualSignaling : FloatComparisonMode # 24
    UnorderedNotGreaterThanOrEqualNonSignaling : FloatComparisonMode # 25
    UnorderedNotGreaterThanNonSignaling : FloatComparisonMode # 26
    OrderedFalseSignaling : FloatComparisonMode # 27
    OrderedNotEqualSignaling : FloatComparisonMode # 28
    OrderedGreaterThanOrEqualNonSignaling : FloatComparisonMode # 29
    OrderedGreaterThanNonSignaling : FloatComparisonMode # 30
    UnorderedTrueSignaling : FloatComparisonMode # 31


class Fma(Avx):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    # Skipped MultiplyAdd due to it being static, abstract and generic.

    MultiplyAdd : MultiplyAdd_MethodGroup
    class MultiplyAdd_MethodGroup:
        @typing.overload
        def __call__(self, a: Vector128_1[float], b: Vector128_1[float], c: Vector128_1[float]) -> Vector128_1[float]:...
        # Method MultiplyAdd(a : Vector128`1, b : Vector128`1, c : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, a: Vector256_1[float], b: Vector256_1[float], c: Vector256_1[float]) -> Vector256_1[float]:...
        # Method MultiplyAdd(a : Vector256`1, b : Vector256`1, c : Vector256`1) was skipped since it collides with above method

    # Skipped MultiplyAddNegated due to it being static, abstract and generic.

    MultiplyAddNegated : MultiplyAddNegated_MethodGroup
    class MultiplyAddNegated_MethodGroup:
        @typing.overload
        def __call__(self, a: Vector128_1[float], b: Vector128_1[float], c: Vector128_1[float]) -> Vector128_1[float]:...
        # Method MultiplyAddNegated(a : Vector128`1, b : Vector128`1, c : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, a: Vector256_1[float], b: Vector256_1[float], c: Vector256_1[float]) -> Vector256_1[float]:...
        # Method MultiplyAddNegated(a : Vector256`1, b : Vector256`1, c : Vector256`1) was skipped since it collides with above method

    # Skipped MultiplyAddNegatedScalar due to it being static, abstract and generic.

    MultiplyAddNegatedScalar : MultiplyAddNegatedScalar_MethodGroup
    class MultiplyAddNegatedScalar_MethodGroup:
        def __call__(self, a: Vector128_1[float], b: Vector128_1[float], c: Vector128_1[float]) -> Vector128_1[float]:...
        # Method MultiplyAddNegatedScalar(a : Vector128`1, b : Vector128`1, c : Vector128`1) was skipped since it collides with above method

    # Skipped MultiplyAddScalar due to it being static, abstract and generic.

    MultiplyAddScalar : MultiplyAddScalar_MethodGroup
    class MultiplyAddScalar_MethodGroup:
        def __call__(self, a: Vector128_1[float], b: Vector128_1[float], c: Vector128_1[float]) -> Vector128_1[float]:...
        # Method MultiplyAddScalar(a : Vector128`1, b : Vector128`1, c : Vector128`1) was skipped since it collides with above method

    # Skipped MultiplyAddSubtract due to it being static, abstract and generic.

    MultiplyAddSubtract : MultiplyAddSubtract_MethodGroup
    class MultiplyAddSubtract_MethodGroup:
        @typing.overload
        def __call__(self, a: Vector128_1[float], b: Vector128_1[float], c: Vector128_1[float]) -> Vector128_1[float]:...
        # Method MultiplyAddSubtract(a : Vector128`1, b : Vector128`1, c : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, a: Vector256_1[float], b: Vector256_1[float], c: Vector256_1[float]) -> Vector256_1[float]:...
        # Method MultiplyAddSubtract(a : Vector256`1, b : Vector256`1, c : Vector256`1) was skipped since it collides with above method

    # Skipped MultiplySubtract due to it being static, abstract and generic.

    MultiplySubtract : MultiplySubtract_MethodGroup
    class MultiplySubtract_MethodGroup:
        @typing.overload
        def __call__(self, a: Vector128_1[float], b: Vector128_1[float], c: Vector128_1[float]) -> Vector128_1[float]:...
        # Method MultiplySubtract(a : Vector128`1, b : Vector128`1, c : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, a: Vector256_1[float], b: Vector256_1[float], c: Vector256_1[float]) -> Vector256_1[float]:...
        # Method MultiplySubtract(a : Vector256`1, b : Vector256`1, c : Vector256`1) was skipped since it collides with above method

    # Skipped MultiplySubtractAdd due to it being static, abstract and generic.

    MultiplySubtractAdd : MultiplySubtractAdd_MethodGroup
    class MultiplySubtractAdd_MethodGroup:
        @typing.overload
        def __call__(self, a: Vector128_1[float], b: Vector128_1[float], c: Vector128_1[float]) -> Vector128_1[float]:...
        # Method MultiplySubtractAdd(a : Vector128`1, b : Vector128`1, c : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, a: Vector256_1[float], b: Vector256_1[float], c: Vector256_1[float]) -> Vector256_1[float]:...
        # Method MultiplySubtractAdd(a : Vector256`1, b : Vector256`1, c : Vector256`1) was skipped since it collides with above method

    # Skipped MultiplySubtractNegated due to it being static, abstract and generic.

    MultiplySubtractNegated : MultiplySubtractNegated_MethodGroup
    class MultiplySubtractNegated_MethodGroup:
        @typing.overload
        def __call__(self, a: Vector128_1[float], b: Vector128_1[float], c: Vector128_1[float]) -> Vector128_1[float]:...
        # Method MultiplySubtractNegated(a : Vector128`1, b : Vector128`1, c : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, a: Vector256_1[float], b: Vector256_1[float], c: Vector256_1[float]) -> Vector256_1[float]:...
        # Method MultiplySubtractNegated(a : Vector256`1, b : Vector256`1, c : Vector256`1) was skipped since it collides with above method

    # Skipped MultiplySubtractNegatedScalar due to it being static, abstract and generic.

    MultiplySubtractNegatedScalar : MultiplySubtractNegatedScalar_MethodGroup
    class MultiplySubtractNegatedScalar_MethodGroup:
        def __call__(self, a: Vector128_1[float], b: Vector128_1[float], c: Vector128_1[float]) -> Vector128_1[float]:...
        # Method MultiplySubtractNegatedScalar(a : Vector128`1, b : Vector128`1, c : Vector128`1) was skipped since it collides with above method

    # Skipped MultiplySubtractScalar due to it being static, abstract and generic.

    MultiplySubtractScalar : MultiplySubtractScalar_MethodGroup
    class MultiplySubtractScalar_MethodGroup:
        def __call__(self, a: Vector128_1[float], b: Vector128_1[float], c: Vector128_1[float]) -> Vector128_1[float]:...
        # Method MultiplySubtractScalar(a : Vector128`1, b : Vector128`1, c : Vector128`1) was skipped since it collides with above method


    class X64(Avx.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...



class Lzcnt(X86Base):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def LeadingZeroCount(value: int) -> int: ...

    class X64(X86Base.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        @staticmethod
        def LeadingZeroCount(value: int) -> int: ...



class Pclmulqdq(Sse2):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    # Skipped CarrylessMultiply due to it being static, abstract and generic.

    CarrylessMultiply : CarrylessMultiply_MethodGroup
    class CarrylessMultiply_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int], control: int) -> Vector128_1[int]:...
        # Method CarrylessMultiply(left : Vector128`1, right : Vector128`1, control : Byte) was skipped since it collides with above method


    class X64(Sse2.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...



class Popcnt(Sse42):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def PopCount(value: int) -> int: ...

    class X64(Sse42.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        @staticmethod
        def PopCount(value: int) -> int: ...



class Sse(X86Base):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def Add(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def AddScalar(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def And(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def AndNot(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareGreaterThan(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareGreaterThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareLessThan(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareLessThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareNotEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareNotGreaterThan(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareNotGreaterThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareNotLessThan(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareNotLessThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareOrdered(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarGreaterThan(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarGreaterThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarLessThan(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarLessThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarNotEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarNotGreaterThan(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarNotGreaterThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarNotLessThan(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarNotLessThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarOrdered(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarOrderedEqual(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarOrderedGreaterThan(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarOrderedGreaterThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarOrderedLessThan(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarOrderedLessThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarOrderedNotEqual(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarUnordered(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarUnorderedEqual(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarUnorderedGreaterThan(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarUnorderedGreaterThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarUnorderedLessThan(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarUnorderedLessThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarUnorderedNotEqual(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareUnordered(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def ConvertScalarToVector128Single(upper: Vector128_1[float], value: int) -> Vector128_1[float]: ...
    @staticmethod
    def ConvertToInt32(value: Vector128_1[float]) -> int: ...
    @staticmethod
    def ConvertToInt32WithTruncation(value: Vector128_1[float]) -> int: ...
    @staticmethod
    def Divide(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def DivideScalar(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def LoadAlignedVector128(address: clr.Reference[float]) -> Vector128_1[float]: ...
    @staticmethod
    def LoadHigh(lower: Vector128_1[float], address: clr.Reference[float]) -> Vector128_1[float]: ...
    @staticmethod
    def LoadLow(upper: Vector128_1[float], address: clr.Reference[float]) -> Vector128_1[float]: ...
    @staticmethod
    def LoadScalarVector128(address: clr.Reference[float]) -> Vector128_1[float]: ...
    @staticmethod
    def LoadVector128(address: clr.Reference[float]) -> Vector128_1[float]: ...
    @staticmethod
    def Max(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def MaxScalar(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def Min(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def MinScalar(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def MoveHighToLow(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def MoveLowToHigh(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def MoveMask(value: Vector128_1[float]) -> int: ...
    @staticmethod
    def MoveScalar(upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def Multiply(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def MultiplyScalar(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def Or(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def Prefetch0(address: clr.Reference[None]) -> None: ...
    @staticmethod
    def Prefetch1(address: clr.Reference[None]) -> None: ...
    @staticmethod
    def Prefetch2(address: clr.Reference[None]) -> None: ...
    @staticmethod
    def PrefetchNonTemporal(address: clr.Reference[None]) -> None: ...
    @staticmethod
    def Reciprocal(value: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def ReciprocalSqrt(value: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def Shuffle(left: Vector128_1[float], right: Vector128_1[float], control: int) -> Vector128_1[float]: ...
    @staticmethod
    def Sqrt(value: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def Store(address: clr.Reference[float], source: Vector128_1[float]) -> None: ...
    @staticmethod
    def StoreAligned(address: clr.Reference[float], source: Vector128_1[float]) -> None: ...
    @staticmethod
    def StoreAlignedNonTemporal(address: clr.Reference[float], source: Vector128_1[float]) -> None: ...
    @staticmethod
    def StoreFence() -> None: ...
    @staticmethod
    def StoreHigh(address: clr.Reference[float], source: Vector128_1[float]) -> None: ...
    @staticmethod
    def StoreLow(address: clr.Reference[float], source: Vector128_1[float]) -> None: ...
    @staticmethod
    def StoreScalar(address: clr.Reference[float], source: Vector128_1[float]) -> None: ...
    @staticmethod
    def Subtract(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def SubtractScalar(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def UnpackHigh(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def UnpackLow(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def Xor(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    # Skipped ReciprocalScalar due to it being static, abstract and generic.

    ReciprocalScalar : ReciprocalScalar_MethodGroup
    class ReciprocalScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped ReciprocalSqrtScalar due to it being static, abstract and generic.

    ReciprocalSqrtScalar : ReciprocalSqrtScalar_MethodGroup
    class ReciprocalSqrtScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped SqrtScalar due to it being static, abstract and generic.

    SqrtScalar : SqrtScalar_MethodGroup
    class SqrtScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]:...


    class X64(X86Base.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        @staticmethod
        def ConvertScalarToVector128Single(upper: Vector128_1[float], value: int) -> Vector128_1[float]: ...
        @staticmethod
        def ConvertToInt64(value: Vector128_1[float]) -> int: ...
        @staticmethod
        def ConvertToInt64WithTruncation(value: Vector128_1[float]) -> int: ...



class Sse2(Sse):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def AddScalar(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareGreaterThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareLessThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareNotEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareNotGreaterThan(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareNotGreaterThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareNotLessThan(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareNotLessThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareOrdered(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarGreaterThan(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarGreaterThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarLessThan(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarLessThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarNotEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarNotGreaterThan(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarNotGreaterThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarNotLessThan(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarNotLessThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarOrdered(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarOrderedEqual(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarOrderedGreaterThan(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarOrderedGreaterThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarOrderedLessThan(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarOrderedLessThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarOrderedNotEqual(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarUnordered(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def CompareScalarUnorderedEqual(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarUnorderedGreaterThan(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarUnorderedGreaterThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarUnorderedLessThan(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarUnorderedLessThanOrEqual(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareScalarUnorderedNotEqual(left: Vector128_1[float], right: Vector128_1[float]) -> bool: ...
    @staticmethod
    def CompareUnordered(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def ConvertScalarToVector128Int32(value: int) -> Vector128_1[int]: ...
    @staticmethod
    def ConvertScalarToVector128Single(upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def ConvertScalarToVector128UInt32(value: int) -> Vector128_1[int]: ...
    @staticmethod
    def ConvertToInt32WithTruncation(value: Vector128_1[float]) -> int: ...
    @staticmethod
    def ConvertToUInt32(value: Vector128_1[int]) -> int: ...
    @staticmethod
    def Divide(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def DivideScalar(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def Extract(value: Vector128_1[int], index: int) -> int: ...
    @staticmethod
    def LoadFence() -> None: ...
    @staticmethod
    def LoadHigh(lower: Vector128_1[float], address: clr.Reference[float]) -> Vector128_1[float]: ...
    @staticmethod
    def LoadLow(upper: Vector128_1[float], address: clr.Reference[float]) -> Vector128_1[float]: ...
    @staticmethod
    def MaxScalar(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def MemoryFence() -> None: ...
    @staticmethod
    def MinScalar(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def MultiplyAddAdjacent(left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def MultiplyScalar(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def PackUnsignedSaturate(left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def Sqrt(value: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def StoreHigh(address: clr.Reference[float], source: Vector128_1[float]) -> None: ...
    @staticmethod
    def StoreLow(address: clr.Reference[float], source: Vector128_1[float]) -> None: ...
    @staticmethod
    def SubtractScalar(left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def SumAbsoluteDifferences(left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]: ...
    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped AddSaturate due to it being static, abstract and generic.

    AddSaturate : AddSaturate_MethodGroup
    class AddSaturate_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped And due to it being static, abstract and generic.

    And : And_MethodGroup
    class And_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped AndNot due to it being static, abstract and generic.

    AndNot : AndNot_MethodGroup
    class AndNot_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped Average due to it being static, abstract and generic.

    Average : Average_MethodGroup
    class Average_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method Average(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped CompareEqual due to it being static, abstract and generic.

    CompareEqual : CompareEqual_MethodGroup
    class CompareEqual_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped CompareGreaterThan due to it being static, abstract and generic.

    CompareGreaterThan : CompareGreaterThan_MethodGroup
    class CompareGreaterThan_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped CompareLessThan due to it being static, abstract and generic.

    CompareLessThan : CompareLessThan_MethodGroup
    class CompareLessThan_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped ConvertScalarToVector128Double due to it being static, abstract and generic.

    ConvertScalarToVector128Double : ConvertScalarToVector128Double_MethodGroup
    class ConvertScalarToVector128Double_MethodGroup:
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: int) -> Vector128_1[float]:...
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped ConvertToInt32 due to it being static, abstract and generic.

    ConvertToInt32 : ConvertToInt32_MethodGroup
    class ConvertToInt32_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> int:...
        # Method ConvertToInt32(value : Vector128`1) was skipped since it collides with above method

    # Skipped ConvertToVector128Double due to it being static, abstract and generic.

    ConvertToVector128Double : ConvertToVector128Double_MethodGroup
    class ConvertToVector128Double_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method ConvertToVector128Double(value : Vector128`1) was skipped since it collides with above method

    # Skipped ConvertToVector128Int32 due to it being static, abstract and generic.

    ConvertToVector128Int32 : ConvertToVector128Int32_MethodGroup
    class ConvertToVector128Int32_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...
        # Method ConvertToVector128Int32(value : Vector128`1) was skipped since it collides with above method

    # Skipped ConvertToVector128Int32WithTruncation due to it being static, abstract and generic.

    ConvertToVector128Int32WithTruncation : ConvertToVector128Int32WithTruncation_MethodGroup
    class ConvertToVector128Int32WithTruncation_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...
        # Method ConvertToVector128Int32WithTruncation(value : Vector128`1) was skipped since it collides with above method

    # Skipped ConvertToVector128Single due to it being static, abstract and generic.

    ConvertToVector128Single : ConvertToVector128Single_MethodGroup
    class ConvertToVector128Single_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method ConvertToVector128Single(value : Vector128`1) was skipped since it collides with above method

    # Skipped Insert due to it being static, abstract and generic.

    Insert : Insert_MethodGroup
    class Insert_MethodGroup:
        def __call__(self, value: Vector128_1[int], data: int, index: int) -> Vector128_1[int]:...
        # Method Insert(value : Vector128`1, data : UInt16, index : Byte) was skipped since it collides with above method

    # Skipped LoadAlignedVector128 due to it being static, abstract and generic.

    LoadAlignedVector128 : LoadAlignedVector128_MethodGroup
    class LoadAlignedVector128_MethodGroup:
        def __call__(self, address: clr.Reference[float]) -> Vector128_1[float]:...
        # Method LoadAlignedVector128(address : SByte*) was skipped since it collides with above method
        # Method LoadAlignedVector128(address : Byte*) was skipped since it collides with above method
        # Method LoadAlignedVector128(address : Int16*) was skipped since it collides with above method
        # Method LoadAlignedVector128(address : UInt16*) was skipped since it collides with above method
        # Method LoadAlignedVector128(address : Int32*) was skipped since it collides with above method
        # Method LoadAlignedVector128(address : UInt32*) was skipped since it collides with above method
        # Method LoadAlignedVector128(address : Int64*) was skipped since it collides with above method
        # Method LoadAlignedVector128(address : UInt64*) was skipped since it collides with above method

    # Skipped LoadScalarVector128 due to it being static, abstract and generic.

    LoadScalarVector128 : LoadScalarVector128_MethodGroup
    class LoadScalarVector128_MethodGroup:
        def __call__(self, address: clr.Reference[float]) -> Vector128_1[float]:...
        # Method LoadScalarVector128(address : Int32*) was skipped since it collides with above method
        # Method LoadScalarVector128(address : UInt32*) was skipped since it collides with above method
        # Method LoadScalarVector128(address : Int64*) was skipped since it collides with above method
        # Method LoadScalarVector128(address : UInt64*) was skipped since it collides with above method

    # Skipped LoadVector128 due to it being static, abstract and generic.

    LoadVector128 : LoadVector128_MethodGroup
    class LoadVector128_MethodGroup:
        def __call__(self, address: clr.Reference[float]) -> Vector128_1[float]:...
        # Method LoadVector128(address : SByte*) was skipped since it collides with above method
        # Method LoadVector128(address : Byte*) was skipped since it collides with above method
        # Method LoadVector128(address : Int16*) was skipped since it collides with above method
        # Method LoadVector128(address : UInt16*) was skipped since it collides with above method
        # Method LoadVector128(address : Int32*) was skipped since it collides with above method
        # Method LoadVector128(address : UInt32*) was skipped since it collides with above method
        # Method LoadVector128(address : Int64*) was skipped since it collides with above method
        # Method LoadVector128(address : UInt64*) was skipped since it collides with above method

    # Skipped MaskMove due to it being static, abstract and generic.

    MaskMove : MaskMove_MethodGroup
    class MaskMove_MethodGroup:
        def __call__(self, source: Vector128_1[int], mask: Vector128_1[int], address: clr.Reference[int]) -> None:...
        # Method MaskMove(source : Vector128`1, mask : Vector128`1, address : Byte*) was skipped since it collides with above method

    # Skipped Max due to it being static, abstract and generic.

    Max : Max_MethodGroup
    class Max_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped Min due to it being static, abstract and generic.

    Min : Min_MethodGroup
    class Min_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped MoveMask due to it being static, abstract and generic.

    MoveMask : MoveMask_MethodGroup
    class MoveMask_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> int:...
        # Method MoveMask(value : Vector128`1) was skipped since it collides with above method
        # Method MoveMask(value : Vector128`1) was skipped since it collides with above method

    # Skipped MoveScalar due to it being static, abstract and generic.

    MoveScalar : MoveScalar_MethodGroup
    class MoveScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MoveScalar(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Multiply(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped MultiplyHigh due to it being static, abstract and generic.

    MultiplyHigh : MultiplyHigh_MethodGroup
    class MultiplyHigh_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped MultiplyLow due to it being static, abstract and generic.

    MultiplyLow : MultiplyLow_MethodGroup
    class MultiplyLow_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped Or due to it being static, abstract and generic.

    Or : Or_MethodGroup
    class Or_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped PackSignedSaturate due to it being static, abstract and generic.

    PackSignedSaturate : PackSignedSaturate_MethodGroup
    class PackSignedSaturate_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method PackSignedSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftLeftLogical due to it being static, abstract and generic.

    ShiftLeftLogical : ShiftLeftLogical_MethodGroup
    class ShiftLeftLogical_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftLeftLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ShiftLeftLogical(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftLeftLogical(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftLeftLogical128BitLane due to it being static, abstract and generic.

    ShiftLeftLogical128BitLane : ShiftLeftLogical128BitLane_MethodGroup
    class ShiftLeftLogical128BitLane_MethodGroup:
        def __call__(self, value: Vector128_1[int], numBytes: int) -> Vector128_1[int]:...
        # Method ShiftLeftLogical128BitLane(value : Vector128`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical128BitLane(value : Vector128`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical128BitLane(value : Vector128`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical128BitLane(value : Vector128`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical128BitLane(value : Vector128`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical128BitLane(value : Vector128`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftLeftLogical128BitLane(value : Vector128`1, numBytes : Byte) was skipped since it collides with above method

    # Skipped ShiftRightArithmetic due to it being static, abstract and generic.

    ShiftRightArithmetic : ShiftRightArithmetic_MethodGroup
    class ShiftRightArithmetic_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightArithmetic(value : Vector128`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ShiftRightArithmetic(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftRightLogical due to it being static, abstract and generic.

    ShiftRightLogical : ShiftRightLogical_MethodGroup
    class ShiftRightLogical_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ShiftRightLogical(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftRightLogical128BitLane due to it being static, abstract and generic.

    ShiftRightLogical128BitLane : ShiftRightLogical128BitLane_MethodGroup
    class ShiftRightLogical128BitLane_MethodGroup:
        def __call__(self, value: Vector128_1[int], numBytes: int) -> Vector128_1[int]:...
        # Method ShiftRightLogical128BitLane(value : Vector128`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical128BitLane(value : Vector128`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical128BitLane(value : Vector128`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical128BitLane(value : Vector128`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical128BitLane(value : Vector128`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical128BitLane(value : Vector128`1, numBytes : Byte) was skipped since it collides with above method
        # Method ShiftRightLogical128BitLane(value : Vector128`1, numBytes : Byte) was skipped since it collides with above method

    # Skipped Shuffle due to it being static, abstract and generic.

    Shuffle : Shuffle_MethodGroup
    class Shuffle_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int], control: int) -> Vector128_1[int]:...
        # Method Shuffle(value : Vector128`1, control : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float], control: int) -> Vector128_1[float]:...

    # Skipped ShuffleHigh due to it being static, abstract and generic.

    ShuffleHigh : ShuffleHigh_MethodGroup
    class ShuffleHigh_MethodGroup:
        def __call__(self, value: Vector128_1[int], control: int) -> Vector128_1[int]:...
        # Method ShuffleHigh(value : Vector128`1, control : Byte) was skipped since it collides with above method

    # Skipped ShuffleLow due to it being static, abstract and generic.

    ShuffleLow : ShuffleLow_MethodGroup
    class ShuffleLow_MethodGroup:
        def __call__(self, value: Vector128_1[int], control: int) -> Vector128_1[int]:...
        # Method ShuffleLow(value : Vector128`1, control : Byte) was skipped since it collides with above method

    # Skipped SqrtScalar due to it being static, abstract and generic.

    SqrtScalar : SqrtScalar_MethodGroup
    class SqrtScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]:...

    # Skipped Store due to it being static, abstract and generic.

    Store : Store_MethodGroup
    class Store_MethodGroup:
        def __call__(self, address: clr.Reference[float], source: Vector128_1[float]) -> None:...
        # Method Store(address : SByte*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : Byte*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : Int16*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : UInt16*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : Int32*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : UInt32*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : Int64*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : UInt64*, source : Vector128`1) was skipped since it collides with above method

    # Skipped StoreAligned due to it being static, abstract and generic.

    StoreAligned : StoreAligned_MethodGroup
    class StoreAligned_MethodGroup:
        def __call__(self, address: clr.Reference[float], source: Vector128_1[float]) -> None:...
        # Method StoreAligned(address : SByte*, source : Vector128`1) was skipped since it collides with above method
        # Method StoreAligned(address : Byte*, source : Vector128`1) was skipped since it collides with above method
        # Method StoreAligned(address : Int16*, source : Vector128`1) was skipped since it collides with above method
        # Method StoreAligned(address : UInt16*, source : Vector128`1) was skipped since it collides with above method
        # Method StoreAligned(address : Int32*, source : Vector128`1) was skipped since it collides with above method
        # Method StoreAligned(address : UInt32*, source : Vector128`1) was skipped since it collides with above method
        # Method StoreAligned(address : Int64*, source : Vector128`1) was skipped since it collides with above method
        # Method StoreAligned(address : UInt64*, source : Vector128`1) was skipped since it collides with above method

    # Skipped StoreAlignedNonTemporal due to it being static, abstract and generic.

    StoreAlignedNonTemporal : StoreAlignedNonTemporal_MethodGroup
    class StoreAlignedNonTemporal_MethodGroup:
        def __call__(self, address: clr.Reference[float], source: Vector128_1[float]) -> None:...
        # Method StoreAlignedNonTemporal(address : SByte*, source : Vector128`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : Byte*, source : Vector128`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : Int16*, source : Vector128`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : UInt16*, source : Vector128`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : Int32*, source : Vector128`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : UInt32*, source : Vector128`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : Int64*, source : Vector128`1) was skipped since it collides with above method
        # Method StoreAlignedNonTemporal(address : UInt64*, source : Vector128`1) was skipped since it collides with above method

    # Skipped StoreNonTemporal due to it being static, abstract and generic.

    StoreNonTemporal : StoreNonTemporal_MethodGroup
    class StoreNonTemporal_MethodGroup:
        def __call__(self, address: clr.Reference[int], value: int) -> None:...
        # Method StoreNonTemporal(address : UInt32*, value : UInt32) was skipped since it collides with above method

    # Skipped StoreScalar due to it being static, abstract and generic.

    StoreScalar : StoreScalar_MethodGroup
    class StoreScalar_MethodGroup:
        def __call__(self, address: clr.Reference[float], source: Vector128_1[float]) -> None:...
        # Method StoreScalar(address : Int32*, source : Vector128`1) was skipped since it collides with above method
        # Method StoreScalar(address : UInt32*, source : Vector128`1) was skipped since it collides with above method
        # Method StoreScalar(address : Int64*, source : Vector128`1) was skipped since it collides with above method
        # Method StoreScalar(address : UInt64*, source : Vector128`1) was skipped since it collides with above method

    # Skipped Subtract due to it being static, abstract and generic.

    Subtract : Subtract_MethodGroup
    class Subtract_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped SubtractSaturate due to it being static, abstract and generic.

    SubtractSaturate : SubtractSaturate_MethodGroup
    class SubtractSaturate_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method SubtractSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped UnpackHigh due to it being static, abstract and generic.

    UnpackHigh : UnpackHigh_MethodGroup
    class UnpackHigh_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method UnpackHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method UnpackHigh(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped UnpackLow due to it being static, abstract and generic.

    UnpackLow : UnpackLow_MethodGroup
    class UnpackLow_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method UnpackLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method UnpackLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped Xor due to it being static, abstract and generic.

    Xor : Xor_MethodGroup
    class Xor_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method


    class X64(Sse.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        @staticmethod
        def ConvertScalarToVector128Double(upper: Vector128_1[float], value: int) -> Vector128_1[float]: ...
        @staticmethod
        def ConvertScalarToVector128Int64(value: int) -> Vector128_1[int]: ...
        @staticmethod
        def ConvertScalarToVector128UInt64(value: int) -> Vector128_1[int]: ...
        @staticmethod
        def ConvertToInt64WithTruncation(value: Vector128_1[float]) -> int: ...
        @staticmethod
        def ConvertToUInt64(value: Vector128_1[int]) -> int: ...
        # Skipped ConvertToInt64 due to it being static, abstract and generic.

        ConvertToInt64 : ConvertToInt64_MethodGroup
        class ConvertToInt64_MethodGroup:
            def __call__(self, value: Vector128_1[float]) -> int:...
            # Method ConvertToInt64(value : Vector128`1) was skipped since it collides with above method

        # Skipped StoreNonTemporal due to it being static, abstract and generic.

        StoreNonTemporal : StoreNonTemporal_MethodGroup
        class StoreNonTemporal_MethodGroup:
            def __call__(self, address: clr.Reference[int], value: int) -> None:...
            # Method StoreNonTemporal(address : UInt64*, value : UInt64) was skipped since it collides with above method




class Sse3(Sse2):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def LoadAndDuplicateToVector128(address: clr.Reference[float]) -> Vector128_1[float]: ...
    @staticmethod
    def MoveAndDuplicate(source: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def MoveHighAndDuplicate(source: Vector128_1[float]) -> Vector128_1[float]: ...
    @staticmethod
    def MoveLowAndDuplicate(source: Vector128_1[float]) -> Vector128_1[float]: ...
    # Skipped AddSubtract due to it being static, abstract and generic.

    AddSubtract : AddSubtract_MethodGroup
    class AddSubtract_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method AddSubtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped HorizontalAdd due to it being static, abstract and generic.

    HorizontalAdd : HorizontalAdd_MethodGroup
    class HorizontalAdd_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method HorizontalAdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped HorizontalSubtract due to it being static, abstract and generic.

    HorizontalSubtract : HorizontalSubtract_MethodGroup
    class HorizontalSubtract_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method HorizontalSubtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped LoadDquVector128 due to it being static, abstract and generic.

    LoadDquVector128 : LoadDquVector128_MethodGroup
    class LoadDquVector128_MethodGroup:
        def __call__(self, address: clr.Reference[int]) -> Vector128_1[int]:...
        # Method LoadDquVector128(address : Byte*) was skipped since it collides with above method
        # Method LoadDquVector128(address : Int16*) was skipped since it collides with above method
        # Method LoadDquVector128(address : UInt16*) was skipped since it collides with above method
        # Method LoadDquVector128(address : Int32*) was skipped since it collides with above method
        # Method LoadDquVector128(address : UInt32*) was skipped since it collides with above method
        # Method LoadDquVector128(address : Int64*) was skipped since it collides with above method
        # Method LoadDquVector128(address : UInt64*) was skipped since it collides with above method


    class X64(Sse2.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...



class Sse41(Ssse3):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def MinHorizontal(value: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def MultipleSumAbsoluteDifferences(left: Vector128_1[int], right: Vector128_1[int], mask: int) -> Vector128_1[int]: ...
    @staticmethod
    def Multiply(left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def PackUnsignedSaturate(left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]: ...
    # Skipped Blend due to it being static, abstract and generic.

    Blend : Blend_MethodGroup
    class Blend_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float], control: int) -> Vector128_1[float]:...
        # Method Blend(left : Vector128`1, right : Vector128`1, control : Byte) was skipped since it collides with above method
        # Method Blend(left : Vector128`1, right : Vector128`1, control : Byte) was skipped since it collides with above method
        # Method Blend(left : Vector128`1, right : Vector128`1, control : Byte) was skipped since it collides with above method

    # Skipped BlendVariable due to it being static, abstract and generic.

    BlendVariable : BlendVariable_MethodGroup
    class BlendVariable_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float], mask: Vector128_1[float]) -> Vector128_1[float]:...
        # Method BlendVariable(left : Vector128`1, right : Vector128`1, mask : Vector128`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector128`1, right : Vector128`1, mask : Vector128`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector128`1, right : Vector128`1, mask : Vector128`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector128`1, right : Vector128`1, mask : Vector128`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector128`1, right : Vector128`1, mask : Vector128`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector128`1, right : Vector128`1, mask : Vector128`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector128`1, right : Vector128`1, mask : Vector128`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector128`1, right : Vector128`1, mask : Vector128`1) was skipped since it collides with above method
        # Method BlendVariable(left : Vector128`1, right : Vector128`1, mask : Vector128`1) was skipped since it collides with above method

    # Skipped Ceiling due to it being static, abstract and generic.

    Ceiling : Ceiling_MethodGroup
    class Ceiling_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Ceiling(value : Vector128`1) was skipped since it collides with above method

    # Skipped CeilingScalar due to it being static, abstract and generic.

    CeilingScalar : CeilingScalar_MethodGroup
    class CeilingScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method CeilingScalar(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method CeilingScalar(upper : Vector128`1, value : Vector128`1) was skipped since it collides with above method

    # Skipped CompareEqual due to it being static, abstract and generic.

    CompareEqual : CompareEqual_MethodGroup
    class CompareEqual_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped ConvertToVector128Int16 due to it being static, abstract and generic.

    ConvertToVector128Int16 : ConvertToVector128Int16_MethodGroup
    class ConvertToVector128Int16_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ConvertToVector128Int16(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, address: clr.Reference[int]) -> Vector128_1[int]:...
        # Method ConvertToVector128Int16(address : Byte*) was skipped since it collides with above method

    # Skipped ConvertToVector128Int32 due to it being static, abstract and generic.

    ConvertToVector128Int32 : ConvertToVector128Int32_MethodGroup
    class ConvertToVector128Int32_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ConvertToVector128Int32(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToVector128Int32(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToVector128Int32(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, address: clr.Reference[int]) -> Vector128_1[int]:...
        # Method ConvertToVector128Int32(address : Byte*) was skipped since it collides with above method
        # Method ConvertToVector128Int32(address : Int16*) was skipped since it collides with above method
        # Method ConvertToVector128Int32(address : UInt16*) was skipped since it collides with above method

    # Skipped ConvertToVector128Int64 due to it being static, abstract and generic.

    ConvertToVector128Int64 : ConvertToVector128Int64_MethodGroup
    class ConvertToVector128Int64_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ConvertToVector128Int64(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToVector128Int64(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToVector128Int64(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToVector128Int64(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToVector128Int64(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, address: clr.Reference[int]) -> Vector128_1[int]:...
        # Method ConvertToVector128Int64(address : Byte*) was skipped since it collides with above method
        # Method ConvertToVector128Int64(address : Int16*) was skipped since it collides with above method
        # Method ConvertToVector128Int64(address : UInt16*) was skipped since it collides with above method
        # Method ConvertToVector128Int64(address : Int32*) was skipped since it collides with above method
        # Method ConvertToVector128Int64(address : UInt32*) was skipped since it collides with above method

    # Skipped DotProduct due to it being static, abstract and generic.

    DotProduct : DotProduct_MethodGroup
    class DotProduct_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float], control: int) -> Vector128_1[float]:...
        # Method DotProduct(left : Vector128`1, right : Vector128`1, control : Byte) was skipped since it collides with above method

    # Skipped Extract due to it being static, abstract and generic.

    Extract : Extract_MethodGroup
    class Extract_MethodGroup:
        def __call__(self, value: Vector128_1[float], index: int) -> float:...
        # Method Extract(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method Extract(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method Extract(value : Vector128`1, index : Byte) was skipped since it collides with above method

    # Skipped Floor due to it being static, abstract and generic.

    Floor : Floor_MethodGroup
    class Floor_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Floor(value : Vector128`1) was skipped since it collides with above method

    # Skipped FloorScalar due to it being static, abstract and generic.

    FloorScalar : FloorScalar_MethodGroup
    class FloorScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method FloorScalar(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method FloorScalar(upper : Vector128`1, value : Vector128`1) was skipped since it collides with above method

    # Skipped Insert due to it being static, abstract and generic.

    Insert : Insert_MethodGroup
    class Insert_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float], data: Vector128_1[float], index: int) -> Vector128_1[float]:...
        @typing.overload
        def __call__(self, value: Vector128_1[int], data: int, index: int) -> Vector128_1[int]:...
        # Method Insert(value : Vector128`1, data : Byte, index : Byte) was skipped since it collides with above method
        # Method Insert(value : Vector128`1, data : Int32, index : Byte) was skipped since it collides with above method
        # Method Insert(value : Vector128`1, data : UInt32, index : Byte) was skipped since it collides with above method

    # Skipped LoadAlignedVector128NonTemporal due to it being static, abstract and generic.

    LoadAlignedVector128NonTemporal : LoadAlignedVector128NonTemporal_MethodGroup
    class LoadAlignedVector128NonTemporal_MethodGroup:
        def __call__(self, address: clr.Reference[int]) -> Vector128_1[int]:...
        # Method LoadAlignedVector128NonTemporal(address : Byte*) was skipped since it collides with above method
        # Method LoadAlignedVector128NonTemporal(address : Int16*) was skipped since it collides with above method
        # Method LoadAlignedVector128NonTemporal(address : UInt16*) was skipped since it collides with above method
        # Method LoadAlignedVector128NonTemporal(address : Int32*) was skipped since it collides with above method
        # Method LoadAlignedVector128NonTemporal(address : UInt32*) was skipped since it collides with above method
        # Method LoadAlignedVector128NonTemporal(address : Int64*) was skipped since it collides with above method
        # Method LoadAlignedVector128NonTemporal(address : UInt64*) was skipped since it collides with above method

    # Skipped Max due to it being static, abstract and generic.

    Max : Max_MethodGroup
    class Max_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped Min due to it being static, abstract and generic.

    Min : Min_MethodGroup
    class Min_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped MultiplyLow due to it being static, abstract and generic.

    MultiplyLow : MultiplyLow_MethodGroup
    class MultiplyLow_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyLow(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped RoundCurrentDirection due to it being static, abstract and generic.

    RoundCurrentDirection : RoundCurrentDirection_MethodGroup
    class RoundCurrentDirection_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method RoundCurrentDirection(value : Vector128`1) was skipped since it collides with above method

    # Skipped RoundCurrentDirectionScalar due to it being static, abstract and generic.

    RoundCurrentDirectionScalar : RoundCurrentDirectionScalar_MethodGroup
    class RoundCurrentDirectionScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method RoundCurrentDirectionScalar(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method RoundCurrentDirectionScalar(upper : Vector128`1, value : Vector128`1) was skipped since it collides with above method

    # Skipped RoundToNearestInteger due to it being static, abstract and generic.

    RoundToNearestInteger : RoundToNearestInteger_MethodGroup
    class RoundToNearestInteger_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method RoundToNearestInteger(value : Vector128`1) was skipped since it collides with above method

    # Skipped RoundToNearestIntegerScalar due to it being static, abstract and generic.

    RoundToNearestIntegerScalar : RoundToNearestIntegerScalar_MethodGroup
    class RoundToNearestIntegerScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method RoundToNearestIntegerScalar(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method RoundToNearestIntegerScalar(upper : Vector128`1, value : Vector128`1) was skipped since it collides with above method

    # Skipped RoundToNegativeInfinity due to it being static, abstract and generic.

    RoundToNegativeInfinity : RoundToNegativeInfinity_MethodGroup
    class RoundToNegativeInfinity_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method RoundToNegativeInfinity(value : Vector128`1) was skipped since it collides with above method

    # Skipped RoundToNegativeInfinityScalar due to it being static, abstract and generic.

    RoundToNegativeInfinityScalar : RoundToNegativeInfinityScalar_MethodGroup
    class RoundToNegativeInfinityScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method RoundToNegativeInfinityScalar(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method RoundToNegativeInfinityScalar(upper : Vector128`1, value : Vector128`1) was skipped since it collides with above method

    # Skipped RoundToPositiveInfinity due to it being static, abstract and generic.

    RoundToPositiveInfinity : RoundToPositiveInfinity_MethodGroup
    class RoundToPositiveInfinity_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method RoundToPositiveInfinity(value : Vector128`1) was skipped since it collides with above method

    # Skipped RoundToPositiveInfinityScalar due to it being static, abstract and generic.

    RoundToPositiveInfinityScalar : RoundToPositiveInfinityScalar_MethodGroup
    class RoundToPositiveInfinityScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method RoundToPositiveInfinityScalar(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method RoundToPositiveInfinityScalar(upper : Vector128`1, value : Vector128`1) was skipped since it collides with above method

    # Skipped RoundToZero due to it being static, abstract and generic.

    RoundToZero : RoundToZero_MethodGroup
    class RoundToZero_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method RoundToZero(value : Vector128`1) was skipped since it collides with above method

    # Skipped RoundToZeroScalar due to it being static, abstract and generic.

    RoundToZeroScalar : RoundToZeroScalar_MethodGroup
    class RoundToZeroScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method RoundToZeroScalar(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, upper: Vector128_1[float], value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method RoundToZeroScalar(upper : Vector128`1, value : Vector128`1) was skipped since it collides with above method

    # Skipped TestC due to it being static, abstract and generic.

    TestC : TestC_MethodGroup
    class TestC_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> bool:...
        # Method TestC(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestC(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestC(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestC(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestC(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestC(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestC(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped TestNotZAndNotC due to it being static, abstract and generic.

    TestNotZAndNotC : TestNotZAndNotC_MethodGroup
    class TestNotZAndNotC_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> bool:...
        # Method TestNotZAndNotC(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestNotZAndNotC(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestNotZAndNotC(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestNotZAndNotC(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestNotZAndNotC(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestNotZAndNotC(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestNotZAndNotC(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped TestZ due to it being static, abstract and generic.

    TestZ : TestZ_MethodGroup
    class TestZ_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> bool:...
        # Method TestZ(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestZ(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestZ(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestZ(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestZ(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestZ(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method TestZ(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method


    class X64(Ssse3.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        # Skipped Extract due to it being static, abstract and generic.

        Extract : Extract_MethodGroup
        class Extract_MethodGroup:
            def __call__(self, value: Vector128_1[int], index: int) -> int:...
            # Method Extract(value : Vector128`1, index : Byte) was skipped since it collides with above method

        # Skipped Insert due to it being static, abstract and generic.

        Insert : Insert_MethodGroup
        class Insert_MethodGroup:
            def __call__(self, value: Vector128_1[int], data: int, index: int) -> Vector128_1[int]:...
            # Method Insert(value : Vector128`1, data : UInt64, index : Byte) was skipped since it collides with above method




class Sse42(Sse41):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def CompareGreaterThan(left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]: ...
    # Skipped Crc32 due to it being static, abstract and generic.

    Crc32 : Crc32_MethodGroup
    class Crc32_MethodGroup:
        def __call__(self, crc: int, data: int) -> int:...
        # Method Crc32(crc : UInt32, data : UInt16) was skipped since it collides with above method
        # Method Crc32(crc : UInt32, data : UInt32) was skipped since it collides with above method


    class X64(Sse41.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        @staticmethod
        def Crc32(crc: int, data: int) -> int: ...



class Ssse3(Sse3):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def HorizontalAddSaturate(left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def HorizontalSubtractSaturate(left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def MultiplyAddAdjacent(left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def MultiplyHighRoundScale(left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]: ...
    # Skipped Abs due to it being static, abstract and generic.

    Abs : Abs_MethodGroup
    class Abs_MethodGroup:
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method Abs(value : Vector128`1) was skipped since it collides with above method
        # Method Abs(value : Vector128`1) was skipped since it collides with above method

    # Skipped AlignRight due to it being static, abstract and generic.

    AlignRight : AlignRight_MethodGroup
    class AlignRight_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int], mask: int) -> Vector128_1[int]:...
        # Method AlignRight(left : Vector128`1, right : Vector128`1, mask : Byte) was skipped since it collides with above method
        # Method AlignRight(left : Vector128`1, right : Vector128`1, mask : Byte) was skipped since it collides with above method
        # Method AlignRight(left : Vector128`1, right : Vector128`1, mask : Byte) was skipped since it collides with above method
        # Method AlignRight(left : Vector128`1, right : Vector128`1, mask : Byte) was skipped since it collides with above method
        # Method AlignRight(left : Vector128`1, right : Vector128`1, mask : Byte) was skipped since it collides with above method
        # Method AlignRight(left : Vector128`1, right : Vector128`1, mask : Byte) was skipped since it collides with above method
        # Method AlignRight(left : Vector128`1, right : Vector128`1, mask : Byte) was skipped since it collides with above method

    # Skipped HorizontalAdd due to it being static, abstract and generic.

    HorizontalAdd : HorizontalAdd_MethodGroup
    class HorizontalAdd_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method HorizontalAdd(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped HorizontalSubtract due to it being static, abstract and generic.

    HorizontalSubtract : HorizontalSubtract_MethodGroup
    class HorizontalSubtract_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method HorizontalSubtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped Shuffle due to it being static, abstract and generic.

    Shuffle : Shuffle_MethodGroup
    class Shuffle_MethodGroup:
        def __call__(self, value: Vector128_1[int], mask: Vector128_1[int]) -> Vector128_1[int]:...
        # Method Shuffle(value : Vector128`1, mask : Vector128`1) was skipped since it collides with above method

    # Skipped Sign due to it being static, abstract and generic.

    Sign : Sign_MethodGroup
    class Sign_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method Sign(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Sign(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method


    class X64(Sse3.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...



class X86Base(abc.ABC):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def CpuId(functionId: int, subFunctionId: int) -> ValueTuple_4[int, int, int, int]: ...
    @staticmethod
    def Pause() -> None: ...
    # Skipped DivRem due to it being static, abstract and generic.

    DivRem : DivRem_MethodGroup
    class DivRem_MethodGroup:
        @typing.overload
        def __call__(self, lower: int, upper: int, divisor: int) -> ValueTuple_2[int, int]:...
        # Method DivRem(lower : UInt32, upper : Int32, divisor : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, lower: UIntPtr, upper: UIntPtr, divisor: UIntPtr) -> ValueTuple_2[UIntPtr, UIntPtr]:...
        @typing.overload
        def __call__(self, lower: UIntPtr, upper: int, divisor: int) -> ValueTuple_2[int, int]:...


    class X64(abc.ABC):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...
        # Skipped DivRem due to it being static, abstract and generic.

        DivRem : DivRem_MethodGroup
        class DivRem_MethodGroup:
            def __call__(self, lower: int, upper: int, divisor: int) -> ValueTuple_2[int, int]:...
            # Method DivRem(lower : UInt64, upper : Int64, divisor : Int64) was skipped since it collides with above method




class X86Serialize(X86Base):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def Serialize() -> None: ...

    class X64(X86Base.X64):
        @classmethod
        @property
        def IsSupported(cls) -> bool: ...


