movieTicketPrice = float(input("Enter the Price: "))
GST = 18
GSTAmount = (movieTicketPrice*(GST/100))
TotalAmount = (movieTicketPrice + GSTAmount)
print(f"Total Price of Movie Ticket (including GST) is: {TotalAmount}")
