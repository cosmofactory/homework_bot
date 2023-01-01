class NoTokenProvidedException(Exception):
    """Token or chat id hasn't been provided."""


class NoResponseFromServer(Exception):
    """No response."""


class HTTPStatusNotOk(Exception):
    """Status not OK."""


class RequestException(Exception):
    """Request exception."""


class NoHomeworksFromAPI(Exception):
    """No homework key from API request."""


class WrongStatusException(Exception):
    """Wrong or no status of homework."""


class MissingHomeworkName(Exception):
    """No homework name."""


class CantSendMessageException(Exception):
    """Unable to send message."""
