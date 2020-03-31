# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
SimpleRollingWindow
"""

__all__ = ["SimpleRollingWindow"]


from ...entrypoints.transforms_simplerollingwindow import \
    transforms_simplerollingwindow
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignature


class SimpleRollingWindow(BasePipelineItem, DefaultSignature):
    """
    **Description**
        Performs simple rolling window calculations.

    :param grain_columns: List of grain columns.

    :param target_column: Target column.

    :param horizon: Maximum horizon value.

    :param max_window_size: Maximum window size.

    :param min_window_size: Minimum window size.

    :param window_calculation: What window calculation to use.

    :param params: Additional arguments sent to compute engine.

    """

    @trace
    def __init__(
            self,
            grain_columns,
            target_column,
            horizon=0,
            max_window_size=0,
            min_window_size=0,
            window_calculation='0',
            **params):
        BasePipelineItem.__init__(
            self, type='transform', **params)

        self.grain_columns = grain_columns
        self.target_column = target_column
        self.horizon = horizon
        self.max_window_size = max_window_size
        self.min_window_size = min_window_size
        self.window_calculation = window_calculation

    @property
    def _entrypoint(self):
        return transforms_simplerollingwindow

    @trace
    def _get_node(self, **all_args):
        algo_args = dict(
            grain_columns=self.grain_columns,
            target_column=self.target_column,
            horizon=self.horizon,
            max_window_size=self.max_window_size,
            min_window_size=self.min_window_size,
            window_calculation=self.window_calculation)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)
