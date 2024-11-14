#!/usr/bin/env python3
"""
Auth class
"""
from typing import List, TypeVar
from flask import request
from models.user import User


class Auth():
    """
    Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth
        """
        if path is None:
            return True

        if path[-1] != '/':
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path[-1] != '/' or excluded_path[-1] != '*':
                excluded_path += '/'

        if excluded_paths is None:
            return True

        if excluded_paths == []:
            return True

        if path not in excluded_paths:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """ method
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        """
        return None
