Basic server and client for gopher protocol

makefile includes the following targets:
compile: cleans and builds the project
serv: starts the gopher server
client: testing client that connects to the server and runs a gopher query
	to change the query you have to edit ln 15 in client.py