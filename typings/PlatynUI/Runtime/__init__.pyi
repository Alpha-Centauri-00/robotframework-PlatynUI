# This file was generated by PythonNetStubGenerator
# mypy: ignore-errors
import typing, abc
from PlatynUI.Runtime.Core import INode, IAttribute
from System.Collections.Generic import IDictionary_2, IList_1, IEnumerable_1
from System import Attribute, Array_1

class Desktop(INode):
    @property
    def Attributes(self) -> IDictionary_2[str, IAttribute]: ...
    @property
    def Children(self) -> IList_1[INode]: ...
    @classmethod
    @property
    def Instance(cls) -> Desktop: ...
    @property
    def LocalName(self) -> str: ...
    @property
    def NamespaceURI(self) -> str: ...
    @property
    def Parent(self) -> typing.Optional[INode]: ...
    def Clone(self) -> INode: ...
    def IsSamePosition(self, other: INode) -> bool: ...
    def Refresh(self) -> None: ...


class Display:
    @classmethod
    @property
    def Instance(cls) -> Display: ...
    @staticmethod
    def GetBoundingRectangle() -> Rect: ...
    # Skipped HighlightRect due to it being static, abstract and generic.

    HighlightRect : HighlightRect_MethodGroup
    class HighlightRect_MethodGroup:
        @typing.overload
        def __call__(self, rect: Rect, time: float) -> None:...
        @typing.overload
        def __call__(self, x: float, y: float, width: float, height: float, time: float) -> None:...



class Finder(abc.ABC):
    @staticmethod
    def EnumAllNodes(parent: typing.Optional[INode], xpath: str, findVirtual: bool = ...) -> IEnumerable_1[INode]: ...
    @staticmethod
    def FindSingleNode(parent: typing.Optional[INode], xpath: str, findVirtual: bool = ...) -> typing.Optional[INode]: ...


class PlatformHelper(abc.ABC):
    @staticmethod
    def GetCurrentPlatform() -> RuntimePlatform: ...


class PlatynUiExtensionAttribute(Attribute):
    def __init__(self, supportedPlatforms: Array_1[RuntimePlatform]) -> None: ...
    @property
    def SupportedPlatforms(self) -> Array_1[RuntimePlatform]: ...
    @property
    def TypeId(self) -> typing.Any: ...


class Point:
    def __init__(self, x: float, y: float) -> None: ...
    @property
    def X(self) -> float: ...
    @X.setter
    def X(self, value: float) -> float: ...
    @property
    def Y(self) -> float: ...
    @Y.setter
    def Y(self, value: float) -> float: ...
    def ToString(self) -> str: ...


class Rect:
    def __init__(self, x: float, y: float, width: float, height: float) -> None: ...
    Empty : Rect
    @property
    def Height(self) -> float: ...
    @Height.setter
    def Height(self, value: float) -> float: ...
    @property
    def Width(self) -> float: ...
    @Width.setter
    def Width(self, value: float) -> float: ...
    @property
    def X(self) -> float: ...
    @X.setter
    def X(self, value: float) -> float: ...
    @property
    def Y(self) -> float: ...
    @Y.setter
    def Y(self, value: float) -> float: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, rect1: Rect, rect2: Rect) -> bool: ...
    def __ne__(self, rect1: Rect, rect2: Rect) -> bool: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, value: Rect) -> bool:...
        @typing.overload
        def __call__(self, o: typing.Optional[typing.Any]) -> bool:...
        @typing.overload
        def __call__(self, rect1: Rect, rect2: Rect) -> bool:...



class RuntimePlatform(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Any : RuntimePlatform # 0
    Windows : RuntimePlatform # 1
    Linux : RuntimePlatform # 2
    FreeBSD : RuntimePlatform # 3
    MacOS : RuntimePlatform # 4
    Android : RuntimePlatform # 5
    IOS : RuntimePlatform # 6
    Unknown : RuntimePlatform # 7


class Size:
    def __init__(self, width: float, height: float) -> None: ...
    @property
    def Height(self) -> float: ...
    @Height.setter
    def Height(self, value: float) -> float: ...
    @property
    def Width(self) -> float: ...
    @Width.setter
    def Width(self, value: float) -> float: ...
    def ToString(self) -> str: ...

