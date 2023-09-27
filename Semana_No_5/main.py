# 1) Write a function that returns a custom HTML block of code as a string, the function will take a list as argument
# with this format: ["i/text inside the tag", "p/another text inside this tag"], you need to validate:
# 	a) If the list does not contain the tags (html, title, body) raise a custom exception.
# 	b) All the child tags such as p, a, i, b, are only generated inside body tag.
# 	c) Every tag generated should also have a closing tag.
# 	d) All the elements from list should be a string.
# 	e) Keep the logical order: '<html><header></header><body></body></html>'.
def custom_html(lst: list) -> str:
    split_list = []
    base_tags = []
    tags = {}

    if not any("html" in item for item in lst) or \
            not any("header" in item for item in lst) or \
            not any("title" in item for item in lst) or \
            not any("body" in item for item in lst):
        raise "You must have correct tags..."
    else:
        for item in lst:
            split_list.append(item.split("/"))

        for value in split_list:
            if len(value) > 1:
                tags[value[0]] = value[1]
            else:
                base_tags.append(value[0])

    def get_tag(tag):
        for k, v in tags.items():
            if tag == k:
                return k

    def get_value(tag):
        for k, v in tags.items():
            if tag == k:
                return v

    html = f"""
        <{base_tags[0]}>
            <{base_tags[1]}>
                {'<title>' if 'title' in tags else ''}
                    {tags['title'] if 'title' in tags else ''}
                {'</title>' if 'title' in tags else ''}
            </{base_tags[1]}>
            <{base_tags[2]}>
                {f'<{get_tag("a")}>' if 'a' in tags else ''}
                    {f'{get_value("a")}' if 'a' in tags else ''}
                {f'</{get_tag("a")}>' if 'a' in tags else ''}
                
                {f'<{get_tag("p")}>' if 'p' in tags else ''}
                    {f'{get_value("p")}' if 'p' in tags else ''}
                {f'</{get_tag("p")}>' if 'p' in tags else ''}
                
                {f'<{get_tag("i")}>' if 'i' in tags else ''}
                    {f'{get_value("i")}' if 'i' in tags else ''}
                {f'</{get_tag("i")}>' if 'i' in tags else ''}
                
                {f'<{get_tag("b")}>' if 'b' in tags else ''}
                    {f'{get_value("b")}' if 'b' in tags else ''}
                {f'</{get_tag("b")}>' if 'b' in tags else ''}
            </{base_tags[2]}>
        </{base_tags[0]}>
    """

    return html



# 2) Create a decorator to add extra functionality to previous function, in this case we need to add different styles to
# specifics html tags, to achieve this the decorator will take a dictionary such as this:
# {"p": "font-size: 14px font-family: Arial"}, add the styles to the corresponding tags, don't apply any changes if
# the tags from the dictionary are not found in the list we pass to the function. Return the html string with
# the new changes.


# 3) Create a decorator that will allow you to add a link tag to use custom css inside the header tag when decorating
# last function.


# 4) Create a decorator to add more functionality to last function, Instead of returning a string save the HTML string
# into a 'index.html' file.


# 5) Create a decorator that will add the capability to return a StringIO object when decorating last function instead
# of returning a simple HTML string.
