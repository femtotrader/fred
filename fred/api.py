"""
Simplified functions for using the Fred API.
"""

import os
from .core import Fred


def key(api_key):
    os.environ['FRED_API_KEY'] = api_key
    return Fred()


#####################
# Category
#####################

def category(**kwargs, session=None):
    """Get a category."""
    if 'series' in kwargs:
        kwargs.pop('series')
        path = 'series'
    else:
        path = None
    return Fred(session=session).category(path, **kwargs)


def categories(identifier, **kwargs, session=None):
    """Just in case someone misspells the method."""
    kwargs['category_id'] = identifier
    return category(**kwargs, session=session)


def children(category_id=None, **kwargs, session=None):
    """Get child categories for a specified parent category."""
    kwargs['category_id'] = category_id
    return Fred(session=session).category('children', **kwargs)


def related(identifier, **kwargs, session=None):
    """Get related categories for a specified category."""
    kwargs['category_id'] = identifier
    return Fred(session=session).category('related', **kwargs)


def category_series(identifier, **kwargs, session=None):
    """Get the series in a category."""
    kwargs['category_id'] = identifier
    return Fred(session=session).category('series', **kwargs)


#####################
# Releases
#####################

def release(release_id, **kwargs, session=None):
    """Get the release of economic data."""
    kwargs['release_id'] = release_id
    return Fred(session=session).release(**kwargs)


def releases(release_id=None, **kwargs, session=None):
    """Get all releases of economic data."""
    if not 'id' in kwargs and release_id is not None:
        kwargs['release_id'] = release_id
        return Fred().release(**kwargs)
    return Fred(session=session).releases(**kwargs)


def dates(**kwargs, session=None):
    """Get release dates for economic data."""
    return Fred(session=session).releases('dates', **kwargs)


#####################
# Series
#####################

def series(identifier=None, **kwargs, session=None):
    """Get an economic data series."""
    if identifier:
        kwargs['series_id'] = identifier
    if 'release' in kwargs:
        kwargs.pop('release')
        path = 'release'
    elif 'releases' in kwargs:
        kwargs.pop('releases')
        path = 'release'
    else:
        path = None
    return Fred(session=session).series(path, **kwargs)


def observations(identifier, **kwargs, session=None):
    """Get an economic data series."""
    kwargs['series_id'] = identifier
    return Fred(session=session).series('observations', **kwargs)


def search(text, **kwargs, session=None):
    """Get economic data series that match keywords."""
    kwargs['search_text'] = text
    return Fred(session=session).series('search', **kwargs)


def updates(**kwargs, session=None):
    """Get economic data series sorted in descending order."""
    return Fred(session=session).series('updates', **kwargs)


def vintage(identifier, **kwargs, session=None):
    """
    Get the dates in history when a series' data values were revised or new
    data values were released.
    """
    kwargs['series_id'] = identifier
    return Fred(session=session).series('vintagedates', **kwargs)


#####################
# Sources
#####################

def source(source_id=None, **kwargs, session=None):
    """Get a source of economic data."""
    if source_id is not None:
        kwargs['source_id'] = source_id
    elif 'id' in kwargs:
        source_id = kwargs.pop('id')
        kwargs['source_id'] = source_id
    if 'releases' in kwargs:
        kwargs.pop('releases')
        path = 'releases'
    else:
        path = None
    return Fred(session=session).source(path, **kwargs)


def sources(source_id=None, **kwargs, session=None):
    """Get the sources of economic data."""
    if source_id or 'id' in kwargs:
        return source(source_id, **kwargs)
    return Fred(session=session).sources(**kwargs)
