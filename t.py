# Supondo que o conjunto se chame 'to_clean'
to_clean = {(1, 0), (2, 3), (4, 5)}

print(to_clean)
# Usando remove (lança KeyError se o item não estiver presente)
to_clean.remove((1, 0))
print(to_clean)
# Usando discard (não lança exceção se o item não estiver presente)
to_clean.discard((2, 3))
print(to_clean)