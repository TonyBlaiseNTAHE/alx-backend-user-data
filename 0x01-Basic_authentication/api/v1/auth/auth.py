#!/usr/bin/env python3
"""
Auth class
"""
from typing import List, TypeVar
from flask import request
import fnmatch


class Auth():
    """
    Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth
        """
        if path is None:
            return True

        for p in excluded_paths:
            if fnmatch.fnmatch(path, p):
                return False

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
        """ auth_header
        """
        if request is None:
            return None

        if request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        """
        return None
