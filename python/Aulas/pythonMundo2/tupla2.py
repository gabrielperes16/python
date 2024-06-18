times = (
    'Botafogo', 'Flamengo', 'Bahia', 'Athletico-PR', 'Palmeiras', 
    'Bragantino', 'Cruzeiro', 'Atlético-MG', 'Internacional', 
    'Juventude', 'Fortaleza', 'Atlético-GO', 'Cuiabá', 'Vasco', 
    'Corinthians', 'Grêmio', 'Criciúma', 'Fluminense', 'Vitória'
)
posição=times.index('Cruzeiro')
alfabetica=sorted(times)
print(f"os 5 primeiros times são : {times[0:5]}")
print(f"O 4 ultimos são {times[-4:]}")
print(f'os times em ordem alfabetica são {alfabetica}')
print(f'o time cruzeiro esta na posição: {posição}')
