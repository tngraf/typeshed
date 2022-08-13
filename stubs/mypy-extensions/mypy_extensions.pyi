import abc
import sys
from _collections_abc import dict_items, dict_keys, dict_values
from _typeshed import IdentityFunction, Self
from collections.abc import Mapping
from typing import Any, ClassVar, Generic, TypeVar, overload, type_check_only

_T = TypeVar("_T")
_U = TypeVar("_U")

# Internal mypy fallback type for all typed dicts (does not exist at runtime)
# N.B. Keep this mostly in sync with typing(_extensions)._TypedDict
@type_check_only
class _TypedDict(Mapping[str, object], metaclass=abc.ABCMeta):
    __total__: ClassVar[bool]
    # Unlike typing(_extensions).TypedDict,
    # subclasses of mypy_extensions.TypedDict do NOT have the __required_keys__ and __optional_keys__ ClassVars
    def copy(self: Self) -> Self: ...
    # Using NoReturn so that only calls using mypy plugin hook that specialize the signature
    # can go through.
    def setdefault(self, k: NoReturn, default: object) -> object: ...
    # Mypy plugin hook for 'pop' expects that 'default' has a type variable type.
    def pop(self, k: NoReturn, default: _T = ...) -> object: ...  # pyright: ignore[reportInvalidTypeVarUse]
    def update(self: Self, __m: Self) -> None: ...
    def items(self) -> dict_items[str, object]: ...
    def keys(self) -> dict_keys[str, object]: ...
    def values(self) -> dict_values[str, object]: ...
    def __delitem__(self, k: NoReturn) -> None: ...
    if sys.version_info >= (3, 9):
        def __or__(self: Self, __other: Self) -> Self: ...
        def __ior__(self: Self, __other: Self) -> Self: ...

def TypedDict(typename: str, fields: dict[str, type[Any]], total: bool = ...) -> type[dict[str, Any]]: ...
@overload
def Arg(type: _T, name: str | None = ...) -> _T: ...
@overload
def Arg(*, name: str | None = ...) -> Any: ...
@overload
def DefaultArg(type: _T, name: str | None = ...) -> _T: ...
@overload
def DefaultArg(*, name: str | None = ...) -> Any: ...
@overload
def NamedArg(type: _T, name: str | None = ...) -> _T: ...
@overload
def NamedArg(*, name: str | None = ...) -> Any: ...
@overload
def DefaultNamedArg(type: _T, name: str | None = ...) -> _T: ...
@overload
def DefaultNamedArg(*, name: str | None = ...) -> Any: ...
@overload
def VarArg(type: _T) -> _T: ...
@overload
def VarArg() -> Any: ...
@overload
def KwArg(type: _T) -> _T: ...
@overload
def KwArg() -> Any: ...

# Return type that indicates a function does not return.
# Deprecated: Use typing.NoReturn instead.
class NoReturn: ...

# This is consistent with implementation. Usage intends for this as
# a class decorator, but mypy does not support type[_T] for abstract
# classes until this issue is resolved, https://github.com/python/mypy/issues/4717.
def trait(cls: _T) -> _T: ...
def mypyc_attr(*attrs: str, **kwattrs: object) -> IdentityFunction: ...

class FlexibleAlias(Generic[_T, _U]): ...
