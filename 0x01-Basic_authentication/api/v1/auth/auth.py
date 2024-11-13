#!/usr/bin/env python3
from typing import List, TypeVar
from flask import request
from models.user import User


class Auth():
    """
    Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ method
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ method
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        """
        return None
