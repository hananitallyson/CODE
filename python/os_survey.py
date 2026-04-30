print("\n-------- OPERATING SYSTEM SURVEY --------")

linux_votes = 0
macos_votes = 0
windows_votes = 0

vote_loop = input("\nWould you like to respond to the survey?\nEnter your answer (Y/n): ").upper()

while vote_loop == "Y" or vote_loop == "":
    question_loop = True
    while question_loop:
        print("\n(1) Linux\n(2) MacOS\n(3) Windows")
        vote = int(input("Enter your vote (1/2/3): "))

        if vote == 1:
            linux_votes += 1
            question_loop = False
        elif vote == 2:
            macos_votes += 1
            question_loop = False
        elif vote == 3:
            windows_votes += 1
            question_loop = False
        else:
            print("\nError: invalid option.")

    vote_loop = input("\nWould you like to respond to the survey?\nEnter your answer (Y/n): ").upper()

total_votes = linux_votes + macos_votes + windows_votes

linux_percentage = linux_votes / total_votes * 100
macos_percentage = macos_votes / total_votes * 100
windows_percentage = windows_votes / total_votes * 100

print("\n-------- SURVEY RESULTS --------")
print(f"\nTOTAL -> {total_votes} | Linux -> {linux_votes} @ {linux_percentage}% | MacOS -> {macos_votes} @ {macos_percentage}% | Windows -> {windows_votes} @ {windows_percentage}%\n")

print("\n[WINNER OS]")
if linux_percentage > macos_votes:
    print(f"Linux @ {linux_percentage}% of the votes\n")    
else:
    if macos_votes > windows_votes:
        print(f"MacOS @ {macos_votes}% of the votes\n")        
    else:
        print(f"Windows @ {windows_percentage}% of the votes\n")
