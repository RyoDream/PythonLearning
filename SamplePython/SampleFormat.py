form = """\
Dear %(name)s,
Please send back my %(item)s or pay me $%(amount)0.2f.
"""

print form % {'name':'Ryo',
              'item':'iPhone',
              'amount':5000.00
              }


import string
form = string.Template("""\
Dear $name,
Please send back my $item or pay me $amount.
""")

print form.substitute({'name':'Ryo',
                       'item':'iPhone',
                       'amount':'%0.2f' % 5000.0 })
