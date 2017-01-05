print ("\t\t\tPriority Scheduling\n\n\n")

TotalProcesses = int (input("\tEnter Total Number of processes you have: "))

ProcessArrivalTimeList = [None] * TotalProcesses
ProcessBurstTimeList = [None] * TotalProcesses
ProcessPriorityList = [None] * TotalProcesses
for processNumber in range(0,TotalProcesses):
    processArrivalTime = int (input("\tEnter Arrival time for process %d: " %(processNumber+1)))
    processBurstTime = int (input("\tEnter Burst time for process %d: " %(processNumber+1)))
    processPriority = int (input("\tEnter Priority for Process %d: " %(processNumber+1)))
    ProcessArrivalTimeList[processNumber] =  processArrivalTime
    ProcessBurstTimeList[processNumber] = processBurstTime
    ProcessPriorityList[processNumber] = processPriority

for index in range(0,TotalProcesses):
    for index2 in range(0,TotalProcesses):
        if ProcessArrivalTimeList[index] <= ProcessArrivalTimeList[index2]:
            ArrivalTimeTemp = ProcessArrivalTimeList[index]
            BurstTimeTemp = ProcessBurstTimeList[index]
            PriorityTemp = ProcessPriorityList[index]
            ProcessArrivalTimeList[index] =  ProcessArrivalTimeList[index2]
            ProcessBurstTimeList[index] = ProcessBurstTimeList[index2]
            ProcessPriorityList[index] = ProcessPriorityList[index2]
            ProcessArrivalTimeList[index2] = ArrivalTimeTemp
            ProcessBurstTimeList[index2] = BurstTimeTemp
            ProcessPriorityList[index2]= PriorityTemp

#print(ProcessArrivalTimeList)
#print(ProcessBurstTimeList)
#print(ProcessPriorityList)

#SortedProcessCounter = 1

for processNumber in range(0,TotalProcesses):
    SortedProcessCounter = processNumber + 1
    for processNumber2 in range(processNumber,TotalProcesses):
        if(ProcessArrivalTimeList[processNumber]+ProcessBurstTimeList[processNumber])>ProcessArrivalTimeList[processNumber2]:
            for prioritySorter in range(processNumber,SortedProcessCounter):
                if ProcessPriorityList[processNumber2]<= ProcessPriorityList[prioritySorter]:
                    ArrivalTimeTemp = ProcessArrivalTimeList[processNumber2]
                    BurstTimeTemp = ProcessBurstTimeList[processNumber2]
                    PriorityTemp = ProcessPriorityList[processNumber2]
                    ProcessArrivalTimeList[processNumber2] = ProcessArrivalTimeList[prioritySorter]
                    ProcessBurstTimeList[processNumber2] = ProcessBurstTimeList[prioritySorter]
                    ProcessPriorityList[processNumber2] = ProcessPriorityList[prioritySorter]
                    ProcessArrivalTimeList[prioritySorter] = ArrivalTimeTemp
                    ProcessBurstTimeList[prioritySorter] = BurstTimeTemp
                    ProcessPriorityList[prioritySorter] = PriorityTemp
            SortedProcessCounter = SortedProcessCounter+1

#print(ProcessArrivalTimeList)
#print(ProcessBurstTimeList)
#print(ProcessPriorityList)

print("\n\n\nDetails:\n\n Process Name \t\t  Priority \t\t Start Time\t\tFinish Time\t\tTurnAround Time\t\t Waiting Time")

ProcessStartTimeList = [None] * TotalProcesses
ProcessFinishTimeList = [None] * TotalProcesses

for processNumber in range(0,TotalProcesses):
    if processNumber == 0:
        ProcessStartTimeList[processNumber] = ProcessArrivalTimeList[0]
        ProcessFinishTimeList[processNumber] = ProcessStartTimeList[0]+ProcessBurstTimeList[0]
    else:
        ProcessStartTimeList[processNumber] = ProcessFinishTimeList[(processNumber-1)]
        ProcessFinishTimeList[processNumber] = ProcessFinishTimeList[(processNumber-1)] + ProcessBurstTimeList[processNumber]
    TurnAroundTime = ProcessFinishTimeList[processNumber] - ProcessArrivalTimeList[processNumber]
    WaitingTime = ProcessStartTimeList[processNumber] - ProcessArrivalTimeList[processNumber]
    print ("Process # ",(processNumber+1),"\t\t ",(ProcessPriorityList[processNumber]),"\t\t   ",ProcessStartTimeList[processNumber]," \t\t\t   ",ProcessFinishTimeList[processNumber],
           "\t\t\t  ",TurnAroundTime," \t\t\t\t   ",WaitingTime)