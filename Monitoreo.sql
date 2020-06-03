SELECT [counter_name], [cntr_value]
FROM sys.dm_os_performance_counters
WHERE
	[object_name] LIKE '%Buffer Manager%'
AND [counter_name] IN ('Page reads/sec', 'Page writes/sec')