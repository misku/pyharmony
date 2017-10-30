#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2013, Jeff Terrace
# All rights reserved.

"""Authentication routines to connect to Logitech web service and Harmony devices."""

def get_auth_token(ip_address, port):
    """Swaps the Logitech auth token for a session token.

    Args:
        ip_address (str): IP Address of the Harmony device IP address
        port (str): Harmony device port

    Returns:
        A string containing the session token.
    """
    return "dummy-token-for-local-login"
