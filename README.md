POP Verifyer
============


Simple multithreaded commandline utility that checks the correctness of the email/password entries that are listed in the input CSV file.

The structure of the CSV should be as follows :

	email@host.com,password,host
	foobar@gmail.com,password,pop.gmail.com

The file can then be called with the following arguments :

	python popverifyer.py input.csv output.csv
