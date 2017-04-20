
import io
import csv
from Queue import Queue
import threading
from threading import Thread
import time

#-----------

#def listToCSV(data.args,fileName,header):

#	csv = csvWriter(data,50)
#	data1Exist = csv.createThreading(args,fileName,header)
#	print('CSV is created')

#-----------

class csvWriter:
	def __init__(self, data, concurrentThreads):
		self.concurrent = concurrentThreads
		self.q = Queue(concurrentThreads)
		self.dataset = data
		self.lock = threading.Lock()

		print("Outputing csv files..")



	def createThreading(self,args,fileName,header):
		for i in range(self.concurrent):
			t = threading.Thread(target=self.writingcsv,args=(args,fileName,header))
			t.daemon = True
			t.start()

		for data in self.dataset:
			self.q.put(data)

		self.q.join()
		if(len(dataset)>0):

			return True
		return False

	def writingcsv(self,args,fileName,header):

		csvfile = open( fileName, 'wb')
		writer = csv.writer(csvfile, delimiter=',', lineterminator='\r\n', quoting=csv.QUOTE_NONE, escapechar=' ')
		writer.writerow(header)
		with self.lock:
			while not self.q.empty():
				data = self.q.get()
				writer.writerow(data)
				self.q.task_done()
		csvfile.close()

