from __future__ import annotations

from typing import Sequence
from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: Sequence[HTMLNode] | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        if tag is None:
            raise ValueError("ParentNode requires a tag")
        super().__init__(tag=tag, props=props, children=children)

    def add_child(self, child: HTMLNode) -> None:
        self.children.append(child)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        content = ''.join(child.to_html() for child in self.children)
        return f'<{self.tag}{self.props_to_html()}>{content}</{self.tag}>'