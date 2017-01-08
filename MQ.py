import queue as Queue

def MQ(all_processes):
    high_priority_queue = Queue.Queue()
    medium_priority_queue = Queue.Queue()
    low_priority_queue = Queue.Queue()

    time_spent = 0
    loop_flag = False
    count_for_process_added_to_queues = 0

    while high_priority_queue.empty() == False or medium_priority_queue.empty() == False or low_priority_queue.empty() == False or loop_flag==False:
        loop_flag = True
        for process_in_original_queue in all_processes:
            if process_in_original_queue["arrival_time"] <= time_spent:
                if process_in_original_queue["burst_time"] < 4:
                    high_priority_queue.put(process_in_original_queue)
                    count_for_process_added_to_queues +=1
                    continue
                elif process_in_original_queue["burst_time"] >= 4 and process_in_original_queue["burst_time"] < 7:
                    medium_priority_queue.put(process_in_original_queue)
                    count_for_process_added_to_queues +=1
                    continue
                else:
                    low_priority_queue.put(process_in_original_queue)
                    count_for_process_added_to_queues +=1
            else:
                if process_in_original_queue["burst_time"] < 4:
                    diffrence_in_time = process_in_original_queue["arrival_time"]-time_spent
                    time_spent+=diffrence_in_time
                    high_priority_queue.put(process_in_original_queue)
                    count_for_process_added_to_queues +=1
                    continue
                elif process_in_original_queue["burst_time"] >= 4 and process_in_original_queue["burst_time"] < 7:
                    diffrence_in_time = process_in_original_queue["arrival_time"]-time_spent
                    time_spent+=diffrence_in_time
                    medium_priority_queue.put(process_in_original_queue)
                    count_for_process_added_to_queues +=1
                    continue
                else:
                    diffrence_in_time = process_in_original_queue["arrival_time"]-time_spent
                    time_spent+=diffrence_in_time
                    low_priority_queue.put(process_in_original_queue)
                    count_for_process_added_to_queues +=1

        if(high_priority_queue.empty() == False):
            poped_from_high_queue = high_priority_queue.get()
            if(time_spent == 0):
                time_spent = poped_from_high_queue["arrival_time"]
                poped_from_high_queue["start_time"] = poped_from_high_queue["arrival_time"]
                time_spent += poped_from_high_queue["burst_time"]
                poped_from_high_queue["finish_time"] = time_spent
                poped_from_high_queue["turn_around_time"] = poped_from_high_queue["finish_time"] - poped_from_high_queue["arrival_time"]
                poped_from_high_queue["waiting_time"] = poped_from_high_queue["finish_time"] - poped_from_high_queue["start_time"]
            elif:
        

print ("\t\t\tMulti Queue Schedualing\n\n\n")

total_processes = int (input("\tEnter Total Number of processes you have: "))

all_processes = [{"process_number":0,"arrival_time": 0,"burst_time":0,"finish_time":0,"sart_time":-1,"waiting_time":0,"quantum_time":4,
              "remaining_time":0,"turn_around_time":0} for index in range(0,total_processes)]

for process_number in range(0,total_processes):
    process_arrival_time = int (input("\tEnter Arrival time for process %d: " %(process_number+1)))
    processBurstTime = int (input("\tEnter Burst time for process %d: " %(process_number+1)))
    all_processes[processNumber]["arrival_time"] = process_arrival_time
    all_processes[process_number]["burst_time"] = process_burst_time
    all_processes[process_number]["remaining_time"] = process_burst_time

all_processes.sort(key=lambda x:(x['arrival_time']))

for process_number in range(0,total_processes):
    all_processes[process_number]["process_number"] = process_number+1



