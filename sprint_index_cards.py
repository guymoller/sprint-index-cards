import sys, getopt
import csv
from jinja2 import Template

def main(argv):
    input_file = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print 'test.py -i <input_file>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <input_file>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
    print 'Input file is "', input_file
     #input_file = 'issues.csv'
    output_file = 'index-cards.html'
    with open(input_file, 'rb') as csvfile:
        issues= csv.reader(csvfile, delimiter=',', quotechar='"')
        template = Template(open('template.html').read())
        html =template.render(records=enumerate(issues))
    with open(output_file, "w") as text_file:
        text_file.write(html)
        print "rendered the index cards to %s" % output_file
if __name__ == "__main__":
    main(sys.argv[1:])






