select o.customer_id, c.customer_name
from orders o
left join customers c on o.customer_id = c. customer_id
group by o.customer_id, c.customer_name
having sum(case when product_name='A' then 1 else 0 end)>=1 and sum(case when product_name='B' then 1 else 0 end)>=1 and sum(case when product_name='C' then 1 else 0 end)=0
order by c.customer_name