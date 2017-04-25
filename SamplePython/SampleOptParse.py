import optparse

p = optparse.OptionParser()

p.add_option("-o", action="store", dest="outfile")
p.add_option("--output", action="store", dest="outfile")

p.add_option("-d", action="store_true", dest="debug")
p.add_option("--debug", action="store_true", dest="debug")

p.set_default(debug=False)

opts, args = p.parse_args()

outfile = opts.outfile
debugmode = opts.debug


