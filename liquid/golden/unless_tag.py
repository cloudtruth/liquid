"""Golden tests cases for testing liquid's `unless` tag."""

from liquid.golden.case import Case

cases = [
    Case(
        description="literal false condition",
        template=r"{% unless false %}foo{% endunless %}",
        expect="foo",
    ),
    Case(
        description="literal true condition",
        template=r"{% unless true %}foo{% endunless %}",
        expect="",
    ),
    Case(
        description="blocks that contain only whitespace are not rendered",
        template=r"{% unless false %}  {% endunless %}",
        expect="",
    ),
    Case(
        description="alternative block",
        template=r"{% unless true %}foo{% else %}bar{% endunless %}",
        expect="bar",
    ),
    Case(
        description="conditional alternative block",
        template=r"{% unless true %}foo{% elsif true %}bar{% endunless %}",
        expect="bar",
    ),
    Case(
        description="conditional alternative block with default",
        template=(
            r"{% unless true %}foo"
            r"{% elsif false %}bar"
            r"{% else %}hello"
            r"{% endunless %}"
        ),
        expect="hello",
    ),
]
