with cte1 as (select *, rank() over(partition by department_id order by salary desc) as rnk
from employee)

select d.name as department, cte1.name as employee, salary
from cte1
inner join department d on d.id=cte1.department_id
where rnk=1