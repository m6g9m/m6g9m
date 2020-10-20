# Use the file name mbox-short.txt as the file name
spam = 0
all = 0
cut = 0
num = 0

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line=line.rstrip()

    if not line.startswith("X-DSPAM-Confidence:") :
        continue

    len = line
    print("line", line)
    point = line.find (":") + 1
    print("p", point)
    num = (line[point:])
    num = float(num)

    print("num", num)
    all = all + float(num)
    print("all", all)

    spam = spam + 1
    print("spam", spam)

spam = float(all) / float(spam)
print("Average spam confidence:",  float(spam))
