def get_all_possible_placements(hint : list[int], current : list[str]) -> list[list[str]]:
    n = len(current)
    if not hint or (len(hint) == 1 and hint[0] == 0):
        return [["." if c == " " else c for c in current]]
    
    def can_place_block(start, size):
        if start + size > n:
            return False
        for i in range(start, start + size):
            if current[i] == ".":
                return False
        return True
    
    def can_place_empty(pos):
        return pos >= n or current[pos] != "#"
    
    def generate(pos, block_idx, placement):
        if block_idx == len(hint):
            while pos < n:
                if current[pos] == "#":
                    return []
                placement.append(".")
                pos += 1
            return [placement[:]]
        
        if pos >= n:
            return []
        
        results = []
        block_size = hint[block_idx]
        remaining_blocks = hint[block_idx + 1:]
        min_remaining_space = sum(remaining_blocks) + len(remaining_blocks)
        
        max_start = n - block_size - min_remaining_space
        
        for start in range(pos, max_start + 1):
            if not can_place_block(start, block_size):
                continue
            
            valid = True
            for i in range(pos, start):
                if current[i] == "#":
                    valid = False
                    break
            
            if not valid:
                continue
            
            new_placement = placement[:]
            for i in range(pos, start):
                new_placement.append(".")
            for i in range(block_size):
                new_placement.append("#")
            
            next_pos = start + block_size
            if block_idx < len(hint) - 1:
                if next_pos < n and not can_place_empty(next_pos):
                    continue
                if next_pos < n:
                    new_placement.append(".")
                    next_pos += 1
            
            results.extend(generate(next_pos, block_idx + 1, new_placement))
        
        return results
    
    return generate(0, 0, [])