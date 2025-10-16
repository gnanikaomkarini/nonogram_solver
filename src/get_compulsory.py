from get_all_possible_placements import get_all_possible_placements

def get_compulsory(hint : list[int], current : list[str]) -> list[str]:
    if not hint or (len(hint) == 1 and hint[0] == 0):
        return ["." if c == " " else c for c in current]
    
    all_placements = get_all_possible_placements(hint, current)
    if not all_placements:
        return current
    
    result = current[:]
    for i in range(len(current)):
        if current[i] == " ":
            values = set(placement[i] for placement in all_placements)
            if len(values) == 1:
                result[i] = values.pop()
    
    return result