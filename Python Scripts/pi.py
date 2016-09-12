from decimal import Decimal, getcontext

def pi_archimedes(n):
    """
    Calculate n iterations of Archimedes PI recurrence relation
    """
    polygon_edge_length_squared = Decimal(2)
    polygon_sides = 2
    for i in range(n):
        polygon_edge_length_squared = 2 - 2 * (1 - polygon_edge_length_squared / 4).sqrt()
        polygon_sides *= 2
    return polygon_sides * polygon_edge_length_squared.sqrt()

def main():
    """
    Try the series
    """
    places = 150
    old_result = None
    for n in range(10*places):
        # Do calculations with double precision
        getcontext().prec = 4*places
        result = pi_archimedes(n)
        # Print the result with single precision
        getcontext().prec = places
        result = +result           # do the rounding on result
        print("%3d: %s" % (n, result))
        if result == old_result:
            break
        old_result = result
main()