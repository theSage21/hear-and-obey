hearAndObey
===========


1. Receive instructions over socket
2. Execute instructions


requirements
------------

1. python3
2. socket (py3 std lib)
3. queue (py3 std lib)
4. threading (py3 std lib)


usage
-----

1. Victim
    1. `python3 hao.py &`
    2. That is all. You are good to go
2. Perp
    1. Take a port scan of the victim before hand.
    2. If any new ports show up it is HAO
    3. Connect to the port like shown in perp.py
    4. Encode and send strings to HAO to execute


things to do
------------

1. Encryption
2. Feedback
3. Stealth
