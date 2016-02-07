serv:
	python3.5 ./gopherserver/server.py

client:
	python3.5 ./gopherserver/client.py

compile:
	-python3.5 setup.py clean --all
	-rm -f `find . -name "*~"`
	-rm -f `find . -name "*.pyc"`
	-rm -f `find . -name "*.pygc"`
	-rm -f `find . -name "*.class"`
	-rm -f `find . -name "*.bak"`
	-rm -f `find . -name ".cache*"`
	-rm -f `find . -name "*.pyc"`
	-rm -rf build
	python3.5 setup.py install