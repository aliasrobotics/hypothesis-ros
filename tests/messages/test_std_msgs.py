# -*- coding: utf-8 -*-
"""
Unit tests for the std_msgs strategies.
"""

from hypothesis import given
from hypothesis.strategies import just
from hypothesis_ros.messages.std_msgs import (
    header,
)
from hypothesis_ros.message_fields import (
    uint32,
    time,
)


@given(header(seq=uint32(min_value=0, max_value=0),
              stamp=time(
                        secs=uint32(min_value=1, max_value=1),
                        nsecs=uint32(min_value=2, max_value=2)
                    ),
              frame_id=just('some_tf_frame_name')
             )
      )
def test_header_accepts_customized_strategies(generated_value):
    """Exemplary customized header."""
    assert generated_value == (0, (1, 2), 'some_tf_frame_name')
