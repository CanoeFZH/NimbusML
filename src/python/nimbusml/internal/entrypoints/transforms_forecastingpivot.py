# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Transforms.ForecastingPivot
"""


from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def transforms_forecastingpivot(
        columns_to_pivot,
        data,
        output_data=None,
        model=None,
        horizon_column_name='Horizon',
        **params):
    """
    **Description**
        Pivots the input colums and drops any rows with N/A

    :param columns_to_pivot: List of columns to pivot (inputs).
    :param horizon_column_name: Name of the horizon column generated.
        (inputs).
    :param data: Input dataset (inputs).
    :param output_data: Transformed dataset (outputs).
    :param model: Transform model (outputs).
    """

    entrypoint_name = 'Transforms.ForecastingPivot'
    inputs = {}
    outputs = {}

    if columns_to_pivot is not None:
        inputs['ColumnsToPivot'] = try_set(
            obj=columns_to_pivot,
            none_acceptable=False,
            is_of_type=list,
            is_column=True)
    if horizon_column_name is not None:
        inputs['HorizonColumnName'] = try_set(
            obj=horizon_column_name,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if data is not None:
        inputs['Data'] = try_set(
            obj=data,
            none_acceptable=False,
            is_of_type=str)
    if output_data is not None:
        outputs['OutputData'] = try_set(
            obj=output_data,
            none_acceptable=False,
            is_of_type=str)
    if model is not None:
        outputs['Model'] = try_set(
            obj=model,
            none_acceptable=False,
            is_of_type=str)

    input_variables = {
        x for x in unlist(inputs.values())
        if isinstance(x, str) and x.startswith("$")}
    output_variables = {
        x for x in unlist(outputs.values())
        if isinstance(x, str) and x.startswith("$")}

    entrypoint = EntryPoint(
        name=entrypoint_name, inputs=inputs, outputs=outputs,
        input_variables=input_variables,
        output_variables=output_variables)
    return entrypoint
