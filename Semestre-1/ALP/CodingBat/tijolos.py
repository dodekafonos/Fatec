# queremos montar uma fila de tijolos de um tamanho denominado meta
# temos tijolos pequenos (tamanho 1) e tijolos grandes (tamanho 5)
# retorna True se for possível montar a fila de tijolos

def fila_tijolos(p, g, meta):
  # p = tamanho da fila de tijolos pequenos
  # g = tamanho da fila de tijolos grandes
  g = g*5
  if p > 0 and g > 0:
    return meta - g >= 0 and meta - g <= p or meta - (g-5) - p == 0
  elif p == 0:
    return meta % g == 0
  elif g == 0:
    return meta <= p


# =================================================
def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ()
  print ('Fila de Tijolos')
  test(fila_tijolos(3, 1, 8), True)
  test(fila_tijolos(3, 1, 9), False)
  test(fila_tijolos(3, 2, 10), True)
  test(fila_tijolos(3, 2, 8), True)
  test(fila_tijolos(3, 2, 9), False)
  test(fila_tijolos(6, 1, 11), True)
  test(fila_tijolos(6, 0, 11), False)
  test(fila_tijolos(3, 1, 7), True)
  test(fila_tijolos(1, 1, 7), False)
  test(fila_tijolos(2, 1, 7), True)
  test(fila_tijolos(7, 1, 11), True)
  test(fila_tijolos(7, 1, 8), True)
  test(fila_tijolos(7, 1, 13), False)
  test(fila_tijolos(43, 1, 46), True)
  test(fila_tijolos(40, 1, 46), False)
  test(fila_tijolos(22, 2, 33), False)
  test(fila_tijolos(0, 2, 10), True)
  test(fila_tijolos(1000000, 1000, 1000100), True)
  test(fila_tijolos(2, 1000000, 100003), False)
  test(fila_tijolos(12, 2, 21), True)

if __name__ == '__main__':
  main()