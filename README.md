hearAndObey
===========


1. Receive instructions over socket
2. Execute instructions


requirements
------------

1. python3
2. socket (py3 std lib)


usage
-----

1. Remote
    1. `python3 hao.py &`
    2. That is all. You are good to go
2. Master
    1. Take a port scan of the remote before hand.
    2. If any new ports show up it is HAO
    3. Connect to the port like shown in master.py
    4. Encode and send strings to HAO to execute


things to do
------------

1. Encryption
2. Feedback
