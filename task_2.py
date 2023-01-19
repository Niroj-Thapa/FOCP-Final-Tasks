print("Park Run Timer\n~~~~~~~~~~~~~~\nLet's go!")

runners = []
time = []

while True:
    data = input(">")
    #Check if the input is "END"
    if data == "END":
        break
    else:
        try:
            data = data.split("::")
            runner1 = int(data[0])
            time1 = int(data[1])
            runners.append(runner1)
            time.append(time1)
        except:
            print("Error in data stream. Ignorning. Carry on.")
    continue
   
try:
    # Function to convert time from seconds to minutes and seconds
    def process_time(time_in_seconds):
        minutes = time_in_seconds // 60
        seconds = time_in_seconds % 60
        return (minutes, seconds)

    #Find average time, fastest time and slowest time
    average_time = sum(time)/len(time)
    fastest_time = min(time)
    slowest_time = max(time)

    #Convert time from seconds to minutes and seconds of average_time, fastest_time and slowest_time
    average_time1 = process_time(average_time)
    fastest_time1 = process_time(fastest_time)
    slowest_time1 = process_time(slowest_time)

    #Find the best runner with the fastest time
    place = time.index(fastest_time)
    best_runner = runners[place]

    #Print all the final data
    print(f"Total Runners: {len(runners)}")
    print(f"Average Time: {average_time1[0]:.0f} minutes, {average_time1[1]:.0f} seconds ")
    print(f"Fastest Time: {fastest_time1[0]} minutes, {fastest_time1[1]} seconds ")
    print(f"Slowest Time: {slowest_time1[0]} minutes, {slowest_time1[1]} seconds ")
    print(f"Best time Here: Runner #{best_runner}")
    
except:
    print("No data found. Nothing to do. What a pity.") 



   



            
