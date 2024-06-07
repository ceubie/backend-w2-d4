# 2. Python Programming Challenges for Customer Service Data Handling

# Objective: This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

#     Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).

#     Implement functions to:

#         Open a new service ticket.

#         Update the status of an existing ticket  to "closed".

#         Display all tickets.

#           (Bonus) filter by status

#     Initialize with some sample tickets and include functionality for additional ticket entry.



#----------------------------------------------------------------------------------------------------------------------


service_tickets = {
     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"},
     "Ticket003": {"Customer": "Steve", "Issue": "Login problem", "Status": "open"},
     "Ticket004": {"Customer": "Megatron", "Issue": "Payment issue", "Status": "closed"},
 }

#----------------------------------------------------------------------------------------------------------------------

def open():
    while True:
        userinput = input(""" 
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                
              Would you like to:
                          
              1. add a ticket
              2. go back 

              --Select a number--
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~            
                          """)
        if userinput == "1":
            tix_num = len(service_tickets) + 1

            placeholder = "00"
            tix_num = str(tix_num)
            z = 'Ticket' + placeholder + tix_num
            
            service_tickets.update({z:{"Customer" : input("What is your name?"), 
                                       "Issue" : input("What is your issue?"), 
                                       "Status" : "open"}})
            
            return service_tickets
            
        elif userinput == "2":
            break
        else:
            print("Please select a valid number!")
        
#----------------------------------------------------------------------------------------------------------------------

def close():
     while True:
        y = input(""" 
              Would you like to:
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                
              1. close a ticket
              2. go back 

              --Select a number--
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
                  """)
        if y == "1":
                x = "Ticket" + input("What is your ticket number? ")
                service_tickets[x]["Status"] = "closed"
        elif y == "2":
            break
        else:
            print("Please select a valid number!")

#----------------------------------------------------------------------------------------------------------------------

def sort():
    for tickets in service_tickets:
            if "open" in service_tickets[tickets]["Status"]:
                print(tickets)
    for tickets in service_tickets:
            if "closed" in service_tickets[tickets]["Status"]:
                print(tickets)


#----------------------------------------------------------------------------------------------------------------------

def ticket():
    while True:
        userinput = input("""
                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    

                          Welcome to ticket support. Would you like to: 

                          1. open a ticket
                          2. close a ticket
                          3. display all tickets
                          4. Sort tickets by status
                          5. exit

                          --Select a number-- 
                          
                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
                          """
                          )
        if userinput == "1":
            open()
        elif userinput == "2":
           close()
        elif userinput == "3":
            print(service_tickets)
        elif userinput == "4":
            sort()
        elif userinput == "5":
            break
        else:
            print("Please select a valid number!")
        
#----------------------------------------------------------------------------------------------------------------------

