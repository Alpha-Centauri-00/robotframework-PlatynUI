import typing, clr, abc
from System.Numerics import Vector2, Vector3, Vector4, Vector_1
from System import UIntPtr, Array_1, Span_1, ReadOnlySpan_1, ValueTuple_2, IEquatable_1

class Vector128_GenericClasses(abc.ABCMeta):
    Generic_Vector128_GenericClasses_Vector128_1_T = typing.TypeVar('Generic_Vector128_GenericClasses_Vector128_1_T')
    def __getitem__(self, types : typing.Type[Generic_Vector128_GenericClasses_Vector128_1_T]) -> typing.Type[Vector128_1[Generic_Vector128_GenericClasses_Vector128_1_T]]: ...

class Vector128(Vector128_0, metaclass =Vector128_GenericClasses): ...

class Vector128_0(abc.ABC):
    @classmethod
    @property
    def IsHardwareAccelerated(cls) -> bool: ...
    @staticmethod
    def AsVector2(value: Vector128_1[float]) -> Vector2: ...
    @staticmethod
    def AsVector3(value: Vector128_1[float]) -> Vector3: ...
    @staticmethod
    def AsVector4(value: Vector128_1[float]) -> Vector4: ...
    @staticmethod
    def ConvertToInt32(vector: Vector128_1[float]) -> Vector128_1[int]: ...
    @staticmethod
    def ConvertToInt64(vector: Vector128_1[float]) -> Vector128_1[int]: ...
    @staticmethod
    def ConvertToUInt32(vector: Vector128_1[float]) -> Vector128_1[int]: ...
    @staticmethod
    def ConvertToUInt64(vector: Vector128_1[float]) -> Vector128_1[int]: ...
    # Skipped Abs due to it being static, abstract and generic.

    Abs : Abs_MethodGroup
    class Abs_MethodGroup:
        def __getitem__(self, t:typing.Type[Abs_1_T1]) -> Abs_1[Abs_1_T1]: ...

        Abs_1_T1 = typing.TypeVar('Abs_1_T1')
        class Abs_1(typing.Generic[Abs_1_T1]):
            Abs_1_T = Vector128_0.Abs_MethodGroup.Abs_1_T1
            def __call__(self, vector: Vector128_1[Abs_1_T]) -> Vector128_1[Abs_1_T]:...


    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        def __getitem__(self, t:typing.Type[Add_1_T1]) -> Add_1[Add_1_T1]: ...

        Add_1_T1 = typing.TypeVar('Add_1_T1')
        class Add_1(typing.Generic[Add_1_T1]):
            Add_1_T = Vector128_0.Add_MethodGroup.Add_1_T1
            def __call__(self, left: Vector128_1[Add_1_T], right: Vector128_1[Add_1_T]) -> Vector128_1[Add_1_T]:...


    # Skipped AndNot due to it being static, abstract and generic.

    AndNot : AndNot_MethodGroup
    class AndNot_MethodGroup:
        def __getitem__(self, t:typing.Type[AndNot_1_T1]) -> AndNot_1[AndNot_1_T1]: ...

        AndNot_1_T1 = typing.TypeVar('AndNot_1_T1')
        class AndNot_1(typing.Generic[AndNot_1_T1]):
            AndNot_1_T = Vector128_0.AndNot_MethodGroup.AndNot_1_T1
            def __call__(self, left: Vector128_1[AndNot_1_T], right: Vector128_1[AndNot_1_T]) -> Vector128_1[AndNot_1_T]:...


    # Skipped As due to it being static, abstract and generic.

    As : As_MethodGroup
    class As_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[As_2_T1], typing.Type[As_2_T2]]) -> As_2[As_2_T1, As_2_T2]: ...

        As_2_T1 = typing.TypeVar('As_2_T1')
        As_2_T2 = typing.TypeVar('As_2_T2')
        class As_2(typing.Generic[As_2_T1, As_2_T2]):
            As_2_TFrom = Vector128_0.As_MethodGroup.As_2_T1
            As_2_TTo = Vector128_0.As_MethodGroup.As_2_T2
            def __call__(self, vector: Vector128_1[As_2_TFrom]) -> Vector128_1[As_2_TTo]:...


    # Skipped AsByte due to it being static, abstract and generic.

    AsByte : AsByte_MethodGroup
    class AsByte_MethodGroup:
        def __getitem__(self, t:typing.Type[AsByte_1_T1]) -> AsByte_1[AsByte_1_T1]: ...

        AsByte_1_T1 = typing.TypeVar('AsByte_1_T1')
        class AsByte_1(typing.Generic[AsByte_1_T1]):
            AsByte_1_T = Vector128_0.AsByte_MethodGroup.AsByte_1_T1
            def __call__(self, vector: Vector128_1[AsByte_1_T]) -> Vector128_1[int]:...


    # Skipped AsDouble due to it being static, abstract and generic.

    AsDouble : AsDouble_MethodGroup
    class AsDouble_MethodGroup:
        def __getitem__(self, t:typing.Type[AsDouble_1_T1]) -> AsDouble_1[AsDouble_1_T1]: ...

        AsDouble_1_T1 = typing.TypeVar('AsDouble_1_T1')
        class AsDouble_1(typing.Generic[AsDouble_1_T1]):
            AsDouble_1_T = Vector128_0.AsDouble_MethodGroup.AsDouble_1_T1
            def __call__(self, vector: Vector128_1[AsDouble_1_T]) -> Vector128_1[float]:...


    # Skipped AsInt16 due to it being static, abstract and generic.

    AsInt16 : AsInt16_MethodGroup
    class AsInt16_MethodGroup:
        def __getitem__(self, t:typing.Type[AsInt16_1_T1]) -> AsInt16_1[AsInt16_1_T1]: ...

        AsInt16_1_T1 = typing.TypeVar('AsInt16_1_T1')
        class AsInt16_1(typing.Generic[AsInt16_1_T1]):
            AsInt16_1_T = Vector128_0.AsInt16_MethodGroup.AsInt16_1_T1
            def __call__(self, vector: Vector128_1[AsInt16_1_T]) -> Vector128_1[int]:...


    # Skipped AsInt32 due to it being static, abstract and generic.

    AsInt32 : AsInt32_MethodGroup
    class AsInt32_MethodGroup:
        def __getitem__(self, t:typing.Type[AsInt32_1_T1]) -> AsInt32_1[AsInt32_1_T1]: ...

        AsInt32_1_T1 = typing.TypeVar('AsInt32_1_T1')
        class AsInt32_1(typing.Generic[AsInt32_1_T1]):
            AsInt32_1_T = Vector128_0.AsInt32_MethodGroup.AsInt32_1_T1
            def __call__(self, vector: Vector128_1[AsInt32_1_T]) -> Vector128_1[int]:...


    # Skipped AsInt64 due to it being static, abstract and generic.

    AsInt64 : AsInt64_MethodGroup
    class AsInt64_MethodGroup:
        def __getitem__(self, t:typing.Type[AsInt64_1_T1]) -> AsInt64_1[AsInt64_1_T1]: ...

        AsInt64_1_T1 = typing.TypeVar('AsInt64_1_T1')
        class AsInt64_1(typing.Generic[AsInt64_1_T1]):
            AsInt64_1_T = Vector128_0.AsInt64_MethodGroup.AsInt64_1_T1
            def __call__(self, vector: Vector128_1[AsInt64_1_T]) -> Vector128_1[int]:...


    # Skipped AsNInt due to it being static, abstract and generic.

    AsNInt : AsNInt_MethodGroup
    class AsNInt_MethodGroup:
        def __getitem__(self, t:typing.Type[AsNInt_1_T1]) -> AsNInt_1[AsNInt_1_T1]: ...

        AsNInt_1_T1 = typing.TypeVar('AsNInt_1_T1')
        class AsNInt_1(typing.Generic[AsNInt_1_T1]):
            AsNInt_1_T = Vector128_0.AsNInt_MethodGroup.AsNInt_1_T1
            def __call__(self, vector: Vector128_1[AsNInt_1_T]) -> Vector128_1[int]:...


    # Skipped AsNUInt due to it being static, abstract and generic.

    AsNUInt : AsNUInt_MethodGroup
    class AsNUInt_MethodGroup:
        def __getitem__(self, t:typing.Type[AsNUInt_1_T1]) -> AsNUInt_1[AsNUInt_1_T1]: ...

        AsNUInt_1_T1 = typing.TypeVar('AsNUInt_1_T1')
        class AsNUInt_1(typing.Generic[AsNUInt_1_T1]):
            AsNUInt_1_T = Vector128_0.AsNUInt_MethodGroup.AsNUInt_1_T1
            def __call__(self, vector: Vector128_1[AsNUInt_1_T]) -> Vector128_1[UIntPtr]:...


    # Skipped AsSByte due to it being static, abstract and generic.

    AsSByte : AsSByte_MethodGroup
    class AsSByte_MethodGroup:
        def __getitem__(self, t:typing.Type[AsSByte_1_T1]) -> AsSByte_1[AsSByte_1_T1]: ...

        AsSByte_1_T1 = typing.TypeVar('AsSByte_1_T1')
        class AsSByte_1(typing.Generic[AsSByte_1_T1]):
            AsSByte_1_T = Vector128_0.AsSByte_MethodGroup.AsSByte_1_T1
            def __call__(self, vector: Vector128_1[AsSByte_1_T]) -> Vector128_1[int]:...


    # Skipped AsSingle due to it being static, abstract and generic.

    AsSingle : AsSingle_MethodGroup
    class AsSingle_MethodGroup:
        def __getitem__(self, t:typing.Type[AsSingle_1_T1]) -> AsSingle_1[AsSingle_1_T1]: ...

        AsSingle_1_T1 = typing.TypeVar('AsSingle_1_T1')
        class AsSingle_1(typing.Generic[AsSingle_1_T1]):
            AsSingle_1_T = Vector128_0.AsSingle_MethodGroup.AsSingle_1_T1
            def __call__(self, vector: Vector128_1[AsSingle_1_T]) -> Vector128_1[float]:...


    # Skipped AsUInt16 due to it being static, abstract and generic.

    AsUInt16 : AsUInt16_MethodGroup
    class AsUInt16_MethodGroup:
        def __getitem__(self, t:typing.Type[AsUInt16_1_T1]) -> AsUInt16_1[AsUInt16_1_T1]: ...

        AsUInt16_1_T1 = typing.TypeVar('AsUInt16_1_T1')
        class AsUInt16_1(typing.Generic[AsUInt16_1_T1]):
            AsUInt16_1_T = Vector128_0.AsUInt16_MethodGroup.AsUInt16_1_T1
            def __call__(self, vector: Vector128_1[AsUInt16_1_T]) -> Vector128_1[int]:...


    # Skipped AsUInt32 due to it being static, abstract and generic.

    AsUInt32 : AsUInt32_MethodGroup
    class AsUInt32_MethodGroup:
        def __getitem__(self, t:typing.Type[AsUInt32_1_T1]) -> AsUInt32_1[AsUInt32_1_T1]: ...

        AsUInt32_1_T1 = typing.TypeVar('AsUInt32_1_T1')
        class AsUInt32_1(typing.Generic[AsUInt32_1_T1]):
            AsUInt32_1_T = Vector128_0.AsUInt32_MethodGroup.AsUInt32_1_T1
            def __call__(self, vector: Vector128_1[AsUInt32_1_T]) -> Vector128_1[int]:...


    # Skipped AsUInt64 due to it being static, abstract and generic.

    AsUInt64 : AsUInt64_MethodGroup
    class AsUInt64_MethodGroup:
        def __getitem__(self, t:typing.Type[AsUInt64_1_T1]) -> AsUInt64_1[AsUInt64_1_T1]: ...

        AsUInt64_1_T1 = typing.TypeVar('AsUInt64_1_T1')
        class AsUInt64_1(typing.Generic[AsUInt64_1_T1]):
            AsUInt64_1_T = Vector128_0.AsUInt64_MethodGroup.AsUInt64_1_T1
            def __call__(self, vector: Vector128_1[AsUInt64_1_T]) -> Vector128_1[int]:...


    # Skipped AsVector due to it being static, abstract and generic.

    AsVector : AsVector_MethodGroup
    class AsVector_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVector_1_T1]) -> AsVector_1[AsVector_1_T1]: ...

        AsVector_1_T1 = typing.TypeVar('AsVector_1_T1')
        class AsVector_1(typing.Generic[AsVector_1_T1]):
            AsVector_1_T = Vector128_0.AsVector_MethodGroup.AsVector_1_T1
            def __call__(self, value: Vector128_1[AsVector_1_T]) -> Vector_1[AsVector_1_T]:...


    # Skipped AsVector128 due to it being static, abstract and generic.

    AsVector128 : AsVector128_MethodGroup
    class AsVector128_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVector128_1_T1]) -> AsVector128_1[AsVector128_1_T1]: ...

        AsVector128_1_T1 = typing.TypeVar('AsVector128_1_T1')
        class AsVector128_1(typing.Generic[AsVector128_1_T1]):
            AsVector128_1_T = Vector128_0.AsVector128_MethodGroup.AsVector128_1_T1
            def __call__(self, value: Vector_1[AsVector128_1_T]) -> Vector128_1[AsVector128_1_T]:...

        @typing.overload
        def __call__(self, value: Vector2) -> Vector128_1[float]:...
        @typing.overload
        def __call__(self, value: Vector3) -> Vector128_1[float]:...
        @typing.overload
        def __call__(self, value: Vector4) -> Vector128_1[float]:...

    # Skipped BitwiseAnd due to it being static, abstract and generic.

    BitwiseAnd : BitwiseAnd_MethodGroup
    class BitwiseAnd_MethodGroup:
        def __getitem__(self, t:typing.Type[BitwiseAnd_1_T1]) -> BitwiseAnd_1[BitwiseAnd_1_T1]: ...

        BitwiseAnd_1_T1 = typing.TypeVar('BitwiseAnd_1_T1')
        class BitwiseAnd_1(typing.Generic[BitwiseAnd_1_T1]):
            BitwiseAnd_1_T = Vector128_0.BitwiseAnd_MethodGroup.BitwiseAnd_1_T1
            def __call__(self, left: Vector128_1[BitwiseAnd_1_T], right: Vector128_1[BitwiseAnd_1_T]) -> Vector128_1[BitwiseAnd_1_T]:...


    # Skipped BitwiseOr due to it being static, abstract and generic.

    BitwiseOr : BitwiseOr_MethodGroup
    class BitwiseOr_MethodGroup:
        def __getitem__(self, t:typing.Type[BitwiseOr_1_T1]) -> BitwiseOr_1[BitwiseOr_1_T1]: ...

        BitwiseOr_1_T1 = typing.TypeVar('BitwiseOr_1_T1')
        class BitwiseOr_1(typing.Generic[BitwiseOr_1_T1]):
            BitwiseOr_1_T = Vector128_0.BitwiseOr_MethodGroup.BitwiseOr_1_T1
            def __call__(self, left: Vector128_1[BitwiseOr_1_T], right: Vector128_1[BitwiseOr_1_T]) -> Vector128_1[BitwiseOr_1_T]:...


    # Skipped Ceiling due to it being static, abstract and generic.

    Ceiling : Ceiling_MethodGroup
    class Ceiling_MethodGroup:
        def __call__(self, vector: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Ceiling(vector : Vector128`1) was skipped since it collides with above method

    # Skipped ConditionalSelect due to it being static, abstract and generic.

    ConditionalSelect : ConditionalSelect_MethodGroup
    class ConditionalSelect_MethodGroup:
        def __getitem__(self, t:typing.Type[ConditionalSelect_1_T1]) -> ConditionalSelect_1[ConditionalSelect_1_T1]: ...

        ConditionalSelect_1_T1 = typing.TypeVar('ConditionalSelect_1_T1')
        class ConditionalSelect_1(typing.Generic[ConditionalSelect_1_T1]):
            ConditionalSelect_1_T = Vector128_0.ConditionalSelect_MethodGroup.ConditionalSelect_1_T1
            def __call__(self, condition: Vector128_1[ConditionalSelect_1_T], left: Vector128_1[ConditionalSelect_1_T], right: Vector128_1[ConditionalSelect_1_T]) -> Vector128_1[ConditionalSelect_1_T]:...


    # Skipped ConvertToDouble due to it being static, abstract and generic.

    ConvertToDouble : ConvertToDouble_MethodGroup
    class ConvertToDouble_MethodGroup:
        def __call__(self, vector: Vector128_1[int]) -> Vector128_1[float]:...
        # Method ConvertToDouble(vector : Vector128`1) was skipped since it collides with above method

    # Skipped ConvertToSingle due to it being static, abstract and generic.

    ConvertToSingle : ConvertToSingle_MethodGroup
    class ConvertToSingle_MethodGroup:
        def __call__(self, vector: Vector128_1[int]) -> Vector128_1[float]:...
        # Method ConvertToSingle(vector : Vector128`1) was skipped since it collides with above method

    # Skipped CopyTo due to it being static, abstract and generic.

    CopyTo : CopyTo_MethodGroup
    class CopyTo_MethodGroup:
        def __getitem__(self, t:typing.Type[CopyTo_1_T1]) -> CopyTo_1[CopyTo_1_T1]: ...

        CopyTo_1_T1 = typing.TypeVar('CopyTo_1_T1')
        class CopyTo_1(typing.Generic[CopyTo_1_T1]):
            CopyTo_1_T = Vector128_0.CopyTo_MethodGroup.CopyTo_1_T1
            @typing.overload
            def __call__(self, vector: Vector128_1[CopyTo_1_T], destination: Array_1[CopyTo_1_T]) -> None:...
            @typing.overload
            def __call__(self, vector: Vector128_1[CopyTo_1_T], destination: Span_1[CopyTo_1_T]) -> None:...
            @typing.overload
            def __call__(self, vector: Vector128_1[CopyTo_1_T], destination: Array_1[CopyTo_1_T], startIndex: int) -> None:...


    # Skipped Create due to it being static, abstract and generic.

    Create : Create_MethodGroup
    class Create_MethodGroup:
        def __getitem__(self, t:typing.Type[Create_1_T1]) -> Create_1[Create_1_T1]: ...

        Create_1_T1 = typing.TypeVar('Create_1_T1')
        class Create_1(typing.Generic[Create_1_T1]):
            Create_1_T = Vector128_0.Create_MethodGroup.Create_1_T1
            @typing.overload
            def __call__(self, values: Array_1[Create_1_T]) -> Vector128_1[Create_1_T]:...
            @typing.overload
            def __call__(self, values: ReadOnlySpan_1[Create_1_T]) -> Vector128_1[Create_1_T]:...
            @typing.overload
            def __call__(self, value: typing.Optional[Create_1_T]) -> Vector128_1[Create_1_T]:...
            @typing.overload
            def __call__(self, values: Array_1[Create_1_T], index: int) -> Vector128_1[Create_1_T]:...
            @typing.overload
            def __call__(self, lower: Vector64_1[Create_1_T], upper: Vector64_1[Create_1_T]) -> Vector128_1[Create_1_T]:...

        @typing.overload
        def __call__(self, value: float) -> Vector128_1[float]:...
        # Method Create(value : Single) was skipped since it collides with above method
        # Method Create(value : Byte) was skipped since it collides with above method
        # Method Create(value : Int16) was skipped since it collides with above method
        # Method Create(value : Int32) was skipped since it collides with above method
        # Method Create(value : Int64) was skipped since it collides with above method
        # Method Create(value : SByte) was skipped since it collides with above method
        # Method Create(value : UInt16) was skipped since it collides with above method
        # Method Create(value : UInt32) was skipped since it collides with above method
        # Method Create(value : UInt64) was skipped since it collides with above method
        # Method Create(value : IntPtr) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> Vector128_1[UIntPtr]:...
        @typing.overload
        def __call__(self, e0: float, e1: float) -> Vector128_1[float]:...
        # Method Create(e0 : Int64, e1 : Int64) was skipped since it collides with above method
        # Method Create(e0 : UInt64, e1 : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, lower: Vector64_1[float], upper: Vector64_1[float]) -> Vector128_1[float]:...
        # Method Create(lower : Vector64`1, upper : Vector64`1) was skipped since it collides with above method
        # Method Create(lower : Vector64`1, upper : Vector64`1) was skipped since it collides with above method
        # Method Create(lower : Vector64`1, upper : Vector64`1) was skipped since it collides with above method
        # Method Create(lower : Vector64`1, upper : Vector64`1) was skipped since it collides with above method
        # Method Create(lower : Vector64`1, upper : Vector64`1) was skipped since it collides with above method
        # Method Create(lower : Vector64`1, upper : Vector64`1) was skipped since it collides with above method
        # Method Create(lower : Vector64`1, upper : Vector64`1) was skipped since it collides with above method
        # Method Create(lower : Vector64`1, upper : Vector64`1) was skipped since it collides with above method
        # Method Create(lower : Vector64`1, upper : Vector64`1) was skipped since it collides with above method
        # Method Create(lower : Vector64`1, upper : Vector64`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, lower: Vector64_1[UIntPtr], upper: Vector64_1[UIntPtr]) -> Vector128_1[UIntPtr]:...
        @typing.overload
        def __call__(self, e0: float, e1: float, e2: float, e3: float) -> Vector128_1[float]:...
        # Method Create(e0 : Int32, e1 : Int32, e2 : Int32, e3 : Int32) was skipped since it collides with above method
        # Method Create(e0 : UInt32, e1 : UInt32, e2 : UInt32, e3 : UInt32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, e0: int, e1: int, e2: int, e3: int, e4: int, e5: int, e6: int, e7: int) -> Vector128_1[int]:...
        # Method Create(e0 : UInt16, e1 : UInt16, e2 : UInt16, e3 : UInt16, e4 : UInt16, e5 : UInt16, e6 : UInt16, e7 : UInt16) was skipped since it collides with above method
        @typing.overload
        def __call__(self, e0: int, e1: int, e2: int, e3: int, e4: int, e5: int, e6: int, e7: int, e8: int, e9: int, e10: int, e11: int, e12: int, e13: int, e14: int, e15: int) -> Vector128_1[int]:...
        # Method Create(e0 : SByte, e1 : SByte, e2 : SByte, e3 : SByte, e4 : SByte, e5 : SByte, e6 : SByte, e7 : SByte, e8 : SByte, e9 : SByte, e10 : SByte, e11 : SByte, e12 : SByte, e13 : SByte, e14 : SByte, e15 : SByte) was skipped since it collides with above method

    # Skipped CreateScalar due to it being static, abstract and generic.

    CreateScalar : CreateScalar_MethodGroup
    class CreateScalar_MethodGroup:
        def __getitem__(self, t:typing.Type[CreateScalar_1_T1]) -> CreateScalar_1[CreateScalar_1_T1]: ...

        CreateScalar_1_T1 = typing.TypeVar('CreateScalar_1_T1')
        class CreateScalar_1(typing.Generic[CreateScalar_1_T1]):
            CreateScalar_1_T = Vector128_0.CreateScalar_MethodGroup.CreateScalar_1_T1
            def __call__(self, value: typing.Optional[CreateScalar_1_T]) -> Vector128_1[CreateScalar_1_T]:...

        @typing.overload
        def __call__(self, value: float) -> Vector128_1[float]:...
        # Method CreateScalar(value : Single) was skipped since it collides with above method
        # Method CreateScalar(value : Byte) was skipped since it collides with above method
        # Method CreateScalar(value : Int16) was skipped since it collides with above method
        # Method CreateScalar(value : Int32) was skipped since it collides with above method
        # Method CreateScalar(value : Int64) was skipped since it collides with above method
        # Method CreateScalar(value : SByte) was skipped since it collides with above method
        # Method CreateScalar(value : UInt16) was skipped since it collides with above method
        # Method CreateScalar(value : UInt32) was skipped since it collides with above method
        # Method CreateScalar(value : UInt64) was skipped since it collides with above method
        # Method CreateScalar(value : IntPtr) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> Vector128_1[UIntPtr]:...

    # Skipped CreateScalarUnsafe due to it being static, abstract and generic.

    CreateScalarUnsafe : CreateScalarUnsafe_MethodGroup
    class CreateScalarUnsafe_MethodGroup:
        def __getitem__(self, t:typing.Type[CreateScalarUnsafe_1_T1]) -> CreateScalarUnsafe_1[CreateScalarUnsafe_1_T1]: ...

        CreateScalarUnsafe_1_T1 = typing.TypeVar('CreateScalarUnsafe_1_T1')
        class CreateScalarUnsafe_1(typing.Generic[CreateScalarUnsafe_1_T1]):
            CreateScalarUnsafe_1_T = Vector128_0.CreateScalarUnsafe_MethodGroup.CreateScalarUnsafe_1_T1
            def __call__(self, value: typing.Optional[CreateScalarUnsafe_1_T]) -> Vector128_1[CreateScalarUnsafe_1_T]:...

        @typing.overload
        def __call__(self, value: float) -> Vector128_1[float]:...
        # Method CreateScalarUnsafe(value : Single) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : Byte) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : Int16) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : Int32) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : Int64) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : SByte) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : UInt16) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : UInt32) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : UInt64) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : IntPtr) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> Vector128_1[UIntPtr]:...

    # Skipped Divide due to it being static, abstract and generic.

    Divide : Divide_MethodGroup
    class Divide_MethodGroup:
        def __getitem__(self, t:typing.Type[Divide_1_T1]) -> Divide_1[Divide_1_T1]: ...

        Divide_1_T1 = typing.TypeVar('Divide_1_T1')
        class Divide_1(typing.Generic[Divide_1_T1]):
            Divide_1_T = Vector128_0.Divide_MethodGroup.Divide_1_T1
            @typing.overload
            def __call__(self, left: Vector128_1[Divide_1_T], right: Vector128_1[Divide_1_T]) -> Vector128_1[Divide_1_T]:...
            @typing.overload
            def __call__(self, left: Vector128_1[Divide_1_T], right: typing.Optional[Divide_1_T]) -> Vector128_1[Divide_1_T]:...


    # Skipped Dot due to it being static, abstract and generic.

    Dot : Dot_MethodGroup
    class Dot_MethodGroup:
        def __getitem__(self, t:typing.Type[Dot_1_T1]) -> Dot_1[Dot_1_T1]: ...

        Dot_1_T1 = typing.TypeVar('Dot_1_T1')
        class Dot_1(typing.Generic[Dot_1_T1]):
            Dot_1_T = Vector128_0.Dot_MethodGroup.Dot_1_T1
            def __call__(self, left: Vector128_1[Dot_1_T], right: Vector128_1[Dot_1_T]) -> Dot_1_T:...


    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        def __getitem__(self, t:typing.Type[Equals_1_T1]) -> Equals_1[Equals_1_T1]: ...

        Equals_1_T1 = typing.TypeVar('Equals_1_T1')
        class Equals_1(typing.Generic[Equals_1_T1]):
            Equals_1_T = Vector128_0.Equals_MethodGroup.Equals_1_T1
            def __call__(self, left: Vector128_1[Equals_1_T], right: Vector128_1[Equals_1_T]) -> Vector128_1[Equals_1_T]:...


    # Skipped EqualsAll due to it being static, abstract and generic.

    EqualsAll : EqualsAll_MethodGroup
    class EqualsAll_MethodGroup:
        def __getitem__(self, t:typing.Type[EqualsAll_1_T1]) -> EqualsAll_1[EqualsAll_1_T1]: ...

        EqualsAll_1_T1 = typing.TypeVar('EqualsAll_1_T1')
        class EqualsAll_1(typing.Generic[EqualsAll_1_T1]):
            EqualsAll_1_T = Vector128_0.EqualsAll_MethodGroup.EqualsAll_1_T1
            def __call__(self, left: Vector128_1[EqualsAll_1_T], right: Vector128_1[EqualsAll_1_T]) -> bool:...


    # Skipped EqualsAny due to it being static, abstract and generic.

    EqualsAny : EqualsAny_MethodGroup
    class EqualsAny_MethodGroup:
        def __getitem__(self, t:typing.Type[EqualsAny_1_T1]) -> EqualsAny_1[EqualsAny_1_T1]: ...

        EqualsAny_1_T1 = typing.TypeVar('EqualsAny_1_T1')
        class EqualsAny_1(typing.Generic[EqualsAny_1_T1]):
            EqualsAny_1_T = Vector128_0.EqualsAny_MethodGroup.EqualsAny_1_T1
            def __call__(self, left: Vector128_1[EqualsAny_1_T], right: Vector128_1[EqualsAny_1_T]) -> bool:...


    # Skipped ExtractMostSignificantBits due to it being static, abstract and generic.

    ExtractMostSignificantBits : ExtractMostSignificantBits_MethodGroup
    class ExtractMostSignificantBits_MethodGroup:
        def __getitem__(self, t:typing.Type[ExtractMostSignificantBits_1_T1]) -> ExtractMostSignificantBits_1[ExtractMostSignificantBits_1_T1]: ...

        ExtractMostSignificantBits_1_T1 = typing.TypeVar('ExtractMostSignificantBits_1_T1')
        class ExtractMostSignificantBits_1(typing.Generic[ExtractMostSignificantBits_1_T1]):
            ExtractMostSignificantBits_1_T = Vector128_0.ExtractMostSignificantBits_MethodGroup.ExtractMostSignificantBits_1_T1
            def __call__(self, vector: Vector128_1[ExtractMostSignificantBits_1_T]) -> int:...


    # Skipped Floor due to it being static, abstract and generic.

    Floor : Floor_MethodGroup
    class Floor_MethodGroup:
        def __call__(self, vector: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Floor(vector : Vector128`1) was skipped since it collides with above method

    # Skipped GetElement due to it being static, abstract and generic.

    GetElement : GetElement_MethodGroup
    class GetElement_MethodGroup:
        def __getitem__(self, t:typing.Type[GetElement_1_T1]) -> GetElement_1[GetElement_1_T1]: ...

        GetElement_1_T1 = typing.TypeVar('GetElement_1_T1')
        class GetElement_1(typing.Generic[GetElement_1_T1]):
            GetElement_1_T = Vector128_0.GetElement_MethodGroup.GetElement_1_T1
            def __call__(self, vector: Vector128_1[GetElement_1_T], index: int) -> GetElement_1_T:...


    # Skipped GetLower due to it being static, abstract and generic.

    GetLower : GetLower_MethodGroup
    class GetLower_MethodGroup:
        def __getitem__(self, t:typing.Type[GetLower_1_T1]) -> GetLower_1[GetLower_1_T1]: ...

        GetLower_1_T1 = typing.TypeVar('GetLower_1_T1')
        class GetLower_1(typing.Generic[GetLower_1_T1]):
            GetLower_1_T = Vector128_0.GetLower_MethodGroup.GetLower_1_T1
            def __call__(self, vector: Vector128_1[GetLower_1_T]) -> Vector64_1[GetLower_1_T]:...


    # Skipped GetUpper due to it being static, abstract and generic.

    GetUpper : GetUpper_MethodGroup
    class GetUpper_MethodGroup:
        def __getitem__(self, t:typing.Type[GetUpper_1_T1]) -> GetUpper_1[GetUpper_1_T1]: ...

        GetUpper_1_T1 = typing.TypeVar('GetUpper_1_T1')
        class GetUpper_1(typing.Generic[GetUpper_1_T1]):
            GetUpper_1_T = Vector128_0.GetUpper_MethodGroup.GetUpper_1_T1
            def __call__(self, vector: Vector128_1[GetUpper_1_T]) -> Vector64_1[GetUpper_1_T]:...


    # Skipped GreaterThan due to it being static, abstract and generic.

    GreaterThan : GreaterThan_MethodGroup
    class GreaterThan_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThan_1_T1]) -> GreaterThan_1[GreaterThan_1_T1]: ...

        GreaterThan_1_T1 = typing.TypeVar('GreaterThan_1_T1')
        class GreaterThan_1(typing.Generic[GreaterThan_1_T1]):
            GreaterThan_1_T = Vector128_0.GreaterThan_MethodGroup.GreaterThan_1_T1
            def __call__(self, left: Vector128_1[GreaterThan_1_T], right: Vector128_1[GreaterThan_1_T]) -> Vector128_1[GreaterThan_1_T]:...


    # Skipped GreaterThanAll due to it being static, abstract and generic.

    GreaterThanAll : GreaterThanAll_MethodGroup
    class GreaterThanAll_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanAll_1_T1]) -> GreaterThanAll_1[GreaterThanAll_1_T1]: ...

        GreaterThanAll_1_T1 = typing.TypeVar('GreaterThanAll_1_T1')
        class GreaterThanAll_1(typing.Generic[GreaterThanAll_1_T1]):
            GreaterThanAll_1_T = Vector128_0.GreaterThanAll_MethodGroup.GreaterThanAll_1_T1
            def __call__(self, left: Vector128_1[GreaterThanAll_1_T], right: Vector128_1[GreaterThanAll_1_T]) -> bool:...


    # Skipped GreaterThanAny due to it being static, abstract and generic.

    GreaterThanAny : GreaterThanAny_MethodGroup
    class GreaterThanAny_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanAny_1_T1]) -> GreaterThanAny_1[GreaterThanAny_1_T1]: ...

        GreaterThanAny_1_T1 = typing.TypeVar('GreaterThanAny_1_T1')
        class GreaterThanAny_1(typing.Generic[GreaterThanAny_1_T1]):
            GreaterThanAny_1_T = Vector128_0.GreaterThanAny_MethodGroup.GreaterThanAny_1_T1
            def __call__(self, left: Vector128_1[GreaterThanAny_1_T], right: Vector128_1[GreaterThanAny_1_T]) -> bool:...


    # Skipped GreaterThanOrEqual due to it being static, abstract and generic.

    GreaterThanOrEqual : GreaterThanOrEqual_MethodGroup
    class GreaterThanOrEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanOrEqual_1_T1]) -> GreaterThanOrEqual_1[GreaterThanOrEqual_1_T1]: ...

        GreaterThanOrEqual_1_T1 = typing.TypeVar('GreaterThanOrEqual_1_T1')
        class GreaterThanOrEqual_1(typing.Generic[GreaterThanOrEqual_1_T1]):
            GreaterThanOrEqual_1_T = Vector128_0.GreaterThanOrEqual_MethodGroup.GreaterThanOrEqual_1_T1
            def __call__(self, left: Vector128_1[GreaterThanOrEqual_1_T], right: Vector128_1[GreaterThanOrEqual_1_T]) -> Vector128_1[GreaterThanOrEqual_1_T]:...


    # Skipped GreaterThanOrEqualAll due to it being static, abstract and generic.

    GreaterThanOrEqualAll : GreaterThanOrEqualAll_MethodGroup
    class GreaterThanOrEqualAll_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanOrEqualAll_1_T1]) -> GreaterThanOrEqualAll_1[GreaterThanOrEqualAll_1_T1]: ...

        GreaterThanOrEqualAll_1_T1 = typing.TypeVar('GreaterThanOrEqualAll_1_T1')
        class GreaterThanOrEqualAll_1(typing.Generic[GreaterThanOrEqualAll_1_T1]):
            GreaterThanOrEqualAll_1_T = Vector128_0.GreaterThanOrEqualAll_MethodGroup.GreaterThanOrEqualAll_1_T1
            def __call__(self, left: Vector128_1[GreaterThanOrEqualAll_1_T], right: Vector128_1[GreaterThanOrEqualAll_1_T]) -> bool:...


    # Skipped GreaterThanOrEqualAny due to it being static, abstract and generic.

    GreaterThanOrEqualAny : GreaterThanOrEqualAny_MethodGroup
    class GreaterThanOrEqualAny_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanOrEqualAny_1_T1]) -> GreaterThanOrEqualAny_1[GreaterThanOrEqualAny_1_T1]: ...

        GreaterThanOrEqualAny_1_T1 = typing.TypeVar('GreaterThanOrEqualAny_1_T1')
        class GreaterThanOrEqualAny_1(typing.Generic[GreaterThanOrEqualAny_1_T1]):
            GreaterThanOrEqualAny_1_T = Vector128_0.GreaterThanOrEqualAny_MethodGroup.GreaterThanOrEqualAny_1_T1
            def __call__(self, left: Vector128_1[GreaterThanOrEqualAny_1_T], right: Vector128_1[GreaterThanOrEqualAny_1_T]) -> bool:...


    # Skipped LessThan due to it being static, abstract and generic.

    LessThan : LessThan_MethodGroup
    class LessThan_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThan_1_T1]) -> LessThan_1[LessThan_1_T1]: ...

        LessThan_1_T1 = typing.TypeVar('LessThan_1_T1')
        class LessThan_1(typing.Generic[LessThan_1_T1]):
            LessThan_1_T = Vector128_0.LessThan_MethodGroup.LessThan_1_T1
            def __call__(self, left: Vector128_1[LessThan_1_T], right: Vector128_1[LessThan_1_T]) -> Vector128_1[LessThan_1_T]:...


    # Skipped LessThanAll due to it being static, abstract and generic.

    LessThanAll : LessThanAll_MethodGroup
    class LessThanAll_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanAll_1_T1]) -> LessThanAll_1[LessThanAll_1_T1]: ...

        LessThanAll_1_T1 = typing.TypeVar('LessThanAll_1_T1')
        class LessThanAll_1(typing.Generic[LessThanAll_1_T1]):
            LessThanAll_1_T = Vector128_0.LessThanAll_MethodGroup.LessThanAll_1_T1
            def __call__(self, left: Vector128_1[LessThanAll_1_T], right: Vector128_1[LessThanAll_1_T]) -> bool:...


    # Skipped LessThanAny due to it being static, abstract and generic.

    LessThanAny : LessThanAny_MethodGroup
    class LessThanAny_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanAny_1_T1]) -> LessThanAny_1[LessThanAny_1_T1]: ...

        LessThanAny_1_T1 = typing.TypeVar('LessThanAny_1_T1')
        class LessThanAny_1(typing.Generic[LessThanAny_1_T1]):
            LessThanAny_1_T = Vector128_0.LessThanAny_MethodGroup.LessThanAny_1_T1
            def __call__(self, left: Vector128_1[LessThanAny_1_T], right: Vector128_1[LessThanAny_1_T]) -> bool:...


    # Skipped LessThanOrEqual due to it being static, abstract and generic.

    LessThanOrEqual : LessThanOrEqual_MethodGroup
    class LessThanOrEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanOrEqual_1_T1]) -> LessThanOrEqual_1[LessThanOrEqual_1_T1]: ...

        LessThanOrEqual_1_T1 = typing.TypeVar('LessThanOrEqual_1_T1')
        class LessThanOrEqual_1(typing.Generic[LessThanOrEqual_1_T1]):
            LessThanOrEqual_1_T = Vector128_0.LessThanOrEqual_MethodGroup.LessThanOrEqual_1_T1
            def __call__(self, left: Vector128_1[LessThanOrEqual_1_T], right: Vector128_1[LessThanOrEqual_1_T]) -> Vector128_1[LessThanOrEqual_1_T]:...


    # Skipped LessThanOrEqualAll due to it being static, abstract and generic.

    LessThanOrEqualAll : LessThanOrEqualAll_MethodGroup
    class LessThanOrEqualAll_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanOrEqualAll_1_T1]) -> LessThanOrEqualAll_1[LessThanOrEqualAll_1_T1]: ...

        LessThanOrEqualAll_1_T1 = typing.TypeVar('LessThanOrEqualAll_1_T1')
        class LessThanOrEqualAll_1(typing.Generic[LessThanOrEqualAll_1_T1]):
            LessThanOrEqualAll_1_T = Vector128_0.LessThanOrEqualAll_MethodGroup.LessThanOrEqualAll_1_T1
            def __call__(self, left: Vector128_1[LessThanOrEqualAll_1_T], right: Vector128_1[LessThanOrEqualAll_1_T]) -> bool:...


    # Skipped LessThanOrEqualAny due to it being static, abstract and generic.

    LessThanOrEqualAny : LessThanOrEqualAny_MethodGroup
    class LessThanOrEqualAny_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanOrEqualAny_1_T1]) -> LessThanOrEqualAny_1[LessThanOrEqualAny_1_T1]: ...

        LessThanOrEqualAny_1_T1 = typing.TypeVar('LessThanOrEqualAny_1_T1')
        class LessThanOrEqualAny_1(typing.Generic[LessThanOrEqualAny_1_T1]):
            LessThanOrEqualAny_1_T = Vector128_0.LessThanOrEqualAny_MethodGroup.LessThanOrEqualAny_1_T1
            def __call__(self, left: Vector128_1[LessThanOrEqualAny_1_T], right: Vector128_1[LessThanOrEqualAny_1_T]) -> bool:...


    # Skipped Load due to it being static, abstract and generic.

    Load : Load_MethodGroup
    class Load_MethodGroup:
        def __getitem__(self, t:typing.Type[Load_1_T1]) -> Load_1[Load_1_T1]: ...

        Load_1_T1 = typing.TypeVar('Load_1_T1')
        class Load_1(typing.Generic[Load_1_T1]):
            Load_1_T = Vector128_0.Load_MethodGroup.Load_1_T1
            def __call__(self, source: clr.Reference[Load_1_T]) -> Vector128_1[Load_1_T]:...


    # Skipped LoadAligned due to it being static, abstract and generic.

    LoadAligned : LoadAligned_MethodGroup
    class LoadAligned_MethodGroup:
        def __getitem__(self, t:typing.Type[LoadAligned_1_T1]) -> LoadAligned_1[LoadAligned_1_T1]: ...

        LoadAligned_1_T1 = typing.TypeVar('LoadAligned_1_T1')
        class LoadAligned_1(typing.Generic[LoadAligned_1_T1]):
            LoadAligned_1_T = Vector128_0.LoadAligned_MethodGroup.LoadAligned_1_T1
            def __call__(self, source: clr.Reference[LoadAligned_1_T]) -> Vector128_1[LoadAligned_1_T]:...


    # Skipped LoadAlignedNonTemporal due to it being static, abstract and generic.

    LoadAlignedNonTemporal : LoadAlignedNonTemporal_MethodGroup
    class LoadAlignedNonTemporal_MethodGroup:
        def __getitem__(self, t:typing.Type[LoadAlignedNonTemporal_1_T1]) -> LoadAlignedNonTemporal_1[LoadAlignedNonTemporal_1_T1]: ...

        LoadAlignedNonTemporal_1_T1 = typing.TypeVar('LoadAlignedNonTemporal_1_T1')
        class LoadAlignedNonTemporal_1(typing.Generic[LoadAlignedNonTemporal_1_T1]):
            LoadAlignedNonTemporal_1_T = Vector128_0.LoadAlignedNonTemporal_MethodGroup.LoadAlignedNonTemporal_1_T1
            def __call__(self, source: clr.Reference[LoadAlignedNonTemporal_1_T]) -> Vector128_1[LoadAlignedNonTemporal_1_T]:...


    # Skipped LoadUnsafe due to it being static, abstract and generic.

    LoadUnsafe : LoadUnsafe_MethodGroup
    class LoadUnsafe_MethodGroup:
        def __getitem__(self, t:typing.Type[LoadUnsafe_1_T1]) -> LoadUnsafe_1[LoadUnsafe_1_T1]: ...

        LoadUnsafe_1_T1 = typing.TypeVar('LoadUnsafe_1_T1')
        class LoadUnsafe_1(typing.Generic[LoadUnsafe_1_T1]):
            LoadUnsafe_1_T = Vector128_0.LoadUnsafe_MethodGroup.LoadUnsafe_1_T1
            @typing.overload
            def __call__(self, source: typing.Optional[clr.Reference[LoadUnsafe_1_T]]) -> Vector128_1[LoadUnsafe_1_T]:...
            @typing.overload
            def __call__(self, source: typing.Optional[clr.Reference[LoadUnsafe_1_T]], elementOffset: UIntPtr) -> Vector128_1[LoadUnsafe_1_T]:...


    # Skipped Max due to it being static, abstract and generic.

    Max : Max_MethodGroup
    class Max_MethodGroup:
        def __getitem__(self, t:typing.Type[Max_1_T1]) -> Max_1[Max_1_T1]: ...

        Max_1_T1 = typing.TypeVar('Max_1_T1')
        class Max_1(typing.Generic[Max_1_T1]):
            Max_1_T = Vector128_0.Max_MethodGroup.Max_1_T1
            def __call__(self, left: Vector128_1[Max_1_T], right: Vector128_1[Max_1_T]) -> Vector128_1[Max_1_T]:...


    # Skipped Min due to it being static, abstract and generic.

    Min : Min_MethodGroup
    class Min_MethodGroup:
        def __getitem__(self, t:typing.Type[Min_1_T1]) -> Min_1[Min_1_T1]: ...

        Min_1_T1 = typing.TypeVar('Min_1_T1')
        class Min_1(typing.Generic[Min_1_T1]):
            Min_1_T = Vector128_0.Min_MethodGroup.Min_1_T1
            def __call__(self, left: Vector128_1[Min_1_T], right: Vector128_1[Min_1_T]) -> Vector128_1[Min_1_T]:...


    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        def __getitem__(self, t:typing.Type[Multiply_1_T1]) -> Multiply_1[Multiply_1_T1]: ...

        Multiply_1_T1 = typing.TypeVar('Multiply_1_T1')
        class Multiply_1(typing.Generic[Multiply_1_T1]):
            Multiply_1_T = Vector128_0.Multiply_MethodGroup.Multiply_1_T1
            @typing.overload
            def __call__(self, left: Vector128_1[Multiply_1_T], right: Vector128_1[Multiply_1_T]) -> Vector128_1[Multiply_1_T]:...
            @typing.overload
            def __call__(self, left: Vector128_1[Multiply_1_T], right: typing.Optional[Multiply_1_T]) -> Vector128_1[Multiply_1_T]:...
            @typing.overload
            def __call__(self, left: typing.Optional[Multiply_1_T], right: Vector128_1[Multiply_1_T]) -> Vector128_1[Multiply_1_T]:...


    # Skipped Narrow due to it being static, abstract and generic.

    Narrow : Narrow_MethodGroup
    class Narrow_MethodGroup:
        def __call__(self, lower: Vector128_1[float], upper: Vector128_1[float]) -> Vector128_1[float]:...
        # Method Narrow(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method

    # Skipped Negate due to it being static, abstract and generic.

    Negate : Negate_MethodGroup
    class Negate_MethodGroup:
        def __getitem__(self, t:typing.Type[Negate_1_T1]) -> Negate_1[Negate_1_T1]: ...

        Negate_1_T1 = typing.TypeVar('Negate_1_T1')
        class Negate_1(typing.Generic[Negate_1_T1]):
            Negate_1_T = Vector128_0.Negate_MethodGroup.Negate_1_T1
            def __call__(self, vector: Vector128_1[Negate_1_T]) -> Vector128_1[Negate_1_T]:...


    # Skipped OnesComplement due to it being static, abstract and generic.

    OnesComplement : OnesComplement_MethodGroup
    class OnesComplement_MethodGroup:
        def __getitem__(self, t:typing.Type[OnesComplement_1_T1]) -> OnesComplement_1[OnesComplement_1_T1]: ...

        OnesComplement_1_T1 = typing.TypeVar('OnesComplement_1_T1')
        class OnesComplement_1(typing.Generic[OnesComplement_1_T1]):
            OnesComplement_1_T = Vector128_0.OnesComplement_MethodGroup.OnesComplement_1_T1
            def __call__(self, vector: Vector128_1[OnesComplement_1_T]) -> Vector128_1[OnesComplement_1_T]:...


    # Skipped ShiftLeft due to it being static, abstract and generic.

    ShiftLeft : ShiftLeft_MethodGroup
    class ShiftLeft_MethodGroup:
        @typing.overload
        def __call__(self, vector: Vector128_1[int], shiftCount: int) -> Vector128_1[int]:...
        # Method ShiftLeft(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, vector: Vector128_1[UIntPtr], shiftCount: int) -> Vector128_1[UIntPtr]:...

    # Skipped ShiftRightArithmetic due to it being static, abstract and generic.

    ShiftRightArithmetic : ShiftRightArithmetic_MethodGroup
    class ShiftRightArithmetic_MethodGroup:
        def __call__(self, vector: Vector128_1[int], shiftCount: int) -> Vector128_1[int]:...
        # Method ShiftRightArithmetic(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method

    # Skipped ShiftRightLogical due to it being static, abstract and generic.

    ShiftRightLogical : ShiftRightLogical_MethodGroup
    class ShiftRightLogical_MethodGroup:
        @typing.overload
        def __call__(self, vector: Vector128_1[int], shiftCount: int) -> Vector128_1[int]:...
        # Method ShiftRightLogical(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector128`1, shiftCount : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, vector: Vector128_1[UIntPtr], shiftCount: int) -> Vector128_1[UIntPtr]:...

    # Skipped Shuffle due to it being static, abstract and generic.

    Shuffle : Shuffle_MethodGroup
    class Shuffle_MethodGroup:
        def __call__(self, vector: Vector128_1[float], indices: Vector128_1[int]) -> Vector128_1[float]:...
        # Method Shuffle(vector : Vector128`1, indices : Vector128`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector128`1, indices : Vector128`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector128`1, indices : Vector128`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector128`1, indices : Vector128`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector128`1, indices : Vector128`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector128`1, indices : Vector128`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector128`1, indices : Vector128`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector128`1, indices : Vector128`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector128`1, indices : Vector128`1) was skipped since it collides with above method

    # Skipped Sqrt due to it being static, abstract and generic.

    Sqrt : Sqrt_MethodGroup
    class Sqrt_MethodGroup:
        def __getitem__(self, t:typing.Type[Sqrt_1_T1]) -> Sqrt_1[Sqrt_1_T1]: ...

        Sqrt_1_T1 = typing.TypeVar('Sqrt_1_T1')
        class Sqrt_1(typing.Generic[Sqrt_1_T1]):
            Sqrt_1_T = Vector128_0.Sqrt_MethodGroup.Sqrt_1_T1
            def __call__(self, vector: Vector128_1[Sqrt_1_T]) -> Vector128_1[Sqrt_1_T]:...


    # Skipped Store due to it being static, abstract and generic.

    Store : Store_MethodGroup
    class Store_MethodGroup:
        def __getitem__(self, t:typing.Type[Store_1_T1]) -> Store_1[Store_1_T1]: ...

        Store_1_T1 = typing.TypeVar('Store_1_T1')
        class Store_1(typing.Generic[Store_1_T1]):
            Store_1_T = Vector128_0.Store_MethodGroup.Store_1_T1
            def __call__(self, source: Vector128_1[Store_1_T], destination: clr.Reference[Store_1_T]) -> None:...


    # Skipped StoreAligned due to it being static, abstract and generic.

    StoreAligned : StoreAligned_MethodGroup
    class StoreAligned_MethodGroup:
        def __getitem__(self, t:typing.Type[StoreAligned_1_T1]) -> StoreAligned_1[StoreAligned_1_T1]: ...

        StoreAligned_1_T1 = typing.TypeVar('StoreAligned_1_T1')
        class StoreAligned_1(typing.Generic[StoreAligned_1_T1]):
            StoreAligned_1_T = Vector128_0.StoreAligned_MethodGroup.StoreAligned_1_T1
            def __call__(self, source: Vector128_1[StoreAligned_1_T], destination: clr.Reference[StoreAligned_1_T]) -> None:...


    # Skipped StoreAlignedNonTemporal due to it being static, abstract and generic.

    StoreAlignedNonTemporal : StoreAlignedNonTemporal_MethodGroup
    class StoreAlignedNonTemporal_MethodGroup:
        def __getitem__(self, t:typing.Type[StoreAlignedNonTemporal_1_T1]) -> StoreAlignedNonTemporal_1[StoreAlignedNonTemporal_1_T1]: ...

        StoreAlignedNonTemporal_1_T1 = typing.TypeVar('StoreAlignedNonTemporal_1_T1')
        class StoreAlignedNonTemporal_1(typing.Generic[StoreAlignedNonTemporal_1_T1]):
            StoreAlignedNonTemporal_1_T = Vector128_0.StoreAlignedNonTemporal_MethodGroup.StoreAlignedNonTemporal_1_T1
            def __call__(self, source: Vector128_1[StoreAlignedNonTemporal_1_T], destination: clr.Reference[StoreAlignedNonTemporal_1_T]) -> None:...


    # Skipped StoreUnsafe due to it being static, abstract and generic.

    StoreUnsafe : StoreUnsafe_MethodGroup
    class StoreUnsafe_MethodGroup:
        def __getitem__(self, t:typing.Type[StoreUnsafe_1_T1]) -> StoreUnsafe_1[StoreUnsafe_1_T1]: ...

        StoreUnsafe_1_T1 = typing.TypeVar('StoreUnsafe_1_T1')
        class StoreUnsafe_1(typing.Generic[StoreUnsafe_1_T1]):
            StoreUnsafe_1_T = Vector128_0.StoreUnsafe_MethodGroup.StoreUnsafe_1_T1
            @typing.overload
            def __call__(self, source: Vector128_1[StoreUnsafe_1_T], destination: typing.Optional[clr.Reference[StoreUnsafe_1_T]]) -> None:...
            @typing.overload
            def __call__(self, source: Vector128_1[StoreUnsafe_1_T], destination: typing.Optional[clr.Reference[StoreUnsafe_1_T]], elementOffset: UIntPtr) -> None:...


    # Skipped Subtract due to it being static, abstract and generic.

    Subtract : Subtract_MethodGroup
    class Subtract_MethodGroup:
        def __getitem__(self, t:typing.Type[Subtract_1_T1]) -> Subtract_1[Subtract_1_T1]: ...

        Subtract_1_T1 = typing.TypeVar('Subtract_1_T1')
        class Subtract_1(typing.Generic[Subtract_1_T1]):
            Subtract_1_T = Vector128_0.Subtract_MethodGroup.Subtract_1_T1
            def __call__(self, left: Vector128_1[Subtract_1_T], right: Vector128_1[Subtract_1_T]) -> Vector128_1[Subtract_1_T]:...


    # Skipped Sum due to it being static, abstract and generic.

    Sum : Sum_MethodGroup
    class Sum_MethodGroup:
        def __getitem__(self, t:typing.Type[Sum_1_T1]) -> Sum_1[Sum_1_T1]: ...

        Sum_1_T1 = typing.TypeVar('Sum_1_T1')
        class Sum_1(typing.Generic[Sum_1_T1]):
            Sum_1_T = Vector128_0.Sum_MethodGroup.Sum_1_T1
            def __call__(self, vector: Vector128_1[Sum_1_T]) -> Sum_1_T:...


    # Skipped ToScalar due to it being static, abstract and generic.

    ToScalar : ToScalar_MethodGroup
    class ToScalar_MethodGroup:
        def __getitem__(self, t:typing.Type[ToScalar_1_T1]) -> ToScalar_1[ToScalar_1_T1]: ...

        ToScalar_1_T1 = typing.TypeVar('ToScalar_1_T1')
        class ToScalar_1(typing.Generic[ToScalar_1_T1]):
            ToScalar_1_T = Vector128_0.ToScalar_MethodGroup.ToScalar_1_T1
            def __call__(self, vector: Vector128_1[ToScalar_1_T]) -> ToScalar_1_T:...


    # Skipped ToVector256 due to it being static, abstract and generic.

    ToVector256 : ToVector256_MethodGroup
    class ToVector256_MethodGroup:
        def __getitem__(self, t:typing.Type[ToVector256_1_T1]) -> ToVector256_1[ToVector256_1_T1]: ...

        ToVector256_1_T1 = typing.TypeVar('ToVector256_1_T1')
        class ToVector256_1(typing.Generic[ToVector256_1_T1]):
            ToVector256_1_T = Vector128_0.ToVector256_MethodGroup.ToVector256_1_T1
            def __call__(self, vector: Vector128_1[ToVector256_1_T]) -> Vector256_1[ToVector256_1_T]:...


    # Skipped ToVector256Unsafe due to it being static, abstract and generic.

    ToVector256Unsafe : ToVector256Unsafe_MethodGroup
    class ToVector256Unsafe_MethodGroup:
        def __getitem__(self, t:typing.Type[ToVector256Unsafe_1_T1]) -> ToVector256Unsafe_1[ToVector256Unsafe_1_T1]: ...

        ToVector256Unsafe_1_T1 = typing.TypeVar('ToVector256Unsafe_1_T1')
        class ToVector256Unsafe_1(typing.Generic[ToVector256Unsafe_1_T1]):
            ToVector256Unsafe_1_T = Vector128_0.ToVector256Unsafe_MethodGroup.ToVector256Unsafe_1_T1
            def __call__(self, vector: Vector128_1[ToVector256Unsafe_1_T]) -> Vector256_1[ToVector256Unsafe_1_T]:...


    # Skipped TryCopyTo due to it being static, abstract and generic.

    TryCopyTo : TryCopyTo_MethodGroup
    class TryCopyTo_MethodGroup:
        def __getitem__(self, t:typing.Type[TryCopyTo_1_T1]) -> TryCopyTo_1[TryCopyTo_1_T1]: ...

        TryCopyTo_1_T1 = typing.TypeVar('TryCopyTo_1_T1')
        class TryCopyTo_1(typing.Generic[TryCopyTo_1_T1]):
            TryCopyTo_1_T = Vector128_0.TryCopyTo_MethodGroup.TryCopyTo_1_T1
            def __call__(self, vector: Vector128_1[TryCopyTo_1_T], destination: Span_1[TryCopyTo_1_T]) -> bool:...


    # Skipped Widen due to it being static, abstract and generic.

    Widen : Widen_MethodGroup
    class Widen_MethodGroup:
        def __call__(self, source: Vector128_1[float]) -> ValueTuple_2[Vector128_1[float], Vector128_1[float]]:...
        # Method Widen(source : Vector128`1) was skipped since it collides with above method
        # Method Widen(source : Vector128`1) was skipped since it collides with above method
        # Method Widen(source : Vector128`1) was skipped since it collides with above method
        # Method Widen(source : Vector128`1) was skipped since it collides with above method
        # Method Widen(source : Vector128`1) was skipped since it collides with above method
        # Method Widen(source : Vector128`1) was skipped since it collides with above method

    # Skipped WidenLower due to it being static, abstract and generic.

    WidenLower : WidenLower_MethodGroup
    class WidenLower_MethodGroup:
        def __call__(self, source: Vector128_1[float]) -> Vector128_1[float]:...
        # Method WidenLower(source : Vector128`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector128`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector128`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector128`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector128`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector128`1) was skipped since it collides with above method

    # Skipped WidenUpper due to it being static, abstract and generic.

    WidenUpper : WidenUpper_MethodGroup
    class WidenUpper_MethodGroup:
        def __call__(self, source: Vector128_1[float]) -> Vector128_1[float]:...
        # Method WidenUpper(source : Vector128`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector128`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector128`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector128`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector128`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector128`1) was skipped since it collides with above method

    # Skipped WithElement due to it being static, abstract and generic.

    WithElement : WithElement_MethodGroup
    class WithElement_MethodGroup:
        def __getitem__(self, t:typing.Type[WithElement_1_T1]) -> WithElement_1[WithElement_1_T1]: ...

        WithElement_1_T1 = typing.TypeVar('WithElement_1_T1')
        class WithElement_1(typing.Generic[WithElement_1_T1]):
            WithElement_1_T = Vector128_0.WithElement_MethodGroup.WithElement_1_T1
            def __call__(self, vector: Vector128_1[WithElement_1_T], index: int, value: typing.Optional[WithElement_1_T]) -> Vector128_1[WithElement_1_T]:...


    # Skipped WithLower due to it being static, abstract and generic.

    WithLower : WithLower_MethodGroup
    class WithLower_MethodGroup:
        def __getitem__(self, t:typing.Type[WithLower_1_T1]) -> WithLower_1[WithLower_1_T1]: ...

        WithLower_1_T1 = typing.TypeVar('WithLower_1_T1')
        class WithLower_1(typing.Generic[WithLower_1_T1]):
            WithLower_1_T = Vector128_0.WithLower_MethodGroup.WithLower_1_T1
            def __call__(self, vector: Vector128_1[WithLower_1_T], value: Vector64_1[WithLower_1_T]) -> Vector128_1[WithLower_1_T]:...


    # Skipped WithUpper due to it being static, abstract and generic.

    WithUpper : WithUpper_MethodGroup
    class WithUpper_MethodGroup:
        def __getitem__(self, t:typing.Type[WithUpper_1_T1]) -> WithUpper_1[WithUpper_1_T1]: ...

        WithUpper_1_T1 = typing.TypeVar('WithUpper_1_T1')
        class WithUpper_1(typing.Generic[WithUpper_1_T1]):
            WithUpper_1_T = Vector128_0.WithUpper_MethodGroup.WithUpper_1_T1
            def __call__(self, vector: Vector128_1[WithUpper_1_T], value: Vector64_1[WithUpper_1_T]) -> Vector128_1[WithUpper_1_T]:...


    # Skipped Xor due to it being static, abstract and generic.

    Xor : Xor_MethodGroup
    class Xor_MethodGroup:
        def __getitem__(self, t:typing.Type[Xor_1_T1]) -> Xor_1[Xor_1_T1]: ...

        Xor_1_T1 = typing.TypeVar('Xor_1_T1')
        class Xor_1(typing.Generic[Xor_1_T1]):
            Xor_1_T = Vector128_0.Xor_MethodGroup.Xor_1_T1
            def __call__(self, left: Vector128_1[Xor_1_T], right: Vector128_1[Xor_1_T]) -> Vector128_1[Xor_1_T]:...




Vector128_1_T = typing.TypeVar('Vector128_1_T')
class Vector128_1(typing.Generic[Vector128_1_T], IEquatable_1[Vector128_1[Vector128_1_T]]):
    @classmethod
    @property
    def AllBitsSet(cls) -> Vector128_1[Vector128_1_T]: ...
    @classmethod
    @property
    def Count(cls) -> int: ...
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @property
    def Item(self) -> typing.Optional[Vector128_1_T]: ...
    @classmethod
    @property
    def One(cls) -> Vector128_1[Vector128_1_T]: ...
    @classmethod
    @property
    def Zero(cls) -> Vector128_1[Vector128_1_T]: ...
    def GetHashCode(self) -> int: ...
    def __add__(self, left: Vector128_1[Vector128_1_T], right: Vector128_1[Vector128_1_T]) -> Vector128_1[Vector128_1_T]: ...
    def __and__(self, left: Vector128_1[Vector128_1_T], right: Vector128_1[Vector128_1_T]) -> Vector128_1[Vector128_1_T]: ...
    def __or__(self, left: Vector128_1[Vector128_1_T], right: Vector128_1[Vector128_1_T]) -> Vector128_1[Vector128_1_T]: ...
    @typing.overload
    def __truediv__(self, left: Vector128_1[Vector128_1_T], right: Vector128_1[Vector128_1_T]) -> Vector128_1[Vector128_1_T]: ...
    @typing.overload
    def __truediv__(self, left: Vector128_1[Vector128_1_T], right: typing.Optional[Vector128_1_T]) -> Vector128_1[Vector128_1_T]: ...
    def __eq__(self, left: Vector128_1[Vector128_1_T], right: Vector128_1[Vector128_1_T]) -> bool: ...
    def __xor__(self, left: Vector128_1[Vector128_1_T], right: Vector128_1[Vector128_1_T]) -> Vector128_1[Vector128_1_T]: ...
    def __ne__(self, left: Vector128_1[Vector128_1_T], right: Vector128_1[Vector128_1_T]) -> bool: ...
    def __lshift__(self, value: Vector128_1[Vector128_1_T], shiftCount: int) -> Vector128_1[Vector128_1_T]: ...
    @typing.overload
    def __mul__(self, left: Vector128_1[Vector128_1_T], right: Vector128_1[Vector128_1_T]) -> Vector128_1[Vector128_1_T]: ...
    @typing.overload
    def __mul__(self, left: Vector128_1[Vector128_1_T], right: typing.Optional[Vector128_1_T]) -> Vector128_1[Vector128_1_T]: ...
    @typing.overload
    def __mul__(self, left: typing.Optional[Vector128_1_T], right: Vector128_1[Vector128_1_T]) -> Vector128_1[Vector128_1_T]: ...
    def __invert__(self, vector: Vector128_1[Vector128_1_T]) -> Vector128_1[Vector128_1_T]: ...
    def __rshift__(self, value: Vector128_1[Vector128_1_T], shiftCount: int) -> Vector128_1[Vector128_1_T]: ...
    def __sub__(self, left: Vector128_1[Vector128_1_T], right: Vector128_1[Vector128_1_T]) -> Vector128_1[Vector128_1_T]: ...
    def __neg__(self, vector: Vector128_1[Vector128_1_T]) -> Vector128_1[Vector128_1_T]: ...
    def __pos__(self, value: Vector128_1[Vector128_1_T]) -> Vector128_1[Vector128_1_T]: ...
    # Operator not supported op_UnsignedRightShift(value: Vector128`1, shiftCount: Int32)
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[Vector128_1_T]
    Equals_MethodGroup_Vector128_1_T = typing.TypeVar('Equals_MethodGroup_Vector128_1_T')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_Vector128_1_T]):
        Equals_MethodGroup_Vector128_1_T = Vector128_1.Equals_MethodGroup_Vector128_1_T
        @typing.overload
        def __call__(self, other: Vector128_1[Equals_MethodGroup_Vector128_1_T]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Optional[typing.Any]) -> bool:...



class Vector256_GenericClasses(abc.ABCMeta):
    Generic_Vector256_GenericClasses_Vector256_1_T = typing.TypeVar('Generic_Vector256_GenericClasses_Vector256_1_T')
    def __getitem__(self, types : typing.Type[Generic_Vector256_GenericClasses_Vector256_1_T]) -> typing.Type[Vector256_1[Generic_Vector256_GenericClasses_Vector256_1_T]]: ...

class Vector256(Vector256_0, metaclass =Vector256_GenericClasses): ...

class Vector256_0(abc.ABC):
    @classmethod
    @property
    def IsHardwareAccelerated(cls) -> bool: ...
    @staticmethod
    def ConvertToInt32(vector: Vector256_1[float]) -> Vector256_1[int]: ...
    @staticmethod
    def ConvertToInt64(vector: Vector256_1[float]) -> Vector256_1[int]: ...
    @staticmethod
    def ConvertToUInt32(vector: Vector256_1[float]) -> Vector256_1[int]: ...
    @staticmethod
    def ConvertToUInt64(vector: Vector256_1[float]) -> Vector256_1[int]: ...
    # Skipped Abs due to it being static, abstract and generic.

    Abs : Abs_MethodGroup
    class Abs_MethodGroup:
        def __getitem__(self, t:typing.Type[Abs_1_T1]) -> Abs_1[Abs_1_T1]: ...

        Abs_1_T1 = typing.TypeVar('Abs_1_T1')
        class Abs_1(typing.Generic[Abs_1_T1]):
            Abs_1_T = Vector256_0.Abs_MethodGroup.Abs_1_T1
            def __call__(self, vector: Vector256_1[Abs_1_T]) -> Vector256_1[Abs_1_T]:...


    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        def __getitem__(self, t:typing.Type[Add_1_T1]) -> Add_1[Add_1_T1]: ...

        Add_1_T1 = typing.TypeVar('Add_1_T1')
        class Add_1(typing.Generic[Add_1_T1]):
            Add_1_T = Vector256_0.Add_MethodGroup.Add_1_T1
            def __call__(self, left: Vector256_1[Add_1_T], right: Vector256_1[Add_1_T]) -> Vector256_1[Add_1_T]:...


    # Skipped AndNot due to it being static, abstract and generic.

    AndNot : AndNot_MethodGroup
    class AndNot_MethodGroup:
        def __getitem__(self, t:typing.Type[AndNot_1_T1]) -> AndNot_1[AndNot_1_T1]: ...

        AndNot_1_T1 = typing.TypeVar('AndNot_1_T1')
        class AndNot_1(typing.Generic[AndNot_1_T1]):
            AndNot_1_T = Vector256_0.AndNot_MethodGroup.AndNot_1_T1
            def __call__(self, left: Vector256_1[AndNot_1_T], right: Vector256_1[AndNot_1_T]) -> Vector256_1[AndNot_1_T]:...


    # Skipped As due to it being static, abstract and generic.

    As : As_MethodGroup
    class As_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[As_2_T1], typing.Type[As_2_T2]]) -> As_2[As_2_T1, As_2_T2]: ...

        As_2_T1 = typing.TypeVar('As_2_T1')
        As_2_T2 = typing.TypeVar('As_2_T2')
        class As_2(typing.Generic[As_2_T1, As_2_T2]):
            As_2_TFrom = Vector256_0.As_MethodGroup.As_2_T1
            As_2_TTo = Vector256_0.As_MethodGroup.As_2_T2
            def __call__(self, vector: Vector256_1[As_2_TFrom]) -> Vector256_1[As_2_TTo]:...


    # Skipped AsByte due to it being static, abstract and generic.

    AsByte : AsByte_MethodGroup
    class AsByte_MethodGroup:
        def __getitem__(self, t:typing.Type[AsByte_1_T1]) -> AsByte_1[AsByte_1_T1]: ...

        AsByte_1_T1 = typing.TypeVar('AsByte_1_T1')
        class AsByte_1(typing.Generic[AsByte_1_T1]):
            AsByte_1_T = Vector256_0.AsByte_MethodGroup.AsByte_1_T1
            def __call__(self, vector: Vector256_1[AsByte_1_T]) -> Vector256_1[int]:...


    # Skipped AsDouble due to it being static, abstract and generic.

    AsDouble : AsDouble_MethodGroup
    class AsDouble_MethodGroup:
        def __getitem__(self, t:typing.Type[AsDouble_1_T1]) -> AsDouble_1[AsDouble_1_T1]: ...

        AsDouble_1_T1 = typing.TypeVar('AsDouble_1_T1')
        class AsDouble_1(typing.Generic[AsDouble_1_T1]):
            AsDouble_1_T = Vector256_0.AsDouble_MethodGroup.AsDouble_1_T1
            def __call__(self, vector: Vector256_1[AsDouble_1_T]) -> Vector256_1[float]:...


    # Skipped AsInt16 due to it being static, abstract and generic.

    AsInt16 : AsInt16_MethodGroup
    class AsInt16_MethodGroup:
        def __getitem__(self, t:typing.Type[AsInt16_1_T1]) -> AsInt16_1[AsInt16_1_T1]: ...

        AsInt16_1_T1 = typing.TypeVar('AsInt16_1_T1')
        class AsInt16_1(typing.Generic[AsInt16_1_T1]):
            AsInt16_1_T = Vector256_0.AsInt16_MethodGroup.AsInt16_1_T1
            def __call__(self, vector: Vector256_1[AsInt16_1_T]) -> Vector256_1[int]:...


    # Skipped AsInt32 due to it being static, abstract and generic.

    AsInt32 : AsInt32_MethodGroup
    class AsInt32_MethodGroup:
        def __getitem__(self, t:typing.Type[AsInt32_1_T1]) -> AsInt32_1[AsInt32_1_T1]: ...

        AsInt32_1_T1 = typing.TypeVar('AsInt32_1_T1')
        class AsInt32_1(typing.Generic[AsInt32_1_T1]):
            AsInt32_1_T = Vector256_0.AsInt32_MethodGroup.AsInt32_1_T1
            def __call__(self, vector: Vector256_1[AsInt32_1_T]) -> Vector256_1[int]:...


    # Skipped AsInt64 due to it being static, abstract and generic.

    AsInt64 : AsInt64_MethodGroup
    class AsInt64_MethodGroup:
        def __getitem__(self, t:typing.Type[AsInt64_1_T1]) -> AsInt64_1[AsInt64_1_T1]: ...

        AsInt64_1_T1 = typing.TypeVar('AsInt64_1_T1')
        class AsInt64_1(typing.Generic[AsInt64_1_T1]):
            AsInt64_1_T = Vector256_0.AsInt64_MethodGroup.AsInt64_1_T1
            def __call__(self, vector: Vector256_1[AsInt64_1_T]) -> Vector256_1[int]:...


    # Skipped AsNInt due to it being static, abstract and generic.

    AsNInt : AsNInt_MethodGroup
    class AsNInt_MethodGroup:
        def __getitem__(self, t:typing.Type[AsNInt_1_T1]) -> AsNInt_1[AsNInt_1_T1]: ...

        AsNInt_1_T1 = typing.TypeVar('AsNInt_1_T1')
        class AsNInt_1(typing.Generic[AsNInt_1_T1]):
            AsNInt_1_T = Vector256_0.AsNInt_MethodGroup.AsNInt_1_T1
            def __call__(self, vector: Vector256_1[AsNInt_1_T]) -> Vector256_1[int]:...


    # Skipped AsNUInt due to it being static, abstract and generic.

    AsNUInt : AsNUInt_MethodGroup
    class AsNUInt_MethodGroup:
        def __getitem__(self, t:typing.Type[AsNUInt_1_T1]) -> AsNUInt_1[AsNUInt_1_T1]: ...

        AsNUInt_1_T1 = typing.TypeVar('AsNUInt_1_T1')
        class AsNUInt_1(typing.Generic[AsNUInt_1_T1]):
            AsNUInt_1_T = Vector256_0.AsNUInt_MethodGroup.AsNUInt_1_T1
            def __call__(self, vector: Vector256_1[AsNUInt_1_T]) -> Vector256_1[UIntPtr]:...


    # Skipped AsSByte due to it being static, abstract and generic.

    AsSByte : AsSByte_MethodGroup
    class AsSByte_MethodGroup:
        def __getitem__(self, t:typing.Type[AsSByte_1_T1]) -> AsSByte_1[AsSByte_1_T1]: ...

        AsSByte_1_T1 = typing.TypeVar('AsSByte_1_T1')
        class AsSByte_1(typing.Generic[AsSByte_1_T1]):
            AsSByte_1_T = Vector256_0.AsSByte_MethodGroup.AsSByte_1_T1
            def __call__(self, vector: Vector256_1[AsSByte_1_T]) -> Vector256_1[int]:...


    # Skipped AsSingle due to it being static, abstract and generic.

    AsSingle : AsSingle_MethodGroup
    class AsSingle_MethodGroup:
        def __getitem__(self, t:typing.Type[AsSingle_1_T1]) -> AsSingle_1[AsSingle_1_T1]: ...

        AsSingle_1_T1 = typing.TypeVar('AsSingle_1_T1')
        class AsSingle_1(typing.Generic[AsSingle_1_T1]):
            AsSingle_1_T = Vector256_0.AsSingle_MethodGroup.AsSingle_1_T1
            def __call__(self, vector: Vector256_1[AsSingle_1_T]) -> Vector256_1[float]:...


    # Skipped AsUInt16 due to it being static, abstract and generic.

    AsUInt16 : AsUInt16_MethodGroup
    class AsUInt16_MethodGroup:
        def __getitem__(self, t:typing.Type[AsUInt16_1_T1]) -> AsUInt16_1[AsUInt16_1_T1]: ...

        AsUInt16_1_T1 = typing.TypeVar('AsUInt16_1_T1')
        class AsUInt16_1(typing.Generic[AsUInt16_1_T1]):
            AsUInt16_1_T = Vector256_0.AsUInt16_MethodGroup.AsUInt16_1_T1
            def __call__(self, vector: Vector256_1[AsUInt16_1_T]) -> Vector256_1[int]:...


    # Skipped AsUInt32 due to it being static, abstract and generic.

    AsUInt32 : AsUInt32_MethodGroup
    class AsUInt32_MethodGroup:
        def __getitem__(self, t:typing.Type[AsUInt32_1_T1]) -> AsUInt32_1[AsUInt32_1_T1]: ...

        AsUInt32_1_T1 = typing.TypeVar('AsUInt32_1_T1')
        class AsUInt32_1(typing.Generic[AsUInt32_1_T1]):
            AsUInt32_1_T = Vector256_0.AsUInt32_MethodGroup.AsUInt32_1_T1
            def __call__(self, vector: Vector256_1[AsUInt32_1_T]) -> Vector256_1[int]:...


    # Skipped AsUInt64 due to it being static, abstract and generic.

    AsUInt64 : AsUInt64_MethodGroup
    class AsUInt64_MethodGroup:
        def __getitem__(self, t:typing.Type[AsUInt64_1_T1]) -> AsUInt64_1[AsUInt64_1_T1]: ...

        AsUInt64_1_T1 = typing.TypeVar('AsUInt64_1_T1')
        class AsUInt64_1(typing.Generic[AsUInt64_1_T1]):
            AsUInt64_1_T = Vector256_0.AsUInt64_MethodGroup.AsUInt64_1_T1
            def __call__(self, vector: Vector256_1[AsUInt64_1_T]) -> Vector256_1[int]:...


    # Skipped AsVector due to it being static, abstract and generic.

    AsVector : AsVector_MethodGroup
    class AsVector_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVector_1_T1]) -> AsVector_1[AsVector_1_T1]: ...

        AsVector_1_T1 = typing.TypeVar('AsVector_1_T1')
        class AsVector_1(typing.Generic[AsVector_1_T1]):
            AsVector_1_T = Vector256_0.AsVector_MethodGroup.AsVector_1_T1
            def __call__(self, value: Vector256_1[AsVector_1_T]) -> Vector_1[AsVector_1_T]:...


    # Skipped AsVector256 due to it being static, abstract and generic.

    AsVector256 : AsVector256_MethodGroup
    class AsVector256_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVector256_1_T1]) -> AsVector256_1[AsVector256_1_T1]: ...

        AsVector256_1_T1 = typing.TypeVar('AsVector256_1_T1')
        class AsVector256_1(typing.Generic[AsVector256_1_T1]):
            AsVector256_1_T = Vector256_0.AsVector256_MethodGroup.AsVector256_1_T1
            def __call__(self, value: Vector_1[AsVector256_1_T]) -> Vector256_1[AsVector256_1_T]:...


    # Skipped BitwiseAnd due to it being static, abstract and generic.

    BitwiseAnd : BitwiseAnd_MethodGroup
    class BitwiseAnd_MethodGroup:
        def __getitem__(self, t:typing.Type[BitwiseAnd_1_T1]) -> BitwiseAnd_1[BitwiseAnd_1_T1]: ...

        BitwiseAnd_1_T1 = typing.TypeVar('BitwiseAnd_1_T1')
        class BitwiseAnd_1(typing.Generic[BitwiseAnd_1_T1]):
            BitwiseAnd_1_T = Vector256_0.BitwiseAnd_MethodGroup.BitwiseAnd_1_T1
            def __call__(self, left: Vector256_1[BitwiseAnd_1_T], right: Vector256_1[BitwiseAnd_1_T]) -> Vector256_1[BitwiseAnd_1_T]:...


    # Skipped BitwiseOr due to it being static, abstract and generic.

    BitwiseOr : BitwiseOr_MethodGroup
    class BitwiseOr_MethodGroup:
        def __getitem__(self, t:typing.Type[BitwiseOr_1_T1]) -> BitwiseOr_1[BitwiseOr_1_T1]: ...

        BitwiseOr_1_T1 = typing.TypeVar('BitwiseOr_1_T1')
        class BitwiseOr_1(typing.Generic[BitwiseOr_1_T1]):
            BitwiseOr_1_T = Vector256_0.BitwiseOr_MethodGroup.BitwiseOr_1_T1
            def __call__(self, left: Vector256_1[BitwiseOr_1_T], right: Vector256_1[BitwiseOr_1_T]) -> Vector256_1[BitwiseOr_1_T]:...


    # Skipped Ceiling due to it being static, abstract and generic.

    Ceiling : Ceiling_MethodGroup
    class Ceiling_MethodGroup:
        def __call__(self, vector: Vector256_1[float]) -> Vector256_1[float]:...
        # Method Ceiling(vector : Vector256`1) was skipped since it collides with above method

    # Skipped ConditionalSelect due to it being static, abstract and generic.

    ConditionalSelect : ConditionalSelect_MethodGroup
    class ConditionalSelect_MethodGroup:
        def __getitem__(self, t:typing.Type[ConditionalSelect_1_T1]) -> ConditionalSelect_1[ConditionalSelect_1_T1]: ...

        ConditionalSelect_1_T1 = typing.TypeVar('ConditionalSelect_1_T1')
        class ConditionalSelect_1(typing.Generic[ConditionalSelect_1_T1]):
            ConditionalSelect_1_T = Vector256_0.ConditionalSelect_MethodGroup.ConditionalSelect_1_T1
            def __call__(self, condition: Vector256_1[ConditionalSelect_1_T], left: Vector256_1[ConditionalSelect_1_T], right: Vector256_1[ConditionalSelect_1_T]) -> Vector256_1[ConditionalSelect_1_T]:...


    # Skipped ConvertToDouble due to it being static, abstract and generic.

    ConvertToDouble : ConvertToDouble_MethodGroup
    class ConvertToDouble_MethodGroup:
        def __call__(self, vector: Vector256_1[int]) -> Vector256_1[float]:...
        # Method ConvertToDouble(vector : Vector256`1) was skipped since it collides with above method

    # Skipped ConvertToSingle due to it being static, abstract and generic.

    ConvertToSingle : ConvertToSingle_MethodGroup
    class ConvertToSingle_MethodGroup:
        def __call__(self, vector: Vector256_1[int]) -> Vector256_1[float]:...
        # Method ConvertToSingle(vector : Vector256`1) was skipped since it collides with above method

    # Skipped CopyTo due to it being static, abstract and generic.

    CopyTo : CopyTo_MethodGroup
    class CopyTo_MethodGroup:
        def __getitem__(self, t:typing.Type[CopyTo_1_T1]) -> CopyTo_1[CopyTo_1_T1]: ...

        CopyTo_1_T1 = typing.TypeVar('CopyTo_1_T1')
        class CopyTo_1(typing.Generic[CopyTo_1_T1]):
            CopyTo_1_T = Vector256_0.CopyTo_MethodGroup.CopyTo_1_T1
            @typing.overload
            def __call__(self, vector: Vector256_1[CopyTo_1_T], destination: Array_1[CopyTo_1_T]) -> None:...
            @typing.overload
            def __call__(self, vector: Vector256_1[CopyTo_1_T], destination: Span_1[CopyTo_1_T]) -> None:...
            @typing.overload
            def __call__(self, vector: Vector256_1[CopyTo_1_T], destination: Array_1[CopyTo_1_T], startIndex: int) -> None:...


    # Skipped Create due to it being static, abstract and generic.

    Create : Create_MethodGroup
    class Create_MethodGroup:
        def __getitem__(self, t:typing.Type[Create_1_T1]) -> Create_1[Create_1_T1]: ...

        Create_1_T1 = typing.TypeVar('Create_1_T1')
        class Create_1(typing.Generic[Create_1_T1]):
            Create_1_T = Vector256_0.Create_MethodGroup.Create_1_T1
            @typing.overload
            def __call__(self, values: Array_1[Create_1_T]) -> Vector256_1[Create_1_T]:...
            @typing.overload
            def __call__(self, values: ReadOnlySpan_1[Create_1_T]) -> Vector256_1[Create_1_T]:...
            @typing.overload
            def __call__(self, value: typing.Optional[Create_1_T]) -> Vector256_1[Create_1_T]:...
            @typing.overload
            def __call__(self, values: Array_1[Create_1_T], index: int) -> Vector256_1[Create_1_T]:...
            @typing.overload
            def __call__(self, lower: Vector128_1[Create_1_T], upper: Vector128_1[Create_1_T]) -> Vector256_1[Create_1_T]:...

        @typing.overload
        def __call__(self, value: float) -> Vector256_1[float]:...
        # Method Create(value : Single) was skipped since it collides with above method
        # Method Create(value : Byte) was skipped since it collides with above method
        # Method Create(value : Int16) was skipped since it collides with above method
        # Method Create(value : Int32) was skipped since it collides with above method
        # Method Create(value : Int64) was skipped since it collides with above method
        # Method Create(value : SByte) was skipped since it collides with above method
        # Method Create(value : UInt16) was skipped since it collides with above method
        # Method Create(value : UInt32) was skipped since it collides with above method
        # Method Create(value : UInt64) was skipped since it collides with above method
        # Method Create(value : IntPtr) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> Vector256_1[UIntPtr]:...
        @typing.overload
        def __call__(self, lower: Vector128_1[float], upper: Vector128_1[float]) -> Vector256_1[float]:...
        # Method Create(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method
        # Method Create(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method
        # Method Create(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method
        # Method Create(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method
        # Method Create(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method
        # Method Create(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method
        # Method Create(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method
        # Method Create(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method
        # Method Create(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method
        # Method Create(lower : Vector128`1, upper : Vector128`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, lower: Vector128_1[UIntPtr], upper: Vector128_1[UIntPtr]) -> Vector256_1[UIntPtr]:...
        @typing.overload
        def __call__(self, e0: float, e1: float, e2: float, e3: float) -> Vector256_1[float]:...
        # Method Create(e0 : Int64, e1 : Int64, e2 : Int64, e3 : Int64) was skipped since it collides with above method
        # Method Create(e0 : UInt64, e1 : UInt64, e2 : UInt64, e3 : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, e0: float, e1: float, e2: float, e3: float, e4: float, e5: float, e6: float, e7: float) -> Vector256_1[float]:...
        # Method Create(e0 : Int32, e1 : Int32, e2 : Int32, e3 : Int32, e4 : Int32, e5 : Int32, e6 : Int32, e7 : Int32) was skipped since it collides with above method
        # Method Create(e0 : UInt32, e1 : UInt32, e2 : UInt32, e3 : UInt32, e4 : UInt32, e5 : UInt32, e6 : UInt32, e7 : UInt32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, e0: int, e1: int, e2: int, e3: int, e4: int, e5: int, e6: int, e7: int, e8: int, e9: int, e10: int, e11: int, e12: int, e13: int, e14: int, e15: int) -> Vector256_1[int]:...
        # Method Create(e0 : UInt16, e1 : UInt16, e2 : UInt16, e3 : UInt16, e4 : UInt16, e5 : UInt16, e6 : UInt16, e7 : UInt16, e8 : UInt16, e9 : UInt16, e10 : UInt16, e11 : UInt16, e12 : UInt16, e13 : UInt16, e14 : UInt16, e15 : UInt16) was skipped since it collides with above method
        @typing.overload
        def __call__(self, e0: int, e1: int, e2: int, e3: int, e4: int, e5: int, e6: int, e7: int, e8: int, e9: int, e10: int, e11: int, e12: int, e13: int, e14: int, e15: int, e16: int, e17: int, e18: int, e19: int, e20: int, e21: int, e22: int, e23: int, e24: int, e25: int, e26: int, e27: int, e28: int, e29: int, e30: int, e31: int) -> Vector256_1[int]:...
        # Method Create(e0 : SByte, e1 : SByte, e2 : SByte, e3 : SByte, e4 : SByte, e5 : SByte, e6 : SByte, e7 : SByte, e8 : SByte, e9 : SByte, e10 : SByte, e11 : SByte, e12 : SByte, e13 : SByte, e14 : SByte, e15 : SByte, e16 : SByte, e17 : SByte, e18 : SByte, e19 : SByte, e20 : SByte, e21 : SByte, e22 : SByte, e23 : SByte, e24 : SByte, e25 : SByte, e26 : SByte, e27 : SByte, e28 : SByte, e29 : SByte, e30 : SByte, e31 : SByte) was skipped since it collides with above method

    # Skipped CreateScalar due to it being static, abstract and generic.

    CreateScalar : CreateScalar_MethodGroup
    class CreateScalar_MethodGroup:
        def __getitem__(self, t:typing.Type[CreateScalar_1_T1]) -> CreateScalar_1[CreateScalar_1_T1]: ...

        CreateScalar_1_T1 = typing.TypeVar('CreateScalar_1_T1')
        class CreateScalar_1(typing.Generic[CreateScalar_1_T1]):
            CreateScalar_1_T = Vector256_0.CreateScalar_MethodGroup.CreateScalar_1_T1
            def __call__(self, value: typing.Optional[CreateScalar_1_T]) -> Vector256_1[CreateScalar_1_T]:...

        @typing.overload
        def __call__(self, value: float) -> Vector256_1[float]:...
        # Method CreateScalar(value : Single) was skipped since it collides with above method
        # Method CreateScalar(value : Byte) was skipped since it collides with above method
        # Method CreateScalar(value : Int16) was skipped since it collides with above method
        # Method CreateScalar(value : Int32) was skipped since it collides with above method
        # Method CreateScalar(value : Int64) was skipped since it collides with above method
        # Method CreateScalar(value : SByte) was skipped since it collides with above method
        # Method CreateScalar(value : UInt16) was skipped since it collides with above method
        # Method CreateScalar(value : UInt32) was skipped since it collides with above method
        # Method CreateScalar(value : UInt64) was skipped since it collides with above method
        # Method CreateScalar(value : IntPtr) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> Vector256_1[UIntPtr]:...

    # Skipped CreateScalarUnsafe due to it being static, abstract and generic.

    CreateScalarUnsafe : CreateScalarUnsafe_MethodGroup
    class CreateScalarUnsafe_MethodGroup:
        def __getitem__(self, t:typing.Type[CreateScalarUnsafe_1_T1]) -> CreateScalarUnsafe_1[CreateScalarUnsafe_1_T1]: ...

        CreateScalarUnsafe_1_T1 = typing.TypeVar('CreateScalarUnsafe_1_T1')
        class CreateScalarUnsafe_1(typing.Generic[CreateScalarUnsafe_1_T1]):
            CreateScalarUnsafe_1_T = Vector256_0.CreateScalarUnsafe_MethodGroup.CreateScalarUnsafe_1_T1
            def __call__(self, value: typing.Optional[CreateScalarUnsafe_1_T]) -> Vector256_1[CreateScalarUnsafe_1_T]:...

        @typing.overload
        def __call__(self, value: float) -> Vector256_1[float]:...
        # Method CreateScalarUnsafe(value : Single) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : Byte) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : Int16) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : Int32) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : Int64) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : SByte) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : UInt16) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : UInt32) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : UInt64) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : IntPtr) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> Vector256_1[UIntPtr]:...

    # Skipped Divide due to it being static, abstract and generic.

    Divide : Divide_MethodGroup
    class Divide_MethodGroup:
        def __getitem__(self, t:typing.Type[Divide_1_T1]) -> Divide_1[Divide_1_T1]: ...

        Divide_1_T1 = typing.TypeVar('Divide_1_T1')
        class Divide_1(typing.Generic[Divide_1_T1]):
            Divide_1_T = Vector256_0.Divide_MethodGroup.Divide_1_T1
            @typing.overload
            def __call__(self, left: Vector256_1[Divide_1_T], right: Vector256_1[Divide_1_T]) -> Vector256_1[Divide_1_T]:...
            @typing.overload
            def __call__(self, left: Vector256_1[Divide_1_T], right: typing.Optional[Divide_1_T]) -> Vector256_1[Divide_1_T]:...


    # Skipped Dot due to it being static, abstract and generic.

    Dot : Dot_MethodGroup
    class Dot_MethodGroup:
        def __getitem__(self, t:typing.Type[Dot_1_T1]) -> Dot_1[Dot_1_T1]: ...

        Dot_1_T1 = typing.TypeVar('Dot_1_T1')
        class Dot_1(typing.Generic[Dot_1_T1]):
            Dot_1_T = Vector256_0.Dot_MethodGroup.Dot_1_T1
            def __call__(self, left: Vector256_1[Dot_1_T], right: Vector256_1[Dot_1_T]) -> Dot_1_T:...


    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        def __getitem__(self, t:typing.Type[Equals_1_T1]) -> Equals_1[Equals_1_T1]: ...

        Equals_1_T1 = typing.TypeVar('Equals_1_T1')
        class Equals_1(typing.Generic[Equals_1_T1]):
            Equals_1_T = Vector256_0.Equals_MethodGroup.Equals_1_T1
            def __call__(self, left: Vector256_1[Equals_1_T], right: Vector256_1[Equals_1_T]) -> Vector256_1[Equals_1_T]:...


    # Skipped EqualsAll due to it being static, abstract and generic.

    EqualsAll : EqualsAll_MethodGroup
    class EqualsAll_MethodGroup:
        def __getitem__(self, t:typing.Type[EqualsAll_1_T1]) -> EqualsAll_1[EqualsAll_1_T1]: ...

        EqualsAll_1_T1 = typing.TypeVar('EqualsAll_1_T1')
        class EqualsAll_1(typing.Generic[EqualsAll_1_T1]):
            EqualsAll_1_T = Vector256_0.EqualsAll_MethodGroup.EqualsAll_1_T1
            def __call__(self, left: Vector256_1[EqualsAll_1_T], right: Vector256_1[EqualsAll_1_T]) -> bool:...


    # Skipped EqualsAny due to it being static, abstract and generic.

    EqualsAny : EqualsAny_MethodGroup
    class EqualsAny_MethodGroup:
        def __getitem__(self, t:typing.Type[EqualsAny_1_T1]) -> EqualsAny_1[EqualsAny_1_T1]: ...

        EqualsAny_1_T1 = typing.TypeVar('EqualsAny_1_T1')
        class EqualsAny_1(typing.Generic[EqualsAny_1_T1]):
            EqualsAny_1_T = Vector256_0.EqualsAny_MethodGroup.EqualsAny_1_T1
            def __call__(self, left: Vector256_1[EqualsAny_1_T], right: Vector256_1[EqualsAny_1_T]) -> bool:...


    # Skipped ExtractMostSignificantBits due to it being static, abstract and generic.

    ExtractMostSignificantBits : ExtractMostSignificantBits_MethodGroup
    class ExtractMostSignificantBits_MethodGroup:
        def __getitem__(self, t:typing.Type[ExtractMostSignificantBits_1_T1]) -> ExtractMostSignificantBits_1[ExtractMostSignificantBits_1_T1]: ...

        ExtractMostSignificantBits_1_T1 = typing.TypeVar('ExtractMostSignificantBits_1_T1')
        class ExtractMostSignificantBits_1(typing.Generic[ExtractMostSignificantBits_1_T1]):
            ExtractMostSignificantBits_1_T = Vector256_0.ExtractMostSignificantBits_MethodGroup.ExtractMostSignificantBits_1_T1
            def __call__(self, vector: Vector256_1[ExtractMostSignificantBits_1_T]) -> int:...


    # Skipped Floor due to it being static, abstract and generic.

    Floor : Floor_MethodGroup
    class Floor_MethodGroup:
        def __call__(self, vector: Vector256_1[float]) -> Vector256_1[float]:...
        # Method Floor(vector : Vector256`1) was skipped since it collides with above method

    # Skipped GetElement due to it being static, abstract and generic.

    GetElement : GetElement_MethodGroup
    class GetElement_MethodGroup:
        def __getitem__(self, t:typing.Type[GetElement_1_T1]) -> GetElement_1[GetElement_1_T1]: ...

        GetElement_1_T1 = typing.TypeVar('GetElement_1_T1')
        class GetElement_1(typing.Generic[GetElement_1_T1]):
            GetElement_1_T = Vector256_0.GetElement_MethodGroup.GetElement_1_T1
            def __call__(self, vector: Vector256_1[GetElement_1_T], index: int) -> GetElement_1_T:...


    # Skipped GetLower due to it being static, abstract and generic.

    GetLower : GetLower_MethodGroup
    class GetLower_MethodGroup:
        def __getitem__(self, t:typing.Type[GetLower_1_T1]) -> GetLower_1[GetLower_1_T1]: ...

        GetLower_1_T1 = typing.TypeVar('GetLower_1_T1')
        class GetLower_1(typing.Generic[GetLower_1_T1]):
            GetLower_1_T = Vector256_0.GetLower_MethodGroup.GetLower_1_T1
            def __call__(self, vector: Vector256_1[GetLower_1_T]) -> Vector128_1[GetLower_1_T]:...


    # Skipped GetUpper due to it being static, abstract and generic.

    GetUpper : GetUpper_MethodGroup
    class GetUpper_MethodGroup:
        def __getitem__(self, t:typing.Type[GetUpper_1_T1]) -> GetUpper_1[GetUpper_1_T1]: ...

        GetUpper_1_T1 = typing.TypeVar('GetUpper_1_T1')
        class GetUpper_1(typing.Generic[GetUpper_1_T1]):
            GetUpper_1_T = Vector256_0.GetUpper_MethodGroup.GetUpper_1_T1
            def __call__(self, vector: Vector256_1[GetUpper_1_T]) -> Vector128_1[GetUpper_1_T]:...


    # Skipped GreaterThan due to it being static, abstract and generic.

    GreaterThan : GreaterThan_MethodGroup
    class GreaterThan_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThan_1_T1]) -> GreaterThan_1[GreaterThan_1_T1]: ...

        GreaterThan_1_T1 = typing.TypeVar('GreaterThan_1_T1')
        class GreaterThan_1(typing.Generic[GreaterThan_1_T1]):
            GreaterThan_1_T = Vector256_0.GreaterThan_MethodGroup.GreaterThan_1_T1
            def __call__(self, left: Vector256_1[GreaterThan_1_T], right: Vector256_1[GreaterThan_1_T]) -> Vector256_1[GreaterThan_1_T]:...


    # Skipped GreaterThanAll due to it being static, abstract and generic.

    GreaterThanAll : GreaterThanAll_MethodGroup
    class GreaterThanAll_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanAll_1_T1]) -> GreaterThanAll_1[GreaterThanAll_1_T1]: ...

        GreaterThanAll_1_T1 = typing.TypeVar('GreaterThanAll_1_T1')
        class GreaterThanAll_1(typing.Generic[GreaterThanAll_1_T1]):
            GreaterThanAll_1_T = Vector256_0.GreaterThanAll_MethodGroup.GreaterThanAll_1_T1
            def __call__(self, left: Vector256_1[GreaterThanAll_1_T], right: Vector256_1[GreaterThanAll_1_T]) -> bool:...


    # Skipped GreaterThanAny due to it being static, abstract and generic.

    GreaterThanAny : GreaterThanAny_MethodGroup
    class GreaterThanAny_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanAny_1_T1]) -> GreaterThanAny_1[GreaterThanAny_1_T1]: ...

        GreaterThanAny_1_T1 = typing.TypeVar('GreaterThanAny_1_T1')
        class GreaterThanAny_1(typing.Generic[GreaterThanAny_1_T1]):
            GreaterThanAny_1_T = Vector256_0.GreaterThanAny_MethodGroup.GreaterThanAny_1_T1
            def __call__(self, left: Vector256_1[GreaterThanAny_1_T], right: Vector256_1[GreaterThanAny_1_T]) -> bool:...


    # Skipped GreaterThanOrEqual due to it being static, abstract and generic.

    GreaterThanOrEqual : GreaterThanOrEqual_MethodGroup
    class GreaterThanOrEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanOrEqual_1_T1]) -> GreaterThanOrEqual_1[GreaterThanOrEqual_1_T1]: ...

        GreaterThanOrEqual_1_T1 = typing.TypeVar('GreaterThanOrEqual_1_T1')
        class GreaterThanOrEqual_1(typing.Generic[GreaterThanOrEqual_1_T1]):
            GreaterThanOrEqual_1_T = Vector256_0.GreaterThanOrEqual_MethodGroup.GreaterThanOrEqual_1_T1
            def __call__(self, left: Vector256_1[GreaterThanOrEqual_1_T], right: Vector256_1[GreaterThanOrEqual_1_T]) -> Vector256_1[GreaterThanOrEqual_1_T]:...


    # Skipped GreaterThanOrEqualAll due to it being static, abstract and generic.

    GreaterThanOrEqualAll : GreaterThanOrEqualAll_MethodGroup
    class GreaterThanOrEqualAll_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanOrEqualAll_1_T1]) -> GreaterThanOrEqualAll_1[GreaterThanOrEqualAll_1_T1]: ...

        GreaterThanOrEqualAll_1_T1 = typing.TypeVar('GreaterThanOrEqualAll_1_T1')
        class GreaterThanOrEqualAll_1(typing.Generic[GreaterThanOrEqualAll_1_T1]):
            GreaterThanOrEqualAll_1_T = Vector256_0.GreaterThanOrEqualAll_MethodGroup.GreaterThanOrEqualAll_1_T1
            def __call__(self, left: Vector256_1[GreaterThanOrEqualAll_1_T], right: Vector256_1[GreaterThanOrEqualAll_1_T]) -> bool:...


    # Skipped GreaterThanOrEqualAny due to it being static, abstract and generic.

    GreaterThanOrEqualAny : GreaterThanOrEqualAny_MethodGroup
    class GreaterThanOrEqualAny_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanOrEqualAny_1_T1]) -> GreaterThanOrEqualAny_1[GreaterThanOrEqualAny_1_T1]: ...

        GreaterThanOrEqualAny_1_T1 = typing.TypeVar('GreaterThanOrEqualAny_1_T1')
        class GreaterThanOrEqualAny_1(typing.Generic[GreaterThanOrEqualAny_1_T1]):
            GreaterThanOrEqualAny_1_T = Vector256_0.GreaterThanOrEqualAny_MethodGroup.GreaterThanOrEqualAny_1_T1
            def __call__(self, left: Vector256_1[GreaterThanOrEqualAny_1_T], right: Vector256_1[GreaterThanOrEqualAny_1_T]) -> bool:...


    # Skipped LessThan due to it being static, abstract and generic.

    LessThan : LessThan_MethodGroup
    class LessThan_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThan_1_T1]) -> LessThan_1[LessThan_1_T1]: ...

        LessThan_1_T1 = typing.TypeVar('LessThan_1_T1')
        class LessThan_1(typing.Generic[LessThan_1_T1]):
            LessThan_1_T = Vector256_0.LessThan_MethodGroup.LessThan_1_T1
            def __call__(self, left: Vector256_1[LessThan_1_T], right: Vector256_1[LessThan_1_T]) -> Vector256_1[LessThan_1_T]:...


    # Skipped LessThanAll due to it being static, abstract and generic.

    LessThanAll : LessThanAll_MethodGroup
    class LessThanAll_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanAll_1_T1]) -> LessThanAll_1[LessThanAll_1_T1]: ...

        LessThanAll_1_T1 = typing.TypeVar('LessThanAll_1_T1')
        class LessThanAll_1(typing.Generic[LessThanAll_1_T1]):
            LessThanAll_1_T = Vector256_0.LessThanAll_MethodGroup.LessThanAll_1_T1
            def __call__(self, left: Vector256_1[LessThanAll_1_T], right: Vector256_1[LessThanAll_1_T]) -> bool:...


    # Skipped LessThanAny due to it being static, abstract and generic.

    LessThanAny : LessThanAny_MethodGroup
    class LessThanAny_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanAny_1_T1]) -> LessThanAny_1[LessThanAny_1_T1]: ...

        LessThanAny_1_T1 = typing.TypeVar('LessThanAny_1_T1')
        class LessThanAny_1(typing.Generic[LessThanAny_1_T1]):
            LessThanAny_1_T = Vector256_0.LessThanAny_MethodGroup.LessThanAny_1_T1
            def __call__(self, left: Vector256_1[LessThanAny_1_T], right: Vector256_1[LessThanAny_1_T]) -> bool:...


    # Skipped LessThanOrEqual due to it being static, abstract and generic.

    LessThanOrEqual : LessThanOrEqual_MethodGroup
    class LessThanOrEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanOrEqual_1_T1]) -> LessThanOrEqual_1[LessThanOrEqual_1_T1]: ...

        LessThanOrEqual_1_T1 = typing.TypeVar('LessThanOrEqual_1_T1')
        class LessThanOrEqual_1(typing.Generic[LessThanOrEqual_1_T1]):
            LessThanOrEqual_1_T = Vector256_0.LessThanOrEqual_MethodGroup.LessThanOrEqual_1_T1
            def __call__(self, left: Vector256_1[LessThanOrEqual_1_T], right: Vector256_1[LessThanOrEqual_1_T]) -> Vector256_1[LessThanOrEqual_1_T]:...


    # Skipped LessThanOrEqualAll due to it being static, abstract and generic.

    LessThanOrEqualAll : LessThanOrEqualAll_MethodGroup
    class LessThanOrEqualAll_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanOrEqualAll_1_T1]) -> LessThanOrEqualAll_1[LessThanOrEqualAll_1_T1]: ...

        LessThanOrEqualAll_1_T1 = typing.TypeVar('LessThanOrEqualAll_1_T1')
        class LessThanOrEqualAll_1(typing.Generic[LessThanOrEqualAll_1_T1]):
            LessThanOrEqualAll_1_T = Vector256_0.LessThanOrEqualAll_MethodGroup.LessThanOrEqualAll_1_T1
            def __call__(self, left: Vector256_1[LessThanOrEqualAll_1_T], right: Vector256_1[LessThanOrEqualAll_1_T]) -> bool:...


    # Skipped LessThanOrEqualAny due to it being static, abstract and generic.

    LessThanOrEqualAny : LessThanOrEqualAny_MethodGroup
    class LessThanOrEqualAny_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanOrEqualAny_1_T1]) -> LessThanOrEqualAny_1[LessThanOrEqualAny_1_T1]: ...

        LessThanOrEqualAny_1_T1 = typing.TypeVar('LessThanOrEqualAny_1_T1')
        class LessThanOrEqualAny_1(typing.Generic[LessThanOrEqualAny_1_T1]):
            LessThanOrEqualAny_1_T = Vector256_0.LessThanOrEqualAny_MethodGroup.LessThanOrEqualAny_1_T1
            def __call__(self, left: Vector256_1[LessThanOrEqualAny_1_T], right: Vector256_1[LessThanOrEqualAny_1_T]) -> bool:...


    # Skipped Load due to it being static, abstract and generic.

    Load : Load_MethodGroup
    class Load_MethodGroup:
        def __getitem__(self, t:typing.Type[Load_1_T1]) -> Load_1[Load_1_T1]: ...

        Load_1_T1 = typing.TypeVar('Load_1_T1')
        class Load_1(typing.Generic[Load_1_T1]):
            Load_1_T = Vector256_0.Load_MethodGroup.Load_1_T1
            def __call__(self, source: clr.Reference[Load_1_T]) -> Vector256_1[Load_1_T]:...


    # Skipped LoadAligned due to it being static, abstract and generic.

    LoadAligned : LoadAligned_MethodGroup
    class LoadAligned_MethodGroup:
        def __getitem__(self, t:typing.Type[LoadAligned_1_T1]) -> LoadAligned_1[LoadAligned_1_T1]: ...

        LoadAligned_1_T1 = typing.TypeVar('LoadAligned_1_T1')
        class LoadAligned_1(typing.Generic[LoadAligned_1_T1]):
            LoadAligned_1_T = Vector256_0.LoadAligned_MethodGroup.LoadAligned_1_T1
            def __call__(self, source: clr.Reference[LoadAligned_1_T]) -> Vector256_1[LoadAligned_1_T]:...


    # Skipped LoadAlignedNonTemporal due to it being static, abstract and generic.

    LoadAlignedNonTemporal : LoadAlignedNonTemporal_MethodGroup
    class LoadAlignedNonTemporal_MethodGroup:
        def __getitem__(self, t:typing.Type[LoadAlignedNonTemporal_1_T1]) -> LoadAlignedNonTemporal_1[LoadAlignedNonTemporal_1_T1]: ...

        LoadAlignedNonTemporal_1_T1 = typing.TypeVar('LoadAlignedNonTemporal_1_T1')
        class LoadAlignedNonTemporal_1(typing.Generic[LoadAlignedNonTemporal_1_T1]):
            LoadAlignedNonTemporal_1_T = Vector256_0.LoadAlignedNonTemporal_MethodGroup.LoadAlignedNonTemporal_1_T1
            def __call__(self, source: clr.Reference[LoadAlignedNonTemporal_1_T]) -> Vector256_1[LoadAlignedNonTemporal_1_T]:...


    # Skipped LoadUnsafe due to it being static, abstract and generic.

    LoadUnsafe : LoadUnsafe_MethodGroup
    class LoadUnsafe_MethodGroup:
        def __getitem__(self, t:typing.Type[LoadUnsafe_1_T1]) -> LoadUnsafe_1[LoadUnsafe_1_T1]: ...

        LoadUnsafe_1_T1 = typing.TypeVar('LoadUnsafe_1_T1')
        class LoadUnsafe_1(typing.Generic[LoadUnsafe_1_T1]):
            LoadUnsafe_1_T = Vector256_0.LoadUnsafe_MethodGroup.LoadUnsafe_1_T1
            @typing.overload
            def __call__(self, source: typing.Optional[clr.Reference[LoadUnsafe_1_T]]) -> Vector256_1[LoadUnsafe_1_T]:...
            @typing.overload
            def __call__(self, source: typing.Optional[clr.Reference[LoadUnsafe_1_T]], elementOffset: UIntPtr) -> Vector256_1[LoadUnsafe_1_T]:...


    # Skipped Max due to it being static, abstract and generic.

    Max : Max_MethodGroup
    class Max_MethodGroup:
        def __getitem__(self, t:typing.Type[Max_1_T1]) -> Max_1[Max_1_T1]: ...

        Max_1_T1 = typing.TypeVar('Max_1_T1')
        class Max_1(typing.Generic[Max_1_T1]):
            Max_1_T = Vector256_0.Max_MethodGroup.Max_1_T1
            def __call__(self, left: Vector256_1[Max_1_T], right: Vector256_1[Max_1_T]) -> Vector256_1[Max_1_T]:...


    # Skipped Min due to it being static, abstract and generic.

    Min : Min_MethodGroup
    class Min_MethodGroup:
        def __getitem__(self, t:typing.Type[Min_1_T1]) -> Min_1[Min_1_T1]: ...

        Min_1_T1 = typing.TypeVar('Min_1_T1')
        class Min_1(typing.Generic[Min_1_T1]):
            Min_1_T = Vector256_0.Min_MethodGroup.Min_1_T1
            def __call__(self, left: Vector256_1[Min_1_T], right: Vector256_1[Min_1_T]) -> Vector256_1[Min_1_T]:...


    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        def __getitem__(self, t:typing.Type[Multiply_1_T1]) -> Multiply_1[Multiply_1_T1]: ...

        Multiply_1_T1 = typing.TypeVar('Multiply_1_T1')
        class Multiply_1(typing.Generic[Multiply_1_T1]):
            Multiply_1_T = Vector256_0.Multiply_MethodGroup.Multiply_1_T1
            @typing.overload
            def __call__(self, left: Vector256_1[Multiply_1_T], right: Vector256_1[Multiply_1_T]) -> Vector256_1[Multiply_1_T]:...
            @typing.overload
            def __call__(self, left: Vector256_1[Multiply_1_T], right: typing.Optional[Multiply_1_T]) -> Vector256_1[Multiply_1_T]:...
            @typing.overload
            def __call__(self, left: typing.Optional[Multiply_1_T], right: Vector256_1[Multiply_1_T]) -> Vector256_1[Multiply_1_T]:...


    # Skipped Narrow due to it being static, abstract and generic.

    Narrow : Narrow_MethodGroup
    class Narrow_MethodGroup:
        def __call__(self, lower: Vector256_1[float], upper: Vector256_1[float]) -> Vector256_1[float]:...
        # Method Narrow(lower : Vector256`1, upper : Vector256`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector256`1, upper : Vector256`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector256`1, upper : Vector256`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector256`1, upper : Vector256`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector256`1, upper : Vector256`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector256`1, upper : Vector256`1) was skipped since it collides with above method

    # Skipped Negate due to it being static, abstract and generic.

    Negate : Negate_MethodGroup
    class Negate_MethodGroup:
        def __getitem__(self, t:typing.Type[Negate_1_T1]) -> Negate_1[Negate_1_T1]: ...

        Negate_1_T1 = typing.TypeVar('Negate_1_T1')
        class Negate_1(typing.Generic[Negate_1_T1]):
            Negate_1_T = Vector256_0.Negate_MethodGroup.Negate_1_T1
            def __call__(self, vector: Vector256_1[Negate_1_T]) -> Vector256_1[Negate_1_T]:...


    # Skipped OnesComplement due to it being static, abstract and generic.

    OnesComplement : OnesComplement_MethodGroup
    class OnesComplement_MethodGroup:
        def __getitem__(self, t:typing.Type[OnesComplement_1_T1]) -> OnesComplement_1[OnesComplement_1_T1]: ...

        OnesComplement_1_T1 = typing.TypeVar('OnesComplement_1_T1')
        class OnesComplement_1(typing.Generic[OnesComplement_1_T1]):
            OnesComplement_1_T = Vector256_0.OnesComplement_MethodGroup.OnesComplement_1_T1
            def __call__(self, vector: Vector256_1[OnesComplement_1_T]) -> Vector256_1[OnesComplement_1_T]:...


    # Skipped ShiftLeft due to it being static, abstract and generic.

    ShiftLeft : ShiftLeft_MethodGroup
    class ShiftLeft_MethodGroup:
        @typing.overload
        def __call__(self, vector: Vector256_1[int], shiftCount: int) -> Vector256_1[int]:...
        # Method ShiftLeft(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, vector: Vector256_1[UIntPtr], shiftCount: int) -> Vector256_1[UIntPtr]:...

    # Skipped ShiftRightArithmetic due to it being static, abstract and generic.

    ShiftRightArithmetic : ShiftRightArithmetic_MethodGroup
    class ShiftRightArithmetic_MethodGroup:
        def __call__(self, vector: Vector256_1[int], shiftCount: int) -> Vector256_1[int]:...
        # Method ShiftRightArithmetic(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method

    # Skipped ShiftRightLogical due to it being static, abstract and generic.

    ShiftRightLogical : ShiftRightLogical_MethodGroup
    class ShiftRightLogical_MethodGroup:
        @typing.overload
        def __call__(self, vector: Vector256_1[int], shiftCount: int) -> Vector256_1[int]:...
        # Method ShiftRightLogical(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector256`1, shiftCount : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, vector: Vector256_1[UIntPtr], shiftCount: int) -> Vector256_1[UIntPtr]:...

    # Skipped Shuffle due to it being static, abstract and generic.

    Shuffle : Shuffle_MethodGroup
    class Shuffle_MethodGroup:
        def __call__(self, vector: Vector256_1[float], indices: Vector256_1[int]) -> Vector256_1[float]:...
        # Method Shuffle(vector : Vector256`1, indices : Vector256`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector256`1, indices : Vector256`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector256`1, indices : Vector256`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector256`1, indices : Vector256`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector256`1, indices : Vector256`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector256`1, indices : Vector256`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector256`1, indices : Vector256`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector256`1, indices : Vector256`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector256`1, indices : Vector256`1) was skipped since it collides with above method

    # Skipped Sqrt due to it being static, abstract and generic.

    Sqrt : Sqrt_MethodGroup
    class Sqrt_MethodGroup:
        def __getitem__(self, t:typing.Type[Sqrt_1_T1]) -> Sqrt_1[Sqrt_1_T1]: ...

        Sqrt_1_T1 = typing.TypeVar('Sqrt_1_T1')
        class Sqrt_1(typing.Generic[Sqrt_1_T1]):
            Sqrt_1_T = Vector256_0.Sqrt_MethodGroup.Sqrt_1_T1
            def __call__(self, vector: Vector256_1[Sqrt_1_T]) -> Vector256_1[Sqrt_1_T]:...


    # Skipped Store due to it being static, abstract and generic.

    Store : Store_MethodGroup
    class Store_MethodGroup:
        def __getitem__(self, t:typing.Type[Store_1_T1]) -> Store_1[Store_1_T1]: ...

        Store_1_T1 = typing.TypeVar('Store_1_T1')
        class Store_1(typing.Generic[Store_1_T1]):
            Store_1_T = Vector256_0.Store_MethodGroup.Store_1_T1
            def __call__(self, source: Vector256_1[Store_1_T], destination: clr.Reference[Store_1_T]) -> None:...


    # Skipped StoreAligned due to it being static, abstract and generic.

    StoreAligned : StoreAligned_MethodGroup
    class StoreAligned_MethodGroup:
        def __getitem__(self, t:typing.Type[StoreAligned_1_T1]) -> StoreAligned_1[StoreAligned_1_T1]: ...

        StoreAligned_1_T1 = typing.TypeVar('StoreAligned_1_T1')
        class StoreAligned_1(typing.Generic[StoreAligned_1_T1]):
            StoreAligned_1_T = Vector256_0.StoreAligned_MethodGroup.StoreAligned_1_T1
            def __call__(self, source: Vector256_1[StoreAligned_1_T], destination: clr.Reference[StoreAligned_1_T]) -> None:...


    # Skipped StoreAlignedNonTemporal due to it being static, abstract and generic.

    StoreAlignedNonTemporal : StoreAlignedNonTemporal_MethodGroup
    class StoreAlignedNonTemporal_MethodGroup:
        def __getitem__(self, t:typing.Type[StoreAlignedNonTemporal_1_T1]) -> StoreAlignedNonTemporal_1[StoreAlignedNonTemporal_1_T1]: ...

        StoreAlignedNonTemporal_1_T1 = typing.TypeVar('StoreAlignedNonTemporal_1_T1')
        class StoreAlignedNonTemporal_1(typing.Generic[StoreAlignedNonTemporal_1_T1]):
            StoreAlignedNonTemporal_1_T = Vector256_0.StoreAlignedNonTemporal_MethodGroup.StoreAlignedNonTemporal_1_T1
            def __call__(self, source: Vector256_1[StoreAlignedNonTemporal_1_T], destination: clr.Reference[StoreAlignedNonTemporal_1_T]) -> None:...


    # Skipped StoreUnsafe due to it being static, abstract and generic.

    StoreUnsafe : StoreUnsafe_MethodGroup
    class StoreUnsafe_MethodGroup:
        def __getitem__(self, t:typing.Type[StoreUnsafe_1_T1]) -> StoreUnsafe_1[StoreUnsafe_1_T1]: ...

        StoreUnsafe_1_T1 = typing.TypeVar('StoreUnsafe_1_T1')
        class StoreUnsafe_1(typing.Generic[StoreUnsafe_1_T1]):
            StoreUnsafe_1_T = Vector256_0.StoreUnsafe_MethodGroup.StoreUnsafe_1_T1
            @typing.overload
            def __call__(self, source: Vector256_1[StoreUnsafe_1_T], destination: typing.Optional[clr.Reference[StoreUnsafe_1_T]]) -> None:...
            @typing.overload
            def __call__(self, source: Vector256_1[StoreUnsafe_1_T], destination: typing.Optional[clr.Reference[StoreUnsafe_1_T]], elementOffset: UIntPtr) -> None:...


    # Skipped Subtract due to it being static, abstract and generic.

    Subtract : Subtract_MethodGroup
    class Subtract_MethodGroup:
        def __getitem__(self, t:typing.Type[Subtract_1_T1]) -> Subtract_1[Subtract_1_T1]: ...

        Subtract_1_T1 = typing.TypeVar('Subtract_1_T1')
        class Subtract_1(typing.Generic[Subtract_1_T1]):
            Subtract_1_T = Vector256_0.Subtract_MethodGroup.Subtract_1_T1
            def __call__(self, left: Vector256_1[Subtract_1_T], right: Vector256_1[Subtract_1_T]) -> Vector256_1[Subtract_1_T]:...


    # Skipped Sum due to it being static, abstract and generic.

    Sum : Sum_MethodGroup
    class Sum_MethodGroup:
        def __getitem__(self, t:typing.Type[Sum_1_T1]) -> Sum_1[Sum_1_T1]: ...

        Sum_1_T1 = typing.TypeVar('Sum_1_T1')
        class Sum_1(typing.Generic[Sum_1_T1]):
            Sum_1_T = Vector256_0.Sum_MethodGroup.Sum_1_T1
            def __call__(self, vector: Vector256_1[Sum_1_T]) -> Sum_1_T:...


    # Skipped ToScalar due to it being static, abstract and generic.

    ToScalar : ToScalar_MethodGroup
    class ToScalar_MethodGroup:
        def __getitem__(self, t:typing.Type[ToScalar_1_T1]) -> ToScalar_1[ToScalar_1_T1]: ...

        ToScalar_1_T1 = typing.TypeVar('ToScalar_1_T1')
        class ToScalar_1(typing.Generic[ToScalar_1_T1]):
            ToScalar_1_T = Vector256_0.ToScalar_MethodGroup.ToScalar_1_T1
            def __call__(self, vector: Vector256_1[ToScalar_1_T]) -> ToScalar_1_T:...


    # Skipped ToVector512 due to it being static, abstract and generic.

    ToVector512 : ToVector512_MethodGroup
    class ToVector512_MethodGroup:
        def __getitem__(self, t:typing.Type[ToVector512_1_T1]) -> ToVector512_1[ToVector512_1_T1]: ...

        ToVector512_1_T1 = typing.TypeVar('ToVector512_1_T1')
        class ToVector512_1(typing.Generic[ToVector512_1_T1]):
            ToVector512_1_T = Vector256_0.ToVector512_MethodGroup.ToVector512_1_T1
            def __call__(self, vector: Vector256_1[ToVector512_1_T]) -> Vector512_1[ToVector512_1_T]:...


    # Skipped ToVector512Unsafe due to it being static, abstract and generic.

    ToVector512Unsafe : ToVector512Unsafe_MethodGroup
    class ToVector512Unsafe_MethodGroup:
        def __getitem__(self, t:typing.Type[ToVector512Unsafe_1_T1]) -> ToVector512Unsafe_1[ToVector512Unsafe_1_T1]: ...

        ToVector512Unsafe_1_T1 = typing.TypeVar('ToVector512Unsafe_1_T1')
        class ToVector512Unsafe_1(typing.Generic[ToVector512Unsafe_1_T1]):
            ToVector512Unsafe_1_T = Vector256_0.ToVector512Unsafe_MethodGroup.ToVector512Unsafe_1_T1
            def __call__(self, vector: Vector256_1[ToVector512Unsafe_1_T]) -> Vector512_1[ToVector512Unsafe_1_T]:...


    # Skipped TryCopyTo due to it being static, abstract and generic.

    TryCopyTo : TryCopyTo_MethodGroup
    class TryCopyTo_MethodGroup:
        def __getitem__(self, t:typing.Type[TryCopyTo_1_T1]) -> TryCopyTo_1[TryCopyTo_1_T1]: ...

        TryCopyTo_1_T1 = typing.TypeVar('TryCopyTo_1_T1')
        class TryCopyTo_1(typing.Generic[TryCopyTo_1_T1]):
            TryCopyTo_1_T = Vector256_0.TryCopyTo_MethodGroup.TryCopyTo_1_T1
            def __call__(self, vector: Vector256_1[TryCopyTo_1_T], destination: Span_1[TryCopyTo_1_T]) -> bool:...


    # Skipped Widen due to it being static, abstract and generic.

    Widen : Widen_MethodGroup
    class Widen_MethodGroup:
        def __call__(self, source: Vector256_1[float]) -> ValueTuple_2[Vector256_1[float], Vector256_1[float]]:...
        # Method Widen(source : Vector256`1) was skipped since it collides with above method
        # Method Widen(source : Vector256`1) was skipped since it collides with above method
        # Method Widen(source : Vector256`1) was skipped since it collides with above method
        # Method Widen(source : Vector256`1) was skipped since it collides with above method
        # Method Widen(source : Vector256`1) was skipped since it collides with above method
        # Method Widen(source : Vector256`1) was skipped since it collides with above method

    # Skipped WidenLower due to it being static, abstract and generic.

    WidenLower : WidenLower_MethodGroup
    class WidenLower_MethodGroup:
        def __call__(self, source: Vector256_1[float]) -> Vector256_1[float]:...
        # Method WidenLower(source : Vector256`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector256`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector256`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector256`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector256`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector256`1) was skipped since it collides with above method

    # Skipped WidenUpper due to it being static, abstract and generic.

    WidenUpper : WidenUpper_MethodGroup
    class WidenUpper_MethodGroup:
        def __call__(self, source: Vector256_1[float]) -> Vector256_1[float]:...
        # Method WidenUpper(source : Vector256`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector256`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector256`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector256`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector256`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector256`1) was skipped since it collides with above method

    # Skipped WithElement due to it being static, abstract and generic.

    WithElement : WithElement_MethodGroup
    class WithElement_MethodGroup:
        def __getitem__(self, t:typing.Type[WithElement_1_T1]) -> WithElement_1[WithElement_1_T1]: ...

        WithElement_1_T1 = typing.TypeVar('WithElement_1_T1')
        class WithElement_1(typing.Generic[WithElement_1_T1]):
            WithElement_1_T = Vector256_0.WithElement_MethodGroup.WithElement_1_T1
            def __call__(self, vector: Vector256_1[WithElement_1_T], index: int, value: typing.Optional[WithElement_1_T]) -> Vector256_1[WithElement_1_T]:...


    # Skipped WithLower due to it being static, abstract and generic.

    WithLower : WithLower_MethodGroup
    class WithLower_MethodGroup:
        def __getitem__(self, t:typing.Type[WithLower_1_T1]) -> WithLower_1[WithLower_1_T1]: ...

        WithLower_1_T1 = typing.TypeVar('WithLower_1_T1')
        class WithLower_1(typing.Generic[WithLower_1_T1]):
            WithLower_1_T = Vector256_0.WithLower_MethodGroup.WithLower_1_T1
            def __call__(self, vector: Vector256_1[WithLower_1_T], value: Vector128_1[WithLower_1_T]) -> Vector256_1[WithLower_1_T]:...


    # Skipped WithUpper due to it being static, abstract and generic.

    WithUpper : WithUpper_MethodGroup
    class WithUpper_MethodGroup:
        def __getitem__(self, t:typing.Type[WithUpper_1_T1]) -> WithUpper_1[WithUpper_1_T1]: ...

        WithUpper_1_T1 = typing.TypeVar('WithUpper_1_T1')
        class WithUpper_1(typing.Generic[WithUpper_1_T1]):
            WithUpper_1_T = Vector256_0.WithUpper_MethodGroup.WithUpper_1_T1
            def __call__(self, vector: Vector256_1[WithUpper_1_T], value: Vector128_1[WithUpper_1_T]) -> Vector256_1[WithUpper_1_T]:...


    # Skipped Xor due to it being static, abstract and generic.

    Xor : Xor_MethodGroup
    class Xor_MethodGroup:
        def __getitem__(self, t:typing.Type[Xor_1_T1]) -> Xor_1[Xor_1_T1]: ...

        Xor_1_T1 = typing.TypeVar('Xor_1_T1')
        class Xor_1(typing.Generic[Xor_1_T1]):
            Xor_1_T = Vector256_0.Xor_MethodGroup.Xor_1_T1
            def __call__(self, left: Vector256_1[Xor_1_T], right: Vector256_1[Xor_1_T]) -> Vector256_1[Xor_1_T]:...




Vector256_1_T = typing.TypeVar('Vector256_1_T')
class Vector256_1(typing.Generic[Vector256_1_T], IEquatable_1[Vector256_1[Vector256_1_T]]):
    @classmethod
    @property
    def AllBitsSet(cls) -> Vector256_1[Vector256_1_T]: ...
    @classmethod
    @property
    def Count(cls) -> int: ...
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @property
    def Item(self) -> typing.Optional[Vector256_1_T]: ...
    @classmethod
    @property
    def One(cls) -> Vector256_1[Vector256_1_T]: ...
    @classmethod
    @property
    def Zero(cls) -> Vector256_1[Vector256_1_T]: ...
    def GetHashCode(self) -> int: ...
    def __add__(self, left: Vector256_1[Vector256_1_T], right: Vector256_1[Vector256_1_T]) -> Vector256_1[Vector256_1_T]: ...
    def __and__(self, left: Vector256_1[Vector256_1_T], right: Vector256_1[Vector256_1_T]) -> Vector256_1[Vector256_1_T]: ...
    def __or__(self, left: Vector256_1[Vector256_1_T], right: Vector256_1[Vector256_1_T]) -> Vector256_1[Vector256_1_T]: ...
    @typing.overload
    def __truediv__(self, left: Vector256_1[Vector256_1_T], right: Vector256_1[Vector256_1_T]) -> Vector256_1[Vector256_1_T]: ...
    @typing.overload
    def __truediv__(self, left: Vector256_1[Vector256_1_T], right: typing.Optional[Vector256_1_T]) -> Vector256_1[Vector256_1_T]: ...
    def __eq__(self, left: Vector256_1[Vector256_1_T], right: Vector256_1[Vector256_1_T]) -> bool: ...
    def __xor__(self, left: Vector256_1[Vector256_1_T], right: Vector256_1[Vector256_1_T]) -> Vector256_1[Vector256_1_T]: ...
    def __ne__(self, left: Vector256_1[Vector256_1_T], right: Vector256_1[Vector256_1_T]) -> bool: ...
    def __lshift__(self, value: Vector256_1[Vector256_1_T], shiftCount: int) -> Vector256_1[Vector256_1_T]: ...
    @typing.overload
    def __mul__(self, left: Vector256_1[Vector256_1_T], right: Vector256_1[Vector256_1_T]) -> Vector256_1[Vector256_1_T]: ...
    @typing.overload
    def __mul__(self, left: Vector256_1[Vector256_1_T], right: typing.Optional[Vector256_1_T]) -> Vector256_1[Vector256_1_T]: ...
    @typing.overload
    def __mul__(self, left: typing.Optional[Vector256_1_T], right: Vector256_1[Vector256_1_T]) -> Vector256_1[Vector256_1_T]: ...
    def __invert__(self, vector: Vector256_1[Vector256_1_T]) -> Vector256_1[Vector256_1_T]: ...
    def __rshift__(self, value: Vector256_1[Vector256_1_T], shiftCount: int) -> Vector256_1[Vector256_1_T]: ...
    def __sub__(self, left: Vector256_1[Vector256_1_T], right: Vector256_1[Vector256_1_T]) -> Vector256_1[Vector256_1_T]: ...
    def __neg__(self, vector: Vector256_1[Vector256_1_T]) -> Vector256_1[Vector256_1_T]: ...
    def __pos__(self, value: Vector256_1[Vector256_1_T]) -> Vector256_1[Vector256_1_T]: ...
    # Operator not supported op_UnsignedRightShift(value: Vector256`1, shiftCount: Int32)
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[Vector256_1_T]
    Equals_MethodGroup_Vector256_1_T = typing.TypeVar('Equals_MethodGroup_Vector256_1_T')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_Vector256_1_T]):
        Equals_MethodGroup_Vector256_1_T = Vector256_1.Equals_MethodGroup_Vector256_1_T
        @typing.overload
        def __call__(self, other: Vector256_1[Equals_MethodGroup_Vector256_1_T]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Optional[typing.Any]) -> bool:...



class Vector512_GenericClasses(abc.ABCMeta):
    Generic_Vector512_GenericClasses_Vector512_1_T = typing.TypeVar('Generic_Vector512_GenericClasses_Vector512_1_T')
    def __getitem__(self, types : typing.Type[Generic_Vector512_GenericClasses_Vector512_1_T]) -> typing.Type[Vector512_1[Generic_Vector512_GenericClasses_Vector512_1_T]]: ...

class Vector512(Vector512_0, metaclass =Vector512_GenericClasses): ...

class Vector512_0(abc.ABC):
    @classmethod
    @property
    def IsHardwareAccelerated(cls) -> bool: ...
    @staticmethod
    def ConvertToInt32(vector: Vector512_1[float]) -> Vector512_1[int]: ...
    @staticmethod
    def ConvertToInt64(vector: Vector512_1[float]) -> Vector512_1[int]: ...
    @staticmethod
    def ConvertToUInt32(vector: Vector512_1[float]) -> Vector512_1[int]: ...
    @staticmethod
    def ConvertToUInt64(vector: Vector512_1[float]) -> Vector512_1[int]: ...
    # Skipped Abs due to it being static, abstract and generic.

    Abs : Abs_MethodGroup
    class Abs_MethodGroup:
        def __getitem__(self, t:typing.Type[Abs_1_T1]) -> Abs_1[Abs_1_T1]: ...

        Abs_1_T1 = typing.TypeVar('Abs_1_T1')
        class Abs_1(typing.Generic[Abs_1_T1]):
            Abs_1_T = Vector512_0.Abs_MethodGroup.Abs_1_T1
            def __call__(self, vector: Vector512_1[Abs_1_T]) -> Vector512_1[Abs_1_T]:...


    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        def __getitem__(self, t:typing.Type[Add_1_T1]) -> Add_1[Add_1_T1]: ...

        Add_1_T1 = typing.TypeVar('Add_1_T1')
        class Add_1(typing.Generic[Add_1_T1]):
            Add_1_T = Vector512_0.Add_MethodGroup.Add_1_T1
            def __call__(self, left: Vector512_1[Add_1_T], right: Vector512_1[Add_1_T]) -> Vector512_1[Add_1_T]:...


    # Skipped AndNot due to it being static, abstract and generic.

    AndNot : AndNot_MethodGroup
    class AndNot_MethodGroup:
        def __getitem__(self, t:typing.Type[AndNot_1_T1]) -> AndNot_1[AndNot_1_T1]: ...

        AndNot_1_T1 = typing.TypeVar('AndNot_1_T1')
        class AndNot_1(typing.Generic[AndNot_1_T1]):
            AndNot_1_T = Vector512_0.AndNot_MethodGroup.AndNot_1_T1
            def __call__(self, left: Vector512_1[AndNot_1_T], right: Vector512_1[AndNot_1_T]) -> Vector512_1[AndNot_1_T]:...


    # Skipped As due to it being static, abstract and generic.

    As : As_MethodGroup
    class As_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[As_2_T1], typing.Type[As_2_T2]]) -> As_2[As_2_T1, As_2_T2]: ...

        As_2_T1 = typing.TypeVar('As_2_T1')
        As_2_T2 = typing.TypeVar('As_2_T2')
        class As_2(typing.Generic[As_2_T1, As_2_T2]):
            As_2_TFrom = Vector512_0.As_MethodGroup.As_2_T1
            As_2_TTo = Vector512_0.As_MethodGroup.As_2_T2
            def __call__(self, vector: Vector512_1[As_2_TFrom]) -> Vector512_1[As_2_TTo]:...


    # Skipped AsByte due to it being static, abstract and generic.

    AsByte : AsByte_MethodGroup
    class AsByte_MethodGroup:
        def __getitem__(self, t:typing.Type[AsByte_1_T1]) -> AsByte_1[AsByte_1_T1]: ...

        AsByte_1_T1 = typing.TypeVar('AsByte_1_T1')
        class AsByte_1(typing.Generic[AsByte_1_T1]):
            AsByte_1_T = Vector512_0.AsByte_MethodGroup.AsByte_1_T1
            def __call__(self, vector: Vector512_1[AsByte_1_T]) -> Vector512_1[int]:...


    # Skipped AsDouble due to it being static, abstract and generic.

    AsDouble : AsDouble_MethodGroup
    class AsDouble_MethodGroup:
        def __getitem__(self, t:typing.Type[AsDouble_1_T1]) -> AsDouble_1[AsDouble_1_T1]: ...

        AsDouble_1_T1 = typing.TypeVar('AsDouble_1_T1')
        class AsDouble_1(typing.Generic[AsDouble_1_T1]):
            AsDouble_1_T = Vector512_0.AsDouble_MethodGroup.AsDouble_1_T1
            def __call__(self, vector: Vector512_1[AsDouble_1_T]) -> Vector512_1[float]:...


    # Skipped AsInt16 due to it being static, abstract and generic.

    AsInt16 : AsInt16_MethodGroup
    class AsInt16_MethodGroup:
        def __getitem__(self, t:typing.Type[AsInt16_1_T1]) -> AsInt16_1[AsInt16_1_T1]: ...

        AsInt16_1_T1 = typing.TypeVar('AsInt16_1_T1')
        class AsInt16_1(typing.Generic[AsInt16_1_T1]):
            AsInt16_1_T = Vector512_0.AsInt16_MethodGroup.AsInt16_1_T1
            def __call__(self, vector: Vector512_1[AsInt16_1_T]) -> Vector512_1[int]:...


    # Skipped AsInt32 due to it being static, abstract and generic.

    AsInt32 : AsInt32_MethodGroup
    class AsInt32_MethodGroup:
        def __getitem__(self, t:typing.Type[AsInt32_1_T1]) -> AsInt32_1[AsInt32_1_T1]: ...

        AsInt32_1_T1 = typing.TypeVar('AsInt32_1_T1')
        class AsInt32_1(typing.Generic[AsInt32_1_T1]):
            AsInt32_1_T = Vector512_0.AsInt32_MethodGroup.AsInt32_1_T1
            def __call__(self, vector: Vector512_1[AsInt32_1_T]) -> Vector512_1[int]:...


    # Skipped AsInt64 due to it being static, abstract and generic.

    AsInt64 : AsInt64_MethodGroup
    class AsInt64_MethodGroup:
        def __getitem__(self, t:typing.Type[AsInt64_1_T1]) -> AsInt64_1[AsInt64_1_T1]: ...

        AsInt64_1_T1 = typing.TypeVar('AsInt64_1_T1')
        class AsInt64_1(typing.Generic[AsInt64_1_T1]):
            AsInt64_1_T = Vector512_0.AsInt64_MethodGroup.AsInt64_1_T1
            def __call__(self, vector: Vector512_1[AsInt64_1_T]) -> Vector512_1[int]:...


    # Skipped AsNInt due to it being static, abstract and generic.

    AsNInt : AsNInt_MethodGroup
    class AsNInt_MethodGroup:
        def __getitem__(self, t:typing.Type[AsNInt_1_T1]) -> AsNInt_1[AsNInt_1_T1]: ...

        AsNInt_1_T1 = typing.TypeVar('AsNInt_1_T1')
        class AsNInt_1(typing.Generic[AsNInt_1_T1]):
            AsNInt_1_T = Vector512_0.AsNInt_MethodGroup.AsNInt_1_T1
            def __call__(self, vector: Vector512_1[AsNInt_1_T]) -> Vector512_1[int]:...


    # Skipped AsNUInt due to it being static, abstract and generic.

    AsNUInt : AsNUInt_MethodGroup
    class AsNUInt_MethodGroup:
        def __getitem__(self, t:typing.Type[AsNUInt_1_T1]) -> AsNUInt_1[AsNUInt_1_T1]: ...

        AsNUInt_1_T1 = typing.TypeVar('AsNUInt_1_T1')
        class AsNUInt_1(typing.Generic[AsNUInt_1_T1]):
            AsNUInt_1_T = Vector512_0.AsNUInt_MethodGroup.AsNUInt_1_T1
            def __call__(self, vector: Vector512_1[AsNUInt_1_T]) -> Vector512_1[UIntPtr]:...


    # Skipped AsSByte due to it being static, abstract and generic.

    AsSByte : AsSByte_MethodGroup
    class AsSByte_MethodGroup:
        def __getitem__(self, t:typing.Type[AsSByte_1_T1]) -> AsSByte_1[AsSByte_1_T1]: ...

        AsSByte_1_T1 = typing.TypeVar('AsSByte_1_T1')
        class AsSByte_1(typing.Generic[AsSByte_1_T1]):
            AsSByte_1_T = Vector512_0.AsSByte_MethodGroup.AsSByte_1_T1
            def __call__(self, vector: Vector512_1[AsSByte_1_T]) -> Vector512_1[int]:...


    # Skipped AsSingle due to it being static, abstract and generic.

    AsSingle : AsSingle_MethodGroup
    class AsSingle_MethodGroup:
        def __getitem__(self, t:typing.Type[AsSingle_1_T1]) -> AsSingle_1[AsSingle_1_T1]: ...

        AsSingle_1_T1 = typing.TypeVar('AsSingle_1_T1')
        class AsSingle_1(typing.Generic[AsSingle_1_T1]):
            AsSingle_1_T = Vector512_0.AsSingle_MethodGroup.AsSingle_1_T1
            def __call__(self, vector: Vector512_1[AsSingle_1_T]) -> Vector512_1[float]:...


    # Skipped AsUInt16 due to it being static, abstract and generic.

    AsUInt16 : AsUInt16_MethodGroup
    class AsUInt16_MethodGroup:
        def __getitem__(self, t:typing.Type[AsUInt16_1_T1]) -> AsUInt16_1[AsUInt16_1_T1]: ...

        AsUInt16_1_T1 = typing.TypeVar('AsUInt16_1_T1')
        class AsUInt16_1(typing.Generic[AsUInt16_1_T1]):
            AsUInt16_1_T = Vector512_0.AsUInt16_MethodGroup.AsUInt16_1_T1
            def __call__(self, vector: Vector512_1[AsUInt16_1_T]) -> Vector512_1[int]:...


    # Skipped AsUInt32 due to it being static, abstract and generic.

    AsUInt32 : AsUInt32_MethodGroup
    class AsUInt32_MethodGroup:
        def __getitem__(self, t:typing.Type[AsUInt32_1_T1]) -> AsUInt32_1[AsUInt32_1_T1]: ...

        AsUInt32_1_T1 = typing.TypeVar('AsUInt32_1_T1')
        class AsUInt32_1(typing.Generic[AsUInt32_1_T1]):
            AsUInt32_1_T = Vector512_0.AsUInt32_MethodGroup.AsUInt32_1_T1
            def __call__(self, vector: Vector512_1[AsUInt32_1_T]) -> Vector512_1[int]:...


    # Skipped AsUInt64 due to it being static, abstract and generic.

    AsUInt64 : AsUInt64_MethodGroup
    class AsUInt64_MethodGroup:
        def __getitem__(self, t:typing.Type[AsUInt64_1_T1]) -> AsUInt64_1[AsUInt64_1_T1]: ...

        AsUInt64_1_T1 = typing.TypeVar('AsUInt64_1_T1')
        class AsUInt64_1(typing.Generic[AsUInt64_1_T1]):
            AsUInt64_1_T = Vector512_0.AsUInt64_MethodGroup.AsUInt64_1_T1
            def __call__(self, vector: Vector512_1[AsUInt64_1_T]) -> Vector512_1[int]:...


    # Skipped AsVector due to it being static, abstract and generic.

    AsVector : AsVector_MethodGroup
    class AsVector_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVector_1_T1]) -> AsVector_1[AsVector_1_T1]: ...

        AsVector_1_T1 = typing.TypeVar('AsVector_1_T1')
        class AsVector_1(typing.Generic[AsVector_1_T1]):
            AsVector_1_T = Vector512_0.AsVector_MethodGroup.AsVector_1_T1
            def __call__(self, value: Vector512_1[AsVector_1_T]) -> Vector_1[AsVector_1_T]:...


    # Skipped AsVector512 due to it being static, abstract and generic.

    AsVector512 : AsVector512_MethodGroup
    class AsVector512_MethodGroup:
        def __getitem__(self, t:typing.Type[AsVector512_1_T1]) -> AsVector512_1[AsVector512_1_T1]: ...

        AsVector512_1_T1 = typing.TypeVar('AsVector512_1_T1')
        class AsVector512_1(typing.Generic[AsVector512_1_T1]):
            AsVector512_1_T = Vector512_0.AsVector512_MethodGroup.AsVector512_1_T1
            def __call__(self, value: Vector_1[AsVector512_1_T]) -> Vector512_1[AsVector512_1_T]:...


    # Skipped BitwiseAnd due to it being static, abstract and generic.

    BitwiseAnd : BitwiseAnd_MethodGroup
    class BitwiseAnd_MethodGroup:
        def __getitem__(self, t:typing.Type[BitwiseAnd_1_T1]) -> BitwiseAnd_1[BitwiseAnd_1_T1]: ...

        BitwiseAnd_1_T1 = typing.TypeVar('BitwiseAnd_1_T1')
        class BitwiseAnd_1(typing.Generic[BitwiseAnd_1_T1]):
            BitwiseAnd_1_T = Vector512_0.BitwiseAnd_MethodGroup.BitwiseAnd_1_T1
            def __call__(self, left: Vector512_1[BitwiseAnd_1_T], right: Vector512_1[BitwiseAnd_1_T]) -> Vector512_1[BitwiseAnd_1_T]:...


    # Skipped BitwiseOr due to it being static, abstract and generic.

    BitwiseOr : BitwiseOr_MethodGroup
    class BitwiseOr_MethodGroup:
        def __getitem__(self, t:typing.Type[BitwiseOr_1_T1]) -> BitwiseOr_1[BitwiseOr_1_T1]: ...

        BitwiseOr_1_T1 = typing.TypeVar('BitwiseOr_1_T1')
        class BitwiseOr_1(typing.Generic[BitwiseOr_1_T1]):
            BitwiseOr_1_T = Vector512_0.BitwiseOr_MethodGroup.BitwiseOr_1_T1
            def __call__(self, left: Vector512_1[BitwiseOr_1_T], right: Vector512_1[BitwiseOr_1_T]) -> Vector512_1[BitwiseOr_1_T]:...


    # Skipped Ceiling due to it being static, abstract and generic.

    Ceiling : Ceiling_MethodGroup
    class Ceiling_MethodGroup:
        def __call__(self, vector: Vector512_1[float]) -> Vector512_1[float]:...
        # Method Ceiling(vector : Vector512`1) was skipped since it collides with above method

    # Skipped ConditionalSelect due to it being static, abstract and generic.

    ConditionalSelect : ConditionalSelect_MethodGroup
    class ConditionalSelect_MethodGroup:
        def __getitem__(self, t:typing.Type[ConditionalSelect_1_T1]) -> ConditionalSelect_1[ConditionalSelect_1_T1]: ...

        ConditionalSelect_1_T1 = typing.TypeVar('ConditionalSelect_1_T1')
        class ConditionalSelect_1(typing.Generic[ConditionalSelect_1_T1]):
            ConditionalSelect_1_T = Vector512_0.ConditionalSelect_MethodGroup.ConditionalSelect_1_T1
            def __call__(self, condition: Vector512_1[ConditionalSelect_1_T], left: Vector512_1[ConditionalSelect_1_T], right: Vector512_1[ConditionalSelect_1_T]) -> Vector512_1[ConditionalSelect_1_T]:...


    # Skipped ConvertToDouble due to it being static, abstract and generic.

    ConvertToDouble : ConvertToDouble_MethodGroup
    class ConvertToDouble_MethodGroup:
        def __call__(self, vector: Vector512_1[int]) -> Vector512_1[float]:...
        # Method ConvertToDouble(vector : Vector512`1) was skipped since it collides with above method

    # Skipped ConvertToSingle due to it being static, abstract and generic.

    ConvertToSingle : ConvertToSingle_MethodGroup
    class ConvertToSingle_MethodGroup:
        def __call__(self, vector: Vector512_1[int]) -> Vector512_1[float]:...
        # Method ConvertToSingle(vector : Vector512`1) was skipped since it collides with above method

    # Skipped CopyTo due to it being static, abstract and generic.

    CopyTo : CopyTo_MethodGroup
    class CopyTo_MethodGroup:
        def __getitem__(self, t:typing.Type[CopyTo_1_T1]) -> CopyTo_1[CopyTo_1_T1]: ...

        CopyTo_1_T1 = typing.TypeVar('CopyTo_1_T1')
        class CopyTo_1(typing.Generic[CopyTo_1_T1]):
            CopyTo_1_T = Vector512_0.CopyTo_MethodGroup.CopyTo_1_T1
            @typing.overload
            def __call__(self, vector: Vector512_1[CopyTo_1_T], destination: Array_1[CopyTo_1_T]) -> None:...
            @typing.overload
            def __call__(self, vector: Vector512_1[CopyTo_1_T], destination: Span_1[CopyTo_1_T]) -> None:...
            @typing.overload
            def __call__(self, vector: Vector512_1[CopyTo_1_T], destination: Array_1[CopyTo_1_T], startIndex: int) -> None:...


    # Skipped Create due to it being static, abstract and generic.

    Create : Create_MethodGroup
    class Create_MethodGroup:
        def __getitem__(self, t:typing.Type[Create_1_T1]) -> Create_1[Create_1_T1]: ...

        Create_1_T1 = typing.TypeVar('Create_1_T1')
        class Create_1(typing.Generic[Create_1_T1]):
            Create_1_T = Vector512_0.Create_MethodGroup.Create_1_T1
            @typing.overload
            def __call__(self, values: Array_1[Create_1_T]) -> Vector512_1[Create_1_T]:...
            @typing.overload
            def __call__(self, values: ReadOnlySpan_1[Create_1_T]) -> Vector512_1[Create_1_T]:...
            @typing.overload
            def __call__(self, value: typing.Optional[Create_1_T]) -> Vector512_1[Create_1_T]:...
            @typing.overload
            def __call__(self, values: Array_1[Create_1_T], index: int) -> Vector512_1[Create_1_T]:...
            @typing.overload
            def __call__(self, lower: Vector256_1[Create_1_T], upper: Vector256_1[Create_1_T]) -> Vector512_1[Create_1_T]:...

        @typing.overload
        def __call__(self, value: float) -> Vector512_1[float]:...
        # Method Create(value : Single) was skipped since it collides with above method
        # Method Create(value : Byte) was skipped since it collides with above method
        # Method Create(value : Int16) was skipped since it collides with above method
        # Method Create(value : Int32) was skipped since it collides with above method
        # Method Create(value : Int64) was skipped since it collides with above method
        # Method Create(value : SByte) was skipped since it collides with above method
        # Method Create(value : UInt16) was skipped since it collides with above method
        # Method Create(value : UInt32) was skipped since it collides with above method
        # Method Create(value : UInt64) was skipped since it collides with above method
        # Method Create(value : IntPtr) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> Vector512_1[UIntPtr]:...
        @typing.overload
        def __call__(self, lower: Vector256_1[float], upper: Vector256_1[float]) -> Vector512_1[float]:...
        # Method Create(lower : Vector256`1, upper : Vector256`1) was skipped since it collides with above method
        # Method Create(lower : Vector256`1, upper : Vector256`1) was skipped since it collides with above method
        # Method Create(lower : Vector256`1, upper : Vector256`1) was skipped since it collides with above method
        # Method Create(lower : Vector256`1, upper : Vector256`1) was skipped since it collides with above method
        # Method Create(lower : Vector256`1, upper : Vector256`1) was skipped since it collides with above method
        # Method Create(lower : Vector256`1, upper : Vector256`1) was skipped since it collides with above method
        # Method Create(lower : Vector256`1, upper : Vector256`1) was skipped since it collides with above method
        # Method Create(lower : Vector256`1, upper : Vector256`1) was skipped since it collides with above method
        # Method Create(lower : Vector256`1, upper : Vector256`1) was skipped since it collides with above method
        # Method Create(lower : Vector256`1, upper : Vector256`1) was skipped since it collides with above method
        @typing.overload
        def __call__(self, lower: Vector256_1[UIntPtr], upper: Vector256_1[UIntPtr]) -> Vector512_1[UIntPtr]:...
        @typing.overload
        def __call__(self, e0: float, e1: float, e2: float, e3: float, e4: float, e5: float, e6: float, e7: float) -> Vector512_1[float]:...
        # Method Create(e0 : Int64, e1 : Int64, e2 : Int64, e3 : Int64, e4 : Int64, e5 : Int64, e6 : Int64, e7 : Int64) was skipped since it collides with above method
        # Method Create(e0 : UInt64, e1 : UInt64, e2 : UInt64, e3 : UInt64, e4 : UInt64, e5 : UInt64, e6 : UInt64, e7 : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, e0: float, e1: float, e2: float, e3: float, e4: float, e5: float, e6: float, e7: float, e8: float, e9: float, e10: float, e11: float, e12: float, e13: float, e14: float, e15: float) -> Vector512_1[float]:...
        # Method Create(e0 : Int32, e1 : Int32, e2 : Int32, e3 : Int32, e4 : Int32, e5 : Int32, e6 : Int32, e7 : Int32, e8 : Int32, e9 : Int32, e10 : Int32, e11 : Int32, e12 : Int32, e13 : Int32, e14 : Int32, e15 : Int32) was skipped since it collides with above method
        # Method Create(e0 : UInt32, e1 : UInt32, e2 : UInt32, e3 : UInt32, e4 : UInt32, e5 : UInt32, e6 : UInt32, e7 : UInt32, e8 : UInt32, e9 : UInt32, e10 : UInt32, e11 : UInt32, e12 : UInt32, e13 : UInt32, e14 : UInt32, e15 : UInt32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, e0: int, e1: int, e2: int, e3: int, e4: int, e5: int, e6: int, e7: int, e8: int, e9: int, e10: int, e11: int, e12: int, e13: int, e14: int, e15: int, e16: int, e17: int, e18: int, e19: int, e20: int, e21: int, e22: int, e23: int, e24: int, e25: int, e26: int, e27: int, e28: int, e29: int, e30: int, e31: int) -> Vector512_1[int]:...
        # Method Create(e0 : UInt16, e1 : UInt16, e2 : UInt16, e3 : UInt16, e4 : UInt16, e5 : UInt16, e6 : UInt16, e7 : UInt16, e8 : UInt16, e9 : UInt16, e10 : UInt16, e11 : UInt16, e12 : UInt16, e13 : UInt16, e14 : UInt16, e15 : UInt16, e16 : UInt16, e17 : UInt16, e18 : UInt16, e19 : UInt16, e20 : UInt16, e21 : UInt16, e22 : UInt16, e23 : UInt16, e24 : UInt16, e25 : UInt16, e26 : UInt16, e27 : UInt16, e28 : UInt16, e29 : UInt16, e30 : UInt16, e31 : UInt16) was skipped since it collides with above method
        @typing.overload
        def __call__(self, e0: int, e1: int, e2: int, e3: int, e4: int, e5: int, e6: int, e7: int, e8: int, e9: int, e10: int, e11: int, e12: int, e13: int, e14: int, e15: int, e16: int, e17: int, e18: int, e19: int, e20: int, e21: int, e22: int, e23: int, e24: int, e25: int, e26: int, e27: int, e28: int, e29: int, e30: int, e31: int, e32: int, e33: int, e34: int, e35: int, e36: int, e37: int, e38: int, e39: int, e40: int, e41: int, e42: int, e43: int, e44: int, e45: int, e46: int, e47: int, e48: int, e49: int, e50: int, e51: int, e52: int, e53: int, e54: int, e55: int, e56: int, e57: int, e58: int, e59: int, e60: int, e61: int, e62: int, e63: int) -> Vector512_1[int]:...
        # Method Create(e0 : SByte, e1 : SByte, e2 : SByte, e3 : SByte, e4 : SByte, e5 : SByte, e6 : SByte, e7 : SByte, e8 : SByte, e9 : SByte, e10 : SByte, e11 : SByte, e12 : SByte, e13 : SByte, e14 : SByte, e15 : SByte, e16 : SByte, e17 : SByte, e18 : SByte, e19 : SByte, e20 : SByte, e21 : SByte, e22 : SByte, e23 : SByte, e24 : SByte, e25 : SByte, e26 : SByte, e27 : SByte, e28 : SByte, e29 : SByte, e30 : SByte, e31 : SByte, e32 : SByte, e33 : SByte, e34 : SByte, e35 : SByte, e36 : SByte, e37 : SByte, e38 : SByte, e39 : SByte, e40 : SByte, e41 : SByte, e42 : SByte, e43 : SByte, e44 : SByte, e45 : SByte, e46 : SByte, e47 : SByte, e48 : SByte, e49 : SByte, e50 : SByte, e51 : SByte, e52 : SByte, e53 : SByte, e54 : SByte, e55 : SByte, e56 : SByte, e57 : SByte, e58 : SByte, e59 : SByte, e60 : SByte, e61 : SByte, e62 : SByte, e63 : SByte) was skipped since it collides with above method

    # Skipped CreateScalar due to it being static, abstract and generic.

    CreateScalar : CreateScalar_MethodGroup
    class CreateScalar_MethodGroup:
        def __getitem__(self, t:typing.Type[CreateScalar_1_T1]) -> CreateScalar_1[CreateScalar_1_T1]: ...

        CreateScalar_1_T1 = typing.TypeVar('CreateScalar_1_T1')
        class CreateScalar_1(typing.Generic[CreateScalar_1_T1]):
            CreateScalar_1_T = Vector512_0.CreateScalar_MethodGroup.CreateScalar_1_T1
            def __call__(self, value: typing.Optional[CreateScalar_1_T]) -> Vector512_1[CreateScalar_1_T]:...

        @typing.overload
        def __call__(self, value: float) -> Vector512_1[float]:...
        # Method CreateScalar(value : Single) was skipped since it collides with above method
        # Method CreateScalar(value : Byte) was skipped since it collides with above method
        # Method CreateScalar(value : Int16) was skipped since it collides with above method
        # Method CreateScalar(value : Int32) was skipped since it collides with above method
        # Method CreateScalar(value : Int64) was skipped since it collides with above method
        # Method CreateScalar(value : SByte) was skipped since it collides with above method
        # Method CreateScalar(value : UInt16) was skipped since it collides with above method
        # Method CreateScalar(value : UInt32) was skipped since it collides with above method
        # Method CreateScalar(value : UInt64) was skipped since it collides with above method
        # Method CreateScalar(value : IntPtr) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> Vector512_1[UIntPtr]:...

    # Skipped CreateScalarUnsafe due to it being static, abstract and generic.

    CreateScalarUnsafe : CreateScalarUnsafe_MethodGroup
    class CreateScalarUnsafe_MethodGroup:
        def __getitem__(self, t:typing.Type[CreateScalarUnsafe_1_T1]) -> CreateScalarUnsafe_1[CreateScalarUnsafe_1_T1]: ...

        CreateScalarUnsafe_1_T1 = typing.TypeVar('CreateScalarUnsafe_1_T1')
        class CreateScalarUnsafe_1(typing.Generic[CreateScalarUnsafe_1_T1]):
            CreateScalarUnsafe_1_T = Vector512_0.CreateScalarUnsafe_MethodGroup.CreateScalarUnsafe_1_T1
            def __call__(self, value: typing.Optional[CreateScalarUnsafe_1_T]) -> Vector512_1[CreateScalarUnsafe_1_T]:...

        @typing.overload
        def __call__(self, value: float) -> Vector512_1[float]:...
        # Method CreateScalarUnsafe(value : Single) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : Byte) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : Int16) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : Int32) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : Int64) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : SByte) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : UInt16) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : UInt32) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : UInt64) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : IntPtr) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> Vector512_1[UIntPtr]:...

    # Skipped Divide due to it being static, abstract and generic.

    Divide : Divide_MethodGroup
    class Divide_MethodGroup:
        def __getitem__(self, t:typing.Type[Divide_1_T1]) -> Divide_1[Divide_1_T1]: ...

        Divide_1_T1 = typing.TypeVar('Divide_1_T1')
        class Divide_1(typing.Generic[Divide_1_T1]):
            Divide_1_T = Vector512_0.Divide_MethodGroup.Divide_1_T1
            @typing.overload
            def __call__(self, left: Vector512_1[Divide_1_T], right: Vector512_1[Divide_1_T]) -> Vector512_1[Divide_1_T]:...
            @typing.overload
            def __call__(self, left: Vector512_1[Divide_1_T], right: typing.Optional[Divide_1_T]) -> Vector512_1[Divide_1_T]:...


    # Skipped Dot due to it being static, abstract and generic.

    Dot : Dot_MethodGroup
    class Dot_MethodGroup:
        def __getitem__(self, t:typing.Type[Dot_1_T1]) -> Dot_1[Dot_1_T1]: ...

        Dot_1_T1 = typing.TypeVar('Dot_1_T1')
        class Dot_1(typing.Generic[Dot_1_T1]):
            Dot_1_T = Vector512_0.Dot_MethodGroup.Dot_1_T1
            def __call__(self, left: Vector512_1[Dot_1_T], right: Vector512_1[Dot_1_T]) -> Dot_1_T:...


    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        def __getitem__(self, t:typing.Type[Equals_1_T1]) -> Equals_1[Equals_1_T1]: ...

        Equals_1_T1 = typing.TypeVar('Equals_1_T1')
        class Equals_1(typing.Generic[Equals_1_T1]):
            Equals_1_T = Vector512_0.Equals_MethodGroup.Equals_1_T1
            def __call__(self, left: Vector512_1[Equals_1_T], right: Vector512_1[Equals_1_T]) -> Vector512_1[Equals_1_T]:...


    # Skipped EqualsAll due to it being static, abstract and generic.

    EqualsAll : EqualsAll_MethodGroup
    class EqualsAll_MethodGroup:
        def __getitem__(self, t:typing.Type[EqualsAll_1_T1]) -> EqualsAll_1[EqualsAll_1_T1]: ...

        EqualsAll_1_T1 = typing.TypeVar('EqualsAll_1_T1')
        class EqualsAll_1(typing.Generic[EqualsAll_1_T1]):
            EqualsAll_1_T = Vector512_0.EqualsAll_MethodGroup.EqualsAll_1_T1
            def __call__(self, left: Vector512_1[EqualsAll_1_T], right: Vector512_1[EqualsAll_1_T]) -> bool:...


    # Skipped EqualsAny due to it being static, abstract and generic.

    EqualsAny : EqualsAny_MethodGroup
    class EqualsAny_MethodGroup:
        def __getitem__(self, t:typing.Type[EqualsAny_1_T1]) -> EqualsAny_1[EqualsAny_1_T1]: ...

        EqualsAny_1_T1 = typing.TypeVar('EqualsAny_1_T1')
        class EqualsAny_1(typing.Generic[EqualsAny_1_T1]):
            EqualsAny_1_T = Vector512_0.EqualsAny_MethodGroup.EqualsAny_1_T1
            def __call__(self, left: Vector512_1[EqualsAny_1_T], right: Vector512_1[EqualsAny_1_T]) -> bool:...


    # Skipped ExtractMostSignificantBits due to it being static, abstract and generic.

    ExtractMostSignificantBits : ExtractMostSignificantBits_MethodGroup
    class ExtractMostSignificantBits_MethodGroup:
        def __getitem__(self, t:typing.Type[ExtractMostSignificantBits_1_T1]) -> ExtractMostSignificantBits_1[ExtractMostSignificantBits_1_T1]: ...

        ExtractMostSignificantBits_1_T1 = typing.TypeVar('ExtractMostSignificantBits_1_T1')
        class ExtractMostSignificantBits_1(typing.Generic[ExtractMostSignificantBits_1_T1]):
            ExtractMostSignificantBits_1_T = Vector512_0.ExtractMostSignificantBits_MethodGroup.ExtractMostSignificantBits_1_T1
            def __call__(self, vector: Vector512_1[ExtractMostSignificantBits_1_T]) -> int:...


    # Skipped Floor due to it being static, abstract and generic.

    Floor : Floor_MethodGroup
    class Floor_MethodGroup:
        def __call__(self, vector: Vector512_1[float]) -> Vector512_1[float]:...
        # Method Floor(vector : Vector512`1) was skipped since it collides with above method

    # Skipped GetElement due to it being static, abstract and generic.

    GetElement : GetElement_MethodGroup
    class GetElement_MethodGroup:
        def __getitem__(self, t:typing.Type[GetElement_1_T1]) -> GetElement_1[GetElement_1_T1]: ...

        GetElement_1_T1 = typing.TypeVar('GetElement_1_T1')
        class GetElement_1(typing.Generic[GetElement_1_T1]):
            GetElement_1_T = Vector512_0.GetElement_MethodGroup.GetElement_1_T1
            def __call__(self, vector: Vector512_1[GetElement_1_T], index: int) -> GetElement_1_T:...


    # Skipped GetLower due to it being static, abstract and generic.

    GetLower : GetLower_MethodGroup
    class GetLower_MethodGroup:
        def __getitem__(self, t:typing.Type[GetLower_1_T1]) -> GetLower_1[GetLower_1_T1]: ...

        GetLower_1_T1 = typing.TypeVar('GetLower_1_T1')
        class GetLower_1(typing.Generic[GetLower_1_T1]):
            GetLower_1_T = Vector512_0.GetLower_MethodGroup.GetLower_1_T1
            def __call__(self, vector: Vector512_1[GetLower_1_T]) -> Vector256_1[GetLower_1_T]:...


    # Skipped GetUpper due to it being static, abstract and generic.

    GetUpper : GetUpper_MethodGroup
    class GetUpper_MethodGroup:
        def __getitem__(self, t:typing.Type[GetUpper_1_T1]) -> GetUpper_1[GetUpper_1_T1]: ...

        GetUpper_1_T1 = typing.TypeVar('GetUpper_1_T1')
        class GetUpper_1(typing.Generic[GetUpper_1_T1]):
            GetUpper_1_T = Vector512_0.GetUpper_MethodGroup.GetUpper_1_T1
            def __call__(self, vector: Vector512_1[GetUpper_1_T]) -> Vector256_1[GetUpper_1_T]:...


    # Skipped GreaterThan due to it being static, abstract and generic.

    GreaterThan : GreaterThan_MethodGroup
    class GreaterThan_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThan_1_T1]) -> GreaterThan_1[GreaterThan_1_T1]: ...

        GreaterThan_1_T1 = typing.TypeVar('GreaterThan_1_T1')
        class GreaterThan_1(typing.Generic[GreaterThan_1_T1]):
            GreaterThan_1_T = Vector512_0.GreaterThan_MethodGroup.GreaterThan_1_T1
            def __call__(self, left: Vector512_1[GreaterThan_1_T], right: Vector512_1[GreaterThan_1_T]) -> Vector512_1[GreaterThan_1_T]:...


    # Skipped GreaterThanAll due to it being static, abstract and generic.

    GreaterThanAll : GreaterThanAll_MethodGroup
    class GreaterThanAll_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanAll_1_T1]) -> GreaterThanAll_1[GreaterThanAll_1_T1]: ...

        GreaterThanAll_1_T1 = typing.TypeVar('GreaterThanAll_1_T1')
        class GreaterThanAll_1(typing.Generic[GreaterThanAll_1_T1]):
            GreaterThanAll_1_T = Vector512_0.GreaterThanAll_MethodGroup.GreaterThanAll_1_T1
            def __call__(self, left: Vector512_1[GreaterThanAll_1_T], right: Vector512_1[GreaterThanAll_1_T]) -> bool:...


    # Skipped GreaterThanAny due to it being static, abstract and generic.

    GreaterThanAny : GreaterThanAny_MethodGroup
    class GreaterThanAny_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanAny_1_T1]) -> GreaterThanAny_1[GreaterThanAny_1_T1]: ...

        GreaterThanAny_1_T1 = typing.TypeVar('GreaterThanAny_1_T1')
        class GreaterThanAny_1(typing.Generic[GreaterThanAny_1_T1]):
            GreaterThanAny_1_T = Vector512_0.GreaterThanAny_MethodGroup.GreaterThanAny_1_T1
            def __call__(self, left: Vector512_1[GreaterThanAny_1_T], right: Vector512_1[GreaterThanAny_1_T]) -> bool:...


    # Skipped GreaterThanOrEqual due to it being static, abstract and generic.

    GreaterThanOrEqual : GreaterThanOrEqual_MethodGroup
    class GreaterThanOrEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanOrEqual_1_T1]) -> GreaterThanOrEqual_1[GreaterThanOrEqual_1_T1]: ...

        GreaterThanOrEqual_1_T1 = typing.TypeVar('GreaterThanOrEqual_1_T1')
        class GreaterThanOrEqual_1(typing.Generic[GreaterThanOrEqual_1_T1]):
            GreaterThanOrEqual_1_T = Vector512_0.GreaterThanOrEqual_MethodGroup.GreaterThanOrEqual_1_T1
            def __call__(self, left: Vector512_1[GreaterThanOrEqual_1_T], right: Vector512_1[GreaterThanOrEqual_1_T]) -> Vector512_1[GreaterThanOrEqual_1_T]:...


    # Skipped GreaterThanOrEqualAll due to it being static, abstract and generic.

    GreaterThanOrEqualAll : GreaterThanOrEqualAll_MethodGroup
    class GreaterThanOrEqualAll_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanOrEqualAll_1_T1]) -> GreaterThanOrEqualAll_1[GreaterThanOrEqualAll_1_T1]: ...

        GreaterThanOrEqualAll_1_T1 = typing.TypeVar('GreaterThanOrEqualAll_1_T1')
        class GreaterThanOrEqualAll_1(typing.Generic[GreaterThanOrEqualAll_1_T1]):
            GreaterThanOrEqualAll_1_T = Vector512_0.GreaterThanOrEqualAll_MethodGroup.GreaterThanOrEqualAll_1_T1
            def __call__(self, left: Vector512_1[GreaterThanOrEqualAll_1_T], right: Vector512_1[GreaterThanOrEqualAll_1_T]) -> bool:...


    # Skipped GreaterThanOrEqualAny due to it being static, abstract and generic.

    GreaterThanOrEqualAny : GreaterThanOrEqualAny_MethodGroup
    class GreaterThanOrEqualAny_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanOrEqualAny_1_T1]) -> GreaterThanOrEqualAny_1[GreaterThanOrEqualAny_1_T1]: ...

        GreaterThanOrEqualAny_1_T1 = typing.TypeVar('GreaterThanOrEqualAny_1_T1')
        class GreaterThanOrEqualAny_1(typing.Generic[GreaterThanOrEqualAny_1_T1]):
            GreaterThanOrEqualAny_1_T = Vector512_0.GreaterThanOrEqualAny_MethodGroup.GreaterThanOrEqualAny_1_T1
            def __call__(self, left: Vector512_1[GreaterThanOrEqualAny_1_T], right: Vector512_1[GreaterThanOrEqualAny_1_T]) -> bool:...


    # Skipped LessThan due to it being static, abstract and generic.

    LessThan : LessThan_MethodGroup
    class LessThan_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThan_1_T1]) -> LessThan_1[LessThan_1_T1]: ...

        LessThan_1_T1 = typing.TypeVar('LessThan_1_T1')
        class LessThan_1(typing.Generic[LessThan_1_T1]):
            LessThan_1_T = Vector512_0.LessThan_MethodGroup.LessThan_1_T1
            def __call__(self, left: Vector512_1[LessThan_1_T], right: Vector512_1[LessThan_1_T]) -> Vector512_1[LessThan_1_T]:...


    # Skipped LessThanAll due to it being static, abstract and generic.

    LessThanAll : LessThanAll_MethodGroup
    class LessThanAll_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanAll_1_T1]) -> LessThanAll_1[LessThanAll_1_T1]: ...

        LessThanAll_1_T1 = typing.TypeVar('LessThanAll_1_T1')
        class LessThanAll_1(typing.Generic[LessThanAll_1_T1]):
            LessThanAll_1_T = Vector512_0.LessThanAll_MethodGroup.LessThanAll_1_T1
            def __call__(self, left: Vector512_1[LessThanAll_1_T], right: Vector512_1[LessThanAll_1_T]) -> bool:...


    # Skipped LessThanAny due to it being static, abstract and generic.

    LessThanAny : LessThanAny_MethodGroup
    class LessThanAny_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanAny_1_T1]) -> LessThanAny_1[LessThanAny_1_T1]: ...

        LessThanAny_1_T1 = typing.TypeVar('LessThanAny_1_T1')
        class LessThanAny_1(typing.Generic[LessThanAny_1_T1]):
            LessThanAny_1_T = Vector512_0.LessThanAny_MethodGroup.LessThanAny_1_T1
            def __call__(self, left: Vector512_1[LessThanAny_1_T], right: Vector512_1[LessThanAny_1_T]) -> bool:...


    # Skipped LessThanOrEqual due to it being static, abstract and generic.

    LessThanOrEqual : LessThanOrEqual_MethodGroup
    class LessThanOrEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanOrEqual_1_T1]) -> LessThanOrEqual_1[LessThanOrEqual_1_T1]: ...

        LessThanOrEqual_1_T1 = typing.TypeVar('LessThanOrEqual_1_T1')
        class LessThanOrEqual_1(typing.Generic[LessThanOrEqual_1_T1]):
            LessThanOrEqual_1_T = Vector512_0.LessThanOrEqual_MethodGroup.LessThanOrEqual_1_T1
            def __call__(self, left: Vector512_1[LessThanOrEqual_1_T], right: Vector512_1[LessThanOrEqual_1_T]) -> Vector512_1[LessThanOrEqual_1_T]:...


    # Skipped LessThanOrEqualAll due to it being static, abstract and generic.

    LessThanOrEqualAll : LessThanOrEqualAll_MethodGroup
    class LessThanOrEqualAll_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanOrEqualAll_1_T1]) -> LessThanOrEqualAll_1[LessThanOrEqualAll_1_T1]: ...

        LessThanOrEqualAll_1_T1 = typing.TypeVar('LessThanOrEqualAll_1_T1')
        class LessThanOrEqualAll_1(typing.Generic[LessThanOrEqualAll_1_T1]):
            LessThanOrEqualAll_1_T = Vector512_0.LessThanOrEqualAll_MethodGroup.LessThanOrEqualAll_1_T1
            def __call__(self, left: Vector512_1[LessThanOrEqualAll_1_T], right: Vector512_1[LessThanOrEqualAll_1_T]) -> bool:...


    # Skipped LessThanOrEqualAny due to it being static, abstract and generic.

    LessThanOrEqualAny : LessThanOrEqualAny_MethodGroup
    class LessThanOrEqualAny_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanOrEqualAny_1_T1]) -> LessThanOrEqualAny_1[LessThanOrEqualAny_1_T1]: ...

        LessThanOrEqualAny_1_T1 = typing.TypeVar('LessThanOrEqualAny_1_T1')
        class LessThanOrEqualAny_1(typing.Generic[LessThanOrEqualAny_1_T1]):
            LessThanOrEqualAny_1_T = Vector512_0.LessThanOrEqualAny_MethodGroup.LessThanOrEqualAny_1_T1
            def __call__(self, left: Vector512_1[LessThanOrEqualAny_1_T], right: Vector512_1[LessThanOrEqualAny_1_T]) -> bool:...


    # Skipped Load due to it being static, abstract and generic.

    Load : Load_MethodGroup
    class Load_MethodGroup:
        def __getitem__(self, t:typing.Type[Load_1_T1]) -> Load_1[Load_1_T1]: ...

        Load_1_T1 = typing.TypeVar('Load_1_T1')
        class Load_1(typing.Generic[Load_1_T1]):
            Load_1_T = Vector512_0.Load_MethodGroup.Load_1_T1
            def __call__(self, source: clr.Reference[Load_1_T]) -> Vector512_1[Load_1_T]:...


    # Skipped LoadAligned due to it being static, abstract and generic.

    LoadAligned : LoadAligned_MethodGroup
    class LoadAligned_MethodGroup:
        def __getitem__(self, t:typing.Type[LoadAligned_1_T1]) -> LoadAligned_1[LoadAligned_1_T1]: ...

        LoadAligned_1_T1 = typing.TypeVar('LoadAligned_1_T1')
        class LoadAligned_1(typing.Generic[LoadAligned_1_T1]):
            LoadAligned_1_T = Vector512_0.LoadAligned_MethodGroup.LoadAligned_1_T1
            def __call__(self, source: clr.Reference[LoadAligned_1_T]) -> Vector512_1[LoadAligned_1_T]:...


    # Skipped LoadAlignedNonTemporal due to it being static, abstract and generic.

    LoadAlignedNonTemporal : LoadAlignedNonTemporal_MethodGroup
    class LoadAlignedNonTemporal_MethodGroup:
        def __getitem__(self, t:typing.Type[LoadAlignedNonTemporal_1_T1]) -> LoadAlignedNonTemporal_1[LoadAlignedNonTemporal_1_T1]: ...

        LoadAlignedNonTemporal_1_T1 = typing.TypeVar('LoadAlignedNonTemporal_1_T1')
        class LoadAlignedNonTemporal_1(typing.Generic[LoadAlignedNonTemporal_1_T1]):
            LoadAlignedNonTemporal_1_T = Vector512_0.LoadAlignedNonTemporal_MethodGroup.LoadAlignedNonTemporal_1_T1
            def __call__(self, source: clr.Reference[LoadAlignedNonTemporal_1_T]) -> Vector512_1[LoadAlignedNonTemporal_1_T]:...


    # Skipped LoadUnsafe due to it being static, abstract and generic.

    LoadUnsafe : LoadUnsafe_MethodGroup
    class LoadUnsafe_MethodGroup:
        def __getitem__(self, t:typing.Type[LoadUnsafe_1_T1]) -> LoadUnsafe_1[LoadUnsafe_1_T1]: ...

        LoadUnsafe_1_T1 = typing.TypeVar('LoadUnsafe_1_T1')
        class LoadUnsafe_1(typing.Generic[LoadUnsafe_1_T1]):
            LoadUnsafe_1_T = Vector512_0.LoadUnsafe_MethodGroup.LoadUnsafe_1_T1
            @typing.overload
            def __call__(self, source: typing.Optional[clr.Reference[LoadUnsafe_1_T]]) -> Vector512_1[LoadUnsafe_1_T]:...
            @typing.overload
            def __call__(self, source: typing.Optional[clr.Reference[LoadUnsafe_1_T]], elementOffset: UIntPtr) -> Vector512_1[LoadUnsafe_1_T]:...


    # Skipped Max due to it being static, abstract and generic.

    Max : Max_MethodGroup
    class Max_MethodGroup:
        def __getitem__(self, t:typing.Type[Max_1_T1]) -> Max_1[Max_1_T1]: ...

        Max_1_T1 = typing.TypeVar('Max_1_T1')
        class Max_1(typing.Generic[Max_1_T1]):
            Max_1_T = Vector512_0.Max_MethodGroup.Max_1_T1
            def __call__(self, left: Vector512_1[Max_1_T], right: Vector512_1[Max_1_T]) -> Vector512_1[Max_1_T]:...


    # Skipped Min due to it being static, abstract and generic.

    Min : Min_MethodGroup
    class Min_MethodGroup:
        def __getitem__(self, t:typing.Type[Min_1_T1]) -> Min_1[Min_1_T1]: ...

        Min_1_T1 = typing.TypeVar('Min_1_T1')
        class Min_1(typing.Generic[Min_1_T1]):
            Min_1_T = Vector512_0.Min_MethodGroup.Min_1_T1
            def __call__(self, left: Vector512_1[Min_1_T], right: Vector512_1[Min_1_T]) -> Vector512_1[Min_1_T]:...


    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        def __getitem__(self, t:typing.Type[Multiply_1_T1]) -> Multiply_1[Multiply_1_T1]: ...

        Multiply_1_T1 = typing.TypeVar('Multiply_1_T1')
        class Multiply_1(typing.Generic[Multiply_1_T1]):
            Multiply_1_T = Vector512_0.Multiply_MethodGroup.Multiply_1_T1
            @typing.overload
            def __call__(self, left: Vector512_1[Multiply_1_T], right: Vector512_1[Multiply_1_T]) -> Vector512_1[Multiply_1_T]:...
            @typing.overload
            def __call__(self, left: Vector512_1[Multiply_1_T], right: typing.Optional[Multiply_1_T]) -> Vector512_1[Multiply_1_T]:...
            @typing.overload
            def __call__(self, left: typing.Optional[Multiply_1_T], right: Vector512_1[Multiply_1_T]) -> Vector512_1[Multiply_1_T]:...


    # Skipped Narrow due to it being static, abstract and generic.

    Narrow : Narrow_MethodGroup
    class Narrow_MethodGroup:
        def __call__(self, lower: Vector512_1[float], upper: Vector512_1[float]) -> Vector512_1[float]:...
        # Method Narrow(lower : Vector512`1, upper : Vector512`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector512`1, upper : Vector512`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector512`1, upper : Vector512`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector512`1, upper : Vector512`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector512`1, upper : Vector512`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector512`1, upper : Vector512`1) was skipped since it collides with above method

    # Skipped Negate due to it being static, abstract and generic.

    Negate : Negate_MethodGroup
    class Negate_MethodGroup:
        def __getitem__(self, t:typing.Type[Negate_1_T1]) -> Negate_1[Negate_1_T1]: ...

        Negate_1_T1 = typing.TypeVar('Negate_1_T1')
        class Negate_1(typing.Generic[Negate_1_T1]):
            Negate_1_T = Vector512_0.Negate_MethodGroup.Negate_1_T1
            def __call__(self, vector: Vector512_1[Negate_1_T]) -> Vector512_1[Negate_1_T]:...


    # Skipped OnesComplement due to it being static, abstract and generic.

    OnesComplement : OnesComplement_MethodGroup
    class OnesComplement_MethodGroup:
        def __getitem__(self, t:typing.Type[OnesComplement_1_T1]) -> OnesComplement_1[OnesComplement_1_T1]: ...

        OnesComplement_1_T1 = typing.TypeVar('OnesComplement_1_T1')
        class OnesComplement_1(typing.Generic[OnesComplement_1_T1]):
            OnesComplement_1_T = Vector512_0.OnesComplement_MethodGroup.OnesComplement_1_T1
            def __call__(self, vector: Vector512_1[OnesComplement_1_T]) -> Vector512_1[OnesComplement_1_T]:...


    # Skipped ShiftLeft due to it being static, abstract and generic.

    ShiftLeft : ShiftLeft_MethodGroup
    class ShiftLeft_MethodGroup:
        @typing.overload
        def __call__(self, vector: Vector512_1[int], shiftCount: int) -> Vector512_1[int]:...
        # Method ShiftLeft(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, vector: Vector512_1[UIntPtr], shiftCount: int) -> Vector512_1[UIntPtr]:...

    # Skipped ShiftRightArithmetic due to it being static, abstract and generic.

    ShiftRightArithmetic : ShiftRightArithmetic_MethodGroup
    class ShiftRightArithmetic_MethodGroup:
        def __call__(self, vector: Vector512_1[int], shiftCount: int) -> Vector512_1[int]:...
        # Method ShiftRightArithmetic(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method

    # Skipped ShiftRightLogical due to it being static, abstract and generic.

    ShiftRightLogical : ShiftRightLogical_MethodGroup
    class ShiftRightLogical_MethodGroup:
        @typing.overload
        def __call__(self, vector: Vector512_1[int], shiftCount: int) -> Vector512_1[int]:...
        # Method ShiftRightLogical(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector512`1, shiftCount : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, vector: Vector512_1[UIntPtr], shiftCount: int) -> Vector512_1[UIntPtr]:...

    # Skipped Shuffle due to it being static, abstract and generic.

    Shuffle : Shuffle_MethodGroup
    class Shuffle_MethodGroup:
        def __call__(self, vector: Vector512_1[float], indices: Vector512_1[int]) -> Vector512_1[float]:...
        # Method Shuffle(vector : Vector512`1, indices : Vector512`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector512`1, indices : Vector512`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector512`1, indices : Vector512`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector512`1, indices : Vector512`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector512`1, indices : Vector512`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector512`1, indices : Vector512`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector512`1, indices : Vector512`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector512`1, indices : Vector512`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector512`1, indices : Vector512`1) was skipped since it collides with above method

    # Skipped Sqrt due to it being static, abstract and generic.

    Sqrt : Sqrt_MethodGroup
    class Sqrt_MethodGroup:
        def __getitem__(self, t:typing.Type[Sqrt_1_T1]) -> Sqrt_1[Sqrt_1_T1]: ...

        Sqrt_1_T1 = typing.TypeVar('Sqrt_1_T1')
        class Sqrt_1(typing.Generic[Sqrt_1_T1]):
            Sqrt_1_T = Vector512_0.Sqrt_MethodGroup.Sqrt_1_T1
            def __call__(self, vector: Vector512_1[Sqrt_1_T]) -> Vector512_1[Sqrt_1_T]:...


    # Skipped Store due to it being static, abstract and generic.

    Store : Store_MethodGroup
    class Store_MethodGroup:
        def __getitem__(self, t:typing.Type[Store_1_T1]) -> Store_1[Store_1_T1]: ...

        Store_1_T1 = typing.TypeVar('Store_1_T1')
        class Store_1(typing.Generic[Store_1_T1]):
            Store_1_T = Vector512_0.Store_MethodGroup.Store_1_T1
            def __call__(self, source: Vector512_1[Store_1_T], destination: clr.Reference[Store_1_T]) -> None:...


    # Skipped StoreAligned due to it being static, abstract and generic.

    StoreAligned : StoreAligned_MethodGroup
    class StoreAligned_MethodGroup:
        def __getitem__(self, t:typing.Type[StoreAligned_1_T1]) -> StoreAligned_1[StoreAligned_1_T1]: ...

        StoreAligned_1_T1 = typing.TypeVar('StoreAligned_1_T1')
        class StoreAligned_1(typing.Generic[StoreAligned_1_T1]):
            StoreAligned_1_T = Vector512_0.StoreAligned_MethodGroup.StoreAligned_1_T1
            def __call__(self, source: Vector512_1[StoreAligned_1_T], destination: clr.Reference[StoreAligned_1_T]) -> None:...


    # Skipped StoreAlignedNonTemporal due to it being static, abstract and generic.

    StoreAlignedNonTemporal : StoreAlignedNonTemporal_MethodGroup
    class StoreAlignedNonTemporal_MethodGroup:
        def __getitem__(self, t:typing.Type[StoreAlignedNonTemporal_1_T1]) -> StoreAlignedNonTemporal_1[StoreAlignedNonTemporal_1_T1]: ...

        StoreAlignedNonTemporal_1_T1 = typing.TypeVar('StoreAlignedNonTemporal_1_T1')
        class StoreAlignedNonTemporal_1(typing.Generic[StoreAlignedNonTemporal_1_T1]):
            StoreAlignedNonTemporal_1_T = Vector512_0.StoreAlignedNonTemporal_MethodGroup.StoreAlignedNonTemporal_1_T1
            def __call__(self, source: Vector512_1[StoreAlignedNonTemporal_1_T], destination: clr.Reference[StoreAlignedNonTemporal_1_T]) -> None:...


    # Skipped StoreUnsafe due to it being static, abstract and generic.

    StoreUnsafe : StoreUnsafe_MethodGroup
    class StoreUnsafe_MethodGroup:
        def __getitem__(self, t:typing.Type[StoreUnsafe_1_T1]) -> StoreUnsafe_1[StoreUnsafe_1_T1]: ...

        StoreUnsafe_1_T1 = typing.TypeVar('StoreUnsafe_1_T1')
        class StoreUnsafe_1(typing.Generic[StoreUnsafe_1_T1]):
            StoreUnsafe_1_T = Vector512_0.StoreUnsafe_MethodGroup.StoreUnsafe_1_T1
            @typing.overload
            def __call__(self, source: Vector512_1[StoreUnsafe_1_T], destination: typing.Optional[clr.Reference[StoreUnsafe_1_T]]) -> None:...
            @typing.overload
            def __call__(self, source: Vector512_1[StoreUnsafe_1_T], destination: typing.Optional[clr.Reference[StoreUnsafe_1_T]], elementOffset: UIntPtr) -> None:...


    # Skipped Subtract due to it being static, abstract and generic.

    Subtract : Subtract_MethodGroup
    class Subtract_MethodGroup:
        def __getitem__(self, t:typing.Type[Subtract_1_T1]) -> Subtract_1[Subtract_1_T1]: ...

        Subtract_1_T1 = typing.TypeVar('Subtract_1_T1')
        class Subtract_1(typing.Generic[Subtract_1_T1]):
            Subtract_1_T = Vector512_0.Subtract_MethodGroup.Subtract_1_T1
            def __call__(self, left: Vector512_1[Subtract_1_T], right: Vector512_1[Subtract_1_T]) -> Vector512_1[Subtract_1_T]:...


    # Skipped Sum due to it being static, abstract and generic.

    Sum : Sum_MethodGroup
    class Sum_MethodGroup:
        def __getitem__(self, t:typing.Type[Sum_1_T1]) -> Sum_1[Sum_1_T1]: ...

        Sum_1_T1 = typing.TypeVar('Sum_1_T1')
        class Sum_1(typing.Generic[Sum_1_T1]):
            Sum_1_T = Vector512_0.Sum_MethodGroup.Sum_1_T1
            def __call__(self, vector: Vector512_1[Sum_1_T]) -> Sum_1_T:...


    # Skipped ToScalar due to it being static, abstract and generic.

    ToScalar : ToScalar_MethodGroup
    class ToScalar_MethodGroup:
        def __getitem__(self, t:typing.Type[ToScalar_1_T1]) -> ToScalar_1[ToScalar_1_T1]: ...

        ToScalar_1_T1 = typing.TypeVar('ToScalar_1_T1')
        class ToScalar_1(typing.Generic[ToScalar_1_T1]):
            ToScalar_1_T = Vector512_0.ToScalar_MethodGroup.ToScalar_1_T1
            def __call__(self, vector: Vector512_1[ToScalar_1_T]) -> ToScalar_1_T:...


    # Skipped TryCopyTo due to it being static, abstract and generic.

    TryCopyTo : TryCopyTo_MethodGroup
    class TryCopyTo_MethodGroup:
        def __getitem__(self, t:typing.Type[TryCopyTo_1_T1]) -> TryCopyTo_1[TryCopyTo_1_T1]: ...

        TryCopyTo_1_T1 = typing.TypeVar('TryCopyTo_1_T1')
        class TryCopyTo_1(typing.Generic[TryCopyTo_1_T1]):
            TryCopyTo_1_T = Vector512_0.TryCopyTo_MethodGroup.TryCopyTo_1_T1
            def __call__(self, vector: Vector512_1[TryCopyTo_1_T], destination: Span_1[TryCopyTo_1_T]) -> bool:...


    # Skipped Widen due to it being static, abstract and generic.

    Widen : Widen_MethodGroup
    class Widen_MethodGroup:
        def __call__(self, source: Vector512_1[float]) -> ValueTuple_2[Vector512_1[float], Vector512_1[float]]:...
        # Method Widen(source : Vector512`1) was skipped since it collides with above method
        # Method Widen(source : Vector512`1) was skipped since it collides with above method
        # Method Widen(source : Vector512`1) was skipped since it collides with above method
        # Method Widen(source : Vector512`1) was skipped since it collides with above method
        # Method Widen(source : Vector512`1) was skipped since it collides with above method
        # Method Widen(source : Vector512`1) was skipped since it collides with above method

    # Skipped WidenLower due to it being static, abstract and generic.

    WidenLower : WidenLower_MethodGroup
    class WidenLower_MethodGroup:
        def __call__(self, source: Vector512_1[float]) -> Vector512_1[float]:...
        # Method WidenLower(source : Vector512`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector512`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector512`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector512`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector512`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector512`1) was skipped since it collides with above method

    # Skipped WidenUpper due to it being static, abstract and generic.

    WidenUpper : WidenUpper_MethodGroup
    class WidenUpper_MethodGroup:
        def __call__(self, source: Vector512_1[float]) -> Vector512_1[float]:...
        # Method WidenUpper(source : Vector512`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector512`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector512`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector512`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector512`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector512`1) was skipped since it collides with above method

    # Skipped WithElement due to it being static, abstract and generic.

    WithElement : WithElement_MethodGroup
    class WithElement_MethodGroup:
        def __getitem__(self, t:typing.Type[WithElement_1_T1]) -> WithElement_1[WithElement_1_T1]: ...

        WithElement_1_T1 = typing.TypeVar('WithElement_1_T1')
        class WithElement_1(typing.Generic[WithElement_1_T1]):
            WithElement_1_T = Vector512_0.WithElement_MethodGroup.WithElement_1_T1
            def __call__(self, vector: Vector512_1[WithElement_1_T], index: int, value: typing.Optional[WithElement_1_T]) -> Vector512_1[WithElement_1_T]:...


    # Skipped WithLower due to it being static, abstract and generic.

    WithLower : WithLower_MethodGroup
    class WithLower_MethodGroup:
        def __getitem__(self, t:typing.Type[WithLower_1_T1]) -> WithLower_1[WithLower_1_T1]: ...

        WithLower_1_T1 = typing.TypeVar('WithLower_1_T1')
        class WithLower_1(typing.Generic[WithLower_1_T1]):
            WithLower_1_T = Vector512_0.WithLower_MethodGroup.WithLower_1_T1
            def __call__(self, vector: Vector512_1[WithLower_1_T], value: Vector256_1[WithLower_1_T]) -> Vector512_1[WithLower_1_T]:...


    # Skipped WithUpper due to it being static, abstract and generic.

    WithUpper : WithUpper_MethodGroup
    class WithUpper_MethodGroup:
        def __getitem__(self, t:typing.Type[WithUpper_1_T1]) -> WithUpper_1[WithUpper_1_T1]: ...

        WithUpper_1_T1 = typing.TypeVar('WithUpper_1_T1')
        class WithUpper_1(typing.Generic[WithUpper_1_T1]):
            WithUpper_1_T = Vector512_0.WithUpper_MethodGroup.WithUpper_1_T1
            def __call__(self, vector: Vector512_1[WithUpper_1_T], value: Vector256_1[WithUpper_1_T]) -> Vector512_1[WithUpper_1_T]:...


    # Skipped Xor due to it being static, abstract and generic.

    Xor : Xor_MethodGroup
    class Xor_MethodGroup:
        def __getitem__(self, t:typing.Type[Xor_1_T1]) -> Xor_1[Xor_1_T1]: ...

        Xor_1_T1 = typing.TypeVar('Xor_1_T1')
        class Xor_1(typing.Generic[Xor_1_T1]):
            Xor_1_T = Vector512_0.Xor_MethodGroup.Xor_1_T1
            def __call__(self, left: Vector512_1[Xor_1_T], right: Vector512_1[Xor_1_T]) -> Vector512_1[Xor_1_T]:...




Vector512_1_T = typing.TypeVar('Vector512_1_T')
class Vector512_1(typing.Generic[Vector512_1_T], IEquatable_1[Vector512_1[Vector512_1_T]]):
    @classmethod
    @property
    def AllBitsSet(cls) -> Vector512_1[Vector512_1_T]: ...
    @classmethod
    @property
    def Count(cls) -> int: ...
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @property
    def Item(self) -> typing.Optional[Vector512_1_T]: ...
    @classmethod
    @property
    def One(cls) -> Vector512_1[Vector512_1_T]: ...
    @classmethod
    @property
    def Zero(cls) -> Vector512_1[Vector512_1_T]: ...
    def GetHashCode(self) -> int: ...
    def __add__(self, left: Vector512_1[Vector512_1_T], right: Vector512_1[Vector512_1_T]) -> Vector512_1[Vector512_1_T]: ...
    def __and__(self, left: Vector512_1[Vector512_1_T], right: Vector512_1[Vector512_1_T]) -> Vector512_1[Vector512_1_T]: ...
    def __or__(self, left: Vector512_1[Vector512_1_T], right: Vector512_1[Vector512_1_T]) -> Vector512_1[Vector512_1_T]: ...
    @typing.overload
    def __truediv__(self, left: Vector512_1[Vector512_1_T], right: Vector512_1[Vector512_1_T]) -> Vector512_1[Vector512_1_T]: ...
    @typing.overload
    def __truediv__(self, left: Vector512_1[Vector512_1_T], right: typing.Optional[Vector512_1_T]) -> Vector512_1[Vector512_1_T]: ...
    def __eq__(self, left: Vector512_1[Vector512_1_T], right: Vector512_1[Vector512_1_T]) -> bool: ...
    def __xor__(self, left: Vector512_1[Vector512_1_T], right: Vector512_1[Vector512_1_T]) -> Vector512_1[Vector512_1_T]: ...
    def __ne__(self, left: Vector512_1[Vector512_1_T], right: Vector512_1[Vector512_1_T]) -> bool: ...
    def __lshift__(self, value: Vector512_1[Vector512_1_T], shiftCount: int) -> Vector512_1[Vector512_1_T]: ...
    @typing.overload
    def __mul__(self, left: Vector512_1[Vector512_1_T], right: Vector512_1[Vector512_1_T]) -> Vector512_1[Vector512_1_T]: ...
    @typing.overload
    def __mul__(self, left: Vector512_1[Vector512_1_T], right: typing.Optional[Vector512_1_T]) -> Vector512_1[Vector512_1_T]: ...
    @typing.overload
    def __mul__(self, left: typing.Optional[Vector512_1_T], right: Vector512_1[Vector512_1_T]) -> Vector512_1[Vector512_1_T]: ...
    def __invert__(self, vector: Vector512_1[Vector512_1_T]) -> Vector512_1[Vector512_1_T]: ...
    def __rshift__(self, value: Vector512_1[Vector512_1_T], shiftCount: int) -> Vector512_1[Vector512_1_T]: ...
    def __sub__(self, left: Vector512_1[Vector512_1_T], right: Vector512_1[Vector512_1_T]) -> Vector512_1[Vector512_1_T]: ...
    def __neg__(self, vector: Vector512_1[Vector512_1_T]) -> Vector512_1[Vector512_1_T]: ...
    def __pos__(self, value: Vector512_1[Vector512_1_T]) -> Vector512_1[Vector512_1_T]: ...
    # Operator not supported op_UnsignedRightShift(value: Vector512`1, shiftCount: Int32)
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[Vector512_1_T]
    Equals_MethodGroup_Vector512_1_T = typing.TypeVar('Equals_MethodGroup_Vector512_1_T')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_Vector512_1_T]):
        Equals_MethodGroup_Vector512_1_T = Vector512_1.Equals_MethodGroup_Vector512_1_T
        @typing.overload
        def __call__(self, other: Vector512_1[Equals_MethodGroup_Vector512_1_T]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Optional[typing.Any]) -> bool:...



class Vector64_GenericClasses(abc.ABCMeta):
    Generic_Vector64_GenericClasses_Vector64_1_T = typing.TypeVar('Generic_Vector64_GenericClasses_Vector64_1_T')
    def __getitem__(self, types : typing.Type[Generic_Vector64_GenericClasses_Vector64_1_T]) -> typing.Type[Vector64_1[Generic_Vector64_GenericClasses_Vector64_1_T]]: ...

class Vector64(Vector64_0, metaclass =Vector64_GenericClasses): ...

class Vector64_0(abc.ABC):
    @classmethod
    @property
    def IsHardwareAccelerated(cls) -> bool: ...
    @staticmethod
    def ConvertToInt32(vector: Vector64_1[float]) -> Vector64_1[int]: ...
    @staticmethod
    def ConvertToInt64(vector: Vector64_1[float]) -> Vector64_1[int]: ...
    @staticmethod
    def ConvertToUInt32(vector: Vector64_1[float]) -> Vector64_1[int]: ...
    @staticmethod
    def ConvertToUInt64(vector: Vector64_1[float]) -> Vector64_1[int]: ...
    # Skipped Abs due to it being static, abstract and generic.

    Abs : Abs_MethodGroup
    class Abs_MethodGroup:
        def __getitem__(self, t:typing.Type[Abs_1_T1]) -> Abs_1[Abs_1_T1]: ...

        Abs_1_T1 = typing.TypeVar('Abs_1_T1')
        class Abs_1(typing.Generic[Abs_1_T1]):
            Abs_1_T = Vector64_0.Abs_MethodGroup.Abs_1_T1
            def __call__(self, vector: Vector64_1[Abs_1_T]) -> Vector64_1[Abs_1_T]:...


    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        def __getitem__(self, t:typing.Type[Add_1_T1]) -> Add_1[Add_1_T1]: ...

        Add_1_T1 = typing.TypeVar('Add_1_T1')
        class Add_1(typing.Generic[Add_1_T1]):
            Add_1_T = Vector64_0.Add_MethodGroup.Add_1_T1
            def __call__(self, left: Vector64_1[Add_1_T], right: Vector64_1[Add_1_T]) -> Vector64_1[Add_1_T]:...


    # Skipped AndNot due to it being static, abstract and generic.

    AndNot : AndNot_MethodGroup
    class AndNot_MethodGroup:
        def __getitem__(self, t:typing.Type[AndNot_1_T1]) -> AndNot_1[AndNot_1_T1]: ...

        AndNot_1_T1 = typing.TypeVar('AndNot_1_T1')
        class AndNot_1(typing.Generic[AndNot_1_T1]):
            AndNot_1_T = Vector64_0.AndNot_MethodGroup.AndNot_1_T1
            def __call__(self, left: Vector64_1[AndNot_1_T], right: Vector64_1[AndNot_1_T]) -> Vector64_1[AndNot_1_T]:...


    # Skipped As due to it being static, abstract and generic.

    As : As_MethodGroup
    class As_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[As_2_T1], typing.Type[As_2_T2]]) -> As_2[As_2_T1, As_2_T2]: ...

        As_2_T1 = typing.TypeVar('As_2_T1')
        As_2_T2 = typing.TypeVar('As_2_T2')
        class As_2(typing.Generic[As_2_T1, As_2_T2]):
            As_2_TFrom = Vector64_0.As_MethodGroup.As_2_T1
            As_2_TTo = Vector64_0.As_MethodGroup.As_2_T2
            def __call__(self, vector: Vector64_1[As_2_TFrom]) -> Vector64_1[As_2_TTo]:...


    # Skipped AsByte due to it being static, abstract and generic.

    AsByte : AsByte_MethodGroup
    class AsByte_MethodGroup:
        def __getitem__(self, t:typing.Type[AsByte_1_T1]) -> AsByte_1[AsByte_1_T1]: ...

        AsByte_1_T1 = typing.TypeVar('AsByte_1_T1')
        class AsByte_1(typing.Generic[AsByte_1_T1]):
            AsByte_1_T = Vector64_0.AsByte_MethodGroup.AsByte_1_T1
            def __call__(self, vector: Vector64_1[AsByte_1_T]) -> Vector64_1[int]:...


    # Skipped AsDouble due to it being static, abstract and generic.

    AsDouble : AsDouble_MethodGroup
    class AsDouble_MethodGroup:
        def __getitem__(self, t:typing.Type[AsDouble_1_T1]) -> AsDouble_1[AsDouble_1_T1]: ...

        AsDouble_1_T1 = typing.TypeVar('AsDouble_1_T1')
        class AsDouble_1(typing.Generic[AsDouble_1_T1]):
            AsDouble_1_T = Vector64_0.AsDouble_MethodGroup.AsDouble_1_T1
            def __call__(self, vector: Vector64_1[AsDouble_1_T]) -> Vector64_1[float]:...


    # Skipped AsInt16 due to it being static, abstract and generic.

    AsInt16 : AsInt16_MethodGroup
    class AsInt16_MethodGroup:
        def __getitem__(self, t:typing.Type[AsInt16_1_T1]) -> AsInt16_1[AsInt16_1_T1]: ...

        AsInt16_1_T1 = typing.TypeVar('AsInt16_1_T1')
        class AsInt16_1(typing.Generic[AsInt16_1_T1]):
            AsInt16_1_T = Vector64_0.AsInt16_MethodGroup.AsInt16_1_T1
            def __call__(self, vector: Vector64_1[AsInt16_1_T]) -> Vector64_1[int]:...


    # Skipped AsInt32 due to it being static, abstract and generic.

    AsInt32 : AsInt32_MethodGroup
    class AsInt32_MethodGroup:
        def __getitem__(self, t:typing.Type[AsInt32_1_T1]) -> AsInt32_1[AsInt32_1_T1]: ...

        AsInt32_1_T1 = typing.TypeVar('AsInt32_1_T1')
        class AsInt32_1(typing.Generic[AsInt32_1_T1]):
            AsInt32_1_T = Vector64_0.AsInt32_MethodGroup.AsInt32_1_T1
            def __call__(self, vector: Vector64_1[AsInt32_1_T]) -> Vector64_1[int]:...


    # Skipped AsInt64 due to it being static, abstract and generic.

    AsInt64 : AsInt64_MethodGroup
    class AsInt64_MethodGroup:
        def __getitem__(self, t:typing.Type[AsInt64_1_T1]) -> AsInt64_1[AsInt64_1_T1]: ...

        AsInt64_1_T1 = typing.TypeVar('AsInt64_1_T1')
        class AsInt64_1(typing.Generic[AsInt64_1_T1]):
            AsInt64_1_T = Vector64_0.AsInt64_MethodGroup.AsInt64_1_T1
            def __call__(self, vector: Vector64_1[AsInt64_1_T]) -> Vector64_1[int]:...


    # Skipped AsNInt due to it being static, abstract and generic.

    AsNInt : AsNInt_MethodGroup
    class AsNInt_MethodGroup:
        def __getitem__(self, t:typing.Type[AsNInt_1_T1]) -> AsNInt_1[AsNInt_1_T1]: ...

        AsNInt_1_T1 = typing.TypeVar('AsNInt_1_T1')
        class AsNInt_1(typing.Generic[AsNInt_1_T1]):
            AsNInt_1_T = Vector64_0.AsNInt_MethodGroup.AsNInt_1_T1
            def __call__(self, vector: Vector64_1[AsNInt_1_T]) -> Vector64_1[int]:...


    # Skipped AsNUInt due to it being static, abstract and generic.

    AsNUInt : AsNUInt_MethodGroup
    class AsNUInt_MethodGroup:
        def __getitem__(self, t:typing.Type[AsNUInt_1_T1]) -> AsNUInt_1[AsNUInt_1_T1]: ...

        AsNUInt_1_T1 = typing.TypeVar('AsNUInt_1_T1')
        class AsNUInt_1(typing.Generic[AsNUInt_1_T1]):
            AsNUInt_1_T = Vector64_0.AsNUInt_MethodGroup.AsNUInt_1_T1
            def __call__(self, vector: Vector64_1[AsNUInt_1_T]) -> Vector64_1[UIntPtr]:...


    # Skipped AsSByte due to it being static, abstract and generic.

    AsSByte : AsSByte_MethodGroup
    class AsSByte_MethodGroup:
        def __getitem__(self, t:typing.Type[AsSByte_1_T1]) -> AsSByte_1[AsSByte_1_T1]: ...

        AsSByte_1_T1 = typing.TypeVar('AsSByte_1_T1')
        class AsSByte_1(typing.Generic[AsSByte_1_T1]):
            AsSByte_1_T = Vector64_0.AsSByte_MethodGroup.AsSByte_1_T1
            def __call__(self, vector: Vector64_1[AsSByte_1_T]) -> Vector64_1[int]:...


    # Skipped AsSingle due to it being static, abstract and generic.

    AsSingle : AsSingle_MethodGroup
    class AsSingle_MethodGroup:
        def __getitem__(self, t:typing.Type[AsSingle_1_T1]) -> AsSingle_1[AsSingle_1_T1]: ...

        AsSingle_1_T1 = typing.TypeVar('AsSingle_1_T1')
        class AsSingle_1(typing.Generic[AsSingle_1_T1]):
            AsSingle_1_T = Vector64_0.AsSingle_MethodGroup.AsSingle_1_T1
            def __call__(self, vector: Vector64_1[AsSingle_1_T]) -> Vector64_1[float]:...


    # Skipped AsUInt16 due to it being static, abstract and generic.

    AsUInt16 : AsUInt16_MethodGroup
    class AsUInt16_MethodGroup:
        def __getitem__(self, t:typing.Type[AsUInt16_1_T1]) -> AsUInt16_1[AsUInt16_1_T1]: ...

        AsUInt16_1_T1 = typing.TypeVar('AsUInt16_1_T1')
        class AsUInt16_1(typing.Generic[AsUInt16_1_T1]):
            AsUInt16_1_T = Vector64_0.AsUInt16_MethodGroup.AsUInt16_1_T1
            def __call__(self, vector: Vector64_1[AsUInt16_1_T]) -> Vector64_1[int]:...


    # Skipped AsUInt32 due to it being static, abstract and generic.

    AsUInt32 : AsUInt32_MethodGroup
    class AsUInt32_MethodGroup:
        def __getitem__(self, t:typing.Type[AsUInt32_1_T1]) -> AsUInt32_1[AsUInt32_1_T1]: ...

        AsUInt32_1_T1 = typing.TypeVar('AsUInt32_1_T1')
        class AsUInt32_1(typing.Generic[AsUInt32_1_T1]):
            AsUInt32_1_T = Vector64_0.AsUInt32_MethodGroup.AsUInt32_1_T1
            def __call__(self, vector: Vector64_1[AsUInt32_1_T]) -> Vector64_1[int]:...


    # Skipped AsUInt64 due to it being static, abstract and generic.

    AsUInt64 : AsUInt64_MethodGroup
    class AsUInt64_MethodGroup:
        def __getitem__(self, t:typing.Type[AsUInt64_1_T1]) -> AsUInt64_1[AsUInt64_1_T1]: ...

        AsUInt64_1_T1 = typing.TypeVar('AsUInt64_1_T1')
        class AsUInt64_1(typing.Generic[AsUInt64_1_T1]):
            AsUInt64_1_T = Vector64_0.AsUInt64_MethodGroup.AsUInt64_1_T1
            def __call__(self, vector: Vector64_1[AsUInt64_1_T]) -> Vector64_1[int]:...


    # Skipped BitwiseAnd due to it being static, abstract and generic.

    BitwiseAnd : BitwiseAnd_MethodGroup
    class BitwiseAnd_MethodGroup:
        def __getitem__(self, t:typing.Type[BitwiseAnd_1_T1]) -> BitwiseAnd_1[BitwiseAnd_1_T1]: ...

        BitwiseAnd_1_T1 = typing.TypeVar('BitwiseAnd_1_T1')
        class BitwiseAnd_1(typing.Generic[BitwiseAnd_1_T1]):
            BitwiseAnd_1_T = Vector64_0.BitwiseAnd_MethodGroup.BitwiseAnd_1_T1
            def __call__(self, left: Vector64_1[BitwiseAnd_1_T], right: Vector64_1[BitwiseAnd_1_T]) -> Vector64_1[BitwiseAnd_1_T]:...


    # Skipped BitwiseOr due to it being static, abstract and generic.

    BitwiseOr : BitwiseOr_MethodGroup
    class BitwiseOr_MethodGroup:
        def __getitem__(self, t:typing.Type[BitwiseOr_1_T1]) -> BitwiseOr_1[BitwiseOr_1_T1]: ...

        BitwiseOr_1_T1 = typing.TypeVar('BitwiseOr_1_T1')
        class BitwiseOr_1(typing.Generic[BitwiseOr_1_T1]):
            BitwiseOr_1_T = Vector64_0.BitwiseOr_MethodGroup.BitwiseOr_1_T1
            def __call__(self, left: Vector64_1[BitwiseOr_1_T], right: Vector64_1[BitwiseOr_1_T]) -> Vector64_1[BitwiseOr_1_T]:...


    # Skipped Ceiling due to it being static, abstract and generic.

    Ceiling : Ceiling_MethodGroup
    class Ceiling_MethodGroup:
        def __call__(self, vector: Vector64_1[float]) -> Vector64_1[float]:...
        # Method Ceiling(vector : Vector64`1) was skipped since it collides with above method

    # Skipped ConditionalSelect due to it being static, abstract and generic.

    ConditionalSelect : ConditionalSelect_MethodGroup
    class ConditionalSelect_MethodGroup:
        def __getitem__(self, t:typing.Type[ConditionalSelect_1_T1]) -> ConditionalSelect_1[ConditionalSelect_1_T1]: ...

        ConditionalSelect_1_T1 = typing.TypeVar('ConditionalSelect_1_T1')
        class ConditionalSelect_1(typing.Generic[ConditionalSelect_1_T1]):
            ConditionalSelect_1_T = Vector64_0.ConditionalSelect_MethodGroup.ConditionalSelect_1_T1
            def __call__(self, condition: Vector64_1[ConditionalSelect_1_T], left: Vector64_1[ConditionalSelect_1_T], right: Vector64_1[ConditionalSelect_1_T]) -> Vector64_1[ConditionalSelect_1_T]:...


    # Skipped ConvertToDouble due to it being static, abstract and generic.

    ConvertToDouble : ConvertToDouble_MethodGroup
    class ConvertToDouble_MethodGroup:
        def __call__(self, vector: Vector64_1[int]) -> Vector64_1[float]:...
        # Method ConvertToDouble(vector : Vector64`1) was skipped since it collides with above method

    # Skipped ConvertToSingle due to it being static, abstract and generic.

    ConvertToSingle : ConvertToSingle_MethodGroup
    class ConvertToSingle_MethodGroup:
        def __call__(self, vector: Vector64_1[int]) -> Vector64_1[float]:...
        # Method ConvertToSingle(vector : Vector64`1) was skipped since it collides with above method

    # Skipped CopyTo due to it being static, abstract and generic.

    CopyTo : CopyTo_MethodGroup
    class CopyTo_MethodGroup:
        def __getitem__(self, t:typing.Type[CopyTo_1_T1]) -> CopyTo_1[CopyTo_1_T1]: ...

        CopyTo_1_T1 = typing.TypeVar('CopyTo_1_T1')
        class CopyTo_1(typing.Generic[CopyTo_1_T1]):
            CopyTo_1_T = Vector64_0.CopyTo_MethodGroup.CopyTo_1_T1
            @typing.overload
            def __call__(self, vector: Vector64_1[CopyTo_1_T], destination: Array_1[CopyTo_1_T]) -> None:...
            @typing.overload
            def __call__(self, vector: Vector64_1[CopyTo_1_T], destination: Span_1[CopyTo_1_T]) -> None:...
            @typing.overload
            def __call__(self, vector: Vector64_1[CopyTo_1_T], destination: Array_1[CopyTo_1_T], startIndex: int) -> None:...


    # Skipped Create due to it being static, abstract and generic.

    Create : Create_MethodGroup
    class Create_MethodGroup:
        def __getitem__(self, t:typing.Type[Create_1_T1]) -> Create_1[Create_1_T1]: ...

        Create_1_T1 = typing.TypeVar('Create_1_T1')
        class Create_1(typing.Generic[Create_1_T1]):
            Create_1_T = Vector64_0.Create_MethodGroup.Create_1_T1
            @typing.overload
            def __call__(self, values: Array_1[Create_1_T]) -> Vector64_1[Create_1_T]:...
            @typing.overload
            def __call__(self, values: ReadOnlySpan_1[Create_1_T]) -> Vector64_1[Create_1_T]:...
            @typing.overload
            def __call__(self, value: typing.Optional[Create_1_T]) -> Vector64_1[Create_1_T]:...
            @typing.overload
            def __call__(self, values: Array_1[Create_1_T], index: int) -> Vector64_1[Create_1_T]:...

        @typing.overload
        def __call__(self, value: float) -> Vector64_1[float]:...
        # Method Create(value : Single) was skipped since it collides with above method
        # Method Create(value : Byte) was skipped since it collides with above method
        # Method Create(value : Int16) was skipped since it collides with above method
        # Method Create(value : Int32) was skipped since it collides with above method
        # Method Create(value : Int64) was skipped since it collides with above method
        # Method Create(value : SByte) was skipped since it collides with above method
        # Method Create(value : UInt16) was skipped since it collides with above method
        # Method Create(value : UInt32) was skipped since it collides with above method
        # Method Create(value : UInt64) was skipped since it collides with above method
        # Method Create(value : IntPtr) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> Vector64_1[UIntPtr]:...
        @typing.overload
        def __call__(self, e0: float, e1: float) -> Vector64_1[float]:...
        # Method Create(e0 : Int32, e1 : Int32) was skipped since it collides with above method
        # Method Create(e0 : UInt32, e1 : UInt32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, e0: int, e1: int, e2: int, e3: int) -> Vector64_1[int]:...
        # Method Create(e0 : UInt16, e1 : UInt16, e2 : UInt16, e3 : UInt16) was skipped since it collides with above method
        @typing.overload
        def __call__(self, e0: int, e1: int, e2: int, e3: int, e4: int, e5: int, e6: int, e7: int) -> Vector64_1[int]:...
        # Method Create(e0 : SByte, e1 : SByte, e2 : SByte, e3 : SByte, e4 : SByte, e5 : SByte, e6 : SByte, e7 : SByte) was skipped since it collides with above method

    # Skipped CreateScalar due to it being static, abstract and generic.

    CreateScalar : CreateScalar_MethodGroup
    class CreateScalar_MethodGroup:
        def __getitem__(self, t:typing.Type[CreateScalar_1_T1]) -> CreateScalar_1[CreateScalar_1_T1]: ...

        CreateScalar_1_T1 = typing.TypeVar('CreateScalar_1_T1')
        class CreateScalar_1(typing.Generic[CreateScalar_1_T1]):
            CreateScalar_1_T = Vector64_0.CreateScalar_MethodGroup.CreateScalar_1_T1
            def __call__(self, value: typing.Optional[CreateScalar_1_T]) -> Vector64_1[CreateScalar_1_T]:...

        @typing.overload
        def __call__(self, value: float) -> Vector64_1[float]:...
        # Method CreateScalar(value : Single) was skipped since it collides with above method
        # Method CreateScalar(value : Byte) was skipped since it collides with above method
        # Method CreateScalar(value : Int16) was skipped since it collides with above method
        # Method CreateScalar(value : Int32) was skipped since it collides with above method
        # Method CreateScalar(value : Int64) was skipped since it collides with above method
        # Method CreateScalar(value : SByte) was skipped since it collides with above method
        # Method CreateScalar(value : UInt16) was skipped since it collides with above method
        # Method CreateScalar(value : UInt32) was skipped since it collides with above method
        # Method CreateScalar(value : UInt64) was skipped since it collides with above method
        # Method CreateScalar(value : IntPtr) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> Vector64_1[UIntPtr]:...

    # Skipped CreateScalarUnsafe due to it being static, abstract and generic.

    CreateScalarUnsafe : CreateScalarUnsafe_MethodGroup
    class CreateScalarUnsafe_MethodGroup:
        def __getitem__(self, t:typing.Type[CreateScalarUnsafe_1_T1]) -> CreateScalarUnsafe_1[CreateScalarUnsafe_1_T1]: ...

        CreateScalarUnsafe_1_T1 = typing.TypeVar('CreateScalarUnsafe_1_T1')
        class CreateScalarUnsafe_1(typing.Generic[CreateScalarUnsafe_1_T1]):
            CreateScalarUnsafe_1_T = Vector64_0.CreateScalarUnsafe_MethodGroup.CreateScalarUnsafe_1_T1
            def __call__(self, value: typing.Optional[CreateScalarUnsafe_1_T]) -> Vector64_1[CreateScalarUnsafe_1_T]:...

        @typing.overload
        def __call__(self, value: float) -> Vector64_1[float]:...
        # Method CreateScalarUnsafe(value : Single) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : Byte) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : Int16) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : Int32) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : Int64) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : SByte) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : UInt16) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : UInt32) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : UInt64) was skipped since it collides with above method
        # Method CreateScalarUnsafe(value : IntPtr) was skipped since it collides with above method
        @typing.overload
        def __call__(self, value: UIntPtr) -> Vector64_1[UIntPtr]:...

    # Skipped Divide due to it being static, abstract and generic.

    Divide : Divide_MethodGroup
    class Divide_MethodGroup:
        def __getitem__(self, t:typing.Type[Divide_1_T1]) -> Divide_1[Divide_1_T1]: ...

        Divide_1_T1 = typing.TypeVar('Divide_1_T1')
        class Divide_1(typing.Generic[Divide_1_T1]):
            Divide_1_T = Vector64_0.Divide_MethodGroup.Divide_1_T1
            @typing.overload
            def __call__(self, left: Vector64_1[Divide_1_T], right: Vector64_1[Divide_1_T]) -> Vector64_1[Divide_1_T]:...
            @typing.overload
            def __call__(self, left: Vector64_1[Divide_1_T], right: typing.Optional[Divide_1_T]) -> Vector64_1[Divide_1_T]:...


    # Skipped Dot due to it being static, abstract and generic.

    Dot : Dot_MethodGroup
    class Dot_MethodGroup:
        def __getitem__(self, t:typing.Type[Dot_1_T1]) -> Dot_1[Dot_1_T1]: ...

        Dot_1_T1 = typing.TypeVar('Dot_1_T1')
        class Dot_1(typing.Generic[Dot_1_T1]):
            Dot_1_T = Vector64_0.Dot_MethodGroup.Dot_1_T1
            def __call__(self, left: Vector64_1[Dot_1_T], right: Vector64_1[Dot_1_T]) -> Dot_1_T:...


    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        def __getitem__(self, t:typing.Type[Equals_1_T1]) -> Equals_1[Equals_1_T1]: ...

        Equals_1_T1 = typing.TypeVar('Equals_1_T1')
        class Equals_1(typing.Generic[Equals_1_T1]):
            Equals_1_T = Vector64_0.Equals_MethodGroup.Equals_1_T1
            def __call__(self, left: Vector64_1[Equals_1_T], right: Vector64_1[Equals_1_T]) -> Vector64_1[Equals_1_T]:...


    # Skipped EqualsAll due to it being static, abstract and generic.

    EqualsAll : EqualsAll_MethodGroup
    class EqualsAll_MethodGroup:
        def __getitem__(self, t:typing.Type[EqualsAll_1_T1]) -> EqualsAll_1[EqualsAll_1_T1]: ...

        EqualsAll_1_T1 = typing.TypeVar('EqualsAll_1_T1')
        class EqualsAll_1(typing.Generic[EqualsAll_1_T1]):
            EqualsAll_1_T = Vector64_0.EqualsAll_MethodGroup.EqualsAll_1_T1
            def __call__(self, left: Vector64_1[EqualsAll_1_T], right: Vector64_1[EqualsAll_1_T]) -> bool:...


    # Skipped EqualsAny due to it being static, abstract and generic.

    EqualsAny : EqualsAny_MethodGroup
    class EqualsAny_MethodGroup:
        def __getitem__(self, t:typing.Type[EqualsAny_1_T1]) -> EqualsAny_1[EqualsAny_1_T1]: ...

        EqualsAny_1_T1 = typing.TypeVar('EqualsAny_1_T1')
        class EqualsAny_1(typing.Generic[EqualsAny_1_T1]):
            EqualsAny_1_T = Vector64_0.EqualsAny_MethodGroup.EqualsAny_1_T1
            def __call__(self, left: Vector64_1[EqualsAny_1_T], right: Vector64_1[EqualsAny_1_T]) -> bool:...


    # Skipped ExtractMostSignificantBits due to it being static, abstract and generic.

    ExtractMostSignificantBits : ExtractMostSignificantBits_MethodGroup
    class ExtractMostSignificantBits_MethodGroup:
        def __getitem__(self, t:typing.Type[ExtractMostSignificantBits_1_T1]) -> ExtractMostSignificantBits_1[ExtractMostSignificantBits_1_T1]: ...

        ExtractMostSignificantBits_1_T1 = typing.TypeVar('ExtractMostSignificantBits_1_T1')
        class ExtractMostSignificantBits_1(typing.Generic[ExtractMostSignificantBits_1_T1]):
            ExtractMostSignificantBits_1_T = Vector64_0.ExtractMostSignificantBits_MethodGroup.ExtractMostSignificantBits_1_T1
            def __call__(self, vector: Vector64_1[ExtractMostSignificantBits_1_T]) -> int:...


    # Skipped Floor due to it being static, abstract and generic.

    Floor : Floor_MethodGroup
    class Floor_MethodGroup:
        def __call__(self, vector: Vector64_1[float]) -> Vector64_1[float]:...
        # Method Floor(vector : Vector64`1) was skipped since it collides with above method

    # Skipped GetElement due to it being static, abstract and generic.

    GetElement : GetElement_MethodGroup
    class GetElement_MethodGroup:
        def __getitem__(self, t:typing.Type[GetElement_1_T1]) -> GetElement_1[GetElement_1_T1]: ...

        GetElement_1_T1 = typing.TypeVar('GetElement_1_T1')
        class GetElement_1(typing.Generic[GetElement_1_T1]):
            GetElement_1_T = Vector64_0.GetElement_MethodGroup.GetElement_1_T1
            def __call__(self, vector: Vector64_1[GetElement_1_T], index: int) -> GetElement_1_T:...


    # Skipped GreaterThan due to it being static, abstract and generic.

    GreaterThan : GreaterThan_MethodGroup
    class GreaterThan_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThan_1_T1]) -> GreaterThan_1[GreaterThan_1_T1]: ...

        GreaterThan_1_T1 = typing.TypeVar('GreaterThan_1_T1')
        class GreaterThan_1(typing.Generic[GreaterThan_1_T1]):
            GreaterThan_1_T = Vector64_0.GreaterThan_MethodGroup.GreaterThan_1_T1
            def __call__(self, left: Vector64_1[GreaterThan_1_T], right: Vector64_1[GreaterThan_1_T]) -> Vector64_1[GreaterThan_1_T]:...


    # Skipped GreaterThanAll due to it being static, abstract and generic.

    GreaterThanAll : GreaterThanAll_MethodGroup
    class GreaterThanAll_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanAll_1_T1]) -> GreaterThanAll_1[GreaterThanAll_1_T1]: ...

        GreaterThanAll_1_T1 = typing.TypeVar('GreaterThanAll_1_T1')
        class GreaterThanAll_1(typing.Generic[GreaterThanAll_1_T1]):
            GreaterThanAll_1_T = Vector64_0.GreaterThanAll_MethodGroup.GreaterThanAll_1_T1
            def __call__(self, left: Vector64_1[GreaterThanAll_1_T], right: Vector64_1[GreaterThanAll_1_T]) -> bool:...


    # Skipped GreaterThanAny due to it being static, abstract and generic.

    GreaterThanAny : GreaterThanAny_MethodGroup
    class GreaterThanAny_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanAny_1_T1]) -> GreaterThanAny_1[GreaterThanAny_1_T1]: ...

        GreaterThanAny_1_T1 = typing.TypeVar('GreaterThanAny_1_T1')
        class GreaterThanAny_1(typing.Generic[GreaterThanAny_1_T1]):
            GreaterThanAny_1_T = Vector64_0.GreaterThanAny_MethodGroup.GreaterThanAny_1_T1
            def __call__(self, left: Vector64_1[GreaterThanAny_1_T], right: Vector64_1[GreaterThanAny_1_T]) -> bool:...


    # Skipped GreaterThanOrEqual due to it being static, abstract and generic.

    GreaterThanOrEqual : GreaterThanOrEqual_MethodGroup
    class GreaterThanOrEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanOrEqual_1_T1]) -> GreaterThanOrEqual_1[GreaterThanOrEqual_1_T1]: ...

        GreaterThanOrEqual_1_T1 = typing.TypeVar('GreaterThanOrEqual_1_T1')
        class GreaterThanOrEqual_1(typing.Generic[GreaterThanOrEqual_1_T1]):
            GreaterThanOrEqual_1_T = Vector64_0.GreaterThanOrEqual_MethodGroup.GreaterThanOrEqual_1_T1
            def __call__(self, left: Vector64_1[GreaterThanOrEqual_1_T], right: Vector64_1[GreaterThanOrEqual_1_T]) -> Vector64_1[GreaterThanOrEqual_1_T]:...


    # Skipped GreaterThanOrEqualAll due to it being static, abstract and generic.

    GreaterThanOrEqualAll : GreaterThanOrEqualAll_MethodGroup
    class GreaterThanOrEqualAll_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanOrEqualAll_1_T1]) -> GreaterThanOrEqualAll_1[GreaterThanOrEqualAll_1_T1]: ...

        GreaterThanOrEqualAll_1_T1 = typing.TypeVar('GreaterThanOrEqualAll_1_T1')
        class GreaterThanOrEqualAll_1(typing.Generic[GreaterThanOrEqualAll_1_T1]):
            GreaterThanOrEqualAll_1_T = Vector64_0.GreaterThanOrEqualAll_MethodGroup.GreaterThanOrEqualAll_1_T1
            def __call__(self, left: Vector64_1[GreaterThanOrEqualAll_1_T], right: Vector64_1[GreaterThanOrEqualAll_1_T]) -> bool:...


    # Skipped GreaterThanOrEqualAny due to it being static, abstract and generic.

    GreaterThanOrEqualAny : GreaterThanOrEqualAny_MethodGroup
    class GreaterThanOrEqualAny_MethodGroup:
        def __getitem__(self, t:typing.Type[GreaterThanOrEqualAny_1_T1]) -> GreaterThanOrEqualAny_1[GreaterThanOrEqualAny_1_T1]: ...

        GreaterThanOrEqualAny_1_T1 = typing.TypeVar('GreaterThanOrEqualAny_1_T1')
        class GreaterThanOrEqualAny_1(typing.Generic[GreaterThanOrEqualAny_1_T1]):
            GreaterThanOrEqualAny_1_T = Vector64_0.GreaterThanOrEqualAny_MethodGroup.GreaterThanOrEqualAny_1_T1
            def __call__(self, left: Vector64_1[GreaterThanOrEqualAny_1_T], right: Vector64_1[GreaterThanOrEqualAny_1_T]) -> bool:...


    # Skipped LessThan due to it being static, abstract and generic.

    LessThan : LessThan_MethodGroup
    class LessThan_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThan_1_T1]) -> LessThan_1[LessThan_1_T1]: ...

        LessThan_1_T1 = typing.TypeVar('LessThan_1_T1')
        class LessThan_1(typing.Generic[LessThan_1_T1]):
            LessThan_1_T = Vector64_0.LessThan_MethodGroup.LessThan_1_T1
            def __call__(self, left: Vector64_1[LessThan_1_T], right: Vector64_1[LessThan_1_T]) -> Vector64_1[LessThan_1_T]:...


    # Skipped LessThanAll due to it being static, abstract and generic.

    LessThanAll : LessThanAll_MethodGroup
    class LessThanAll_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanAll_1_T1]) -> LessThanAll_1[LessThanAll_1_T1]: ...

        LessThanAll_1_T1 = typing.TypeVar('LessThanAll_1_T1')
        class LessThanAll_1(typing.Generic[LessThanAll_1_T1]):
            LessThanAll_1_T = Vector64_0.LessThanAll_MethodGroup.LessThanAll_1_T1
            def __call__(self, left: Vector64_1[LessThanAll_1_T], right: Vector64_1[LessThanAll_1_T]) -> bool:...


    # Skipped LessThanAny due to it being static, abstract and generic.

    LessThanAny : LessThanAny_MethodGroup
    class LessThanAny_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanAny_1_T1]) -> LessThanAny_1[LessThanAny_1_T1]: ...

        LessThanAny_1_T1 = typing.TypeVar('LessThanAny_1_T1')
        class LessThanAny_1(typing.Generic[LessThanAny_1_T1]):
            LessThanAny_1_T = Vector64_0.LessThanAny_MethodGroup.LessThanAny_1_T1
            def __call__(self, left: Vector64_1[LessThanAny_1_T], right: Vector64_1[LessThanAny_1_T]) -> bool:...


    # Skipped LessThanOrEqual due to it being static, abstract and generic.

    LessThanOrEqual : LessThanOrEqual_MethodGroup
    class LessThanOrEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanOrEqual_1_T1]) -> LessThanOrEqual_1[LessThanOrEqual_1_T1]: ...

        LessThanOrEqual_1_T1 = typing.TypeVar('LessThanOrEqual_1_T1')
        class LessThanOrEqual_1(typing.Generic[LessThanOrEqual_1_T1]):
            LessThanOrEqual_1_T = Vector64_0.LessThanOrEqual_MethodGroup.LessThanOrEqual_1_T1
            def __call__(self, left: Vector64_1[LessThanOrEqual_1_T], right: Vector64_1[LessThanOrEqual_1_T]) -> Vector64_1[LessThanOrEqual_1_T]:...


    # Skipped LessThanOrEqualAll due to it being static, abstract and generic.

    LessThanOrEqualAll : LessThanOrEqualAll_MethodGroup
    class LessThanOrEqualAll_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanOrEqualAll_1_T1]) -> LessThanOrEqualAll_1[LessThanOrEqualAll_1_T1]: ...

        LessThanOrEqualAll_1_T1 = typing.TypeVar('LessThanOrEqualAll_1_T1')
        class LessThanOrEqualAll_1(typing.Generic[LessThanOrEqualAll_1_T1]):
            LessThanOrEqualAll_1_T = Vector64_0.LessThanOrEqualAll_MethodGroup.LessThanOrEqualAll_1_T1
            def __call__(self, left: Vector64_1[LessThanOrEqualAll_1_T], right: Vector64_1[LessThanOrEqualAll_1_T]) -> bool:...


    # Skipped LessThanOrEqualAny due to it being static, abstract and generic.

    LessThanOrEqualAny : LessThanOrEqualAny_MethodGroup
    class LessThanOrEqualAny_MethodGroup:
        def __getitem__(self, t:typing.Type[LessThanOrEqualAny_1_T1]) -> LessThanOrEqualAny_1[LessThanOrEqualAny_1_T1]: ...

        LessThanOrEqualAny_1_T1 = typing.TypeVar('LessThanOrEqualAny_1_T1')
        class LessThanOrEqualAny_1(typing.Generic[LessThanOrEqualAny_1_T1]):
            LessThanOrEqualAny_1_T = Vector64_0.LessThanOrEqualAny_MethodGroup.LessThanOrEqualAny_1_T1
            def __call__(self, left: Vector64_1[LessThanOrEqualAny_1_T], right: Vector64_1[LessThanOrEqualAny_1_T]) -> bool:...


    # Skipped Load due to it being static, abstract and generic.

    Load : Load_MethodGroup
    class Load_MethodGroup:
        def __getitem__(self, t:typing.Type[Load_1_T1]) -> Load_1[Load_1_T1]: ...

        Load_1_T1 = typing.TypeVar('Load_1_T1')
        class Load_1(typing.Generic[Load_1_T1]):
            Load_1_T = Vector64_0.Load_MethodGroup.Load_1_T1
            def __call__(self, source: clr.Reference[Load_1_T]) -> Vector64_1[Load_1_T]:...


    # Skipped LoadAligned due to it being static, abstract and generic.

    LoadAligned : LoadAligned_MethodGroup
    class LoadAligned_MethodGroup:
        def __getitem__(self, t:typing.Type[LoadAligned_1_T1]) -> LoadAligned_1[LoadAligned_1_T1]: ...

        LoadAligned_1_T1 = typing.TypeVar('LoadAligned_1_T1')
        class LoadAligned_1(typing.Generic[LoadAligned_1_T1]):
            LoadAligned_1_T = Vector64_0.LoadAligned_MethodGroup.LoadAligned_1_T1
            def __call__(self, source: clr.Reference[LoadAligned_1_T]) -> Vector64_1[LoadAligned_1_T]:...


    # Skipped LoadAlignedNonTemporal due to it being static, abstract and generic.

    LoadAlignedNonTemporal : LoadAlignedNonTemporal_MethodGroup
    class LoadAlignedNonTemporal_MethodGroup:
        def __getitem__(self, t:typing.Type[LoadAlignedNonTemporal_1_T1]) -> LoadAlignedNonTemporal_1[LoadAlignedNonTemporal_1_T1]: ...

        LoadAlignedNonTemporal_1_T1 = typing.TypeVar('LoadAlignedNonTemporal_1_T1')
        class LoadAlignedNonTemporal_1(typing.Generic[LoadAlignedNonTemporal_1_T1]):
            LoadAlignedNonTemporal_1_T = Vector64_0.LoadAlignedNonTemporal_MethodGroup.LoadAlignedNonTemporal_1_T1
            def __call__(self, source: clr.Reference[LoadAlignedNonTemporal_1_T]) -> Vector64_1[LoadAlignedNonTemporal_1_T]:...


    # Skipped LoadUnsafe due to it being static, abstract and generic.

    LoadUnsafe : LoadUnsafe_MethodGroup
    class LoadUnsafe_MethodGroup:
        def __getitem__(self, t:typing.Type[LoadUnsafe_1_T1]) -> LoadUnsafe_1[LoadUnsafe_1_T1]: ...

        LoadUnsafe_1_T1 = typing.TypeVar('LoadUnsafe_1_T1')
        class LoadUnsafe_1(typing.Generic[LoadUnsafe_1_T1]):
            LoadUnsafe_1_T = Vector64_0.LoadUnsafe_MethodGroup.LoadUnsafe_1_T1
            @typing.overload
            def __call__(self, source: typing.Optional[clr.Reference[LoadUnsafe_1_T]]) -> Vector64_1[LoadUnsafe_1_T]:...
            @typing.overload
            def __call__(self, source: typing.Optional[clr.Reference[LoadUnsafe_1_T]], elementOffset: UIntPtr) -> Vector64_1[LoadUnsafe_1_T]:...


    # Skipped Max due to it being static, abstract and generic.

    Max : Max_MethodGroup
    class Max_MethodGroup:
        def __getitem__(self, t:typing.Type[Max_1_T1]) -> Max_1[Max_1_T1]: ...

        Max_1_T1 = typing.TypeVar('Max_1_T1')
        class Max_1(typing.Generic[Max_1_T1]):
            Max_1_T = Vector64_0.Max_MethodGroup.Max_1_T1
            def __call__(self, left: Vector64_1[Max_1_T], right: Vector64_1[Max_1_T]) -> Vector64_1[Max_1_T]:...


    # Skipped Min due to it being static, abstract and generic.

    Min : Min_MethodGroup
    class Min_MethodGroup:
        def __getitem__(self, t:typing.Type[Min_1_T1]) -> Min_1[Min_1_T1]: ...

        Min_1_T1 = typing.TypeVar('Min_1_T1')
        class Min_1(typing.Generic[Min_1_T1]):
            Min_1_T = Vector64_0.Min_MethodGroup.Min_1_T1
            def __call__(self, left: Vector64_1[Min_1_T], right: Vector64_1[Min_1_T]) -> Vector64_1[Min_1_T]:...


    # Skipped Multiply due to it being static, abstract and generic.

    Multiply : Multiply_MethodGroup
    class Multiply_MethodGroup:
        def __getitem__(self, t:typing.Type[Multiply_1_T1]) -> Multiply_1[Multiply_1_T1]: ...

        Multiply_1_T1 = typing.TypeVar('Multiply_1_T1')
        class Multiply_1(typing.Generic[Multiply_1_T1]):
            Multiply_1_T = Vector64_0.Multiply_MethodGroup.Multiply_1_T1
            @typing.overload
            def __call__(self, left: Vector64_1[Multiply_1_T], right: Vector64_1[Multiply_1_T]) -> Vector64_1[Multiply_1_T]:...
            @typing.overload
            def __call__(self, left: Vector64_1[Multiply_1_T], right: typing.Optional[Multiply_1_T]) -> Vector64_1[Multiply_1_T]:...
            @typing.overload
            def __call__(self, left: typing.Optional[Multiply_1_T], right: Vector64_1[Multiply_1_T]) -> Vector64_1[Multiply_1_T]:...


    # Skipped Narrow due to it being static, abstract and generic.

    Narrow : Narrow_MethodGroup
    class Narrow_MethodGroup:
        def __call__(self, lower: Vector64_1[float], upper: Vector64_1[float]) -> Vector64_1[float]:...
        # Method Narrow(lower : Vector64`1, upper : Vector64`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector64`1, upper : Vector64`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector64`1, upper : Vector64`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector64`1, upper : Vector64`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector64`1, upper : Vector64`1) was skipped since it collides with above method
        # Method Narrow(lower : Vector64`1, upper : Vector64`1) was skipped since it collides with above method

    # Skipped Negate due to it being static, abstract and generic.

    Negate : Negate_MethodGroup
    class Negate_MethodGroup:
        def __getitem__(self, t:typing.Type[Negate_1_T1]) -> Negate_1[Negate_1_T1]: ...

        Negate_1_T1 = typing.TypeVar('Negate_1_T1')
        class Negate_1(typing.Generic[Negate_1_T1]):
            Negate_1_T = Vector64_0.Negate_MethodGroup.Negate_1_T1
            def __call__(self, vector: Vector64_1[Negate_1_T]) -> Vector64_1[Negate_1_T]:...


    # Skipped OnesComplement due to it being static, abstract and generic.

    OnesComplement : OnesComplement_MethodGroup
    class OnesComplement_MethodGroup:
        def __getitem__(self, t:typing.Type[OnesComplement_1_T1]) -> OnesComplement_1[OnesComplement_1_T1]: ...

        OnesComplement_1_T1 = typing.TypeVar('OnesComplement_1_T1')
        class OnesComplement_1(typing.Generic[OnesComplement_1_T1]):
            OnesComplement_1_T = Vector64_0.OnesComplement_MethodGroup.OnesComplement_1_T1
            def __call__(self, vector: Vector64_1[OnesComplement_1_T]) -> Vector64_1[OnesComplement_1_T]:...


    # Skipped ShiftLeft due to it being static, abstract and generic.

    ShiftLeft : ShiftLeft_MethodGroup
    class ShiftLeft_MethodGroup:
        @typing.overload
        def __call__(self, vector: Vector64_1[int], shiftCount: int) -> Vector64_1[int]:...
        # Method ShiftLeft(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftLeft(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, vector: Vector64_1[UIntPtr], shiftCount: int) -> Vector64_1[UIntPtr]:...

    # Skipped ShiftRightArithmetic due to it being static, abstract and generic.

    ShiftRightArithmetic : ShiftRightArithmetic_MethodGroup
    class ShiftRightArithmetic_MethodGroup:
        def __call__(self, vector: Vector64_1[int], shiftCount: int) -> Vector64_1[int]:...
        # Method ShiftRightArithmetic(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightArithmetic(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method

    # Skipped ShiftRightLogical due to it being static, abstract and generic.

    ShiftRightLogical : ShiftRightLogical_MethodGroup
    class ShiftRightLogical_MethodGroup:
        @typing.overload
        def __call__(self, vector: Vector64_1[int], shiftCount: int) -> Vector64_1[int]:...
        # Method ShiftRightLogical(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        # Method ShiftRightLogical(vector : Vector64`1, shiftCount : Int32) was skipped since it collides with above method
        @typing.overload
        def __call__(self, vector: Vector64_1[UIntPtr], shiftCount: int) -> Vector64_1[UIntPtr]:...

    # Skipped Shuffle due to it being static, abstract and generic.

    Shuffle : Shuffle_MethodGroup
    class Shuffle_MethodGroup:
        def __call__(self, vector: Vector64_1[float], indices: Vector64_1[int]) -> Vector64_1[float]:...
        # Method Shuffle(vector : Vector64`1, indices : Vector64`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector64`1, indices : Vector64`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector64`1, indices : Vector64`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector64`1, indices : Vector64`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector64`1, indices : Vector64`1) was skipped since it collides with above method
        # Method Shuffle(vector : Vector64`1, indices : Vector64`1) was skipped since it collides with above method

    # Skipped Sqrt due to it being static, abstract and generic.

    Sqrt : Sqrt_MethodGroup
    class Sqrt_MethodGroup:
        def __getitem__(self, t:typing.Type[Sqrt_1_T1]) -> Sqrt_1[Sqrt_1_T1]: ...

        Sqrt_1_T1 = typing.TypeVar('Sqrt_1_T1')
        class Sqrt_1(typing.Generic[Sqrt_1_T1]):
            Sqrt_1_T = Vector64_0.Sqrt_MethodGroup.Sqrt_1_T1
            def __call__(self, vector: Vector64_1[Sqrt_1_T]) -> Vector64_1[Sqrt_1_T]:...


    # Skipped Store due to it being static, abstract and generic.

    Store : Store_MethodGroup
    class Store_MethodGroup:
        def __getitem__(self, t:typing.Type[Store_1_T1]) -> Store_1[Store_1_T1]: ...

        Store_1_T1 = typing.TypeVar('Store_1_T1')
        class Store_1(typing.Generic[Store_1_T1]):
            Store_1_T = Vector64_0.Store_MethodGroup.Store_1_T1
            def __call__(self, source: Vector64_1[Store_1_T], destination: clr.Reference[Store_1_T]) -> None:...


    # Skipped StoreAligned due to it being static, abstract and generic.

    StoreAligned : StoreAligned_MethodGroup
    class StoreAligned_MethodGroup:
        def __getitem__(self, t:typing.Type[StoreAligned_1_T1]) -> StoreAligned_1[StoreAligned_1_T1]: ...

        StoreAligned_1_T1 = typing.TypeVar('StoreAligned_1_T1')
        class StoreAligned_1(typing.Generic[StoreAligned_1_T1]):
            StoreAligned_1_T = Vector64_0.StoreAligned_MethodGroup.StoreAligned_1_T1
            def __call__(self, source: Vector64_1[StoreAligned_1_T], destination: clr.Reference[StoreAligned_1_T]) -> None:...


    # Skipped StoreAlignedNonTemporal due to it being static, abstract and generic.

    StoreAlignedNonTemporal : StoreAlignedNonTemporal_MethodGroup
    class StoreAlignedNonTemporal_MethodGroup:
        def __getitem__(self, t:typing.Type[StoreAlignedNonTemporal_1_T1]) -> StoreAlignedNonTemporal_1[StoreAlignedNonTemporal_1_T1]: ...

        StoreAlignedNonTemporal_1_T1 = typing.TypeVar('StoreAlignedNonTemporal_1_T1')
        class StoreAlignedNonTemporal_1(typing.Generic[StoreAlignedNonTemporal_1_T1]):
            StoreAlignedNonTemporal_1_T = Vector64_0.StoreAlignedNonTemporal_MethodGroup.StoreAlignedNonTemporal_1_T1
            def __call__(self, source: Vector64_1[StoreAlignedNonTemporal_1_T], destination: clr.Reference[StoreAlignedNonTemporal_1_T]) -> None:...


    # Skipped StoreUnsafe due to it being static, abstract and generic.

    StoreUnsafe : StoreUnsafe_MethodGroup
    class StoreUnsafe_MethodGroup:
        def __getitem__(self, t:typing.Type[StoreUnsafe_1_T1]) -> StoreUnsafe_1[StoreUnsafe_1_T1]: ...

        StoreUnsafe_1_T1 = typing.TypeVar('StoreUnsafe_1_T1')
        class StoreUnsafe_1(typing.Generic[StoreUnsafe_1_T1]):
            StoreUnsafe_1_T = Vector64_0.StoreUnsafe_MethodGroup.StoreUnsafe_1_T1
            @typing.overload
            def __call__(self, source: Vector64_1[StoreUnsafe_1_T], destination: typing.Optional[clr.Reference[StoreUnsafe_1_T]]) -> None:...
            @typing.overload
            def __call__(self, source: Vector64_1[StoreUnsafe_1_T], destination: typing.Optional[clr.Reference[StoreUnsafe_1_T]], elementOffset: UIntPtr) -> None:...


    # Skipped Subtract due to it being static, abstract and generic.

    Subtract : Subtract_MethodGroup
    class Subtract_MethodGroup:
        def __getitem__(self, t:typing.Type[Subtract_1_T1]) -> Subtract_1[Subtract_1_T1]: ...

        Subtract_1_T1 = typing.TypeVar('Subtract_1_T1')
        class Subtract_1(typing.Generic[Subtract_1_T1]):
            Subtract_1_T = Vector64_0.Subtract_MethodGroup.Subtract_1_T1
            def __call__(self, left: Vector64_1[Subtract_1_T], right: Vector64_1[Subtract_1_T]) -> Vector64_1[Subtract_1_T]:...


    # Skipped Sum due to it being static, abstract and generic.

    Sum : Sum_MethodGroup
    class Sum_MethodGroup:
        def __getitem__(self, t:typing.Type[Sum_1_T1]) -> Sum_1[Sum_1_T1]: ...

        Sum_1_T1 = typing.TypeVar('Sum_1_T1')
        class Sum_1(typing.Generic[Sum_1_T1]):
            Sum_1_T = Vector64_0.Sum_MethodGroup.Sum_1_T1
            def __call__(self, vector: Vector64_1[Sum_1_T]) -> Sum_1_T:...


    # Skipped ToScalar due to it being static, abstract and generic.

    ToScalar : ToScalar_MethodGroup
    class ToScalar_MethodGroup:
        def __getitem__(self, t:typing.Type[ToScalar_1_T1]) -> ToScalar_1[ToScalar_1_T1]: ...

        ToScalar_1_T1 = typing.TypeVar('ToScalar_1_T1')
        class ToScalar_1(typing.Generic[ToScalar_1_T1]):
            ToScalar_1_T = Vector64_0.ToScalar_MethodGroup.ToScalar_1_T1
            def __call__(self, vector: Vector64_1[ToScalar_1_T]) -> ToScalar_1_T:...


    # Skipped ToVector128 due to it being static, abstract and generic.

    ToVector128 : ToVector128_MethodGroup
    class ToVector128_MethodGroup:
        def __getitem__(self, t:typing.Type[ToVector128_1_T1]) -> ToVector128_1[ToVector128_1_T1]: ...

        ToVector128_1_T1 = typing.TypeVar('ToVector128_1_T1')
        class ToVector128_1(typing.Generic[ToVector128_1_T1]):
            ToVector128_1_T = Vector64_0.ToVector128_MethodGroup.ToVector128_1_T1
            def __call__(self, vector: Vector64_1[ToVector128_1_T]) -> Vector128_1[ToVector128_1_T]:...


    # Skipped ToVector128Unsafe due to it being static, abstract and generic.

    ToVector128Unsafe : ToVector128Unsafe_MethodGroup
    class ToVector128Unsafe_MethodGroup:
        def __getitem__(self, t:typing.Type[ToVector128Unsafe_1_T1]) -> ToVector128Unsafe_1[ToVector128Unsafe_1_T1]: ...

        ToVector128Unsafe_1_T1 = typing.TypeVar('ToVector128Unsafe_1_T1')
        class ToVector128Unsafe_1(typing.Generic[ToVector128Unsafe_1_T1]):
            ToVector128Unsafe_1_T = Vector64_0.ToVector128Unsafe_MethodGroup.ToVector128Unsafe_1_T1
            def __call__(self, vector: Vector64_1[ToVector128Unsafe_1_T]) -> Vector128_1[ToVector128Unsafe_1_T]:...


    # Skipped TryCopyTo due to it being static, abstract and generic.

    TryCopyTo : TryCopyTo_MethodGroup
    class TryCopyTo_MethodGroup:
        def __getitem__(self, t:typing.Type[TryCopyTo_1_T1]) -> TryCopyTo_1[TryCopyTo_1_T1]: ...

        TryCopyTo_1_T1 = typing.TypeVar('TryCopyTo_1_T1')
        class TryCopyTo_1(typing.Generic[TryCopyTo_1_T1]):
            TryCopyTo_1_T = Vector64_0.TryCopyTo_MethodGroup.TryCopyTo_1_T1
            def __call__(self, vector: Vector64_1[TryCopyTo_1_T], destination: Span_1[TryCopyTo_1_T]) -> bool:...


    # Skipped Widen due to it being static, abstract and generic.

    Widen : Widen_MethodGroup
    class Widen_MethodGroup:
        def __call__(self, source: Vector64_1[float]) -> ValueTuple_2[Vector64_1[float], Vector64_1[float]]:...
        # Method Widen(source : Vector64`1) was skipped since it collides with above method
        # Method Widen(source : Vector64`1) was skipped since it collides with above method
        # Method Widen(source : Vector64`1) was skipped since it collides with above method
        # Method Widen(source : Vector64`1) was skipped since it collides with above method
        # Method Widen(source : Vector64`1) was skipped since it collides with above method
        # Method Widen(source : Vector64`1) was skipped since it collides with above method

    # Skipped WidenLower due to it being static, abstract and generic.

    WidenLower : WidenLower_MethodGroup
    class WidenLower_MethodGroup:
        def __call__(self, source: Vector64_1[float]) -> Vector64_1[float]:...
        # Method WidenLower(source : Vector64`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector64`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector64`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector64`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector64`1) was skipped since it collides with above method
        # Method WidenLower(source : Vector64`1) was skipped since it collides with above method

    # Skipped WidenUpper due to it being static, abstract and generic.

    WidenUpper : WidenUpper_MethodGroup
    class WidenUpper_MethodGroup:
        def __call__(self, source: Vector64_1[float]) -> Vector64_1[float]:...
        # Method WidenUpper(source : Vector64`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector64`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector64`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector64`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector64`1) was skipped since it collides with above method
        # Method WidenUpper(source : Vector64`1) was skipped since it collides with above method

    # Skipped WithElement due to it being static, abstract and generic.

    WithElement : WithElement_MethodGroup
    class WithElement_MethodGroup:
        def __getitem__(self, t:typing.Type[WithElement_1_T1]) -> WithElement_1[WithElement_1_T1]: ...

        WithElement_1_T1 = typing.TypeVar('WithElement_1_T1')
        class WithElement_1(typing.Generic[WithElement_1_T1]):
            WithElement_1_T = Vector64_0.WithElement_MethodGroup.WithElement_1_T1
            def __call__(self, vector: Vector64_1[WithElement_1_T], index: int, value: typing.Optional[WithElement_1_T]) -> Vector64_1[WithElement_1_T]:...


    # Skipped Xor due to it being static, abstract and generic.

    Xor : Xor_MethodGroup
    class Xor_MethodGroup:
        def __getitem__(self, t:typing.Type[Xor_1_T1]) -> Xor_1[Xor_1_T1]: ...

        Xor_1_T1 = typing.TypeVar('Xor_1_T1')
        class Xor_1(typing.Generic[Xor_1_T1]):
            Xor_1_T = Vector64_0.Xor_MethodGroup.Xor_1_T1
            def __call__(self, left: Vector64_1[Xor_1_T], right: Vector64_1[Xor_1_T]) -> Vector64_1[Xor_1_T]:...




Vector64_1_T = typing.TypeVar('Vector64_1_T')
class Vector64_1(typing.Generic[Vector64_1_T], IEquatable_1[Vector64_1[Vector64_1_T]]):
    @classmethod
    @property
    def AllBitsSet(cls) -> Vector64_1[Vector64_1_T]: ...
    @classmethod
    @property
    def Count(cls) -> int: ...
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @property
    def Item(self) -> typing.Optional[Vector64_1_T]: ...
    @classmethod
    @property
    def One(cls) -> Vector64_1[Vector64_1_T]: ...
    @classmethod
    @property
    def Zero(cls) -> Vector64_1[Vector64_1_T]: ...
    def GetHashCode(self) -> int: ...
    def __add__(self, left: Vector64_1[Vector64_1_T], right: Vector64_1[Vector64_1_T]) -> Vector64_1[Vector64_1_T]: ...
    def __and__(self, left: Vector64_1[Vector64_1_T], right: Vector64_1[Vector64_1_T]) -> Vector64_1[Vector64_1_T]: ...
    def __or__(self, left: Vector64_1[Vector64_1_T], right: Vector64_1[Vector64_1_T]) -> Vector64_1[Vector64_1_T]: ...
    @typing.overload
    def __truediv__(self, left: Vector64_1[Vector64_1_T], right: Vector64_1[Vector64_1_T]) -> Vector64_1[Vector64_1_T]: ...
    @typing.overload
    def __truediv__(self, left: Vector64_1[Vector64_1_T], right: typing.Optional[Vector64_1_T]) -> Vector64_1[Vector64_1_T]: ...
    def __eq__(self, left: Vector64_1[Vector64_1_T], right: Vector64_1[Vector64_1_T]) -> bool: ...
    def __xor__(self, left: Vector64_1[Vector64_1_T], right: Vector64_1[Vector64_1_T]) -> Vector64_1[Vector64_1_T]: ...
    def __ne__(self, left: Vector64_1[Vector64_1_T], right: Vector64_1[Vector64_1_T]) -> bool: ...
    def __lshift__(self, value: Vector64_1[Vector64_1_T], shiftCount: int) -> Vector64_1[Vector64_1_T]: ...
    @typing.overload
    def __mul__(self, left: Vector64_1[Vector64_1_T], right: Vector64_1[Vector64_1_T]) -> Vector64_1[Vector64_1_T]: ...
    @typing.overload
    def __mul__(self, left: Vector64_1[Vector64_1_T], right: typing.Optional[Vector64_1_T]) -> Vector64_1[Vector64_1_T]: ...
    @typing.overload
    def __mul__(self, left: typing.Optional[Vector64_1_T], right: Vector64_1[Vector64_1_T]) -> Vector64_1[Vector64_1_T]: ...
    def __invert__(self, vector: Vector64_1[Vector64_1_T]) -> Vector64_1[Vector64_1_T]: ...
    def __rshift__(self, value: Vector64_1[Vector64_1_T], shiftCount: int) -> Vector64_1[Vector64_1_T]: ...
    def __sub__(self, left: Vector64_1[Vector64_1_T], right: Vector64_1[Vector64_1_T]) -> Vector64_1[Vector64_1_T]: ...
    def __neg__(self, vector: Vector64_1[Vector64_1_T]) -> Vector64_1[Vector64_1_T]: ...
    def __pos__(self, value: Vector64_1[Vector64_1_T]) -> Vector64_1[Vector64_1_T]: ...
    # Operator not supported op_UnsignedRightShift(value: Vector64`1, shiftCount: Int32)
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[Vector64_1_T]
    Equals_MethodGroup_Vector64_1_T = typing.TypeVar('Equals_MethodGroup_Vector64_1_T')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_Vector64_1_T]):
        Equals_MethodGroup_Vector64_1_T = Vector64_1.Equals_MethodGroup_Vector64_1_T
        @typing.overload
        def __call__(self, other: Vector64_1[Equals_MethodGroup_Vector64_1_T]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Optional[typing.Any]) -> bool:...


