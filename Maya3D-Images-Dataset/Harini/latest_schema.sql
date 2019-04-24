set @a := 'Animal';
set @c := (select count(*) from category where category_name = @a);
set @p := (select 'category already exists');

set @n := (select category_id from category order by category_id desc limit 1);
set @increment := (select right((select @n),2));
set @new_category := (select CONCAT('C_',@increment+1));

select @new_category;



set @n := (select category_id into @r from category order by category_id desc limit 1);

