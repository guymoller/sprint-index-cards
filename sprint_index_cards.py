import csv
from jinja2 import Template

input_file = 'issues.csv'
output_file = 'index-cards.html'
with open(input_file, 'rb') as csvfile:
    issues= csv.reader(csvfile, delimiter=',', quotechar='|')
    template = Template(open('template.html').read())
    html =template.render(records=enumerate(issues))
    with open(output_file, "w") as text_file:
        text_file.write(html)

print "rendered the index cards to %s" % output_file
