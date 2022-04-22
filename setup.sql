-- Create a user database table:

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);

-- insert dummy data
INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Aaron",
    "Erebholo",
    "Basketball"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "John",
    "Doe",
    "Fishing"
);
INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Jane",
    "Doe",
    "Hiking"
);