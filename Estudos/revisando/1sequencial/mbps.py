"""
O tamanho do arquivo � convertido de megabytes para megabits mult2iplicando por 8, pois h� 8 bits em um byte.
A velocidade da Internet � dada em megabits por segundo.
"""

mb_file = int(input("Insert the MB value: "))
mbps = int(input("Insert the value mbps: "))

sec = mb_file * 8 / 100

print(f"Seconds {sec}")