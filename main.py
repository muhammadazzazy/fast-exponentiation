from sys import exit


def main() -> None:
    while True:
        try:
            base: int = int(input('Enter the base: '))
            exp: int = int(input('Enter the exponent: '))
            print(pow(base, exp))
            choice: str = input(
                'Do you want to continue using the program? (Y/n) ')
            if choice.lower() == 'y':
                continue
            else:
                print('Thanks for trying my program!')
                exit()
        except ValueError:
            print('Invalid input...')
            continue
        except KeyboardInterrupt:
            print('Exiting...')
            exit()


if __name__ == '__main__':
    main()
