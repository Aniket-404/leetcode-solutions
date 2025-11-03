# Write your MySQL query statement below
select E.name as Employee
from Employee as E
join Employee as M
on E.managerId = M.id
where E.salary > M.salary;