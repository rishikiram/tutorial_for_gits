"""Draw a git history graph (branch, then merge) and save it as a PNG."""

import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path

tree_color = "#2f6fdb"

# Commits in chronological order: (id, lane, parents, message).
# A commit with two parents is a merge commit.
COMMITS = [
    ("a1f3",  None, "Initial commit"),
    ("b72c", "a1f3", "Add README"),
    ("c9e0", "b72c", "Start feature"),
    ("d415", "b72c", "Fix typo"),
    # ("e829", "d415", "WRITE A SIMULATED COMMIT MSG HERE")
]

X_STEP = 1.6
Y_STEP = 1.2
OUTPUT = "images/git_tree_v1.png"


def position(index):
    return (index * X_STEP, 0)


def draw_edge(ax, start, end, color):
    """Creates a Straight line"""
    verts = [start, end]
    codes = [Path.MOVETO, Path.LINETO]
    ax.add_patch(PathPatch(Path(verts, codes), facecolor="none",
                           edgecolor=color, linewidth=3, zorder=1))


def main():
    fig, ax = plt.subplots(figsize=(10, 3.5))

    positions = {cid: position(i) for i, (cid, _, _) in enumerate(COMMITS)}

    # Edges: color by the branch the line leads into, except merges,
    # which keep the color of the branch being merged in.
    for cid, parent, _ in COMMITS:
        if parent:
            draw_edge(ax, positions[parent], positions[cid], tree_color)

    # Commit nodes and labels.
    for cid, parent, message in COMMITS:
        x, y = positions[cid]
        color = tree_color
        ax.scatter(x, y, s=350, color="white",
                   edgecolor=color, linewidth=3, zorder=2)
        ax.text(x, y, cid[:2], ha="center", va="center", fontsize=8,
                fontweight="bold", color=color, zorder=3)
        offset = 0.4 
        ax.text(x, y + offset, message, ha="center",
                va="bottom" if offset > 0 else "top", fontsize=9)

    # Branch name tags at each lane's latest commit.
    # for lane_index, (name, color) in enumerate(LANES):
    #     last = [cid for cid, lane, _, _ in COMMITS if lane == lane_index][-1]
    #     x, y = positions[last]
    #     ax.text(x + 0.45, y, name, va="center", fontsize=10, color="white",
    #             fontweight="bold",
    #             bbox=dict(boxstyle="round,pad=0.3", facecolor=color, edgecolor="none"))

    ax.set_xlim(-0.8, (len(COMMITS) - 1) * X_STEP + 1.6)
    ax.set_ylim(-(1 - 1) * Y_STEP - 1, 1)
    ax.set_aspect("equal")
    ax.axis("off")

    fig.savefig(OUTPUT, dpi=200, bbox_inches="tight")
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()
