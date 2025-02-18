from sys import exit


def main() -> None:
    exit_message: str = 'Exiting program...'
    print('Welcome to The Fast Exponentiation 🖩!')
    while True:
        try:
            user_input: int = input('Enter the base: ')

            if user_input == 'exit':
                print(exit_message)
                exit()

            if user_input.isnumeric():
                base: int = int(user_input)

            user_input = input('Enter the exponent: ')
            if user_input.isnumeric():
                exp: int = int(user_input)

            print(pow(base, exp))

        except KeyboardInterrupt:
            print(exit_message)
            exit()


if __name__ == '__main__':
    main()
