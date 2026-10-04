"""Draw a git history graph (branch, then merge) and save it as a PNG."""

import os

import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path

# Each branch: (name, color). Branch index = vertical position.
BRANCHES = [
    ("main", "#2f6fdb"),
    ("feature", "#e07b39"),
]

# Commits in chronological order: (id, branch, parents, message).
# A commit with two parents is a merge commit.
COMMITS = [
    ("a1f3", 0, [], "Initial commit"),
    ("b72c", 0, ["a1f3"], "Add README"),
    ("c9e0", 1, ["b72c"], "Start feature"),
    ("d415", 0, ["b72c"], "Fix typo"),
    ("e8b2", 1, ["c9e0"], "Finish feature"),
    ("f03d", 0, ["d415", "e8b2"], "Merge feature"),
]

X_STEP = 1.6
Y_STEP = 1.2
OUTPUT = "images/git_tree_v4.png"


def position(index, branch):
    return index * X_STEP, -branch * Y_STEP


def draw_edge(ax, start, end, color):
    """Straight line within a branch, smooth S-curve between branches."""
    (x0, y0), (x1, y1) = start, end
    if y0 == y1:
        verts = [start, end]
        codes = [Path.MOVETO, Path.LINETO]
    else:
        mid = (x0 + x1) / 2
        verts = [start, (mid, y0), (mid, y1), end]
        codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    ax.add_patch(PathPatch(Path(verts, codes), facecolor="none",
                           edgecolor=color, linewidth=3, zorder=1))


def main():
    fig, ax = plt.subplots(figsize=(10, 3.5))

    positions = {cid: position(i, branch) for i, (cid, branch, _, _) in enumerate(COMMITS)}
    branches = {cid: branch for cid, branch, _, _ in COMMITS}

    # Edges: color by the branch the line leads into, except merges,
    # which keep the color of the branch being merged in.
    for cid, branch, parents, _ in COMMITS:
        for parent in parents:
            color_branch = branches[parent] if branches[parent] != branch and len(parents) > 1 else branch
            draw_edge(ax, positions[parent], positions[cid], BRANCHES[color_branch][1])

    # Commit nodes and labels.
    for cid, branch, parents, message in COMMITS:
        x, y = positions[cid]
        color = BRANCHES[branch][1]
        is_merge = len(parents) > 1
        ax.scatter(x, y, s=500 if is_merge else 350, color="white",
                   edgecolor=color, linewidth=3, zorder=2)
        ax.text(x, y, cid[:2], ha="center", va="center", fontsize=8,
                fontweight="bold", color=color, zorder=3)
        offset = 0.4 if branch == 0 else -0.4
        ax.text(x, y + offset, message, ha="center",
                va="bottom" if offset > 0 else "top", fontsize=9)

    # Branch name tags at each branch's latest commit.
    for branch_index, (name, color) in enumerate(BRANCHES):
        last = [cid for cid, branch, _, _ in COMMITS if branch == branch_index][-1]
        x, y = positions[last]
        ax.text(x + 0.45, y, name, va="center", fontsize=10, color="white",
                fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", facecolor=color, edgecolor="none"))

    ax.set_xlim(-0.8, (len(COMMITS) - 1) * X_STEP + 1.6)
    ax.set_ylim(-(len(BRANCHES) - 1) * Y_STEP - 1, 1)
    ax.set_aspect("equal")
    ax.axis("off")

    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    fig.savefig(OUTPUT, dpi=200, bbox_inches="tight")
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()
