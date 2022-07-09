select
    e.left_operand,
    e.operator,
    e.right_operand,
    case
        when operator = '>' then if(lv.value > rv.value, 'true', 'false')
        when operator = '<' then if(lv.value < rv.value, 'true', 'false')
        else if(lv.value = rv.value, 'true', 'false')
    end as value
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

