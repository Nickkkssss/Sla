from datetime import datetime
now = datetime.now()

print ('%02d/%02d/%04d') % (now.month, now.day, now.year)
print ("%02d/%02d/%02d") % (now.day, now.month, now.year)
print ("%02d/%02d/") % (now.day, now.month) + str(now.year)[2] + str(now.year)[3]
