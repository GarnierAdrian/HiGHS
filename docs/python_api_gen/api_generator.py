from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import griffe
from griffe import Alias, Class, Function, Module

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "highspy"

print("Importing Package")
package = griffe.load(
    "highspy",
    search_paths=[str(PACKAGE)],
)
print("Importing Improted")

if not isinstance(package, Module):
    sys.exit(-1)
    print("Failed")


def render_docstring(obj: Any) -> str:
    print("Rendering DOC")

    if obj.docstring is None:
        return ""

    return obj.docstring.value.strip()


def is_highspy_path(path: str) -> bool:
    return path == "highspy" or path.startswith("highspy.")


def resolve_highspy_alias(obj: Any) -> None | Any:
    while isinstance(obj, Alias):
        target_path = obj.target_path

        if not is_highspy_path(target_path):
            return None
        print(obj)
        obj.resolve_target()
        print(obj)

    return obj


def render_function(function: Function, level: int) -> list[str]:
    print("Rendering Func")
    lines = [
        f"{'#' * level} {function.name}",
        "",
    ]

    signature = function.signature

    lines.extend(
        [
            "```python",
            f"{function.name}{signature}",
            "```",
            "",
        ]
    )

    docstring = render_docstring(function)
    if docstring:
        lines.extend([docstring, ""])

    return lines


def render_class(cls: Class, level: int) -> list[str]:
    print("Rendering Class")

    lines = [
        f"{'#' * level} {cls.name}",
        "",
    ]

    docstring = render_docstring(cls)
    if docstring:
        lines.extend([docstring, ""])

    for member in cls.members.values():
        if isinstance(member, Function):
            lines.extend(render_function(member, level + 1))

    return lines


def render_module(module: Module) -> str:
    lines = [
        f"# {module.name}",
        "",
    ]

    docstring = render_docstring(module)
    if docstring:
        lines.extend([docstring, ""])

    for member in module.members.values():
        member = resolve_highspy_alias(member)
        if isinstance(member, Class):
            lines.extend(render_class(member, 2))

        elif isinstance(member, Function):
            lines.extend(render_function(member, 2))

    return "\n".join(lines)


print("Start rendering")
markdown = render_module(package)

Path("api.md").write_text(markdown, encoding="utf-8")
