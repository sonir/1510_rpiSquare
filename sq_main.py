import sq_square, sq_osc_receive

square = sq_square.SqSquare()
osc = sq_osc_receive.SqOscReceive(54321, square)


while True:
    square.update()

# except KeyboardInterrupt :
#     pass
