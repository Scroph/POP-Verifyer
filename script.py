import sys
import os
import poplib
import threading
import Queue

def usage():
	print '%s <input.csv> <output.csv> <threads> <timeout>' % sys.argv[0]
	sys.exit(0)

def processing():
	while not queue.empty():
		user, pswd, host, timeout, output = queue.get()
		
		try:
			pop = poplib.POP3_SSL(host)
			pop.user(user)
			res = pop.pass_(pswd)
			
			output.write('%s,%s,%s,%s\n' % (user, pswd, host, str(res)))
		except Exception, e:
			output.write('%s,%s,%s,%s\n' % (user, pswd, host, e))
		
		queue.task_done()

if __name__ == '__main__':
	if len(sys.argv) < 3:
		usage()

input_file = sys.argv[1]
output_file = sys.argv[2]
try:
	max_threads = int(sys.argv[3])
except:
	max_threads = 3
try:
	timeout = int(sys.argv[4])
except:
	timeout = 4

queue = Queue.Queue()

try:
	accounts = open(input_file, 'r')
	status = open(output_file, 'w')
except IOError, e:
	print e
	sys.exit(1)

print 'The results will be written to ' + output_file

for a in accounts:
	user, pswd, host = a.strip().split(',')
	queue.put((user, pswd, host, timeout, status))

for x in xrange(max_threads):
	t = threading.Thread(target = processing)
	t.start()

queue.join()

print 'All done !'
