"""
blocklist.py

This file jst contains blocklist of the JWT tokens. 
It will be imported by the app and the logout resource so that 
tokens can be added to the blocklist when the user logs out.
"""

BLOCKLIST = set()

# BETTER TO USE REDIS (GIVES PERFORMANCE BENEFITS)
