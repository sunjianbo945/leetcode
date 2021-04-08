https://leetcode.com/problems/rank-scores/
Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.

+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+

For example, given the above Scores table, your query should generate the following report (order by highest score):

+-------+---------+
| score | Rank    |
+-------+---------+
| 4.00  | 1       |
| 4.00  | 1       |
| 3.85  | 2       |
| 3.65  | 3       |
| 3.65  | 3       |
| 3.50  | 4       |
+-------+---------+

Important Note: For MySQL solutions, to escape reserved words used as column names, you can use an apostrophe before
and after the keyword. For example `Rank`.

SELECT Score, DENSE_RANK() OVER(ORDER BY Score DESC) AS 'Rank'
FROM Scores
ORDER BY 'Rank'

 has tie

RANK(): this has a hole if data have same ranks, then jump to next rank. for example 4,4,6
DENSE_RANK(): this does not have a hole, for example, 4,4,5
 no tie
ROW_NUMBER(): need more specific instruction when the selected fields are same

extension1
SELECT Score, DENSE_RANK() OVER(PARTITION BY xxx ORDER BY Score DESC) AS 'Rank'
FROM Scores
ORDER BY 'Rank'  this will rank in each partition

extension2
SELECT Score, DENSE_RANK() OVER(PARTITION BY xxx ORDER BY Score DESC) AS 'Rank'
FROM Scores
WHERE 'Rank' = 1 this gives the rank 1 in each partition xxx
ORDER BY 'Rank'
------------------------------------------------------------------------------------------------------------------------
The Employee table holds all employees. Every employee has an Id, and there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+

The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+

Write a SQL query to find employees who earn the top three salaries in each of the department. For the above tables,
your SQL query should return the following rows (order of rows does not matter).

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Randy    | 85000  |
| IT         | Joe      | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+

Explanation:

In IT department, Max earns the highest salary, both Randy and Joe earn the second highest salary,
and Will earns the third highest salary. There are only two employees in the Sales department, Henry earns the highest
salary while Sam earns the second highest salary.

select d.Name as Department, a. Name as Employee, a. Salary
from (
select e.*, dense_rank() over (partition by DepartmentId order by Salary desc) as DeptPayRank
from Employee e
) a
join Department d
on a. DepartmentId = d. Id
where DeptPayRank <=3;

OR

SELECT d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
FROM Employee e1 JOIN Department d ON e1.DepartmentId = d.Id
WHERE 3 > (SELECT COUNT(DISTINCT e2.Salary)
        FROM Employee e2
        WHERE  e2.Salary > e1.Salary AND e1.DepartmentId = e2.DepartmentId)
-----------------------------------------------------------------------------------------------------------------------
Table: Enrollments

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| course_id     | int     |
| grade         | int     |
+---------------+---------+
(student_id, course_id) is the primary key of this table.

Write a SQL query to find the highest grade with its corresponding course for each student. In case of a tie, you should find the course with the smallest course_id. The output must be sorted by increasing student_id.

The query result format is in the following example:

Enrollments table:
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 2          | 2         | 95    |
| 2          | 3         | 95    |
| 1          | 1         | 90    |
| 1          | 2         | 99    |
| 3          | 1         | 80    |
| 3          | 2         | 75    |
| 3          | 3         | 82    |
+------------+-----------+-------+

Result table:
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 1          | 2         | 99    |
| 2          | 2         | 95    |
| 3          | 3         | 82    |
+------------+-----------+-------+



select
    student_id, course_id, grade
from
    (select
        student_id, course_id, grade, row_number() over(partition by student_id order by grade desc, course_id asc) as rn
    from
        enrollments) temp
    where
        temp.rn = 1
------------------------------------------------------------------------------------------------------------------------




