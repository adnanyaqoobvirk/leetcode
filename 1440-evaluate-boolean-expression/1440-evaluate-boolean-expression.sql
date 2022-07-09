select
    e.left_operand,
    e.operator,
    e.right_operand,
    if(
        case
            when operator = '>' then lv.value > rv.value
            when operator = '<' then lv.value < rv.value
            else lv.value = rv.value
        end,
        'true',
        'false'
    ) as value
from
    Expressions as e
    inner join
    Variables as lv
    on
        e.left_operand = lv.name
    inner join
    Variables as rv
    on
        e.right_operand = rv.name

