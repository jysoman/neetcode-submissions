-- Write your query below
with cte1 as (select product_id, (width*length*height) as vol
from products
group by product_id)

select name as warehouse_name, sum(vol*units) as volume
from warehouse w
left join cte1 c on w.product_id=c.product_id
group by warehouse_name