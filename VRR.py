

import queue as Queue

print ("\t\t\tVirtual Round Robin\n\n\n")

print("\t\tQuantum Time is: 4 sec")
print("\t\tInput Time for Process is: 10 sec")
print("\t\tInputOutput Cycle Time for Process is: 3 sec\n\n")

TotalProcesses = int (input("\tEnter Total Number of processes you have: "))

Processes = [{"ProcessNumber":0,"ArrivalTime": 0,"BurstTime":0,"FinishTime":0,"StartTime":-1,"WaitingTime":0,"QuantumTime":4,"InputOutPutCycle":3,
              "RemainingTime":0,"TurnAroundTime":0} for index in range(0,TotalProcesses)]

for processNumber in range(0,TotalProcesses):
    processArrivalTime = int (input("\tEnter Arrival time for process %d: " %(processNumber+1)))
    processBurstTime = int (input("\tEnter Burst time for process %d: " %(processNumber+1)))
    Processes[processNumber]["ArrivalTime"] = processArrivalTime
    Processes[processNumber]["BurstTime"] = processBurstTime
    Processes[processNumber]["RemainingTime"] = processBurstTime

Processes.sort(key=lambda x:(x['ArrivalTime']))

for processNumber in range(0,TotalProcesses):
    Processes[processNumber]["ProcessNumber"] = processNumber+1

ReadyQue = Queue.Queue()
WaitingQue = Queue.Queue()
AuxilaryQue = Queue.Queue()

for process in Processes:
    ReadyQue.put(process)

#while ReadyQue.empty() == False:
#    print(ReadyQue.get())

FlagForFirstProcess=False
TimeSpent=0

while WaitingQue.empty() == False or ReadyQue.empty() == False:
    if WaitingQue.empty() != True:
        PopedFromWaitingQueue = WaitingQue.get()
        if PopedFromWaitingQueue["FinishTime"] + 10 <= TimeSpent:
            AuxilaryQue.put(PopedFromWaitingQueue)
        elif PopedFromWaitingQueue["FinishTime"] + 10 > TimeSpent and ReadyQue.empty() == True:
            RemainingTime = (PopedFromWaitingQueue["FinishTime"] + 10) - TimeSpent
            TimeSpent += RemainingTime
            AuxilaryQue.put(PopedFromWaitingQueue)
            continue
        else:
            OtherElements = []
            while WaitingQue.empty() != True:
                OtherElements.append(WaitingQue.get())
            WaitingQue.put(PopedFromWaitingQueue)
            if len(OtherElements) > 0:
                for ProcessinOther in OtherElements:
                    WaitingQue.put(ProcessinOther)

    if AuxilaryQue.empty() == False:
        PopedProcessFromAuxilary = AuxilaryQue.get()

        if PopedProcessFromAuxilary["QuantumTime"] == 0:
            PopedProcessFromAuxilary["QuantumTime"] == 4
            ReadyQue.put(PopedProcessFromAuxilary)
            continue

        if PopedProcessFromAuxilary["RemainingTime"] < PopedProcessFromAuxilary["InputOutPutCycle"] and PopedProcessFromAuxilary["QuantumTime"] <= PopedProcessFromAuxilary["RemainingTime"]:
            PopedProcessFromAuxilary["RemainingTime"] = PopedProcessFromAuxilary["RemainingTime"] - PopedProcessFromAuxilary["QuantumTime"]
            PopedProcessFromAuxilary["InputOutPutCycle"] = PopedProcessFromAuxilary["InputOutPutCycle"] - PopedProcessFromAuxilary["QuantumTime"]
            TimeSpent += PopedProcessFromAuxilary["QuantumTime"]
            PopedProcessFromAuxilary["FinishTime"] = TimeSpent
            PopedProcessFromAuxilary["QuantumTime"] = 4
            Processes[PopedProcessFromAuxilary["ProcessNumber"] - 1] = PopedProcessFromAuxilary
            ReadyQue.put(PopedProcessFromAuxilary)
            continue

        if PopedProcessFromAuxilary["RemainingTime"] <= PopedProcessFromAuxilary["InputOutPutCycle"] and PopedProcessFromAuxilary["QuantumTime"] > PopedProcessFromAuxilary["InputOutPutCycle"]:
            TimeSpent += PopedProcessFromAuxilary["RemainingTime"]
            PopedProcessFromAuxilary["FinishTime"] = TimeSpent
            PopedProcessFromAuxilary["RemainingTime"] = 0
            PopedProcessFromAuxilary["WaitingTime"] = PopedProcessFromAuxilary["FinishTime"] - PopedProcessFromAuxilary["BurstTime"] - PopedProcessFromAuxilary["ArrivalTime"]
            PopedProcessFromAuxilary["TurnAroundTime"] = PopedProcessFromAuxilary["FinishTime"] - PopedProcessFromAuxilary["ArrivalTime"]
            Processes[PopedProcessFromAuxilary["ProcessNumber"]-1] = PopedProcessFromAuxilary
            continue
        elif PopedProcessFromAuxilary["RemainingTime"] == PopedProcessFromAuxilary["InputOutPutCycle"] and PopedProcessFromAuxilary["QuantumTime"] == PopedProcessFromAuxilary["InputOutPutCycle"]:
            TimeSpent += PopedProcessFromAuxilary["RemainingTime"]
            PopedProcessFromAuxilary["FinishTime"] = TimeSpent
            PopedProcessFromAuxilary["RemainingTime"] = 0
            PopedProcessFromAuxilary["WaitingTime"] = PopedProcessFromAuxilary["FinishTime"] - PopedProcessFromAuxilary["BurstTime"] - PopedProcessFromAuxilary["ArrivalTime"]
            PopedProcessFromAuxilary["TurnAroundTime"] = PopedProcessFromAuxilary["FinishTime"] - PopedProcessFromAuxilary["ArrivalTime"]
            Processes[PopedProcessFromAuxilary["ProcessNumber"]-1] = PopedProcessFromAuxilary
        elif PopedProcessFromAuxilary["RemainingTime"] > PopedProcessFromAuxilary["InputOutPutCycle"] and PopedProcessFromAuxilary["QuantumTime"] < PopedProcessFromAuxilary["InputOutPutCycle"]:
            PopedProcessFromAuxilary["RemainingTime"] = PopedProcessFromAuxilary["RemainingTime"] - PopedProcessFromAuxilary["QuantumTime"]
            PopedProcessFromAuxilary["InputOutPutCycle"] = PopedProcessFromAuxilary["InputOutPutCycle"] - PopedProcessFromAuxilary["QuantumTime"]
            TimeSpent += PopedProcessFromAuxilary["QuantumTime"]
            PopedProcessFromAuxilary["FinishTime"] = TimeSpent
            PopedProcessFromAuxilary["QuantumTime"] = 4
            Processes[PopedProcessFromAuxilary["ProcessNumber"]-1] = PopedProcessFromAuxilary
            ReadyQue.put(PopedProcessFromAuxilary)

    if ReadyQue.empty() == False:
        PopedProcess = ReadyQue.get()
        if FlagForFirstProcess == False:
            TimeSpent= PopedProcess["ArrivalTime"]
            FlagForFirstProcess = True

        if PopedProcess["StartTime"]==-1:
            if PopedProcess["ArrivalTime"] > TimeSpent:
                IdelTimeToAdd = PopedProcess["ArrivalTime"] - TimeSpent
                TimeSpent += IdelTimeToAdd
            PopedProcess["StartTime"] = TimeSpent
            Processes[PopedProcess["ProcessNumber"]-1] = PopedProcess

        if PopedProcess["QuantumTime"] == 0:
            PopedProcess["QuantumTime"] == 4
            ReadyQue.put(PopedProcess)
            continue

        if PopedProcess["InputOutPutCycle"] == 0:
            PopedProcess["InputOutPutCycle"] == 3
            WaitingQue.put(PopedProcess)
            continue

        if PopedProcess["RemainingTime"] < PopedProcess["InputOutPutCycle"] and PopedProcess["QuantumTime"] <= PopedProcess["RemainingTime"]:
            PopedProcess["RemainingTime"] = PopedProcess["RemainingTime"] - PopedProcess["QuantumTime"]
            PopedProcess["InputOutPutCycle"] = PopedProcess["InputOutPutCycle"] - PopedProcess["QuantumTime"]
            TimeSpent += PopedProcess["QuantumTime"]
            PopedProcess["FinishTime"] = TimeSpent
            PopedProcess["QuantumTime"] = 4
            Processes[PopedProcess["ProcessNumber"] - 1] = PopedProcess
            ReadyQue.put(PopedProcess)

        if PopedProcess["RemainingTime"] <= PopedProcess["InputOutPutCycle"] and PopedProcess["QuantumTime"] > PopedProcess["InputOutPutCycle"]:
            TimeSpent += PopedProcess["RemainingTime"]
            PopedProcess["FinishTime"] = TimeSpent
            PopedProcess["RemainingTime"] = 0
            PopedProcess["WaitingTime"] = PopedProcess["FinishTime"] - PopedProcess["BurstTime"] - PopedProcess["ArrivalTime"]
            PopedProcess["TurnAroundTime"] = PopedProcess["FinishTime"] - PopedProcess["ArrivalTime"]
            Processes[PopedProcess["ProcessNumber"]-1] = PopedProcess
        elif PopedProcess["RemainingTime"] == PopedProcess["InputOutPutCycle"] and PopedProcess["QuantumTime"] == PopedProcess["InputOutPutCycle"]:
            TimeSpent += PopedProcess["RemainingTime"]
            PopedProcess["FinishTime"] = TimeSpent
            PopedProcess["RemainingTime"] = 0
            PopedProcess["WaitingTime"] = PopedProcess["FinishTime"] - PopedProcess["BurstTime"] - PopedProcess["ArrivalTime"]
            PopedProcess["TurnAroundTime"] = PopedProcess["FinishTime"] - PopedProcess["ArrivalTime"]
            Processes[PopedProcess["ProcessNumber"]-1] = PopedProcess
        elif PopedProcess["RemainingTime"] > PopedProcess["InputOutPutCycle"] and PopedProcess["QuantumTime"] < PopedProcess["InputOutPutCycle"]:
            PopedProcess["RemainingTime"] = PopedProcess["RemainingTime"] - PopedProcess["QuantumTime"]
            PopedProcess["InputOutPutCycle"] = PopedProcess["InputOutPutCycle"] - PopedProcess["QuantumTime"]
            TimeSpent += PopedProcess["QuantumTime"]
            PopedProcess["FinishTime"] = TimeSpent
            PopedProcess["QuantumTime"] = 4
            Processes[PopedProcess["ProcessNumber"]-1] = PopedProcess
            ReadyQue.put(PopedProcess)
        elif PopedProcess["RemainingTime"] > PopedProcess["InputOutPutCycle"] and PopedProcess["QuantumTime"] > PopedProcess["InputOutPutCycle"]:
            PopedProcess["RemainingTime"] = PopedProcess["RemainingTime"] - PopedProcess["InputOutPutCycle"]
            TimeSpent += PopedProcess["InputOutPutCycle"]
            PopedProcess["FinishTime"] = TimeSpent
            PopedProcess["InputOutPutCycle"] = 3
            Processes[PopedProcess["ProcessNumber"]-1] = PopedProcess
            WaitingQue.put(PopedProcess)

    

print("\n\n\nDetails:\n\nProcess Name\tStart Time\tFinish Time\tTurnAround Time\t Waiting Time")

for CompletedProcess in Processes:
    print ("Process # ",CompletedProcess["ProcessNumber"],"\t   ",CompletedProcess["StartTime"]," \t\t   ",CompletedProcess["FinishTime"],
           "\t\t  ",CompletedProcess["TurnAroundTime"]," \t\t\t   ",CompletedProcess["WaitingTime"])