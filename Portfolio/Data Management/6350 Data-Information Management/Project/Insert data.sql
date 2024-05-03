-- Insert data into Object_Type
INSERT INTO Project.Object_Type (Type_ID, Type)
VALUES
    (1, 'Rocket Body'),
    (2, 'Payload'),
    (3, 'Launch Vehicle'),
    (4, 'Station Part'),
    (5, 'Fragment'),
    (6, 'Observation Satellite'),
    (7, 'Communication Satellite'),
    (8, 'Space Station Module'),
    (9, 'Weather Satellite'),
    (10, 'Navigation Satellite');

-- Insert data into Launch_Sites
INSERT INTO Project.Launch_Sites (Site_ID, Name, Latitude, Longitude, Altitude)
VALUES
    (1, 'Kennedy Space Center', 28.3922, -80.6077, 3),
    (2, 'Baikonur Cosmodrome', 45.965, 63.305, 90),
    (3, 'Cape Canaveral Space Force Station', 28.5623, -80.5774, 3),
    (4, 'Vostochny Cosmodrome', 51.8507, 128.3317, 300),
    (5, 'Guiana Space Centre', 5.2361, -52.7681, 50),
    (6, 'Satish Dhawan Space Centre', 13.7337, 80.2344, 15),
    (7, 'Jiuquan Satellite Launch Center', 40.9601, 100.2986, 100);

-- Insert data into Original_Launch
INSERT INTO Project.Original_Launch(Launch_ID, Site_ID, Launch_Date, Launch_Time, Success_Failure)
VALUES
    (1, 1, '2023-11-12', '18:30:00', 'Success'),
    (2, 2, '2023-11-15', '15:45:00', 'Failure'),
    (3, 3, '2023-11-20', '12:00:00', 'Success'),
    (4, 4, '2023-11-25', '08:00:00', 'Failure'),
    (5, 5, '2023-12-01', '14:30:00', 'Success'),
    (6, 6, '2023-12-05', '10:15:00', 'Failure'),
    (7, 7, '2023-12-10', '20:00:00', 'Success');

-- Insert data into Orbit
INSERT INTO Project.Orbit (Orbit_ID, Inclination, Periapsis, Apoapsis)
VALUES
    (1, 28.5, 200, 400),
    (2, 51.6, 300, 600),
    (3, 45.0, 250, 500),
    (4, 60.0, 400, 700),
    (5, 30.0, 180, 350),
    (6, 75.0, 500, 800),
    (7, 35.0, 220, 450);

-- Insert data into Projected_Reentry
INSERT INTO Project.Projected_Reentry (Projected_ID, Inclination, Periapsis, Apoapsis, Projected_Date, Projected_Time, Projected_Latitude, Projected_Longitude)
VALUES
    (1, 30, 250, 450, '2023-12-01', '12:00:00', 35.0, -90.0),
    (2, 45, 350, 650, '2023-12-10', '08:30:00', 40.0, 120.0),
    (3, 25, 200, 400, '2023-12-15', '14:45:00', 30.0, -100.0),
    (4, 40, 300, 600, '2023-12-20', '10:00:00', 45.0, 130.0),
    (5, 20, 150, 300, '2023-12-25', '18:30:00', 25.0, -95.0),
    (6, 55, 450, 750, '2023-12-30', '16:15:00', 50.0, 110.0),
    (7, 33, 210, 420, '2024-01-05', '22:00:00', 37.0, -85.0);
    
-- Insert data into Docked_Objects
INSERT INTO Project.Docked_Objects (Dock_ID, Name, Shipment_Date)
VALUES
    (1, 'Space Station Alpha', '2023-10-01'),
    (2, 'Satellite Cluster Beta', '2023-09-15'),
    (3, 'Research Module Gamma', '2024-01-15'),
    (4, 'Communication Hub Delta', '2023-11-30'),
    (5, 'Weather Satellite Epsilon', '2023-08-20'),
    (6, 'Navigation Satellite Zeta', '2023-12-05'),
    (7, 'Observation Satellite Eta', '2023-09-10');

-- Insert data into Objects
INSERT INTO Project.Objects (Object_ID, Mass, Width, Height, Name, Type_ID, Launch_ID, Orbit_ID, Projected_ID, Sites_ID, Dock_ID)
VALUES
    (1, 5000, 3, 10, 'Satellite A', 2, 1, 1, 2, 1, NULL),
    (2, 8000, 5, 15, 'Rocket Body X', 1, 2, 2, NULL, 2, 1),
    (3, 3500, 2, 8, 'Satellite B', 2, 3, 3, 3, 4, NULL),
    (4, 6000, 4, 12, 'Rocket Body Y', 1, 4, 4, NULL, 5, NULL),
    (5, 4200, 3, 11, 'Satellite C', 2, 5, 5, 5, 6, NULL),
    (6, 7500, 6, 18, 'Rocket Body Z', 1, 6, 6, NULL, 7, 2),
    (7, 2800, 2, 7, 'Observation Satellite X', 6, 7, 7, 1, 3, NULL);
