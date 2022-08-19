from typing import List
from knot import Knot
from spline import Spline
from dataclasses import dataclass
@dataclass
class SplineHistory:
    splinehist:List[List[Knot]]=[]