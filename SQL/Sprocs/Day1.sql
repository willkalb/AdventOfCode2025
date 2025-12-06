USE [AdventOfCode2025]
GO
/****** Object:  StoredProcedure [dbo].[Day1]    Script Date: 11/25/2025 9:58:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE [dbo].[Day1] 
	@part INT = NULL,
	@input_as_string VARCHAR(MAX) = NULL
AS
BEGIN

	SET NOCOUNT ON;

	IF @part IS NULL OR (@part <= 0 OR @part >= 3)
	BEGIN
		SELECT 'Must define @part as 1 or 2' [result]
	END

	DECLARE @input TABLE(line VARCHAR(MAX))
	INSERT @input
	SELECT value FROM STRING_SPLIT(@input_as_string, ',')

	DECLARE @instructions TABLE(id INT identity(1,1), dir VARCHAR(1), times INT)
	INSERT @instructions
	SELECT SUBSTRING(line, 1, 1), SUBSTRING(line, 2, LEN(line) - 1) FROM @input

	DECLARE @steps TABLE(id INT, dir VARCHAR(1), step INT);
	WITH cte AS (
		SELECT id, dir, times, 0 level
		FROM @instructions instr

		UNION ALL

		SELECT i.id, i.dir, r_cte.times - 1 times, level + 1 level
		FROM @instructions i
		JOIN cte r_cte on i.id = r_cte.id and i.times = r_cte.times + level
		WHERE r_cte.times > 0
	)
	INSERT @steps
	SELECT id, dir, times [step] FROM cte WHERE times > 0
	OPTION (MAXRECURSION 1000)

	DECLARE @num INT = 50

	IF @part = 1
	BEGIN
		DECLARE @steps_agg TABLE(id INT, c INT)
		INSERT @steps_agg
		SELECT id, CASE WHEN dir = 'r' THEN COUNT(*) WHEN dir = 'l' THEN COUNT(*) * -1 END FROM @steps GROUP BY id, dir

		DECLARE @rows_1 INT = (SELECT COUNT(*) FROM @steps_agg)
		DECLARE @curr_id_1 INT = (SELECT MIN(id) FROM @steps)
		DECLARE @zero_counter_1 INT = 0

		DECLARE steps_agg_cursor CURSOR FOR SELECT id, c FROM @steps_agg ORDER BY id;
		DECLARE @id_1 INT, @c_1 INT
		BEGIN
			OPEN steps_agg_cursor

			FETCH NEXT FROM steps_agg_cursor INTO @id_1, @c_1
			WHILE @@FETCH_STATUS = 0
			BEGIN
				SET @num += @c_1
				WHILE @num < 0
				BEGIN
					SET @num += 100
				END

				WHILE @num > 99
				BEGIN
					SET @num -= 100
				END

				IF @num = 0
				BEGIN
					SET @zero_counter_1 += 1
				END
				FETCH NEXT FROM steps_agg_cursor INTO @id_1, @c_1
			END
			CLOSE steps_agg_cursor
			DEALLOCATE steps_agg_cursor
		END

		SELECT @zero_counter_1
	END

    IF @part = 2
	BEGIN
		DECLARE @ordered_steps TABLE(id INT identity(1,1), num INT)
		INSERT @ordered_steps
		SELECT CASE dir WHEN 'r' THEN 1 WHEN 'l' THEN -1 END FROM @steps ORDER BY id, step desc

		DECLARE @rows_2 INT = (SELECT COUNT(*) FROM @ordered_steps)
		DECLARE @curr_id_2 INT = (SELECT MIN(id) FROM @ordered_steps)
		DECLARE @zero_counter_2 INT = 0

		DECLARE ordered_steps_cursor CURSOR FOR SELECT id, num FROM @ordered_steps ORDER BY id;
		DECLARE @id_2 INT, @c_2 INT
		BEGIN
			OPEN ordered_steps_cursor

			FETCH NEXT FROM ordered_steps_cursor INTO @id_2, @c_2
			WHILE @@FETCH_STATUS = 0
			BEGIN
				SET @num += @c_2
				WHILE @num < 0
				BEGIN
					SET @num += 100
				END

				WHILE @num > 99
				BEGIN
					SET @num -= 100
				END

				IF @num = 0
				BEGIN
					SET @zero_counter_2 += 1
				END
				FETCH NEXT FROM ordered_steps_cursor INTO @id_2, @c_2
			END
			CLOSE ordered_steps_cursor
			DEALLOCATE ordered_steps_cursor
		END

		SELECT @zero_counter_2
	END
	
END
