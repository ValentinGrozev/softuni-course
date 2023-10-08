def loading_bar(percent):
    if percent == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    elif 0 <= percent < 100:
        loaded_screen = percent / 10
        return f"{percent}% [{int(loaded_screen) * '%'}{(10 - int(loaded_screen)) * '.'}]\nStill loading..."


loaded_percent = int(input())
print(loading_bar(loaded_percent))