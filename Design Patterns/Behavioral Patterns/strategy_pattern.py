from abc import ABC, abstractmethod

class TextFormatterStrategy(ABC):
    @abstractmethod
    def format(self, text: str) -> str:
        pass

class PlainTextFormatter(TextFormatterStrategy):
    def format(self, text: str) -> str:
        return text

class HTMLFormatter(TextFormatterStrategy):
    def format(self, text: str) -> str:
        return f"<p>{text}</p>"

class MarkdownFormatter(TextFormatterStrategy):
    def format(self, text: str) -> str:
        return f"*{text}*"

class TextEditor:
    def __init__(self, strategy: TextFormatterStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: TextFormatterStrategy) -> None:
        self._strategy = strategy

    def publish_text(self, text: str) -> str:
        return self._strategy.format(text)


if __name__ == "__main__":
    text = "Hello, Strategy Pattern!"

    plain_text_formatter = PlainTextFormatter()
    html_formatter = HTMLFormatter()
    markdown_formatter = MarkdownFormatter()

    editor = TextEditor(plain_text_formatter)
    print(editor.publish_text(text))

    editor.set_strategy(html_formatter)
    print(editor.publish_text(text))

    editor.set_strategy(markdown_formatter)
    print(editor.publish_text(text))
