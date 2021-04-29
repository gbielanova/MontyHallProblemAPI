from random import choice

for mode in ['change', 'keep']:
    win = 0
    lost = 0
    attempts = 1000

    for attempt in range(attempts):
        doors = [1, 2, 3]
        win_door = choice(doors)
        original_choice = choice(doors)
        host_choice = choice([door for door in doors if door not in [win_door, original_choice]])
        doors.remove(host_choice)

        if mode == 'keep':
            if win_door == original_choice:
                win += 1
            else:
                lost += 1
        elif mode == 'change':
            doors.remove(original_choice)
            new_choice = doors[0]
            if win_door == new_choice:
                win += 1
            else:
                lost += 1
        else:
            "Unsupported mode"

    print(f'Mode = {mode}, wins = {win}, lose = {lost}')
