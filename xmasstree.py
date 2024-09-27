def make_decoration(inputs: list[str]):
    postcard = create_postcard()
    max_height = int(inputs[0]) + 2
    max_width = int(inputs[0]) + max_height - 3
    while True:
        third_row = '/*\\'
        forth_row = '/*O*\\'
        if len(inputs) == 2:
            print(f'{"X".center(max_width)}\n'
                  f'{"^".center(max_width)}\n'
                  f'{third_row.center(max_width)}\n'
                  f'{forth_row.center(max_width)}')
        else:
            line, col = int(inputs[2]), int(inputs[3])
            postcard[line][col] = "X"
            postcard[line + 1][col] = "^"
            for i, c in enumerate('/*\\'):
                postcard[line + 2][col - 1 + i] = c
            for i, c in enumerate('/*O*\\'):
                postcard[line + 3][col - 2 + i] = c
        interval_count = 1
        tree_line = 4
        # continue creating tree starting with row 5 and decorate on interval
        for row in range(5, (int(inputs[0]) * 2) - 1, 2):
            tree_row = '/'
            for asterisk in range(1, row + 1):
                if asterisk % 2 != 0:
                    tree_row += '*'
                else:
                    if asterisk % 2 == 0 and interval_count == int(inputs[1]):
                        tree_row += 'O'
                        interval_count = 1
                    else:
                        tree_row += '*'
                        interval_count += 1
            tree_row += '\\'
            if len(inputs) == 2:
                print(tree_row.center(max_width))
            else:
                for i, c in enumerate(tree_row):
                    line, col = int(inputs[2]), int(inputs[3])
                    postcard[line + tree_line][col - int(len(tree_row) / 2) + i] = c
            tree_line += 1
        if len(inputs) == 2:
            print('| |'.center(max_width))
            break
        else:
            line, col = int(inputs[2]), int(inputs[3])
            postcard[line + tree_line][col - 1] = '|'
            postcard[line + tree_line][col + 1] = '|'
            for _ in range(4):
                inputs.pop(0)
            if len(inputs) == 0:
                for h in range(30):
                    for w in range(50):
                        print(postcard[h][w], end='')
                    print()
                break


def create_postcard() -> list[list[str]]:
    height, width = 30, 50
    postcard = [[' ' for _ in range(width)] for _ in range(height)]
    for i in range(width):
        postcard[0][i] = '-'
        postcard[height - 1][i] = '-'
    for i in range(1, height - 1):
        postcard[i][0] = '|'
        postcard[i][width - 1] = '|'
    postcard_message = 'Merry Xmas'
    for i, letter in enumerate(postcard_message):
        postcard[27][i + 20] = letter
    return postcard


def main():
    make_decoration(input().strip().split())


if __name__ == '__main__':
    main()
