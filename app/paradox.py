from random import choice


# mode in ['change', 'keep']
def simulate_paradox(mode, attempts):
    win = 0
    lost = 0

    for _ in range(attempts):
        doors = [1, 2, 3]
        win_door = choice(doors)
        original_choice = choice(doors)
        host_choice = choice([door for door in doors if door not in [win_door, original_choice]])
        doors.remove(host_choice)

        compare_door = original_choice
        if mode == 'change':
            doors.remove(original_choice)
            compare_door = doors[0]

        if win_door == compare_door:
            win += 1
        else:
            lost += 1

    return {
            'wins': win,
            'loose': lost
            }
