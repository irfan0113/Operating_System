def findWaitingTime(process, n, bt, wt, at):
    
    service_time = [0] * n
    service_time[0] = 0
    wt[0] = 0
    
    for i in range(1,n):
        service_time[i] = service_time[i-1] + bt[i-1]
        wt[i] = service_time[i] - at[i]
        
        if wt[i]<0:
            wt[i] = 0

def findTurnAroundTime(process, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def findAvgTime(process, n, bt, at):
    
    wt = [0] * n
    tat = [0] * n
    
    findWaitingTime(process, n, bt, wt, at)
    findTurnAroundTime(process, n, bt, wt, tat)
    
    total_wt = 0
    total_tat = 0
    
    print("Processes   Burst Time   Arrival Time     Waiting",  
          "Time   Turn-Around Time  Completion Time \n")
    
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        complete_time = tat[i] + at[i]
    
        print(" ", i + 1, "\t\t", bt[i], "\t\t", at[i],  
                "\t\t", wt[i], "\t\t ", tat[i], "\t\t ", complete_time)
    
    print("Average waiting time = %.5f "%(total_wt /n)) 
    print("\nAverage turn around time = ", total_tat / n)



if __name__ == "__main__":
    
    process = [1,2,3]
    n = 3
    
    burst_time = [5,9,6]
    
    arrival_time = [0,3,6]
    
    findAvgTime(process, n, burst_time, arrival_time)