from __future__ import annotations

from typing import Sequence


class HTMLNode():
    """Base de todos los nodos HTML.

    Cualquier subclase debe implementar to_html.
    """

    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: Sequence[HTMLNode] | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        self.tag: str | None = tag
        self.value: str | None = value
        # Convertimos a lista propia para evitar aliasing si pasan una tupla u otra secuencia
        self.children: list[HTMLNode] = list(children) if children else []
        self.props: dict[str, str] = props if props else {}

    def to_html(self) -> str:
        """Devolver representación HTML del nodo."""
        raise NotImplementedError

    def props_to_html(self) -> str:
        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result

    def __repr__(self) -> str:  # pragma: no cover - ayuda debug
        return (
            f"tag={self.tag!r}, "
            f"value={self.value!r}, "
            f"children={self.children!r}, "
            f"props={self.props!r}"
        )

