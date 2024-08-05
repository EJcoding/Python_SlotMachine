import random  # Import the random module for random number generation

# Constants for maximum number of lines, bets, and dimensions of the slot machine
MAX_LINES = 3  # Maximum number of lines the player can bet on
MAX_BET = 100  # Maximum bet per line
MIN_BET = 1    # Minimum bet per line

ROWS = 3  # Number of rows in the slot machine
COLS = 3  # Number of columns in the slot machine

# Define the symbol counts and their corresponding values
symbol_count = {
    "A": 2,  # Number of 'A' symbols in the slot machine
    "B": 4,  # Number of 'B' symbols in the slot machine
    "C": 6,  # Number of 'C' symbols in the slot machine
    "D": 8   # Number of 'D' symbols in the slot machine
}

symbol_value = {
    "A": 5,  # Value of 'A' symbol when part of a winning line
    "B": 4,  # Value of 'B' symbol when part of a winning line
    "C": 3,  # Value of 'C' symbol when part of a winning line
    "D": 2   # Value of 'D' symbol when part of a winning line
}

# Check the winnings based on the slot machine columns and lines bet on
def check_winnings(columns, lines, bet, values):
    winnings = 0  # Initialize the total winnings
    winning_lines = []  # Initialize the list of winning lines
    for line in range(lines):  # Loop over each line the player has bet on
        symbol = columns[0][line]  # Get the symbol in the first column of the current line
        for column in columns:  # Check all columns for the same symbol in the current line
            symbol_to_check = column[line]  # Get the symbol in the current column and line
            if symbol != symbol_to_check:  # If symbols do not match, break out of the loop
                break
        else:  # If the loop wasn't broken, all symbols in the line are the same
            winnings += values[symbol] * bet  # Add the winnings for this line
            winning_lines.append(line + 1)  # Add this line to the list of winning lines
                
    return winnings, winning_lines  # Return the total winnings and the list of winning lines

# Generate the items in the slot machine based on rows, columns, and symbols
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []  # List to hold all the symbols in the slot machine
    for symbol, symbol_count in symbols.items():  # Loop over each symbol and its count
        for i in range(symbol_count):  # Add the symbol to the list for its count
            all_symbols.append(symbol)
            
    columns = []  # List to hold the columns of the slot machine
    for i in range(cols):  # Loop over the number of columns
        column = []  # List to hold the symbols in the current column
        current_symbols = all_symbols[:]  # Copy the list of all symbols
        for j in range(rows):  # Loop over the number of rows
            value = random.choice(current_symbols)  # Randomly select a symbol
            current_symbols.remove(value)  # Remove the selected symbol from the list
            column.append(value)  # Add the selected symbol to the column
            
        columns.append(column)  # Add the column to the list of columns
        
    return columns  # Return the list of columns

# Print the slot machine columns in a readable format
def print_slot_machine(columns):
    for row in range(len(columns[0])):  # Loop over each row
        for i, column in enumerate(columns):  # Loop over each column
            if i != len(columns) - 1:  # If not the last column, add a separator
                print(column[row], end=" | ")
            else:  # If the last column, do not add a separator
                print(column[row], end="")
        
        print()  # Print a newline after each row

# Ask the user to input an amount to deposit and return it
def deposit():
    while True:  # Loop until a valid amount is entered
        amount = input("What would you like to deposit? $")  # Ask the user to input an amount
        if amount.isdigit():  # Check if the input is a digit
            amount = int(amount)  # Convert the input to an integer
            if amount > 0:  # Check if the amount is greater than 0
                break  # Exit the loop if the amount is valid
            else:
                print("Amount must be greater than 0.")  # Print an error message
        else:
            print("Please enter a number.")  # Print an error message
    
    return amount  # Return the valid amount

# Ask the user to input the number of lines to bet on and return it
def get_number_of_lines():
    while True:  # Loop until a valid number of lines is entered
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")  # Ask the user to input the number of lines
        if lines.isdigit():  # Check if the input is a digit
            lines = int(lines)  # Convert the input to an integer
            if 1 <= lines <= MAX_LINES:  # Check if the number of lines is within the valid range
                break  # Exit the loop if the number of lines is valid
            else:
                print("Enter valid number of lines.")  # Print an error message
        else:
            print("Please enter a number.")  # Print an error message
    
    return lines  # Return the valid number of lines

# Ask the user to input the bet amount for each line and return it
def get_bet():
    while True:  # Loop until a valid bet amount is entered
        amount = input("What would you like to bet on each line? $")  # Ask the user to input the bet amount
        if amount.isdigit():  # Check if the input is a digit
            amount = int(amount)  # Convert the input to an integer
            if MIN_BET <= amount <= MAX_BET:  # Check if the bet amount is within the valid range
                break  # Exit the loop if the bet amount is valid
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")  # Print an error message
        else:
            print("Please enter a number.")  # Print an error message
    
    return amount  # Return the valid bet amount

# Perform a spin, calculate winnings, and return the net change in balance
def spin(balance):
    lines = get_number_of_lines()  # Get the number of lines to bet on
    while True:  # Loop until a valid total bet is entered
        bet = get_bet()  # Get the bet amount for each line
        total_bet = bet * lines  # Calculate the total bet
        
        if total_bet > balance:  # Check if the total bet exceeds the balance
            print(f"Insufficient funds. Your current balance is: ${balance}")  # Print an error message
        else:
            break  # Exit the loop if the total bet is valid
        
    print(f"Your are betting ${bet} on {lines} lines. Total bet equals: ${total_bet}")  # Print the betting details
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)  # Generate the slot machine spin
    print_slot_machine(slots)  # Print the slot machine spin
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)  # Calculate the winnings
    print(f"You won: ${winnings}.")  # Print the winnings
    print(f"You won on lines:", *winning_lines)  # Print the winning lines
    return winnings - total_bet  # Return the net change in balance

# Main function to run the slot machine game
def main():
    balance = deposit()  # Get the initial deposit amount from the user
    while True:  # Loop until the user chooses to quit
        print(f"Current balance is ${balance}")  # Print the current balance
        answer = input("Press enter to play or 'q' to quit.")  # Ask the user to play or quit
        if answer == "q":  # Check if the user wants to quit
            break  # Exit the loop if the user wants to quit
        balance += spin(balance)  # Perform a spin and update the balance

    print(f"You left with ${balance}")  # Print the final balance

# Run the main function
main()  # Call the main function to start the game
