"""

"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """
            CREATE SEQUENCE incr START 1;
            CREATE TABLE test (
                id integer PRIMARY KEY DEFAULT nextval('incr') NOT NULL,
                id_sendsay integer NOT NULL,
                alias char(250),
                name char(250),
                template char(10),
                create_date timestamp,
                update_date timestamp,
                reltype text,
                relref text
            );
        """,
        """
            DROP TABLE test;
            DROP SEQUENCE incr;
        """
    )
]
