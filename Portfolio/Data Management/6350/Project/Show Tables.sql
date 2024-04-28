-- Select all data from Object_Type
SELECT * FROM Project.Object_Type ORDER BY Type_ID DESC;

-- Select all data from Launch_Sites
SELECT * FROM Project.Launch_Sites ORDER BY Site_ID DESC;

-- Select all data from Original_Launch
SELECT * FROM Project.Original_Launch ORDER BY Launch_ID DESC;

-- Select all data from Orbit
SELECT * FROM Project.Orbit ORDER BY Orbit_ID DESC;

-- Select all data from Projected_Reentry
SELECT * FROM Project.Projected_Reentry ORDER BY Projected_ID DESC;

-- Select all data from Docked_Objects
SELECT * FROM Project.Docked_Objects ORDER BY Dock_ID DESC;

-- Select all data from Objects
SELECT * FROM Project.Objects ORDER BY Object_ID DESC;