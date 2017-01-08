

import queue as Queue

def RR(processes):
    ready_que = Queue.Queue()
    waiting_que = Queue.Queue()

    for process in processes:
        ready_que.put(process)

    #while ready_que.empty() == False:
    #    print(ready_que.get())

    flag_for_first_process=False
    time_spent=0

    while waiting_que.empty() == False or ready_que.empty() == False:
        if ready_que.empty() == False:
            poped_process = ready_que.get()
            if flag_for_first_process == False:
                time_spent= poped_process["ArrivalTime"]
                flag_for_first_process = True

            if poped_process["StartTime"]==-1:
                if poped_process["ArrivalTime"] > time_spent:
                    IdelTimeToAdd = poped_process["ArrivalTime"] - time_spent
                    time_spent += IdelTimeToAdd
                poped_process["StartTime"] = time_spent
                processes[poped_process["ProcessNumber"]-1] = poped_process

            if poped_process["QuantumTime"] == 0:
                poped_process["QuantumTime"] == 4
                ready_que.put(poped_process)
                continue

            if poped_process["InputOutPutCycle"] == 0:
                poped_process["InputOutPutCycle"] == 3
                waiting_que.put(poped_process)
                continue

            if poped_process["RemainingTime"] < poped_process["InputOutPutCycle"] and poped_process["QuantumTime"] <= poped_process["RemainingTime"]:
                poped_process["RemainingTime"] = poped_process["RemainingTime"] - poped_process["QuantumTime"]
                poped_process["InputOutPutCycle"] = poped_process["InputOutPutCycle"] - poped_process["QuantumTime"]
                time_spent += poped_process["QuantumTime"]
                poped_process["FinishTime"] = time_spent
                poped_process["QuantumTime"] = 4
                processes[poped_process["ProcessNumber"] - 1] = poped_process
                ready_que.put(poped_process)

            if poped_process["RemainingTime"] <= poped_process["InputOutPutCycle"] and poped_process["QuantumTime"] > poped_process["InputOutPutCycle"]:
                time_spent += poped_process["RemainingTime"]
                poped_process["FinishTime"] = time_spent
                poped_process["RemainingTime"] = 0
                poped_process["WaitingTime"] = poped_process["FinishTime"] - poped_process["BurstTime"] - poped_process["ArrivalTime"]
                poped_process["TurnAroundTime"] = poped_process["FinishTime"] - poped_process["ArrivalTime"]
                processes[poped_process["ProcessNumber"]-1] = poped_process
            elif poped_process["RemainingTime"] == poped_process["InputOutPutCycle"] and poped_process["QuantumTime"] == poped_process["InputOutPutCycle"]:
                time_spent += poped_process["RemainingTime"]
                poped_process["FinishTime"] = time_spent
                poped_process["RemainingTime"] = 0
                poped_process["WaitingTime"] = poped_process["FinishTime"] - poped_process["BurstTime"] - poped_process["ArrivalTime"]
                poped_process["TurnAroundTime"] = poped_process["FinishTime"] - poped_process["ArrivalTime"]
                processes[poped_process["ProcessNumber"]-1] = poped_process
            elif poped_process["RemainingTime"] > poped_process["InputOutPutCycle"] and poped_process["QuantumTime"] < poped_process["InputOutPutCycle"]:
                poped_process["RemainingTime"] = poped_process["RemainingTime"] - poped_process["QuantumTime"]
                poped_process["InputOutPutCycle"] = poped_process["InputOutPutCycle"] - poped_process["QuantumTime"]
                time_spent += poped_process["QuantumTime"]
                poped_process["FinishTime"] = time_spent
                poped_process["QuantumTime"] = 4
                processes[poped_process["ProcessNumber"]-1] = poped_process
                ready_que.put(poped_process)
            elif poped_process["RemainingTime"] > poped_process["InputOutPutCycle"] and poped_process["QuantumTime"] > poped_process["InputOutPutCycle"]:
                poped_process["RemainingTime"] = poped_process["RemainingTime"] - poped_process["InputOutPutCycle"]
                time_spent += poped_process["InputOutPutCycle"]
                poped_process["FinishTime"] = time_spent
                poped_process["InputOutPutCycle"] = 3
                processes[poped_process["ProcessNumber"]-1] = poped_process
                waiting_que.put(poped_process)

        if waiting_que.empty() != True:
            foped_fromwaiting_queue = waiting_que.get()
            if poped_from_waiting_queue["FinishTime"] + 10 <= time_spent:
                ready_que.put(poped_from_waiting_queue)
            elif poped_process["FinishTime"] + 10 > time_spent and ready_que.empty() == True:
                remaining_time = (poped_from_waiting_queue["FinishTime"] + 10) - time_spent
                time_spent += remaining_time
                ready_que.put(poped_from_waiting_queue)
            else:
                other_elements = []
                while waiting_que.empty() != True:
                    other_elements.append(waiting_que.get())
                waiting_que.put(poped_From_waiting_queue)
                if len(other_elements) > 0:
                    for process_in_other in other_elements:
                        waiting_que.put(process_in_other)
    return process

print ("\t\t\tRound Robin Scheduling\n\n\n")

print("\t\tQuantum Time is: 4 sec")
print("\t\tInput Time for Process is: 10 sec")
print("\t\tInputOutput Cycle Time for Process is: 3 sec\n\n")

total_processes = int (input("\tEnter Total Number of processes you have: "))

processes = [{"ProcessNumber":0,"ArrivalTime": 0,"BurstTime":0,"FinishTime":0,"StartTime":-1,"WaitingTime":0,"QuantumTime":4,"InputOutPutCycle":3,
              "RemainingTime":0,"TurnAroundTime":0} for index in range(0,total_processes)]

for process_number in range(0,total_processes):
    process_arrival_time = int (input("\tEnter Arrival time for process %d: " %(process_number+1)))
    process_burst_time = int (input("\tEnter Burst time for process %d: " %(process_number+1)))
    processes[process_number]["ArrivalTime"] = process_arrival_time
    processes[process_number]["BurstTime"] = process_burst_time
    processes[process_number]["RemainingTime"] = process_burst_time

processes.sort(key=lambda x:(x['ArrivalTime']))

for process_number in range(0,total_processes):
    processes[process_number]["ProcessNumber"] = process_number+1


print("\n\n\nDetails:\n\nProcess Name\tStart Time\tFinish Time\tTurnAround Time\t Waiting Time")

returned_process = RR(processes)

for completed_process in returned_process:
    print ("Process # ",completed_process["ProcessNumber"],"\t   ",completed_process["StartTime"]," \t\t   ",completed_process["FinishTime"],
           "\t\t  ",completed_process["TurnAroundTime"]," \t\t\t   ",completed_process["WaitingTime"])