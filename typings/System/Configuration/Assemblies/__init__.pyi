# This file was generated by PythonNetStubGenerator
# mypy: ignore-errors
import typing

class AssemblyHashAlgorithm(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : AssemblyHashAlgorithm # 0
    MD5 : AssemblyHashAlgorithm # 32771
    SHA1 : AssemblyHashAlgorithm # 32772
    SHA256 : AssemblyHashAlgorithm # 32780
    SHA384 : AssemblyHashAlgorithm # 32781
    SHA512 : AssemblyHashAlgorithm # 32782


class AssemblyVersionCompatibility(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    SameMachine : AssemblyVersionCompatibility # 1
    SameProcess : AssemblyVersionCompatibility # 2
    SameDomain : AssemblyVersionCompatibility # 3

