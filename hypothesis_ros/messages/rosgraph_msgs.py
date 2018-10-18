# -*- coding: utf-8 -*-

"""
Provides hypothesis strategies for `ROS1 rosgraph_msgs`_.

.. _ROS1 std_msgs:
   http://wiki.ros.org/rosgraph_msgs

"""

from collections import namedtuple
from hypothesis.strategies import composite

from hypothesis_ros.message_fields import (
    uint8,  # Represents ROS1 Byte msg
    uint32,
    string,
    array,
)

from hypothesis_ros.messages.std_msgs import header

_Log = namedtuple('Log', 'header level name msg file function line topics')

@composite
def log(draw,  # DEBUG=uint8(), INFO=uint8(), WARN=uint8(), ERROR=uint8(), FATAL=uint8(),
        header=header(), level=uint8(), name=string(), msg=string(),
            file=string(), function=string(), line=uint32(), topics=array(elements=string())):
    """
    Generate value for ROS1 rosgraph message type "log".

    Parameters
    ----------
    header
    level
    name
    msg
    file
    function
    line
    topics

    """

    header_value = draw(header)
    level_value = draw(level)
    name_value = draw(name)
    msg_value = draw(msg)
    file_value = draw(file)
    function_value = draw(function)
    line_value = draw(line)
    topics_value = draw(topics)

    assert isinstance(level_value, int), 'drew invalid level={level_value} from {level} for int field'.format(level_value, level)
    assert isinstance(name_value, str), 'drew invalid name={name_value} from {name} for string field'.format(name_value, name)
    assert isinstance(msg_value, str), 'drew invalid msg={msg_value} from {msg} for string field'.format(msg_value, msg)
    assert isinstance(file_value, str), 'drew invalid file={file_value} from {file} for string field'.format(file_value, file)
    assert isinstance(function_value, str), 'drew invalid function={function_value} from {function} for string field'.format(function_value, function)
    assert isinstance(line_value, int), 'drew invalid line={line_value} from {line} for int field'.format(line_value, line)
    assert isinstance(topics_value, list), 'drew invalid topics={topics_value} from {msg} for list field'.format(topics_value, topics)

    return _Log(header_value, level_value, name_value, msg_value, file_value, function_value, line_value, topics_value)

