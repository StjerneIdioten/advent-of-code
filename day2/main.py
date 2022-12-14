import sys
import os

if __name__ == "__main__":

    scoring_card_1 = {
                "AX": 1 + 3, # Rock = Rock 
                "AY": 2 + 6, # Rock < Paper
                "AZ": 3 + 0, # Rock > Scissors
                "BX": 1 + 0, # Paper > Rock
                "BY": 2 + 3, # Paper = Paper
                "BZ": 3 + 6, # Paper < Scissors
                "CX": 1 + 6, # Scissors < Rock
                "CY": 2 + 0, # Scissors > Paper
                "CZ": 3 + 3  # Scissors = Scissors
                }

    scoring_card_2 = {
                "AX": 3 + 0, # Rock > Scissors
                "AY": 1 + 3, # Rock = Rock
                "AZ": 2 + 6, # Rock < Paper
                "BX": 1 + 0, # Paper > Rock
                "BY": 2 + 3, # Paper = Paper
                "BZ": 3 + 6, # Paper < Scissors
                "CX": 2 + 0, # Scissors > Paper
                "CY": 3 + 3, # Scissors = Scissors
                "CZ": 1 + 6  # Scissors < rock
                }

    with open(os.path.join(sys.path[0], "data")) as file:
        total_score_1 = 0
        total_score_2 = 0
        while (line := file.readline()):
            round = "".join([line[i] for i in [0,2]])
            total_score_1 += scoring_card_1[round]
            total_score_2 += scoring_card_2[round]
        print(f"1: {total_score_1}, 2: {total_score_2}")