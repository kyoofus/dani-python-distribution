import markdown

class MarkdownUtils:
    @staticmethod
    def markdown_to_html(markdown_text: str) -> str:
        return markdown.markdown(
            markdown_text,
            extensions=[
                "markdown.extensions.fenced_code",
                "markdown.extensions.tables",
            ],
        )
