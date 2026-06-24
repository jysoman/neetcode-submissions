-- Write your query below
select name, balance
from (select account, sum(amount) as balance
from transactions group by account having sum(amount)>10000) a
join users u on u.account=a.account