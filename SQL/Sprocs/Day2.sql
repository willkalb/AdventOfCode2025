USE [AdventOfCode2025]
GO
/****** Object:  StoredProcedure [dbo].[Day2]    Script Date: 12/5/2025 1:21:29 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE [dbo].[Day2]
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

	DECLARE @ranges TABLE(id INT IDENTITY(1, 1), start BIGINT, [end] BIGINT)
	INSERT @ranges
	SELECT SUBSTRING(line, 0, CHARINDEX('-', line)), SUBSTRING(line, CHARINDEX('-', line) + 1, LEN(line)) FROM @input


	IF @part = 1
	BEGIN
		WITH cte AS (
			SELECT id, [start], [end], [start] curr
			FROM @ranges

			UNION ALL
			
			SELECT r.id, r.[start], r.[end], ids_cte.curr + 1
			FROM @ranges r
			JOIN cte ids_cte on r.id = ids_cte.id 
			WHERE ids_cte.curr <= r.[end]

		)
		SELECT SUM(cte.curr) invalid_ids_sum
		FROM cte
		WHERE
			CASE
				WHEN LEN(cte.curr) % 2 = 0 THEN 
					CASE
						WHEN SUBSTRING(CAST(cte.curr AS VARCHAR), 1, (LEN(cte.curr) / 2)) = SUBSTRING(CAST(cte.curr AS VARCHAR), (LEN(cte.curr) / 2) + 1, LEN(cte.curr)) THEN 1
						ELSE 0
					END
				ELSE 0
			END = 1
		OPTION (MAXRECURSION 0)
	END

    IF @part = 2
	BEGIN
		WITH cte AS (
			SELECT id, [start], [end], [start] curr
			FROM @ranges

			UNION ALL
			
			SELECT r.id, r.[start], r.[end], ids_cte.curr + 1
			FROM @ranges r
			JOIN cte ids_cte on r.id = ids_cte.id 
			WHERE ids_cte.curr <= r.[end]

		)
		SELECT SUM(cte.curr) invalid_ids_sum
		FROM cte
		WHERE
			CASE LEN(cte.curr)
				WHEN 2 THEN 
					CASE
						WHEN REPLICATE(SUBSTRING(CAST(cte.curr AS VARCHAR), 1, 1), 2) = cte.curr THEN 1
						ELSE 0
					END
				WHEN 3 THEN 
					CASE
						WHEN REPLICATE(SUBSTRING(CAST(cte.curr AS VARCHAR), 1, 1), 3) = cte.curr THEN 1
						ELSE 0
					END
				WHEN 4 THEN 
					CASE
						WHEN REPLICATE(SUBSTRING(CAST(cte.curr AS VARCHAR), 1, 1), 4) = cte.curr THEN 1
						WHEN REPLICATE(SUBSTRING(CAST(cte.curr AS VARCHAR), 1, 2), 2) = cte.curr THEN 1
						ELSE 0
					END
				WHEN 5 THEN 
					CASE
						WHEN REPLICATE(SUBSTRING(CAST(cte.curr AS VARCHAR), 1, 1), 5) = cte.curr THEN 1
						ELSE 0
					END
				WHEN 6 THEN 
					CASE
						WHEN REPLICATE(SUBSTRING(CAST(cte.curr AS VARCHAR), 1, 1), 6) = cte.curr THEN 1
						WHEN REPLICATE(SUBSTRING(CAST(cte.curr AS VARCHAR), 1, 2), 3) = cte.curr THEN 1
						WHEN REPLICATE(SUBSTRING(CAST(cte.curr AS VARCHAR), 1, 3), 2) = cte.curr THEN 1
						ELSE 0
					END
				WHEN 7 THEN 
					CASE
						WHEN REPLICATE(SUBSTRING(CAST(cte.curr AS VARCHAR), 1, 1), 7) = cte.curr THEN 1
						ELSE 0
					END
				WHEN 8 THEN 
					CASE
						WHEN REPLICATE(SUBSTRING(CAST(cte.curr AS VARCHAR), 1, 1), 8) = cte.curr THEN 1
						WHEN REPLICATE(SUBSTRING(CAST(cte.curr AS VARCHAR), 1, 2), 4) = cte.curr THEN 1
						WHEN REPLICATE(SUBSTRING(CAST(cte.curr AS VARCHAR), 1, 4), 2) = cte.curr THEN 1
						ELSE 0
					END
				WHEN 9 THEN 
					CASE
						WHEN REPLICATE(SUBSTRING(CAST(cte.curr AS VARCHAR), 1, 1), 9) = cte.curr THEN 1
						WHEN REPLICATE(SUBSTRING(CAST(cte.curr AS VARCHAR), 1, 3), 3) = cte.curr THEN 1
						ELSE 0
					END
				WHEN 10 THEN 
					CASE
						WHEN REPLICATE(SUBSTRING(CAST(cte.curr AS VARCHAR), 1, 1), 10) = cte.curr THEN 1
						WHEN REPLICATE(SUBSTRING(CAST(cte.curr AS VARCHAR), 1, 2), 5) = cte.curr THEN 1
						WHEN REPLICATE(SUBSTRING(CAST(cte.curr AS VARCHAR), 1, 5), 2) = cte.curr THEN 1
						ELSE 0
					END
				ELSE 0
			END = 1
		OPTION (MAXRECURSION 0)
	END
END