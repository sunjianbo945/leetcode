Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the primary key for this table.
This table contains information about the temperature in a certain day.



Write an SQL query to find all dates' id with higher temperature compared to its previous dates (yesterday).

Return the result table in any order.

The query result format is in the following example:

Weather
+----+------------+-------------+
| id | recordDate | Temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+

Result table:
+----+
| id |
+----+
| 2  |
| 4  |
+----+
In 2015-01-02, temperature was higher than the previous day (10 -> 25).
In 2015-01-04, temperature was higher than the previous day (20 -> 30).


* DATEDIFF(date1, date2) -> Required. Two dates to calculate the number of days between. (date1 - date2)

* TO_DAYS(wt1.recordDate) return the number of days between from year 0 to date DATE
* TO_DAYS(wt1.recordDate)-TO_DAYS(wt2.recordDate)=1 check if wt2.recordDate is yesterday respect to wt1.recordDate

SELECT today.id AS 'Id'
FROM weather today JOIN weather yesterday ON DATEDIFF(today.recordDate, yesterday.recordDate) = 1
AND today.Temperature > yesterday.Temperature
-----------------------------------------------------------------------------------------------------------------------












