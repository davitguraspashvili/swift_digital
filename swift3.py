def cast_bombs_to_seconds(grid): #bombermans second job
    new_grid = []
    for row in grid:             #cast bombs to seconds
        if "O" in row:
            new_row = row.replace("O", "1")
            new_grid.append(new_row)
        else: new_grid.append(row)
    
    return new_grid

def recursion(n, grid): 
    if n == 0:
        return grid
    n -= 1
    for row in grid:            #bombermans third job
        index_of_row = grid.index(row)
        if "1" in row:
            row = row.replace("1", "2") 

        if "0" in row:
            row = row.replace("0", "1")

        if "." in row:
            row = row.replace(".", "0")

        grid[index_of_row] = row    

    if n == 0:
        return grid
    n -= 1
    grid = detonate(grid)

    return recursion(n, grid)

def detonate(grid):              #bombermans fourth job
    for row in grid:
        if "2" in row:
            index_of_row = grid.index(row)
            index_of_bombs = [row.index(i) for i in row if i == "2"]

            for i in index_of_bombs:

                if index_of_row < len(grid) - 1:
                    try:
                        bottom_row = grid[index_of_row+1]
                    except: pass

                if index_of_row > 0:
                    try: 
                        top_row = grid[index_of_row-1]
                    except: pass
                
                try:                 #trying to destroy bottom side of bomb
                    bottom_row = list(bottom_row)
                    bottom_row[i] = "."
                except: pass

                try:                 #trying to destroy top side of bomb
                    top_row = list(top_row)
                    top_row[i] = "."
                except: pass

                if i > 0:
                    try:
                        row = list(row) 
                        row[i-1] = "."   #trying to destroy left side of bomb
                    except: pass
                
                try:
                    row = list(row)
                    row[i+1] = "."   #trying to destroy right side of bomb
                except: pass
            
                row = "".join(row).replace("2", ".")

                try:
                    bottom_row = "".join(bottom_row)
                except: pass

                try:
                    top_row = "".join(top_row)
                except: pass

                try:
                    grid[index_of_row] = row
                except: pass

                try:
                    grid[index_of_row+1] = bottom_row
                except: pass

                try:
                    grid[index_of_row-1] = top_row
                except: pass

    return grid

def bomber_man(n, grid):
    if n == 0:
        return grid
    
    n -= 1
    grid = cast_bombs_to_seconds(grid)
    
    return recursion(n, grid)

print(bomber_man(0, ["O..",
                     "O..",
                     ".O."]))    

