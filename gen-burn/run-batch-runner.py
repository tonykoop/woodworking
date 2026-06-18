"""Resumable codex-spark batch runner for woodworking gen-burn projects.

Usage:
  python3 gen-burn/run-batch-runner.py \
    --max-credits 8 \
    --state-path gen-burn/batch-state.json \
    --projects-path gen-burn/woodworking-project-list.json
"""

import argparse
import json
from pathlib import Path

DEFAULT_STATE_PATH = Path("gen-burn/batch-state.json")
DEFAULT_PROJECTS_PATH = Path("gen-burn/woodworking-project-list.json")
DEFAULT_OUTPUT_PATH = Path("gen-burn/combined-manifest.json")


def load_json(path: Path, fallback):
    if not path.exists():
        return fallback
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state-path", type=Path, default=DEFAULT_STATE_PATH)
    parser.add_argument("--projects-path", type=Path, default=DEFAULT_PROJECTS_PATH)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    parser.add_argument("--max-credits", type=int, default=6)
    args = parser.parse_args()

    projects_data = load_json(args.projects_path, {"projects": []})
    state = load_json(args.state_path, {"completed": [], "credits_spent": 0, "manifest": []})

    completed = set(state.get("completed", []))
    credits_spent = state.get("credits_spent", 0)
    manifest = list(state.get("manifest", []))

    for slug in projects_data.get("projects", []):
        if slug in completed:
            continue

        cost = projects_data.get("credit_cost", {}).get(slug, 1)
        if credits_spent + cost > args.max_credits:
            break

        manifest.append(
            {
                "project_slug": slug,
                "status": "queued",
                "credit_cost": cost,
                "runner_issue": 7,
            }
        )
        completed.add(slug)
        credits_spent += cost

    updated = {
        "completed": sorted(completed),
        "credits_spent": credits_spent,
        "manifest": manifest,
    }

    args.output.write_text(json.dumps(updated, indent=2) + "\n", encoding="utf-8")
    args.state_path.write_text(json.dumps(updated, indent=2) + "\n", encoding="utf-8")

    if manifest:
        print(json.dumps({"status": "ran", "output": str(args.output), "credits_spent": credits_spent}, indent=2))
        return 0

    print(json.dumps({"status": "no-op", "output": str(args.output), "credits_spent": credits_spent}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
