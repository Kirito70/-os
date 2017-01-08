def SJF(process_arrival_time_list,process_burst_time_list):
    print("\n\n\nDetails:\n\nProcess Name\t\tStart Time\t\tFinish Time\t\tTurnAround Time\t\t Waiting Time")

    process_start_time_list = [None] * total_processes
    process_finish_time_list = [None] * total_processes

    for process_number in range(0,total_processes):
        if process_number == 0:
            process_start_time_list[process_number] = process_arrival_time_list[0]
            process_finish_time_list[process_number] = process_start_time_list[0]+process_burst_time_list[0]
        else:
            process_start_time_list[process_number] = process_finish_time_list[(process_number-1)]
            process_finish_time_list[process_number] = process_finish_time_list[(process_number-1)] + process_burst_time_list[process_number]
        turn_around_time = process_finish_time_list[process_number]-process_arrival_time_list[process_number]
        waiting_time = process_start_time_list[process_number]-process_arrival_time_list[process_number]
        print ("Process # ",(process_number+1),"\t\t   ",process_start_time_list[process_number]," \t\t\t   ",process_finish_time_list[process_number],
               "\t\t\t  ",turn_around_time," \t\t\t\t   ",waiting_time)

print ("\t\t\tShortest Job First\n\n\n")

total_processes = int (input("\tEnter Total Number of processes you have: "))

process_arrival_time_list = [None] * total_processes
process_burst_time_list = [None] * total_processes
for process_number in range(0,total_processes):
    process_arrival_time = int (input("\tEnter Arrival time for process %d: " %(process_number+1)))
    process_burst_time = int (input("\tEnter Burst time for process %d: " %(process_number+1)))
    process_arrival_time_list[process_number] =  process_arrival_time
    process_burst_time_list[process_number] = process_burst_time

for index in range(0,total_processes):
    for index2 in range(0,total_processes):
        if process_arrival_time_list[index] <= process_arrival_time_list[index2]:
            arrival_time_temp = process_arrival_time_list[index]
            burst_time_temp = process_burst_time_list[index]
            process_arrival_time_list[index] =  process_arrival_time_list[index2]
            process_burst_time_list[index] = process_burst_time_list[index2]
            process_arrival_time_list[index2] = arrival_time_temp
            process_burst_time_list[index2] = burst_time_temp

for index in range(0,total_processes):
    for index2 in range(0,total_processes):
        if process_arrival_time_list[index] == process_arrival_time_list[index2]:
            if process_burst_time_list[index] <= process_burst_time_list[index2]:
                arrival_time_temp = process_arrival_time_list[index]
                burst_time_temp = process_burst_time_list[index]
                process_arrival_time_list[index] = process_arrival_time_list[index2]
                process_burst_time_list[index] = process_burst_time_list[index2]
                process_arrival_time_list[index2] = arrival_time_temp
                process_burst_time_list[index2] = burst_time_temp

SJF(process_arrival_time_list,process_burst_time_list)

#print(process_burst_time_list)
#print(process_arrival_time_list)