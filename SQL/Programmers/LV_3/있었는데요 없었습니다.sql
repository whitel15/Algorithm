SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS A
LEFT OUTER JOIN ANIMAL_INS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.DATETIME < B.DATETIME
ORDER BY B.DATETIME