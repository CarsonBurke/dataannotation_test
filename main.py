import pandas as pd

URL = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"

def find_xy_max(table):
    x_max = 0
    y_max = 0
    
    for _, row in table.iterrows():
        x = int(row[0])
        if x > x_max:
            x_max = x
        y = int(row[2])
        if y > y_max:
            y_max = y
            
    return x_max, y_max

def create_map(headless_table, x_max, y_max):
    # Default to space
    map = [[' ' for x in range(x_max + 1)] for y in range(y_max + 1)]
    
    for _, row in headless_table.iterrows():
        # print(index, row)
        x = int(row[0])
        char = row[1]
        y = int(row[2])
        
        map[y][x] = char
    return map

def visualize(map):
    for row in map:
        print(''.join(row))

def main(url):
    df = pd.read_html(url, encoding='utf-8')
    table = df[0]
    headless_table = table.iloc[1:]
    
    (x_max, y_max) = find_xy_max(headless_table)
    map = create_map(headless_table, x_max, y_max)
    visualize(map)
    
main(URL)

# ████████░     ████████░   ██████████░    ███████░     ██░     ██░     ███░    ███░ ██░     ██░
# ██░     ██░ ███░     ███░ ██░          ███░    ██░   ████░   ████░      ██░  ██░   ██░     ██░
# ██░     ██░ ██░       ██░ ██░         ███░           ██░██░ ██░██░       ██░██░    ██░     ██░
# ████████░   ██░       ██░ ████████░   ██░           ███░ ██░██░ ██░       ███░     ██████████░
# ██░     ██░ ██░       ██░ ██░         ███░          ██░  █████░ ███░     ██░██░    ██░     ██░
# ██░     ██░ ███░     ███░ ██░          ███░    ██░ ███░   ███░   ██░    ██░  ██░   ██░     ██░
# ████████░     ████████░   ██████████░    ███████░  ██░           ███░ ███░    ███░ ██░     ██░