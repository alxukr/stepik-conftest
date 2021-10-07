# stepik-conftest
Repository for the third module of the test automation course

Solving the Stepik course problem "running autotests for different interface languages"

This repository is only for working with the Stepik course
https://stepik.org/course/575

 Examples of command line launches:
 
 pytest
 
 pytest test_items.py
 
 pytest --language=es
 
 pytest --browser_name=firefox
 
 pytest --language=es test_items.py
 
 pytest --browser_name=firefox test_items.py
 
 pytest --language=es --browser_name=chrome
 
 pytest --language=es --browser_name=firefox
 
 pytest --language=es --browser_name=firefox test_items.py


default options:

--language=en --browser_name=chrome
