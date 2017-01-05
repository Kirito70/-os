print ("\t\t\tFirst Come First Serve\n\n\n")

TotalProcesses = int (input("\tEnter Total Number of processes you have: "))

ProcessArrivalTimeList = [None] * TotalProcesses
ProcessBurstTimeList = [None] * TotalProcesses
for processNumber in range(0,TotalProcesses):
    processArrivalTime = int (input("\tEnter Arrival time for process %d: " %(processNumber+1)))
    processBurstTime = int (input("\tEnter Burst time for process %d: " %(processNumber+1)))
    ProcessArrivalTimeList[processNumber] =  processArrivalTime
    ProcessBurstTimeList[processNumber] = processBurstTime

for index in range(0,TotalProcesses):
    for index2 in range(0,TotalProcesses):
        if ProcessArrivalTimeList[index] <= ProcessArrivalTimeList[index2]:
            ArrivalTimeTemp = ProcessArrivalTimeList[index]
            BurstTimeTemp = ProcessBurstTimeList[index]
            ProcessArrivalTimeList[index] =  ProcessArrivalTimeList[index2]
            ProcessBurstTimeList[index] = ProcessBurstTimeList[index2]
            ProcessArrivalTimeList[index2] = ArrivalTimeTemp
            ProcessBurstTimeList[index2] = BurstTimeTemp

print("\n\n\nDetails:\n\nProcess Name\t\tStart Time\t\tFinish Time\t\tTurnAround Time\t\t Waiting Time")

ProcessStartTimeList = [None] * TotalProcesses
ProcessFinishTimeList = [None] * TotalProcesses

for processNumber in range(0,TotalProcesses):
    if processNumber == 0:
        ProcessStartTimeList[processNumber] = ProcessArrivalTimeList[0]
        ProcessFinishTimeList[processNumber] = ProcessStartTimeList[0]+ProcessBurstTimeList[0]
    else:
        ProcessStartTimeList[processNumber] = ProcessFinishTimeList[(processNumber-1)]
        ProcessFinishTimeList[processNumber] = ProcessFinishTimeList[(processNumber-1)] + ProcessBurstTimeList[processNumber]
    TurnAroundTime = ProcessFinishTimeList[processNumber]-ProcessArrivalTimeList[processNumber]
    WaitingTime = ProcessStartTimeList[processNumber]-ProcessArrivalTimeList[processNumber]
    print ("Process # ",(processNumber+1),"\t\t   ",ProcessStartTimeList[processNumber]," \t\t\t   ",ProcessFinishTimeList[processNumber],
           "\t\t\t  ",TurnAroundTime," \t\t\t\t   ",WaitingTime)