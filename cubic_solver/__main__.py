from cubic_solver.parser import SolverArguementParser

from .factory import SolverFactory


def main():
    parser = SolverArguementParser(
        description="Solves polynomial equations up to the third degree."
    )
    parser.add_argument("a", type=float, help="Coefficient of x^3")
    parser.add_argument("b", type=float, help="Coefficient of x^2")
    parser.add_argument("c", type=float, help="Coefficient of x")
    parser.add_argument("d", type=float, help="Constant term")
    parser.add_argument(
        "-n",
        "--n_digits",
        type=int,
        help="Number of digits after the decimal point",
        required=False,
        default=10,
    )
    parser.add_argument(
        "-d",
        "--display_digits",
        type=int,
        help="Number of digits after the decimal point to display",
        required=False,
        default=4,
    )
    args = parser.parse_args()

    solver = SolverFactory.create_solver(
        args.a, args.b, args.c, args.d, args.n_digits, args.display_digits
    )
    solution = solver.solve()

    print(solution)


if __name__ == "__main__":
    main()
