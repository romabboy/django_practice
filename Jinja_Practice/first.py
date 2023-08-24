from jinja2 import Template


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


per = Person('Romeo', 23)

tm = Template('I am {{p.age}} years old and My name is {{ p.name.upper() }}')
msg = tm.render(p = per)

print(msg)
