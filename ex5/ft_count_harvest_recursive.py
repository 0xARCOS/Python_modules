def ft_count_harvest_recursive(days, current=0):
    print(f"Days: {current}")
    if current == days:
        print("Harvest time!")
        return
    if current >= days:
        return
    ft_count_harvest_recursive(days, current + 1)

days = int(input("Days until harvest: "))
ft_count_harvest_recursive(days)