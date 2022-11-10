SELECT t.title, count(v.title)
FROM public.notebooks_brand t, public.notebooks_notebook v
WHERE t.id = v.brand_id
GROUP BY t.title
ORDER BY count(v.title) DESC
