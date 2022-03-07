from body import Body
from constants import M, x_0, v_0

def trapezoid(alpha: float, dt: float, range: int, first: bool = True, subdir: str = "other"):
    body = Body(M, x_0, v_0, alpha, dt)