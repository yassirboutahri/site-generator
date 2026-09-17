
class HTMLNode:
    def __init__(
            self, 
            tag: str |None = None, 
            value:str | None =  None, 
            children: list[HTMLNode] | None = None, 
            props: dict[str, str] | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props == None:
            return ""
        
        resutl = ""
        for prop in self.props:
            resutl += f' {prop}="{self.props[prop]}"'

        return resutl

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'


class LeafNode(HTMLNode):
    def __init__(
        self, 
        tag: str | None, 
        value: str,
        props: dict[str, str] | None = None) -> None:
            super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == "":
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value

        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'


class ParentNode(HTMLNode):
    def __init__(self, tag: str , children:list[HTMLNode] , props:dict[str, str] | None = None) -> None:
        super().__init__(tag ,None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")

        result =  ""
        for child in self.children:
            result += f'{child.to_html()}'
           
        return f'<{self.tag}{self.props_to_html()}>{result}</{self.tag}>'

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"