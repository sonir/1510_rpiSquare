import sq_square, sq_osc_receive, sys

square = sq_square.SqSquare()
osc = sq_osc_receive.SqOscReceive(54321, square)

try:
    while True:
        square.update()

except KeyboardInterrupt :
    square.destroy()
    sys.exit()
    osc.terminate()

# except KeyboardInterrupt :
#     pass
