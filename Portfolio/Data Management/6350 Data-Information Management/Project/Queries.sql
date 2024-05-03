-- List Launch Sites with the Total Number of Launches
SELECT ls.Name AS LaunchSite, COUNT(ol.Launch_ID) AS TotalLaunches
FROM Project.Launch_Sites ls
LEFT JOIN Project.Original_Launch ol ON ls.Site_ID = ol.Site_ID
GROUP BY ls.Name;

-- Retrieve Objects and Their Types
SELECT o.Name AS ObjectName, ot.Type AS ObjectType
FROM Project.Objects o
JOIN Project.Object_Type ot ON o.Type_ID = ot.Type_ID;

-- Average Mass of Objects by Object Type
SELECT ot.Type AS ObjectType, AVG(o.Mass) AS AvgMass
FROM Project.Objects o
JOIN Project.Object_Type ot ON o.Type_ID = ot.Type_ID
GROUP BY ot.Type;

-- List Docked Objects and Their Shipment Dates
SELECT do.Name AS DockedObjectName, do.Shipment_Date
FROM Project.Docked_Objects do;

-- Total Mass Launched from Each Launch Site
SELECT ls.Name AS LaunchSite, SUM(o.Mass) AS TotalMassLaunched
FROM Project.Launch_Sites ls
LEFT JOIN Project.Original_Launch ol ON ls.Site_ID = ol.Site_ID
LEFT JOIN Project.Objects o ON ol.Launch_ID = o.Launch_ID
GROUP BY ls.Name;
