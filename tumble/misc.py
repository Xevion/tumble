"""
misc.py
Holds basic ratelimiting functionality to ensure ratelimits are never hit by the application.
"""
import ratelimit


@ratelimit.sleep_and_retry
@ratelimit.limits(calls=2, period=1)
def pageQuery() -> None:
    """
    A blank function for ratelimiting page requests.
    """
    pass


@ratelimit.sleep_and_retry
@ratelimit.limits(calls=3, period=1)
def mediaQuery() -> None:
    """
    A blank function for ratelimiting media requests.
    """
    pass
