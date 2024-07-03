import typing, clr, abc
from System.Runtime.Intrinsics import Vector128_1
from System import UIntPtr

class PackedSimd(abc.ABC):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def Dot(left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def MultiplyRoundedSaturateQ15(left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]: ...
    @staticmethod
    def PopCount(value: Vector128_1[int]) -> Vector128_1[int]: ...
    # Skipped Abs due to it being static, abstract and generic.

    Abs : Abs_MethodGroup
    class Abs_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Abs(value : Vector128`1) was skipped since it collides with above method
        # Method Abs(value : Vector128`1) was skipped since it collides with above method
        # Method Abs(value : Vector128`1) was skipped since it collides with above method
        # Method Abs(value : Vector128`1) was skipped since it collides with above method
        # Method Abs(value : Vector128`1) was skipped since it collides with above method
        # Method Abs(value : Vector128`1) was skipped since it collides with above method

    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Add(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[UIntPtr], right: Vector128_1[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped AddPairwiseWidening due to it being static, abstract and generic.

    AddPairwiseWidening : AddPairwiseWidening_MethodGroup
    class AddPairwiseWidening_MethodGroup:
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method AddPairwiseWidening(value : Vector128`1) was skipped since it collides with above method
        # Method AddPairwiseWidening(value : Vector128`1) was skipped since it collides with above method
        # Method AddPairwiseWidening(value : Vector128`1) was skipped since it collides with above method

    # Skipped AddSaturate due to it being static, abstract and generic.

    AddSaturate : AddSaturate_MethodGroup
    class AddSaturate_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AddSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped AllTrue due to it being static, abstract and generic.

    AllTrue : AllTrue_MethodGroup
    class AllTrue_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> bool:...
        # Method AllTrue(value : Vector128`1) was skipped since it collides with above method
        # Method AllTrue(value : Vector128`1) was skipped since it collides with above method
        # Method AllTrue(value : Vector128`1) was skipped since it collides with above method
        # Method AllTrue(value : Vector128`1) was skipped since it collides with above method
        # Method AllTrue(value : Vector128`1) was skipped since it collides with above method
        # Method AllTrue(value : Vector128`1) was skipped since it collides with above method
        # Method AllTrue(value : Vector128`1) was skipped since it collides with above method
        # Method AllTrue(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[UIntPtr]) -> bool:...

    # Skipped And due to it being static, abstract and generic.

    And : And_MethodGroup
    class And_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method And(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[UIntPtr], right: Vector128_1[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped AndNot due to it being static, abstract and generic.

    AndNot : AndNot_MethodGroup
    class AndNot_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method AndNot(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[UIntPtr], right: Vector128_1[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped AnyTrue due to it being static, abstract and generic.

    AnyTrue : AnyTrue_MethodGroup
    class AnyTrue_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> bool:...
        # Method AnyTrue(value : Vector128`1) was skipped since it collides with above method
        # Method AnyTrue(value : Vector128`1) was skipped since it collides with above method
        # Method AnyTrue(value : Vector128`1) was skipped since it collides with above method
        # Method AnyTrue(value : Vector128`1) was skipped since it collides with above method
        # Method AnyTrue(value : Vector128`1) was skipped since it collides with above method
        # Method AnyTrue(value : Vector128`1) was skipped since it collides with above method
        # Method AnyTrue(value : Vector128`1) was skipped since it collides with above method
        # Method AnyTrue(value : Vector128`1) was skipped since it collides with above method
        # Method AnyTrue(value : Vector128`1) was skipped since it collides with above method
        # Method AnyTrue(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[UIntPtr]) -> bool:...

    # Skipped AverageRounded due to it being static, abstract and generic.

    AverageRounded : AverageRounded_MethodGroup
    class AverageRounded_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method AverageRounded(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped Bitmask due to it being static, abstract and generic.

    Bitmask : Bitmask_MethodGroup
    class Bitmask_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int]) -> int:...
        # Method Bitmask(value : Vector128`1) was skipped since it collides with above method
        # Method Bitmask(value : Vector128`1) was skipped since it collides with above method
        # Method Bitmask(value : Vector128`1) was skipped since it collides with above method
        # Method Bitmask(value : Vector128`1) was skipped since it collides with above method
        # Method Bitmask(value : Vector128`1) was skipped since it collides with above method
        # Method Bitmask(value : Vector128`1) was skipped since it collides with above method
        # Method Bitmask(value : Vector128`1) was skipped since it collides with above method
        # Method Bitmask(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[UIntPtr]) -> int:...

    # Skipped BitwiseSelect due to it being static, abstract and generic.

    BitwiseSelect : BitwiseSelect_MethodGroup
    class BitwiseSelect_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float], select: Vector128_1[float]) -> Vector128_1[float]:...
        # Method BitwiseSelect(left : Vector128`1, right : Vector128`1, select : Vector128`1) was skipped since it collides with above method
        # Method BitwiseSelect(left : Vector128`1, right : Vector128`1, select : Vector128`1) was skipped since it collides with above method
        # Method BitwiseSelect(left : Vector128`1, right : Vector128`1, select : Vector128`1) was skipped since it collides with above method
        # Method BitwiseSelect(left : Vector128`1, right : Vector128`1, select : Vector128`1) was skipped since it collides with above method
        # Method BitwiseSelect(left : Vector128`1, right : Vector128`1, select : Vector128`1) was skipped since it collides with above method
        # Method BitwiseSelect(left : Vector128`1, right : Vector128`1, select : Vector128`1) was skipped since it collides with above method
        # Method BitwiseSelect(left : Vector128`1, right : Vector128`1, select : Vector128`1) was skipped since it collides with above method
        # Method BitwiseSelect(left : Vector128`1, right : Vector128`1, select : Vector128`1) was skipped since it collides with above method
        # Method BitwiseSelect(left : Vector128`1, right : Vector128`1, select : Vector128`1) was skipped since it collides with above method
        # Method BitwiseSelect(left : Vector128`1, right : Vector128`1, select : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[UIntPtr], right: Vector128_1[UIntPtr], select: Vector128_1[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped Ceiling due to it being static, abstract and generic.

    Ceiling : Ceiling_MethodGroup
    class Ceiling_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Ceiling(value : Vector128`1) was skipped since it collides with above method

    # Skipped CompareEqual due to it being static, abstract and generic.

    CompareEqual : CompareEqual_MethodGroup
    class CompareEqual_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[UIntPtr], right: Vector128_1[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped CompareGreaterThan due to it being static, abstract and generic.

    CompareGreaterThan : CompareGreaterThan_MethodGroup
    class CompareGreaterThan_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[UIntPtr], right: Vector128_1[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped CompareGreaterThanOrEqual due to it being static, abstract and generic.

    CompareGreaterThanOrEqual : CompareGreaterThanOrEqual_MethodGroup
    class CompareGreaterThanOrEqual_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareGreaterThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[UIntPtr], right: Vector128_1[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped CompareLessThan due to it being static, abstract and generic.

    CompareLessThan : CompareLessThan_MethodGroup
    class CompareLessThan_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThan(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[UIntPtr], right: Vector128_1[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped CompareLessThanOrEqual due to it being static, abstract and generic.

    CompareLessThanOrEqual : CompareLessThanOrEqual_MethodGroup
    class CompareLessThanOrEqual_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareLessThanOrEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[UIntPtr], right: Vector128_1[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped CompareNotEqual due to it being static, abstract and generic.

    CompareNotEqual : CompareNotEqual_MethodGroup
    class CompareNotEqual_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method CompareNotEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareNotEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareNotEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareNotEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareNotEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareNotEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareNotEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareNotEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareNotEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method CompareNotEqual(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[UIntPtr], right: Vector128_1[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped ConvertNarrowingSaturateSigned due to it being static, abstract and generic.

    ConvertNarrowingSaturateSigned : ConvertNarrowingSaturateSigned_MethodGroup
    class ConvertNarrowingSaturateSigned_MethodGroup:
        def __call__(self, lower: Vector128_1[int], upper: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ConvertNarrowingSaturateSigned(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method

    # Skipped ConvertNarrowingSaturateUnsigned due to it being static, abstract and generic.

    ConvertNarrowingSaturateUnsigned : ConvertNarrowingSaturateUnsigned_MethodGroup
    class ConvertNarrowingSaturateUnsigned_MethodGroup:
        def __call__(self, lower: Vector128_1[int], upper: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ConvertNarrowingSaturateUnsigned(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method

    # Skipped ConvertToDoubleLower due to it being static, abstract and generic.

    ConvertToDoubleLower : ConvertToDoubleLower_MethodGroup
    class ConvertToDoubleLower_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method ConvertToDoubleLower(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToDoubleLower(value : Vector128`1) was skipped since it collides with above method

    # Skipped ConvertToInt32Saturate due to it being static, abstract and generic.

    ConvertToInt32Saturate : ConvertToInt32Saturate_MethodGroup
    class ConvertToInt32Saturate_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...
        # Method ConvertToInt32Saturate(value : Vector128`1) was skipped since it collides with above method

    # Skipped ConvertToSingle due to it being static, abstract and generic.

    ConvertToSingle : ConvertToSingle_MethodGroup
    class ConvertToSingle_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method ConvertToSingle(value : Vector128`1) was skipped since it collides with above method
        # Method ConvertToSingle(value : Vector128`1) was skipped since it collides with above method

    # Skipped ConvertToUInt32Saturate due to it being static, abstract and generic.

    ConvertToUInt32Saturate : ConvertToUInt32Saturate_MethodGroup
    class ConvertToUInt32Saturate_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[int]:...
        # Method ConvertToUInt32Saturate(value : Vector128`1) was skipped since it collides with above method

    # Skipped Divide due to it being static, abstract and generic.

    Divide : Divide_MethodGroup
    class Divide_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Divide(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped ExtractScalar due to it being static, abstract and generic.

    ExtractScalar : ExtractScalar_MethodGroup
    class ExtractScalar_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float], index: int) -> float:...
        # Method ExtractScalar(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method ExtractScalar(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method ExtractScalar(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method ExtractScalar(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method ExtractScalar(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method ExtractScalar(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method ExtractScalar(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method ExtractScalar(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method ExtractScalar(value : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method ExtractScalar(value : Vector128`1, index : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[UIntPtr], index: int) -> UIntPtr:...

    # Skipped Floor due to it being static, abstract and generic.

    Floor : Floor_MethodGroup
    class Floor_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Floor(value : Vector128`1) was skipped since it collides with above method

    # Skipped LoadScalarAndInsert due to it being static, abstract and generic.

    LoadScalarAndInsert : LoadScalarAndInsert_MethodGroup
    class LoadScalarAndInsert_MethodGroup:
        @typing.overload
        def __call__(self, address: clr.Reference[float], vector: Vector128_1[float], index: int) -> Vector128_1[float]:...
        # Method LoadScalarAndInsert(address : Double*, vector : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method LoadScalarAndInsert(address : SByte*, vector : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method LoadScalarAndInsert(address : Byte*, vector : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method LoadScalarAndInsert(address : Int16*, vector : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method LoadScalarAndInsert(address : UInt16*, vector : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method LoadScalarAndInsert(address : Int32*, vector : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method LoadScalarAndInsert(address : UInt32*, vector : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method LoadScalarAndInsert(address : Int64*, vector : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method LoadScalarAndInsert(address : UInt64*, vector : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method LoadScalarAndInsert(address : IntPtr*, vector : Vector128`1, index : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, address: clr.Reference[UIntPtr], vector: Vector128_1[UIntPtr], index: int) -> Vector128_1[UIntPtr]:...

    # Skipped LoadScalarAndSplatVector128 due to it being static, abstract and generic.

    LoadScalarAndSplatVector128 : LoadScalarAndSplatVector128_MethodGroup
    class LoadScalarAndSplatVector128_MethodGroup:
        @typing.overload
        def __call__(self, address: clr.Reference[float]) -> Vector128_1[float]:...
        # Method LoadScalarAndSplatVector128(address : Double*) was skipped since it collides with above method
        # Method LoadScalarAndSplatVector128(address : SByte*) was skipped since it collides with above method
        # Method LoadScalarAndSplatVector128(address : Byte*) was skipped since it collides with above method
        # Method LoadScalarAndSplatVector128(address : Int16*) was skipped since it collides with above method
        # Method LoadScalarAndSplatVector128(address : UInt16*) was skipped since it collides with above method
        # Method LoadScalarAndSplatVector128(address : Int32*) was skipped since it collides with above method
        # Method LoadScalarAndSplatVector128(address : UInt32*) was skipped since it collides with above method
        # Method LoadScalarAndSplatVector128(address : Int64*) was skipped since it collides with above method
        # Method LoadScalarAndSplatVector128(address : UInt64*) was skipped since it collides with above method
        # Method LoadScalarAndSplatVector128(address : IntPtr*) was skipped since it collides with above method
        @typing.overload
        def __call__(self, address: clr.Reference[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped LoadScalarVector128 due to it being static, abstract and generic.

    LoadScalarVector128 : LoadScalarVector128_MethodGroup
    class LoadScalarVector128_MethodGroup:
        @typing.overload
        def __call__(self, address: clr.Reference[float]) -> Vector128_1[float]:...
        # Method LoadScalarVector128(address : Double*) was skipped since it collides with above method
        # Method LoadScalarVector128(address : Int32*) was skipped since it collides with above method
        # Method LoadScalarVector128(address : UInt32*) was skipped since it collides with above method
        # Method LoadScalarVector128(address : Int64*) was skipped since it collides with above method
        # Method LoadScalarVector128(address : UInt64*) was skipped since it collides with above method
        # Method LoadScalarVector128(address : IntPtr*) was skipped since it collides with above method
        @typing.overload
        def __call__(self, address: clr.Reference[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped LoadVector128 due to it being static, abstract and generic.

    LoadVector128 : LoadVector128_MethodGroup
    class LoadVector128_MethodGroup:
        @typing.overload
        def __call__(self, address: clr.Reference[float]) -> Vector128_1[float]:...
        # Method LoadVector128(address : Double*) was skipped since it collides with above method
        # Method LoadVector128(address : SByte*) was skipped since it collides with above method
        # Method LoadVector128(address : Byte*) was skipped since it collides with above method
        # Method LoadVector128(address : Int16*) was skipped since it collides with above method
        # Method LoadVector128(address : UInt16*) was skipped since it collides with above method
        # Method LoadVector128(address : Int32*) was skipped since it collides with above method
        # Method LoadVector128(address : UInt32*) was skipped since it collides with above method
        # Method LoadVector128(address : Int64*) was skipped since it collides with above method
        # Method LoadVector128(address : UInt64*) was skipped since it collides with above method
        # Method LoadVector128(address : IntPtr*) was skipped since it collides with above method
        @typing.overload
        def __call__(self, address: clr.Reference[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped LoadWideningVector128 due to it being static, abstract and generic.

    LoadWideningVector128 : LoadWideningVector128_MethodGroup
    class LoadWideningVector128_MethodGroup:
        def __call__(self, address: clr.Reference[int]) -> Vector128_1[int]:...
        # Method LoadWideningVector128(address : Byte*) was skipped since it collides with above method
        # Method LoadWideningVector128(address : Int16*) was skipped since it collides with above method
        # Method LoadWideningVector128(address : UInt16*) was skipped since it collides with above method
        # Method LoadWideningVector128(address : Int32*) was skipped since it collides with above method
        # Method LoadWideningVector128(address : UInt32*) was skipped since it collides with above method

    # Skipped Max due to it being static, abstract and generic.

    Max : Max_MethodGroup
    class Max_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Max(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped Min due to it being static, abstract and generic.

    Min : Min_MethodGroup
    class Min_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Min(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Multiply(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Multiply(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Multiply(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Multiply(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Multiply(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Multiply(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Multiply(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Multiply(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[UIntPtr], right: Vector128_1[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped MultiplyWideningLower due to it being static, abstract and generic.

    MultiplyWideningLower : MultiplyWideningLower_MethodGroup
    class MultiplyWideningLower_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyWideningLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningLower(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped MultiplyWideningUpper due to it being static, abstract and generic.

    MultiplyWideningUpper : MultiplyWideningUpper_MethodGroup
    class MultiplyWideningUpper_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method MultiplyWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method MultiplyWideningUpper(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped Negate due to it being static, abstract and generic.

    Negate : Negate_MethodGroup
    class Negate_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Negate(value : Vector128`1) was skipped since it collides with above method
        # Method Negate(value : Vector128`1) was skipped since it collides with above method
        # Method Negate(value : Vector128`1) was skipped since it collides with above method
        # Method Negate(value : Vector128`1) was skipped since it collides with above method
        # Method Negate(value : Vector128`1) was skipped since it collides with above method
        # Method Negate(value : Vector128`1) was skipped since it collides with above method
        # Method Negate(value : Vector128`1) was skipped since it collides with above method
        # Method Negate(value : Vector128`1) was skipped since it collides with above method
        # Method Negate(value : Vector128`1) was skipped since it collides with above method
        # Method Negate(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped Not due to it being static, abstract and generic.

    Not : Not_MethodGroup
    class Not_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        # Method Not(value : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped Or due to it being static, abstract and generic.

    Or : Or_MethodGroup
    class Or_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Or(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[UIntPtr], right: Vector128_1[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped PseudoMax due to it being static, abstract and generic.

    PseudoMax : PseudoMax_MethodGroup
    class PseudoMax_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method PseudoMax(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped PseudoMin due to it being static, abstract and generic.

    PseudoMin : PseudoMin_MethodGroup
    class PseudoMin_MethodGroup:
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method PseudoMin(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped ReplaceScalar due to it being static, abstract and generic.

    ReplaceScalar : ReplaceScalar_MethodGroup
    class ReplaceScalar_MethodGroup:
        @typing.overload
        def __call__(self, vector: Vector128_1[float], imm: int, value: float) -> Vector128_1[float]:...
        # Method ReplaceScalar(vector : Vector128`1, imm : Byte, value : Double) was skipped since it collides with above method
        # Method ReplaceScalar(vector : Vector128`1, imm : Byte, value : Int32) was skipped since it collides with above method
        # Method ReplaceScalar(vector : Vector128`1, imm : Byte, value : UInt32) was skipped since it collides with above method
        # Method ReplaceScalar(vector : Vector128`1, imm : Byte, value : Int32) was skipped since it collides with above method
        # Method ReplaceScalar(vector : Vector128`1, imm : Byte, value : UInt32) was skipped since it collides with above method
        # Method ReplaceScalar(vector : Vector128`1, imm : Byte, value : Int32) was skipped since it collides with above method
        # Method ReplaceScalar(vector : Vector128`1, imm : Byte, value : UInt32) was skipped since it collides with above method
        # Method ReplaceScalar(vector : Vector128`1, imm : Byte, value : Int64) was skipped since it collides with above method
        # Method ReplaceScalar(vector : Vector128`1, imm : Byte, value : UInt64) was skipped since it collides with above method
        # Method ReplaceScalar(vector : Vector128`1, imm : Byte, value : IntPtr) was skipped since it collides with above method
        @typing.overload
        def __call__(self, vector: Vector128_1[UIntPtr], imm: int, value: UIntPtr) -> Vector128_1[UIntPtr]:...

    # Skipped RoundToNearest due to it being static, abstract and generic.

    RoundToNearest : RoundToNearest_MethodGroup
    class RoundToNearest_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method RoundToNearest(value : Vector128`1) was skipped since it collides with above method

    # Skipped ShiftLeft due to it being static, abstract and generic.

    ShiftLeft : ShiftLeft_MethodGroup
    class ShiftLeft_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftLeft(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftLeft(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftLeft(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftLeft(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftLeft(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftLeft(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftLeft(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftLeft(value : Vector128`1, count : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[UIntPtr], count: int) -> Vector128_1[UIntPtr]:...

    # Skipped ShiftRightArithmetic due to it being static, abstract and generic.

    ShiftRightArithmetic : ShiftRightArithmetic_MethodGroup
    class ShiftRightArithmetic_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightArithmetic(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(value : Vector128`1, count : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[UIntPtr], count: int) -> Vector128_1[UIntPtr]:...

    # Skipped ShiftRightLogical due to it being static, abstract and generic.

    ShiftRightLogical : ShiftRightLogical_MethodGroup
    class ShiftRightLogical_MethodGroup:
        @typing.overload
        def __call__(self, value: Vector128_1[int], count: int) -> Vector128_1[int]:...
        # Method ShiftRightLogical(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(value : Vector128`1, count : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: Vector128_1[UIntPtr], count: int) -> Vector128_1[UIntPtr]:...

    # Skipped SignExtendWideningLower due to it being static, abstract and generic.

    SignExtendWideningLower : SignExtendWideningLower_MethodGroup
    class SignExtendWideningLower_MethodGroup:
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method SignExtendWideningLower(value : Vector128`1) was skipped since it collides with above method
        # Method SignExtendWideningLower(value : Vector128`1) was skipped since it collides with above method
        # Method SignExtendWideningLower(value : Vector128`1) was skipped since it collides with above method
        # Method SignExtendWideningLower(value : Vector128`1) was skipped since it collides with above method
        # Method SignExtendWideningLower(value : Vector128`1) was skipped since it collides with above method

    # Skipped SignExtendWideningUpper due to it being static, abstract and generic.

    SignExtendWideningUpper : SignExtendWideningUpper_MethodGroup
    class SignExtendWideningUpper_MethodGroup:
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method SignExtendWideningUpper(value : Vector128`1) was skipped since it collides with above method
        # Method SignExtendWideningUpper(value : Vector128`1) was skipped since it collides with above method
        # Method SignExtendWideningUpper(value : Vector128`1) was skipped since it collides with above method
        # Method SignExtendWideningUpper(value : Vector128`1) was skipped since it collides with above method
        # Method SignExtendWideningUpper(value : Vector128`1) was skipped since it collides with above method

    # Skipped Splat due to it being static, abstract and generic.

    Splat : Splat_MethodGroup
    class Splat_MethodGroup:
        @typing.overload
        def __call__(self, value: float) -> Vector128_1[float]:...
        # Method Splat(value : Double) was skipped since it collides with above method
        # Method Splat(value : SByte) was skipped since it collides with above method
        # Method Splat(value : Byte) was skipped since it collides with above method
        # Method Splat(value : Int16) was skipped since it collides with above method
        # Method Splat(value : UInt16) was skipped since it collides with above method
        # Method Splat(value : Int32) was skipped since it collides with above method
        # Method Splat(value : UInt32) was skipped since it collides with above method
        # Method Splat(value : Int64) was skipped since it collides with above method
        # Method Splat(value : UInt64) was skipped since it collides with above method
        # Method Splat(value : IntPtr) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> Vector128_1[UIntPtr]:...

    # Skipped Sqrt due to it being static, abstract and generic.

    Sqrt : Sqrt_MethodGroup
    class Sqrt_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Sqrt(value : Vector128`1) was skipped since it collides with above method

    # Skipped Store due to it being static, abstract and generic.

    Store : Store_MethodGroup
    class Store_MethodGroup:
        @typing.overload
        def __call__(self, address: clr.Reference[float], source: Vector128_1[float]) -> None:...
        # Method Store(address : Double*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : SByte*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : Byte*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : Int16*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : UInt16*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : Int32*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : UInt32*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : Int64*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : UInt64*, source : Vector128`1) was skipped since it collides with above method
        # Method Store(address : IntPtr*, source : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, address: clr.Reference[UIntPtr], source: Vector128_1[UIntPtr]) -> None:...

    # Skipped StoreSelectedScalar due to it being static, abstract and generic.

    StoreSelectedScalar : StoreSelectedScalar_MethodGroup
    class StoreSelectedScalar_MethodGroup:
        @typing.overload
        def __call__(self, address: clr.Reference[float], source: Vector128_1[float], index: int) -> None:...
        # Method StoreSelectedScalar(address : Double*, source : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : SByte*, source : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : Byte*, source : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : Int16*, source : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : UInt16*, source : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : Int32*, source : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : UInt32*, source : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : Int64*, source : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : UInt64*, source : Vector128`1, index : Byte) was skipped since it collides with above method
        # Method StoreSelectedScalar(address : IntPtr*, source : Vector128`1, index : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, address: clr.Reference[UIntPtr], source: Vector128_1[UIntPtr], index: int) -> None:...

    # Skipped Subtract due to it being static, abstract and generic.

    Subtract : Subtract_MethodGroup
    class Subtract_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Subtract(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[UIntPtr], right: Vector128_1[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped SubtractSaturate due to it being static, abstract and generic.

    SubtractSaturate : SubtractSaturate_MethodGroup
    class SubtractSaturate_MethodGroup:
        def __call__(self, left: Vector128_1[int], right: Vector128_1[int]) -> Vector128_1[int]:...
        # Method SubtractSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method SubtractSaturate(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method

    # Skipped Swizzle due to it being static, abstract and generic.

    Swizzle : Swizzle_MethodGroup
    class Swizzle_MethodGroup:
        def __call__(self, vector: Vector128_1[int], indices: Vector128_1[int]) -> Vector128_1[int]:...
        # Method Swizzle(vector : Vector128`1, indices : Vector128`1) was skipped since it collides with above method

    # Skipped Truncate due to it being static, abstract and generic.

    Truncate : Truncate_MethodGroup
    class Truncate_MethodGroup:
        def __call__(self, value: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Truncate(value : Vector128`1) was skipped since it collides with above method

    # Skipped Xor due to it being static, abstract and generic.

    Xor : Xor_MethodGroup
    class Xor_MethodGroup:
        @typing.overload
        def __call__(self, left: Vector128_1[float], right: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        # Method Xor(left : Vector128`1, right : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, left: Vector128_1[UIntPtr], right: Vector128_1[UIntPtr]) -> Vector128_1[UIntPtr]:...

    # Skipped ZeroExtendWideningLower due to it being static, abstract and generic.

    ZeroExtendWideningLower : ZeroExtendWideningLower_MethodGroup
    class ZeroExtendWideningLower_MethodGroup:
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ZeroExtendWideningLower(value : Vector128`1) was skipped since it collides with above method
        # Method ZeroExtendWideningLower(value : Vector128`1) was skipped since it collides with above method
        # Method ZeroExtendWideningLower(value : Vector128`1) was skipped since it collides with above method
        # Method ZeroExtendWideningLower(value : Vector128`1) was skipped since it collides with above method
        # Method ZeroExtendWideningLower(value : Vector128`1) was skipped since it collides with above method

    # Skipped ZeroExtendWideningUpper due to it being static, abstract and generic.

    ZeroExtendWideningUpper : ZeroExtendWideningUpper_MethodGroup
    class ZeroExtendWideningUpper_MethodGroup:
        def __call__(self, value: Vector128_1[int]) -> Vector128_1[int]:...
        # Method ZeroExtendWideningUpper(value : Vector128`1) was skipped since it collides with above method
        # Method ZeroExtendWideningUpper(value : Vector128`1) was skipped since it collides with above method
        # Method ZeroExtendWideningUpper(value : Vector128`1) was skipped since it collides with above method
        # Method ZeroExtendWideningUpper(value : Vector128`1) was skipped since it collides with above method
        # Method ZeroExtendWideningUpper(value : Vector128`1) was skipped since it collides with above method


