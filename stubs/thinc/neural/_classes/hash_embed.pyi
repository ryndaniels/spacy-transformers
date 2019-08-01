# Stubs for thinc.neural._classes.hash_embed (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ...describe import Dimension, Gradient, Weights
from .._lsuv import do_lsuv
from ..util import copy_array
from .model import Model
from typing import Any, Optional

def LSUVinit(model: Any, X: Any, y: Optional[Any] = ...): ...

class HashEmbed(Model):
    name: str = ...
    column: Any = ...
    nO: Any = ...
    nV: Any = ...
    seed: Any = ...
    def __init__(self, nO: Any, nV: Any, seed: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def predict(self, ids: Any): ...
    def begin_update(self, ids: Any, drop: float = ...): ...