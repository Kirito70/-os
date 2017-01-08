def priority_schedualling(process_arrival_time_list,process_burst_time_list,process_priority_list):
    print("\n\n\nDetails:\n\n Process Name \t\t  Priority \t\t Start Time\t\tFinish Time\t\tTurnAround Time\t\t Waiting Time")

    process_start_time_list = [None] * total_processes
    process_finish_time_list = [None] * total_processes

    for process_number in range(0,total_processes):
        if process_number == 0:
            process_start_time_list[process_number] = process_arrival_time_list[0]
            process_finish_time_list[process_number] = process_start_time_list[0]+process_burst_time_list[0]
        else:
            process_start_time_list[process_number] = process_finish_time_list[(process_number-1)]
            process_finish_time_list[process_number] = process_finish_time_list[(process_number-1)] + process_burst_time_list[process_number]
        turnAround_time = process_finish_time_list[process_number] - process_arrival_time_list[process_number]
        waiting_time = process_start_time_list[process_number] - process_arrival_time_list[process_number]
        print ("Process # ",(process_number+1),"\t\t ",(process_priority_list[process_number]),"\t\t   ",process_start_time_list[process_number]," \t\t\t   ",process_finish_time_list[process_number],
               "\t\t\t  ",turnAround_time," \t\t\t\t   ",waiting_time)

print ("\t\t\tPriority Scheduling\n\n\n")

total_processes = int (input("\tEnter Total Number of processes you have: "))

process_arrival_time_list = [None] * total_processes
process_burst_time_list = [None] * total_processes
process_priority_list = [None] * total_processes
for process_number in range(0,total_processes):
    process_arrival_time = int (input("\tEnter Arrival time for process %d: " %(process_number+1)))
    process_burst_time = int (input("\tEnter Burst time for process %d: " %(process_number+1)))
    process_priority = int (input("\tEnter Priority for Process %d: " %(process_number+1)))
    process_arrival_time_list[process_number] =  process_arrival_time
    process_burst_time_list[process_number] = process_burst_time
    process_priority_list[process_number] = process_priority

for index in range(0,total_processes):
    for index2 in range(0,total_processes):
        if process_arrival_time_list[index] <= process_arrival_time_list[index2]:
            arrival_time_temp = process_arrival_time_list[index]
            burst_time_temp = process_burst_time_list[index]
            priority_temp = process_priority_list[index]
            process_arrival_time_list[index] =  process_arrival_time_list[index2]
            process_burst_time_list[index] = process_burst_time_list[index2]
            process_priority_list[index] = process_priority_list[index2]
            process_arrival_time_list[index2] = arrival_time_temp
            process_burst_time_list[index2] = burst_time_temp
            process_priority_list[index2]= priority_temp

for process_number in range(0,total_processes):
    sorted_process_counter = process_number + 1
    for process_number2 in range(process_number,total_processes):
        if(process_arrival_time_list[process_number]+process_burst_time_list[process_number])>process_arrival_time_list[process_number2]:
            for priority_sorter in range(process_number,sorted_process_counter):
                if process_priority_list[process_number2]<= process_priority_list[priority_sorter]:
                    arrival_time_temp = process_arrival_time_list[process_number2]
                    burst_time_temp = process_burst_time_list[process_number2]
                    priority_temp = process_priority_list[process_number2]
                    process_arrival_time_list[process_number2] = process_arrival_time_list[priority_sorter]
                    process_burst_time_list[process_number2] = process_burst_time_list[priority_sorter]
                    process_priority_list[process_number2] = process_priority_list[priority_sorter]
                    process_arrival_time_list[priority_sorter] = arrival_time_temp
                    process_burst_time_list[priority_sorter] = burst_time_temp
                    process_priority_list[priority_sorter] = priority_temp
            sorted_process_counter = sorted_process_counter+1

priority_schedualling(process_arrival_time_list,process_burst_time_list,process_priority_list)