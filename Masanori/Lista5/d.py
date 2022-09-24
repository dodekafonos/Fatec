start = 18644
end = 33087
sortudos = []

for num in range(start, end+1):
    if "2" in str(num) and "7" not in str(num):
        sortudos.append(num)

print(f"Entre {start} e {end} existem {len(sortudos)} números sortudos.")