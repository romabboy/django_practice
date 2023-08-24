from jinja2 import Template

cars = [
    {'model': 'Audi','price': 23000},
    {'model': 'Shoda', 'price': 17300},
    {'model': 'Opel', 'price': 44333},
    {'model': 'Volvo', 'price': 21300},
    {'model': 'Volkswagen', 'price': 20000},

]

names = ['kakadu','roman','lol']

tpl = "price all auto is {{ cs | sum(attribute='price') }} "
tpl2 = "price all auto is {{ cs | max(attribute='price') }}"
tpl3 = "price all auto is {{ cs | min(attribute='price') }}"
tpl4 = "price all auto is {{ cs | random }}"
tpl5 = "price all auto is {{ cs | replace('o','___') }}"
tpl6 = """
    {% for x in names -%}
        {% filter upper %} {{x}} {% endfilter %}
    {% endfor -%}
"""


tm = Template(tpl)
tm2 = Template(tpl2)
tm3 = Template(tpl3)
tm4 = Template(tpl4)
tm5 = Template(tpl5)
tm6 = Template(tpl6)

msg = tm.render(cs = cars)
msg2 = tm2.render(cs = cars)
msg3 = tm3.render(cs = cars)
msg4 = tm4.render(cs = cars)
msg5 = tm5.render(cs = cars)
msg6 = tm6.render(names = names)

print(msg)
print(msg2)
print(msg3)
print(msg4)
print(msg5)
print(msg6)
