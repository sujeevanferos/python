import sys
import time

def progress_bar(total, current, bar_length=50):
    progress = current / total
    arrow = '#' * int(progress * bar_length)
    spaces = ' ' * (bar_length - len(arrow))
    sys.stdout.write('\rProgress: [{0}] {1:.2f}%'.format(arrow + spaces, progress * 100))
    sys.stdout.flush()

# Example usage
total_items = 100
for i in range(total_items):
    # Simulate some work
    time.sleep(0.1)
    # Update the progress bar
    progress_bar(total_items, i + 1)

print("\nTask completed!")
