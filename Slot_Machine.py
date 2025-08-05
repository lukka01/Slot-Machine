MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [ [], [], [] ]

    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(columns[0]):
        for i, column in enumerate(columns):
            print(column[row])
            if i != len(columns) - 1:
                print(column[row], '|')
            else:
                print(column[row])


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        try:
            amount = float(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0")
        except ValueError:
            print("Please enter a valid number.")



def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1- " + str(MAX_LINES) + ")? ")
        try:
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("number of lines must be  between 1 and 3")
        except ValueError:
            print("Please enter a valid line number.")


def get_bet():
    while True:
        bet = input("What would you like to bet? $")
        try:
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print(f"amount of bet must be between {MIN_BET}, {MAX_BET}")
        except ValueError:
            print("Please enter a valid amount.")


def main():

    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Ypu dont have enough, your current balance is: ${balance}")
        else:
            break

    print(f"You have bet {bet} on {lines} lines. Total bet - ${total_bet} ")

if __name__ == '__main__':
    main()