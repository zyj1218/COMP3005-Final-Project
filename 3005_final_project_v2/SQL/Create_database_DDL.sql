CREATE TABLE IF NOT EXISTS members(
    member_id 	SERIAL 			PRIMARY KEY,
    username 	VARCHAR(255) 	UNIQUE NOT NULL, 
    password 	VARCHAR(255) 	NOT NULL,
    name 		VARCHAR(255), 
    email 		VARCHAR(255) 	UNIQUE
);

CREATE TABLE IF NOT EXISTS fitness_goals (
    goal_id 	SERIAL 			PRIMARY KEY,
    member_id 	INT 			NOT NULL UNIQUE,
    goal_1 		VARCHAR(255),
    goal_2 		VARCHAR(255),
    goal_3 		VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

CREATE TABLE IF NOT EXISTS health_metrics (
    metric_id 	SERIAL 			PRIMARY KEY,
    member_id 	INT 			NOT NULL UNIQUE,
    height 		DECIMAL(5,2),  
    weight 		DECIMAL(5,2), 
    BMI 		DECIMAL(5,2),  
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

CREATE TABLE IF NOT EXISTS exercise_routines (
    routine_id 	SERIAL 			PRIMARY KEY,
    member_id 	INT 			NOT NULL UNIQUE,
    routine_1 	VARCHAR(255),
    routine_2 	VARCHAR(255),
    routine_3 	VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);


CREATE TABLE IF NOT EXISTS achievements(
    achievement_id 	SERIAL 			PRIMARY KEY,
    member_id 		INT 			NOT NULL UNIQUE,
    a_1 			VARCHAR(255),
    a_2 			VARCHAR(255),
    a_3 			VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);


CREATE TABLE IF NOT EXISTS health_statistics(
    statistic_id 		SERIAL 	PRIMARY KEY,
    member_id 			INT 	NOT NULL UNIQUE,
    resting_heart_rate 	INT,
    average_daily_steps INT,
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

CREATE TABLE IF NOT EXISTS trainers(
    trainer_id 	SERIAL 			PRIMARY KEY,
    name 		VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS classes(
    class_id 	SERIAL 			PRIMARY KEY,
    class_name 	VARCHAR(255) 	NOT NULL,
    complexity 	VARCHAR(255) 	NOT NULL,
    price       DECIMAL(10,2)   NOT NULL
);

CREATE TABLE IF NOT EXISTS trainer_schedules(
   schedule_id 		SERIAL 			PRIMARY KEY,
   trainer_id 		INT 			NOT NULL,
   class_id  		INT 			NOT NULL,
   class_type  		VARCHAR(255) 	NOT NULL,
   available_date 	DATE 			NOT NULL,
   FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id),
   FOREIGN KEY (class_id) REFERENCES classes(class_id)
);


CREATE TABLE IF NOT EXISTS staffs(
    staff_id 	SERIAL 		PRIMARY KEY,
    name 		VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS final_class_schedules(
    final_schedule_id 	SERIAL 			PRIMARY KEY,
    schedule_id 		INT 			NOT NULL,
    trainer_id 			INT 			NOT NULL,
    class_id 			INT 			NOT NULL,
    class_type 			VARCHAR(255) 	NOT NULL, 
    start_time 			TIME 			NOT NULL,
    end_time 			TIME 			NOT NULL,
    class_date 			DATE 			NOT NULL, 
    FOREIGN KEY (schedule_id) REFERENCES trainer_schedules(schedule_id),
    FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id),
    FOREIGN KEY (class_id) REFERENCES classes(class_id)
);



CREATE TABLE IF NOT EXISTS bookings (
    booking_id 			SERIAL 	PRIMARY KEY,
    member_id 			INT 	NOT NULL,
    final_schedule_id 	INT 	NOT NULL,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (final_schedule_id) REFERENCES final_class_schedules(final_schedule_id)
);


CREATE TABLE IF NOT EXISTS devices (
    device_id 		SERIAL 			PRIMARY KEY,
    device_name 	VARCHAR(255) 	NOT NULL,
    purchase_date 	DATE
 );

CREATE TABLE IF NOT EXISTS maintenance (
    maintenance_id 			SERIAL 	PRIMARY KEY,
    device_id 				INT 	NOT NULL,
    maintenance_date 		DATE,
    next_maintenance_date 	DATE,
    FOREIGN KEY (device_id) REFERENCES devices(device_id)
);

CREATE TABLE IF NOT EXISTS rooms (
    room_id 	SERIAL 			PRIMARY KEY,
    room_name 	VARCHAR(255) 	NOT NULL,
    capacity 	INT,
    features 	TEXT  
);

CREATE TABLE IF NOT EXISTS room_bookings(
    booking_id 	SERIAL 	PRIMARY KEY,
    room_id 	INT 	NOT NULL,
    start_time 	TIME 	NOT NULL,
    end_time 	TIME 	NOT NULL,
    event_date 	DATE 	NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

CREATE TABLE IF NOT EXISTS bills (
    bill_id 	SERIAL 			PRIMARY KEY,
    booking_id  INT,
    member_id 	INT,
    amount 		DECIMAL(10, 2) 	NOT NULL,
    status 		VARCHAR(255) 	NOT NULL,
    bill_type 	VARCHAR(255) 	NOT NULL,
    created_at 	TIMESTAMP 		DEFAULT CURRENT_TIMESTAMP,
    updated_at 	TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);
