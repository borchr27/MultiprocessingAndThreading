# Give credit where credit is due
# Tutorial here: https://www.youtube.com/watch?v=ecKWiaHCEKs

from multiprocessing import Process
import os

def main():
	pass

processes= []
for i in range(os.cpu_count()):
	print('registering process %d' %i)
	processes.append(Process(target=main))

for process in processes:
	process.start

for process in processes:
	process.join