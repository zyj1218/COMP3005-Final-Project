INSERT INTO members (username, password, name, email)
VALUES 
('user1', '123456', 'user1Name', 'user1@gmail.com'),
('user2', '123456', 'user2Name', 'user2@gmail.com'),
('user3', '123456', 'user3Name', 'user3@gmail.com'),
('user4', '123456', 'user4Name', 'user4@gmail.com'),
('user5', '123456', 'user5Name', 'user5@gmail.com'),
('user6', '123456', 'user6Name', 'user6@gmail.com');

INSERT INTO exercise_routines (member_id, routine_1, routine_2, routine_3)
VALUES 
(1, 'run for 10 mins', '10 push ups', '10 squats'),
(2, 'run for 10 mins', '10 push ups', '10 squats');

INSERT INTO achievements(member_id, a_1, a_2, a_3)
VALUES
(1, 'run for 1km', 'run for 10km', 'run for 100km'),
(2, 'run for 1km', 'run for 10km', 'run for 100km');

INSERT INTO health_statistics(member_id, resting_heart_rate, average_daily_steps)
VALUES
(1, '60', '1000'),
(2, '70', '2000');

INSERT INTO trainers(name)
VALUES
('James'),
('Sam'),
('Leo');

INSERT INTO classes(class_name, complexity, price)
VALUES
('yoga', 'low', 30),
('cycling', 'low', 30),
('boxing', 'moderate', 50),
('dance', 'high', 60);

INSERT INTO staffs(name)
VALUES
('Kate'),
('Andrew'),
('Charlie');

INSERT INTO devices(device_name, purchase_date)
VALUES
('computer','2024-01-01'),
('computer','2024-01-02'),
('treadmill','2024-01-03');

INSERT INTO rooms(room_name, capacity, features)
VALUES
('Room GA', '15', 'for group class'),
('Room GB', '15', 'for group class'),
('Room PA', '5', 'for personal class'),
('Room PB', '5', 'for personal class'),
('Room OA', '50', 'for party');

INSERT INTO trainer_schedules (trainer_id, class_id, class_type, available_date)
VALUES 
(1, 1, 'group', '2024-05-01'),
(2, 2, 'personal', '2024-05-02'),
(3, 3, 'group', '2024-05-03');

INSERT INTO final_class_schedules (schedule_id, trainer_id, class_id, class_type, start_time, end_time, class_date)
VALUES 
(1, 1, 1, 'group', '08:00', '10:00', '2024-05-01'),
(2, 2, 2, 'personal', '09:00', '11:00', '2024-05-01'),
(3, 3, 3, 'group', '12:00', '13:00', '2024-05-03');

INSERT INTO bookings(member_id, final_schedule_id)
VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1);
