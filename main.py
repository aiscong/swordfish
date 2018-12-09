from quote import *

def main():
    print(current_quote(['MSFT', 'FB', 'TSLA']))
    print("====historical starts below=======")
    print(historical_quote(['MSFT', 'FB', 'TSLA'], '1d5min', 'regular'))


main()