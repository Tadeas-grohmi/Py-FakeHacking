import time
import os
import pyfiglet
from rich.console import Console
from rich.console import RenderGroup
from rich.panel import Panel
from rich.prompt import IntPrompt
from rich.progress import Progress, track
from os import walk

banner = pyfiglet.figlet_format("MASTER HACKER", font="banner3-D")
con = Console()
prompt = Console()

def main():
    con.print(banner, "HACKING TOOL FOR ALL KINDS OF THINGS", style="bold green")
    stuff = RenderGroup(
        Panel("WEB HACKING"),
        Panel("FBI HACKING"),
        Panel("WIFI HACKING"),
        Panel("------"),
        Panel("------"),
    )
    con.print(Panel(stuff), style="bold green")
    answer = IntPrompt.ask("Which one do you pick? ", choices=['1', '2', '3', '4', '5'])

    if answer == 1:
        web_hacking()
    if answer == 2:
        fbi()
    if answer == 3:
        wifi()
    if answer == 4:
        main()
    if answer == 5:
        main()


def web_hacking():
    for x in track(range(25), "Initializing..."):
        time.sleep(0.1)
    url = input("Enter the website's url:")
    for i in track(range(100), f"Gathering information on {url}"):
        time.sleep(0.1)

    with Progress() as prog:
        exploiting = prog.add_task("Exploiting the website", total=150)
        decoding = prog.add_task("Cracking the passwords hashes", total=250)
        dumping = prog.add_task("Dumping plain text passwords", total=350)
        while not prog.finished:
            prog.update(exploiting, advance=0.3)
            prog.update(decoding, advance=0.4)
            prog.update(dumping, advance=0.5)
            time.sleep(0.05)

    print(f"{url} has been hacked, all passwords are dumped")
    time.sleep(5)
    return main()

def fbi():
    for x in track(range(25), "STARTING THE HACK"):
        time.sleep(0.15)

    for i in track(range(100), f"BYPASSING MAIN-FRAME"):
        time.sleep(0.2)

    for i in track(range(100), f"HACKING THE SECURITY"):
        time.sleep(0.15)

    with Progress() as progress:
        task1 = progress.add_task("[red]HACKING MAIN-FRAME", total=100)
        task2 = progress.add_task("[green]GETTING PERSONAL INFO", total=150)
        while not progress.finished:
            progress.update(task1, advance=0.7)
            progress.update(task2, advance=0.6)
            time.sleep(0.04)

    with Progress() as progress:
        task1 = progress.add_task("[cyan]UPLOADING", total=150)
        while not progress.finished:
            progress.update(task1, advance=0.5)
            time.sleep(0.04)

    banner = pyfiglet.figlet_format("fbi has been hacked", font="standard")
    con.print(banner, style="green")
    time.sleep(5)
    return main()

def wifi():
    co = input("What IP to DDOS:")
    if co != int:
        print("Please select valid IP")
        return wifi()
    for i in range(50000):
        print(f"SENDING PACKET TO {co} {i}")

    banner = pyfiglet.figlet_format("IP has been disabled", font="standard")
    con.print(banner, style="green")
    time.sleep(5)
    return main()


if __name__ == "__main__":
    main()