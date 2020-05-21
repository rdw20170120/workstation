from my_assert import has_type
from my_assert import has_type_message
from my_exception import UnrecognizedValueError
from types import StringType


SERVICE_DATA_ID = 'kv'
SERVICE_DATA_NAME = 'Data Service'
SERVICE_INDEX_ID = 'index'
SERVICE_INDEX_NAME = 'Index Service'
SERVICE_QUERY_ID = 'n1ql'
SERVICE_QUERY_NAME = 'Query Service'
SERVICE_SEARCH_ID = 'fts'
SERVICE_SEARCH_NAME = 'Full-Text Search Service'


def service_name(service_identifier):
    result = None
    if service_identifier == SERVICE_DATA_ID:     result = SERVICE_DATA_NAME
    elif service_identifier == SERVICE_INDEX_ID:  result = SERVICE_INDEX_NAME
    elif service_identifier == SERVICE_QUERY_ID:  result = SERVICE_QUERY_NAME
    elif service_identifier == SERVICE_SEARCH_ID: result = SERVICE_SEARCH_NAME
    else:
      raise UnrecognizedValueError(
          service_identifier, type(service_identifier), 'Couchbase service identifier'
      )
    assert has_type(result, StringType), has_type_message(result, StringType)
    return result


""" Disabled content
"""

