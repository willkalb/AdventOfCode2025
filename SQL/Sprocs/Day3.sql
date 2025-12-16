USE [AdventOfCode2025]
GO
/****** Object:  StoredProcedure [dbo].[Day3]    Script Date: 12/15/2025 7:31:19 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[Day3]
	
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

	DECLARE @specs TABLE(val VARCHAR(100), i INT, c INT);
	WITH cte AS (
		SELECT 1 i, line val FROM @input
		UNION ALL
		SELECT c.i + 1 i, val
		FROM cte c
		where c.i < LEN(val)

	)
	INSERT @specs
	SELECT val, i, CAST(SUBSTRING(val, i, 1) AS INT) FROM cte

	IF @part = 1
	BEGIN
		DECLARE @tens_specs TABLE(val VARCHAR(100), tens_val INT, tens_i INT)
		INSERT @tens_specs
		SELECT val, MAX(c), CHARINDEX(CAST(MAX(c) AS VARCHAR), val) FROM @specs WHERE i > 0 AND i < LEN(val) GROUP BY val



		SELECT SUM(j) 
		FROM (
			SELECT s.val, MAX(CAST(CAST(ts.tens_val AS VARCHAR) + CAST(s.c AS VARCHAR) AS INT)) j
			FROM @specs s
			JOIN @tens_specs ts ON s.val = ts.val
			WHERE s.i > ts.tens_i AND s.i < LEN(s.val) + 1 
			GROUP BY s.val
		) t
	END

    IF @part = 2
	BEGIN
		select 1
	END
END
