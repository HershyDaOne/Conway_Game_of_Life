from colorama import Fore


def conways():
  grid = []
  for i in range(20):
    row1 = []
    for j in range(20):
      row1.append(0)
    print(row1)
    grid.append(row1)

  def printRow(row):
    print("[", end=" ")
    for i in row:
      if i == 0:
        print("0", end=" ")
      elif i == 1:
        print(Fore.BLUE + '1', end=" ")
        print(Fore.WHITE + "", end="")
    print("]")

  def single(x1, y1, GRID):
    for i in range(20):
      for j in range(20):
        if i + 1 == x1:
          if j + 1 == y1:
            GRID[i][j] = 1
    return (GRID)

  h = 0
  while h != '4':
    h = input(
        'Welcome to conways game of life. If you want to input a single cell press 1, for glider press 2, or press 3 for a blinker. If you want to exit press 4. X=row and Y=column. Also please only type in lowercase.: '
    )

    if h == '1':
      m = int(input('Enter the number of the x coordinate: '))
      l = int(input('Enter the number of the y coordinate: '))
      grid = single(m, l, grid)
      for list in grid:
        printRow(list)
    elif h == '2':
      print(
          'whichever x and y coordinate you input will be the tip of the glider.'
      )
      m = int(input('Enter the number of the x coordinate: '))
      l = int(input('Enter the number of the y coordinate: '))
      grid = single(m, l, grid)
      grid = single(m + 1, l + 1, grid)
      grid = single(m + 2, l + 1, grid)
      grid = single(m + 2, l, grid)
      grid = single(m + 2, l - 1, grid)
      for list in grid:
        printRow(list)
    elif h == '3':
      print(
          'whichever x and y coordinate you input will be the tip of the blinker.'
      )
      m = int(input('Enter the number of the x coordinate: '))
      l = int(input('Enter the number of the y coordinate: '))
      grid = single(m, l, grid)
      grid = single(m + 1, l, grid)
      grid = single(m + 2, l, grid)
      for list in grid:
        printRow(list)
    elif h == '4':
      break

  def countn(x, y, grid):
    count = 0
    for i in range(x - 1, x + 2):
      for j in range(y - 1, y + 2):
        if 0 <= i < 20 and 0 <= j < 20 and (i != x or j != y):
          count += grid[i][j]
    return count

  def nextgen(grid):
    new_grid = []
    for i in range(20):
      row = []
      for j in range(20):
        neighbors = countn(i, j, grid)
        if grid[i][j] == 1:
          if (neighbors < 2) or (neighbors > 3):
            row.append(0)
          else:
            row.append(1)
        else:
          if neighbors == 3:
            row.append(1)
          else:
            row.append(0)
      new_grid.append(row)
    return new_grid

  while True:
    for row in grid:
      printRow(row)

    choice = input(
        'Press Enter to continue to next generation (or type exit to quit(lowercase)): '
    )
    if choice == 'exit':
      break

    grid = nextgen(grid)





conways()
