from jinja2 import Template

data = """{% raw %} {{ name }} {% endraw %}"""
link = """In Html document links are defined as <a href="#">LINK</a>"""

tm = Template(data)
msg = tm.render(name="Roman")
print(msg)

tm2 = Template("{{ link|e }}")
msg = tm2.render(link=link)
print(msg)