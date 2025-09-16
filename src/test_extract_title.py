
from extract_title import extract_title


class TestExtractTitle:
    def test_extract_title(self):
        assert extract_title("# Title\nContent") == "Title"
        
    def test_no_title(self):
        try:
            extract_title("No title here")
        except Exception as e:
            assert str(e) == "No title found in the markdown content."
