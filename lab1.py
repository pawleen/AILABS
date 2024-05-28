class BlockWorld:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    def display_grid(self):
        print("  " + "   ".join(str(i) for i in range(self.grid_size)))
        print("  " + "---" * self.grid_size)
        for idx, row in enumerate(self.grid):
            print(idx, "| " + " | ".join(row) + " |")

    def place_block(self, block, x, y):
        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            if self.grid[y][x] == ' ':
                self.grid[y][x] = block
            else:
                print(f"Cell ({x}, {y}) is already occupied")
        else:
            print(f"Invalid coordinates ({x}, {y})")

    def move_block(self, block, target_x, target_y):
        block_x, block_y = self.find_block(block)
        if block_x is None:
            print(f"Block '{block}' not found")
            return

        if 0 <= target_x < self.grid_size and 0 <= target_y < self.grid_size:
            if self.grid[target_y][target_x] == ' ':
                self.grid[target_y][target_x] = block
                self.grid[block_y][block_x] = ' '
            else:
                print(f"Cell ({target_x}, {target_y}) is occupied")
        else:
            print(f"Invalid target coordinates ({target_x}, {target_y})")

    def find_block(self, block):
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                if self.grid[y][x] == block:
                    return x, y
        return None, None

def main():
    grid_size = int(input("Enter grid size: "))
    world = BlockWorld(grid_size)

    while True:
        world.display_grid()

        action = input("Enter action (place/move): ").strip().lower()
        if action == "place":
            block = input("Enter block to place: ")
            x = int(input("Enter X coordinate: "))
            y = int(input("Enter Y coordinate: "))
            world.place_block(block, x, y)
        elif action == "move":
            block = input("Enter block to move: ")
            target_x = int(input("Enter target X coordinate: "))
            target_y = int(input("Enter target Y coordinate: "))
            world.move_block(block, target_x, target_y)
        else:
            print("Invalid action. Please enter 'place' or 'move'.")

        if input("Continue? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
