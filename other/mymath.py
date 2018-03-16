
def getmoney(years, rates):
    return(((1 + rates)**(years + 1) - 1)/(rates))


if __name__ == '__main__':
    print(getmoney(10, 0.03))
