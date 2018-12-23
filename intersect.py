import sys

studentID = set()

with open(sys.argv[0]) as fA:
    for line in fA:
        if line == '':
            continue
        studentID.add(line)

scoreMap = dict()

with open(sys.argv[1]) as fB:
    for line in fB:
        if line == '':
            continue

        v = line.split(',')
        sid = v[0]

        if sid in studentID:
            value = v[1]
            print('%s,%s' % (sid, value))