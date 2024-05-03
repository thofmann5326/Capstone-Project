CREATE SCHEMA Project;
-- Object Type Table
CREATE TABLE Project.Object_Type (
    Type_ID INT PRIMARY KEY,
    Type VARCHAR(255)
);
-- Launch Sites Table
CREATE TABLE Project.Launch_Sites (
    Site_ID INT PRIMARY KEY,
    Name VARCHAR(255),
    Latitude FLOAT,
    Longitude FLOAT,
    Altitude FLOAT
);
-- Original Launch Table
CREATE TABLE Project.Original_Launch (
    Launch_ID INT PRIMARY KEY,
    Site_ID INT,
    Launch_Date DATE,
    Launch_Time TIME,
    Success_Failure VARCHAR(50),
    FOREIGN KEY (Site_ID) REFERENCES Project.Launch_Sites(Site_ID)
);
-- Orbit Table
CREATE TABLE Project.Orbit (
    Orbit_ID INT PRIMARY KEY,
    Inclination FLOAT,
    Periapsis FLOAT,
    Apoapsis FLOAT
);
-- Projected Reentry Table
CREATE TABLE Project.Projected_Reentry (
    Projected_ID INT PRIMARY KEY,
    Inclination FLOAT,
    Periapsis FLOAT,
    Apoapsis FLOAT,
    Projected_Date DATE,
    Projected_Time TIME,
    Projected_Latitude FLOAT,
    Projected_Longitude FLOAT
);
-- Docked Objects Table
CREATE TABLE Project.Docked_Objects (
    Dock_ID INT PRIMARY KEY,
    Name VARCHAR(255),
    Shipment_Date DATE
);
-- Objects Table
CREATE TABLE Project.Objects (
    Object_ID INT PRIMARY KEY,
    Mass FLOAT,
    Width FLOAT,
    Height FLOAT,
    Name VARCHAR(255),
    Type_ID INT,
    Launch_ID INT,
    Orbit_ID INT,
    Projected_ID INT,
    Sites_ID INT,
    Dock_ID INT,
    FOREIGN KEY (Type_ID) REFERENCES Project.Object_Type(Type_ID),
    FOREIGN KEY (Launch_ID) REFERENCES Project.Original_Launch(Launch_ID),
    FOREIGN KEY (Orbit_ID) REFERENCES Project.Orbit(Orbit_ID),
    FOREIGN KEY (Projected_ID) REFERENCES Project.Projected_Reentry(Projected_ID),
    FOREIGN KEY (Sites_ID) REFERENCES Project.Launch_Sites(Site_ID),
    FOREIGN KEY (Dock_ID) REFERENCES Project.Docked_Objects(Dock_ID)
);
