-- Write your query below
select s.seller_name
from seller s
left join orders o on s.seller_id=o.seller_id
group by s.seller_id
having sum(case when sale_date>='2020-01-01' and sale_date<='2020-12-31' then 1 else 0 end)=0
order by seller_name