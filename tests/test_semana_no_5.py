import unittest


from Semana_No_5.main import custom_html


class TestCreateCustomHTML(unittest.TestCase):
    def test_create_basic_html(self):
        lst = [
            "html",
            "header",
            "title/Hello World",
            "body",
            "a/This is a Anchor",
            "p/This is a Paragraph",
            "i/This is a Italic Text",
            "b/This is a Bold Text",
        ]

        result = f"""
        <html>
            <header>
                <title>
                    Hello World
                </title>
            </header>
            <body>
                <a>
                    This is a Anchor
                </a>
                
                <p>
                    This is a Paragraph
                </p>
                
                <i>
                    This is a Italic Text
                </i>
                
                <b>
                    This is a Bold Text
                </b>
            </body>
        </html>
        """
        self.assertMultiLineEqual(custom_html(lst=lst), result)
