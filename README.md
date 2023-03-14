# Back-end

## Com crear el Virutal Enviroment
Entra a l'arrel del projecte i executa:
  ```
  python -m venv .
  ```
Aixo creara el virtual enviorment el qual NO s'ha de posar al repositori git.

## Com obrir activar el Virutal Enviroment
  Entra a l'arrel del projecte i executa l'script Activate:
- Si s'utilitza PowerShell:
  ```
  .\Scripts\Activate.ps1
  ```

## Com instalar les llibreries:
Per actualitzar totes les llibreries de python, amb els Virutal Enviroment activat executa:
```
python -m pip install -r requirements.txt
```

## Com instalar noves llibreries:
Per instalar una llibreria python instalarla utilitzant pip:
```
python -m pip install Django
```
A continuació actualitzar el fitxer requirements.txt
```
python -m pip freeze > requirements.txt
```



# Com executar el server en Django
Dins el directori src executar:
```
python manage.py runserver 
```