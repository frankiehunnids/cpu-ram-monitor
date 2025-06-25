# This is a CPU and RAM monitoring program

import time 
import psutil
import csv
from rich.console import Console
from rich.table import Table
from rich.progress import BarColumn
from rich.text import Text


def usage_bar(value: float) -> Text:
    bar_length = 20
    filled_length = int(bar_length * value // 100)
    bar = "█" * filled_length + "─" * (bar_length - filled_length)
    
    if value < 50:
        color = "green"
    elif value < 80:
        color = "yellow"
    else:
        color = "red"

    return Text(bar, style=color)

def main():

    console = Console()
    table = Table(title='CPU and RAM Monitor')
    table.add_column('CPU')
    table.add_column('RAM')
    table.add_column('Time')

    cpu_per = 0
    virt_mem = 0 
    fields = ['CPU', 'RAM', 'Time']
    rows = []
    count = 0

    

    while True: 
        table = Table(title='CPU and RAM Monitor')
        table.add_column('CPU')
        table.add_column('RAM')
        table.add_column('Time')

        
        cpu_per = psutil.cpu_percent()
        ram_per = psutil.virtual_memory().percent
        curr_time = time.ctime()

        cpu_bar = usage_bar(cpu_per)
        ram_bar = usage_bar(ram_per)

        table.add_row(str(cpu_per), str(ram_per), str(curr_time))
        table.add_row(cpu_bar, ram_bar)

        rows.append([cpu_per, ram_per, curr_time])

        console.print(table)
        count += 1
        time.sleep(2)
        console.clear()
        
        
    filename = 'results.csv'

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


if __name__ == '__main__': 
    main()
