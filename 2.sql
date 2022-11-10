SELECT
    CASE
        WHEN mod(CAST(diagonal AS numeric), 1) = 0 THEN diagonal
        WHEN mod(CAST(diagonal AS numeric), 1) <= 0.5 THEN div(CAST(diagonal AS numeric), 1) + 0.5
        ELSE round(diagonal)
    END RoundDiagonal,
    count(*) as CountDiagonal
FROM public.notebooks_notebook
GROUP BY
    CASE
        WHEN mod(CAST(diagonal AS numeric), 1) = 0 THEN diagonal
        WHEN mod(CAST(diagonal AS numeric), 1) <= 0.5 THEN div(CAST(diagonal AS numeric), 1) + 0.5
        ELSE round(diagonal)
    END
