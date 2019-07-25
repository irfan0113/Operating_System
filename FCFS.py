process_due = []
total_wtime = 0

n = int(input('Enter the number of processes: '))

for i in range(n):
    process_due.append([])
    process_due[i].append(input("Enter P_name: "))
    process_due[i].append(int(input('Enter P_arrival: ')))
    total_wtime += process_due[i][1]
    process_due[i].append(int(input('Enter P_bust: ')))
    
process_due.sort(key = lambda process_due:process_due[1])

print('\nProcessName\tArrivalTime\tBurstTime')

for i in range(n):
    print(process_due[i][0],'\t\t', process_due[i][1],'\t\t', process_due[i][2])
    
print('Total waiting time: ', total_wtime)
print('Average waiting time: ', total_wtime/n)