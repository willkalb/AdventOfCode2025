USE [AdventOfCode2025]
GO
/****** Object:  StoredProcedure [dbo].[Day1]    Script Date: 11/25/2025 9:58:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
ALTER PROCEDURE [dbo].[Day1] 
	@part INT = NULL,
	@input_as_string varchar(max) = NULL
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	IF @part IS NULL OR (@part <= 0 OR @part >= 3)
	BEGIN
		SELECT 'Must define @part as 1 or 2' [result]
	END

	declare @input table(line varchar(max))
	insert @input
	select value from string_split(@input_as_string, ',')

	IF @part = 1
	BEGIN 
		SELECT STRING_AGG(line, ', ') [result] from @input
	END

    IF @part = 2
	BEGIN 
		SELECT STRING_AGG(line, ', ') [result] from @input
	END
	
END
