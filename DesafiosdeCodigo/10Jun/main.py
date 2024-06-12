#reversing list with slice in python
def inverte_lista(lista_A):
	lista_invertida = []
	for i in lista_A[::-1]:
		lista_invertida.append(i)
	return lista_invertida

print(inverte_lista([16,15,10,5]))




    