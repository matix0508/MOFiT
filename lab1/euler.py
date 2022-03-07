import matplotlib.pyplot as plt
from body import Body
from utils import plot, create_dir
from constants import M, x_0, v_0


def euler(alpha: float, dt: float, range: float, first: bool = True, subdir: str = "other", axph=plt):
    body = Body(M, x_0, v_0, alpha=alpha, dt=dt)
    body.calculate_euler(range=range)
    if first:
        fig, [ax1, ax2, ax3] = plt.subplots(3, 1, sharex=True)
        print("[INFO]::Plotting x(t)...")
        plot(
            body.past_times,
            body.past_positions,
            title=rf"$x(t)$, $\Delta t={dt}$, $\alpha={alpha}$ $(0,{range}s)$",
            subdir=subdir,
            ax=ax1

        )
        print("[INFO]::Plotting v(t)...")
        plot(
            body.past_times,
            body.past_velocities,
            title=rf"$v(t)$, $\Delta t={dt}$, $\alpha={alpha}$ $(0,{range}s)$",
            subdir=subdir,
            ax=ax2
        )
        print("[INFO]::Plotting E(t)...")
        plot(
            [body.past_times] * 3,
            [body.Eks, body.Vs, body.Vs + body.Eks],
            title=rf"$E(t)$, $\Delta t={dt}$, $\alpha={alpha}$ $(0,{range}s)$",
            subdir=subdir,
            legend=[r"$Ek(t)$", r"$V(t)$", r"$Ec(t)$"],
            ax=ax3
        )
        create_dir("output")
        fig.tight_layout()
        path = f"output/alpha {alpha} st {dt} range {range}.png"
        fig.savefig(path)
        print(f"[SUCCESS]::Saved Figure in {path}")

    else:
        print("[INFO]::Plotting v(x)...")
        plot(
            body.past_positions,
            body.past_velocities,
            title=rf"$v(x)$ $\Delta t={dt}$, $\alpha={alpha}$ ${range}s$",
            subdir=subdir,
            ax=axph
        )
