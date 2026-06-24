-- Write your query below
with cte1 as (select sales_id
from orders o
left join company c on c.com_id=o.com_id
group by sales_id
having sum(case when c.name like 'CRIMSON' then 1 else 0 end)>0)

select name 
from sales_person s
left join cte1 c on c.sales_id=s.sales_id
where c.sales_id is null  