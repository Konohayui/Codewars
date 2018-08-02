SELECT 
       e.employee_id,
       e.first_name,
       e.last_name,
       d.department_name,
       e.salary AS old_salary,
       e.salary * d.pct_intc AS new_salary
  FROM employees   e,
        (SELECT department_id, 
                department_name, 
                (1 + pctIncrease(department_id)) AS pct_intc
        FROM departments) d
 WHERE e.department_id = d.department_id
ORDER BY 1;
