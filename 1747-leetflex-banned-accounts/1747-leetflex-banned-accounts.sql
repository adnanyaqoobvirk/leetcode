select
    distinct l1.account_id
from
    LogInfo as l1
    inner join
    LogInfo as l2
    on
        l1.account_id = l2.account_id
        and
        l1.ip_address != l2.ip_address
        and
        l1.login between l2.login and l2.logout
