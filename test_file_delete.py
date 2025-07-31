ic.strt(length=30).put(0)
m = mmi(length=50).put()
ic.bend(angle=-30).put()
ic.bend(angle=30).put(m.pin['b1'])

# inverted version:
ici.strt(length=30).put(0, -50)
mi = mmi(length=50, inverse=True).put()
ici.bend(angle=-30).put()
ici.bend(angle=30).put(mi.pin['b1'])

nd.export_gds()