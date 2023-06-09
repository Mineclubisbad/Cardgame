def generate_card_row(cards, hidden):
    rows = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    
    for card in cards:
        rows[0] += "\t ________________"
        rows[1] += "\t|                |"
        
        if card.value == '10':
            rows[2] += "\t|  {}            |".format(card.value)
        else:
            rows[2] += "\t|  {}             |".format(card.value)
        
        rows[3] += "\t|                |"
        rows[4] += "\t|                |"
        rows[5] += "\t|                |"
        rows[6] += "\t|                |"
        rows[7] += "\t|       {}        |".format(card.suit)
        rows[8] += "\t|                |"
        rows[9] += "\t|                |"
        
        if card.value == '10':
            rows[10] += "\t|            {}  |".format(card.value)
        else:
            rows[10] += "\t|            {}   |".format(card.value)
        
        rows[11] += "\t|________________|"
        rows[12] += "\t                "
    
    if hidden:
        rows[0] += "\t ________________"
        rows[1] += "\t|                |"
        rows[2] += "\t|                |"
        rows[3] += "\t|      * *       |"
        rows[4] += "\t|    *     *     |"
        rows[5] += "\t|   *       *    |"
        rows[6] += "\t|   *       *    |"
        rows[7] += "\t|          *     |"
        rows[8] += "\t|         *      |"
        rows[9] += "\t|        *       |"
        rows[10] += "\t|        *       |"
        rows[11] += "\t|          *     |"
        rows[12] += "\t|        *       |"
    
    return rows

def print_card_layout(rows):
    for row in rows:
        print(row)
    print()

cards = [...]  # Your list of cards
hidden = True  # Set to True if the card is hidden, False otherwise

rows = generate_card_row(cards, hidden)
print_card_layout(rows)
