from rest_framework.test import APIClient


def main():
    client = APIClient()
    url = 'nattech.fib.upc.edu:40410/api/updateBD/'
    client.get(url)
    print('BASE DE DATOS ACTUALIZADA')

if __name__ == '__main__':
    main()