from sys import stdin

steps = 26

class Worker:
    def __init__(self):
        self.avail = True
        self.tr = 0
    def assignJob(self, job, time):
        self.avail = False
        self.job = job
        self.tr = time
    def work(self):
        self.tr -= 1
        if self.tr == 0:
            self.avail = True
            return self.job
        return -1    

def getFirstFreeJob():
    for index, dep in enumerate(deps):
        if dep == 0:
            deps[index] = -1
            return index
    return -1

def getFirstFreeWorker():
    for index, w in enumerate(workers):
        if w.avail:
            return index
    return -1

done = []
deps = [0 for i in range(steps)]
al = [[] for i in range(steps)]
for line in stdin.readlines():
    pre, post = ord(line[5]) - ord('A'), ord(line[36]) - ord('A')
    deps[post] += 1
    al[pre].append(post)

workers = [Worker() for _ in range(5)]

# simulation approach
time = 0
# while we haven't finished all jobs
while len(done) < 26:
    # assign available jobs to available workers
    while True:
        w = getFirstFreeWorker()
        j = getFirstFreeJob()
        if w == -1 or j == -1: # no worker or no job available
            break
        workers[w].assignJob(j, j + 60 + 1)

    # make all workers work for one second
    for worker in workers:
        finishedJob = worker.work()
        if finishedJob != -1:
            # job is done
            done.append(finishedJob)
            for nex in al[finishedJob]:
                deps[nex] -= 1        
    time += 1

print(time)
        
        